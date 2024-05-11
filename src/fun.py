import os
import multiprocessing
import re

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def get_prompt(prompt_template: str, mapper: dict):
    prompt = prompt_template
    for tag, value in mapper.items():
        prompt = prompt.replace(tag, value)

    return prompt


def send_message_mistral(
    client: MistralClient, message: str, mistral_model="open-mistral-7b"
) -> str:
    """
    Send a message to the Mistral API and return the response.

    Parameters:
        client: Mistral API client.
        message: The message to send to the API.

    Returns:
        str: Model response.
    """
    messages = [ChatMessage(role="user", content=message)]
    chat_response = client.chat(
        model=mistral_model,
        messages=messages,
    )
    return chat_response.choices[0].message.content


def ask_mistral_for_evaluation(
    client, prompt_template, mapper, mistral_model="open-mistral-7b"
):
    message = get_prompt(prompt_template, mapper)
    response = send_message_mistral(
        client=client, message=message, mistral_model=mistral_model
    )

    match = re.match(r"\d+", response)
    score = int(match) if match else None

    return response, score
