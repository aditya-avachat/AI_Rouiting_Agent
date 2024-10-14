import google.generativeai as genai
import os
from dotenv import load_dotenv
from transformers import BertTokenizer

load_dotenv()  # Load environment variables from .env file

class TextSummarizer: 
    """A class for summarizing text using the Google Gemini API.
    This class uses a BERT tokenizer to count tokens in the input text and 
    summarizes it using the Gemini API."""
    
    def __init__(self) -> None:
        self.API_KEY = os.getenv('GEMINI_API_KEY')
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')  # using BERT tokenizer for token counting

    def count_tokens(self, text: str) -> int:
        
        """Counts the number of tokens in the provided text.

        Args:
            text (str): The input text to tokenize.

        Returns:
            int: The number of tokens in the input text.
        """
        tokens = self.tokenizer.tokenize(text)
        return len(tokens)

    def summarize(self, prompt: str) -> str:
        """Generates a summary for the given prompt.

        This method dynamically sets the maximum number of output tokens 
        based on the input token count to ensure a concise summary.

        Args:
            prompt (str): The text to be summarized.

        Returns:
            str: The summarized text.
        """
        genai.configure(api_key=self.API_KEY)
        input_tokens = self.count_tokens(prompt)

        # dynamically set max tokens for the output

        max_tokens = int(input_tokens * 0.60) # to nesure that the generated response is shorter i.e. summarized version of the input
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content('summarize the follwing'+prompt, generation_config = genai.GenerationConfig(
        max_output_tokens=max_tokens))
        summary = response.text 
        
        return summary
