import os
import pandas as pd
import json
import re


def generate_mapper(row):
    return {
        "[ORIGINAL LANGUAGE]": row["l1"],
        "[TRANSLATED LANGUAGE]": row["l2"],
        "[ORIGINAL TEXT]": row["src"],
        "[TRANSLATED TEXT]": row["mt"],
    }


def get_prompt(prompt_template: str, mapper: dict):
    prompt = prompt_template
    for tag, value in mapper.items():
        prompt = prompt.replace(tag, value)

    return prompt


def recover_all_files(path: str):
    files_content = []

    for filename in os.listdir(path):
        with open(f"{path}/{filename}") as infile:
            file_content = json.load(infile)
            files_content += file_content
    return pd.DataFrame(files_content).sort_values(by="id").reset_index(drop=True)


def compute_correlation(
    df: pd.DataFrame,
    ground_truth: str = "raw",
    predicted: str = "gemma_score",
    method: str = "pearson",
    decimals=3,
):
    correlations = {
        "overall": round(df[ground_truth].corr(df[predicted], method=method), decimals)
    }

    for language_pair in df["lp"].unique():
        sub_df = df[df.lp == language_pair]
        correlations[language_pair] = round(
            sub_df[ground_truth].corr(sub_df[predicted], method=method), decimals
        )

    return correlations

def get_score(response: str):
    pattern = r"\d+(?:\.\d+)?"
    
    match = re.search(pattern, response)
    score = float(match.group(0)) if match else None

    return score