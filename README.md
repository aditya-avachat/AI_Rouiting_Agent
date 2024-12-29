# AI Routing Agent

This project implements a suite of tools (summarizer, funifier, multiplication tool, and vowel counter) with an AI Routing Agent to handle user prompts and route them to the correct tool.

## Project Overview

**AIRoutingAgent** is an AI-powered tool designed to intelligently route user prompts to various specialized tools. It leverages natural language processing to understand user requests and perform specific actions such as summarizing text, adding humor to text, multiplying numbers, and counting vowels in a sentence. The underlying architecture uses the SentenceTransformer model for semantic similarity analysis, enabling efficient routing to the correct functionality based on the user's input.

### Key Features

- **Text Summarization**: Reduces lengthy texts to their essential points.
- **Text Funification**: Modifies texts to introduce humor.
- **Multiplication Tool**: Processes and multiplies numbers found within user input.
- **Vowel Counting**: Tallies the number of vowels in a provided sentence.
- **Semantic Routing**: Uses advanced natural language understanding to determine the appropriate tool for each request.

## Prerequisites

Before installing and running the AIRoutingAgent, ensure you have the following:

- Python 3.7 or higher installed on your machine.
- An API key for the Gemini AI service (this is necessary for certain functionalities).

## Installation/Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/AIRoutingAgent.git
   cd AIRoutingAgent
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv\Scripts\activate # on windows
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your Gemini's API key**:

   - Create a `.env` file in the project root directory and add your Gemini API key as follows:

     ```
     GEMINI_API_KEY='your_api_key_here'
     ```
5. **Run the AI Routing Agent**:

   - Example to summarize text:

     ```bash
     python ai_routing_agent.py
     ```
   - Enter your prompt when prompted. For example:

     ```bash
     Please enter your prompt: Summarize this paragraph: [your text here]
     ```
   - Example to multiply numbers:

     ```bash
     Please enter your prompt: Multiply 4 and 5.
     ```
   - Example to count vowels:

     ```bash
     Please enter your prompt: Count vowels in this sentence.
     ```
6. **Note**:

   - Please follow the instructions in the command line as the flow of execution may change based on user input and available options.

## Project Structure

- `ai_routing_agent.py`: Main routing agent that interacts with the tools.
- `tools/`: Contains individual tools for text summarization, fun-ifying, multiplication, and vowel counting.
- `requirements.txt`: List of required dependencies.

## Assumptions & Design Choices

- LLM-based tools (Summarizer and Funifier) use Gemini-1.5-flash API.
- The routing agent determines the appropriate tool based on keywords in the prompt.
