
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