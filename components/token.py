from haystack.utils import Secret
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()
secret_HF = Secret.from_token(os.getenv('HF_TOKEN'))
secret_QDRANT = Secret.from_token(os.getenv('QDRANT_API_KEY'))
secret_GEMINI = Secret.from_token(os.getenv('GEMINI_API_KEY'))