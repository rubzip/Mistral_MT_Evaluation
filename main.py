from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv

import multiprocessing
import os

load_dotenv()
MISTRAL_API = os.getenv("MISTRAL_API")
client = MistralClient(api_key=MISTRAL_API)



pool = multiprocessing.Pool(4)
