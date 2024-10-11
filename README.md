# AI Routing Agent

This project implements a suite of tools (summarizer, funifier, multiplication tool, and vowel counter) with an AI Routing Agent to handle user prompts and route them to the correct tool.

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repo/mycroft_ai_tools.git
   cd mycroft_ai_tools
   ```
2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your OpenAI API key**:

   - Replace `your-openai-api-key` in `ai_routing_agent.py` with your actual OpenAI API key.
5. **Run the AI Routing Agent**:

   - Example to summarize text:

     ```bash
     python ai_routing_agent.py "Summarize this: 'Artificial intelligence is transforming industries.'"
     ```
   - Example to multiply numbers:

     ```bash
     python ai_routing_agent.py "What is the product of 20 and 5?"
     ```
   - Example to count vowels:

     ```bash
     python ai_routing_agent.py "How many vowels are in 'Hello World'?"
     ```

## Project Structure

- `ai_routing_agent.py`: Main routing agent that interacts with the tools.
- `tools/`: Contains individual tools for text summarization, fun-ifying, multiplication, and vowel counting.
- `requirements.txt`: List of required dependencies.

## Assumptions & Design Choices

- LLM-based tools (Summarizer and Funifier) use OpenAI's GPT-3 API.
- The routing agent determines the appropriate tool based on keywords in the prompt.
