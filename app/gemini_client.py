from google import genai

from app.config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)


def create_chat():

    return client.chats.create(model="gemini-2.5-flash")

def ask_gemini_with_context(prompt: str) -> str:

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    return response.text
