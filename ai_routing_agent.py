# ai_routing_agent.py
import re
from tools.text_summarizer import TextSummarizer
from tools.text_funifier import TextFunifier
from tools.multiplication_tool import MultiplicationTool
from tools.vowel_counter import VowelCounter

class AIRoutingAgent:
    def __init__(self, api_key: str):
        self.text_summarizer = TextSummarizer(api_key)
        self.text_funifier = TextFunifier(api_key)
        self.multiplication_tool = MultiplicationTool()
        self.vowel_counter = VowelCounter()
    
    def route(self, prompt: str):
        if "summarize" in prompt.lower():
            text = self.extract_text(prompt)
            return self.text_summarizer.summarize(text)
        elif "funny" in prompt.lower() or "fun-ify" in prompt.lower():
            text = self.extract_text(prompt)
            return self.text_funifier.funify(text)
        elif "multiply" in prompt.lower() or "product" in prompt.lower():
            numbers = self.extract_numbers(prompt)
            return self.multiplication_tool.multiply(numbers)
        elif "vowel" in prompt.lower():
            text = self.extract_text(prompt)
            return self.vowel_counter.count_vowels(text)
        else:
            return "Sorry, I don't understand that request."

    def extract_numbers(self, prompt: str):
        """Extracts numbers from a prompt."""
        numbers = re.findall(r'\d+', prompt)
        return list(map(int, numbers))

    def extract_text(self, prompt: str):
        """Extracts text for summarization or fun-ifying."""
        match = re.search(r'["\'](.*?)["\']', prompt)
        if match:
            return match.group(1)
        return prompt  # Return entire prompt if no quotes found

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI Routing Agent")
    parser.add_argument("prompt", type=str, help="User prompt")
    args = parser.parse_args()

    # Example: Provide your OpenAI API Key here
    api_key = "your-openai-api-key"

    agent = AIRoutingAgent(api_key)
    result = agent.route(args.prompt)
    print(result)
