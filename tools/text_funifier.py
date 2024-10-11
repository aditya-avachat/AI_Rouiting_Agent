# tools/text_funifier.py
import openai

class TextFunifier:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def funify(self, text: str) -> str:
        """Uses OpenAI to make text funnier."""
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Make this funnier: {text}",
            max_tokens=60
        )
        return response.choices[0].text.strip()