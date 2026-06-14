from app.gemini_client import create_chat
from app.gemini_client import (ask_gemini_with_context)


class CustomerSupportAgent:

    def __init__(self):

        self.chat = create_chat()

    def ask(self, prompt: str) -> str:

        response = self.chat.send_message(message=prompt)

        return response.text
    
    def ask_with_context(self, context: str, message: str) -> str:

        prompt = f"""
        Previous Conversation:

        {context}

        Current User Message:

        {message}
        """

        return ask_gemini_with_context(prompt)
