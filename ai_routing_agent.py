from sentence_transformers import SentenceTransformer, util
import re
from tools.text_summarizer import TextSummarizer
from tools.text_funifier import TextFunifier
from tools.multiplication_tool import MultiplicationTool
from tools.vowel_counter import VowelCounter
import google.generativeai as genai
import os
from word2number import w2n  # This library converts written numbers to digits


class AIRoutingAgent:
    def __init__(self):
        """Initializes the AI Routing Agent with required tools and models."""
        self.text_summarizer = TextSummarizer()
        self.text_funifier = TextFunifier()
        self.multiplication_tool = MultiplicationTool()
        self.vowel_counter = VowelCounter()
        self.model = SentenceTransformer('all-mpnet-base-v2')
        self.API_KEY = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=self.API_KEY)
        self.tools_purposes = {
            'summarize the sentence': self.text_summarizer,
            'make this text funny': self.text_funifier,
            'multiply the numbers': self.multiplication_tool,
            'count vowels in the sentence': self.vowel_counter
        }

    def route_prompt(self, prompt: str):
        """
        Routes the user's prompt to the appropriate tool based on semantic similarity.

        Args:
            prompt (str): The user's input prompt that describes the desired action.

        Returns:
            str: The result from the routed tool or a message prompting the user for clarification.
        """
        best_score = 0.7  # Similarity threshold
        best_tool = None
        best_purpose = ""

        for tool_purpose, tool in self.tools_purposes.items():
            route_score = self.similarity_score(tool_purpose, prompt)
            if route_score >= best_score: 
                best_score = route_score
                best_tool = tool
                best_purpose = tool_purpose

        if best_tool is not None:
            if best_purpose == 'summarize the sentence':
                print("Routing to Text Summarizer")
                return self.text_summarizer.summarize(prompt)
            elif best_purpose == 'make this text funny':
                print("Routing to Text Funifier")
                return self.text_funifier.funify(prompt)
            elif best_purpose == 'multiply the numbers':
                number_list = self.extract_numbers(prompt)
                print(f"The numbers you wish to multiply are: {number_list}")
                print("Routing to Multiplication Tool")
                return self.multiplication_tool.multiply(number_list)
            elif best_purpose == 'count vowels in the sentence':
                clean_prompt = self.preprocess_prompt(prompt)
                print("Routing to Vowel Counter")
                return self.vowel_counter.count_vowels(clean_prompt)

        # Ask the user for clarification if no suitable tool is found
        user_action = self.ask_user_for_action()
        if user_action == 'summarize':
            print("Routing to Text Summarizer")
            return self.text_summarizer.summarize(prompt)
        elif user_action == 'funify':
            print("Routing to Text Funifier")
            return self.text_funifier.funify(prompt)
        elif user_action == 'multiply':
            number_list = self.extract_numbers(prompt)
            print(f"The numbers you wish to multiply are: {number_list}")
            print("Routing to Multiplication Tool")
            return self.multiplication_tool.multiply(number_list)
        elif user_action == 'count vowels':
            clean_prompt = self.preprocess_prompt(prompt)
            print("Routing to Vowel Counter")
            return self.vowel_counter.count_vowels(clean_prompt)
            
    def similarity_score(self, tool_purpose: str, prompt: str) -> float:
        """
        Calculates the cosine similarity between the tool purpose and the user's prompt.

        Args:
            tool_purpose (str): The purpose of the tool to compare against.
            prompt (str): The user's input prompt.

        Returns:
            float: The cosine similarity score between 0 and 1.
        """
        embedding1 = self.model.encode(tool_purpose, convert_to_tensor=True)
        embedding2 = self.model.encode(prompt, convert_to_tensor=True)
        similarity_score = util.pytorch_cos_sim(embedding1, embedding2)
        return similarity_score.item()
    
    def preprocess_prompt(self, prompt: str) -> str:
        """
        Cleans the user prompt by removing action phrases and instructions using Gemini.

        Args:
            prompt (str): The original user prompt.

        Returns:
            str: The cleaned prompt, focusing on core content.
        """
        model = genai.GenerativeModel("gemini-1.5-flash")
        task = "Remove any instructions or action phrases and return only the core content of the following prompt:"

        # Pass the prompt to the model with the task instruction
        response = model.generate_content(f"{task} {prompt}")
        cleaned_prompt = response.text.strip()  # Processed and cleaned text
        
        return cleaned_prompt

    def ask_user_for_action(self) -> str:
        """
        Prompts the user to specify what they want to do when the agent cannot determine the action.

        Returns:
            str: The action the user wants to perform.
        """
        print("I'm not sure how to process your request. Could you please specify what you would like to do?")
        print("Options: 'summarize', 'funify', 'multiply', 'count vowels'")
        user_input = input("What would you like to do? ").strip().lower()
        return user_input
        
    def extract_numbers(self, text: str):
        """
        Extracts numbers from a given text, including both digit-based and word-based representations.

        Args:
            text (str): The input text from which to extract numbers.

        Returns:
            list: A list of unique integers extracted from the text.
        """
        numbers = []

        # Use regex to find digit-based numbers
        digit_numbers = re.findall(r'\d+', text)
        numbers.extend(map(int, digit_numbers))  # Convert and append to list

        # Handle words in the form of numbers (like "thirty-two")
        # This regex captures words for numbers, including compound forms like "thirty-two" and "three hundred"
        words_numbers = re.findall(r'\b(?:one|two|three|four|five|six|seven|eight|nine|ten|'
                                   r'eleven|twelve|thirteen|fourteen|fifteen|sixteen|'
                                   r'seventeen|eighteen|nineteen|twenty|thirty|forty|'
                                   r'fifty|sixty|seventy|eighty|ninety|hundred|'
                                   r'thousand|and|[\s\-])+\b', text, flags=re.IGNORECASE)

        # Combine the matched words and convert them to numbers
        for phrase in words_numbers:
            try:
                number = w2n.word_to_num(phrase.strip())
                numbers.append(number)
            except ValueError:
                continue  # Skip any that can't be converted

        return list(set(numbers))  # Return unique numbers
        
    
if __name__ == "__main__":
    prompt = input("Please enter your prompt: ")
    agent = AIRoutingAgent()
    result = agent.route_prompt(prompt)
    print(result)
