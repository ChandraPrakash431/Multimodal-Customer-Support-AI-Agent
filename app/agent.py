from gemini_client import create_chat


class CustomerSupportAgent:

    def __init__(self):

        self.chat = create_chat()

    def ask(self, prompt: str) -> str:

        response = self.chat.send_message(
            message=prompt
        )

        return response.text