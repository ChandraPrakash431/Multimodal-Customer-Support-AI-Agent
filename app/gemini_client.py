from google import genai

from app.config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)


def create_chat():

    return client.chats.create(model="gemini-2.5-flash")