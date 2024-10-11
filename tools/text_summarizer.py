# tools/text_summarizer.py
import openai

class TextSummarizer:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def summarize(self, text: str) -> str:
        """Uses OpenAI to summarize text."""
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Summarize this: {text}",
            max_tokens=60
        )
        return response.choices[0].text.strip()
