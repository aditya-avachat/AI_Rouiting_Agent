import google.generativeai as genai
import os
from dotenv import load_dotenv
from transformers import BertTokenizer

load_dotenv()  # Load environment variables from .env file

class TextSummarizer:
    def __init__(self) -> None:
        self.API_KEY = os.getenv('GEMINI_API_KEY')
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')  # using BERT tokenizer for token counting

    def count_tokens(self, text: str) -> int:
        # tokenize the input text and count the number of tokens
        tokens = self.tokenizer.tokenize(text)
        return len(tokens)

    def summarize(self, prompt: str) -> str:
        genai.configure(api_key=self.API_KEY)
        input_tokens = self.count_tokens(prompt)

        # dynamically set max tokens for the output

        max_tokens = int(input_tokens * 0.5) # to nesure that the generated response is shorter i.e. summarized version of the input
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(prompt=prompt, max_tokens=max_tokens)
        summary = response.generations[0].text if response.generations else "No summary available."
        
        return summary
