import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class TextFunifier:
    """A class for funifying text using the Gemini API.

    This class takes user input text and modifies it to make it more humorous 
    or entertaining using the generative capabilities of the Gemini model.

    Attributes:
        API_KEY (str): The API key for authenticating with the Gemini API.
    """

    def __init__(self) -> None:
        """Initializes the TextFunifier with the Gemini API key."""
        self.API_KEY = os.getenv('GEMINI_API_KEY')

    def funify(self, prompt: str) -> str:
        """Generates a funified version of the given text prompt.

        Args:
            prompt (str): The text prompt to be funified.

        Returns:
            str: A funified version of the input prompt.

        Raises:
            Exception: If there is an issue with the API call.
        """
        genai.configure(api_key=self.API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content('make the following sentence very very funny'+prompt)
        funny_response = response.text 

        return funny_response
