# TerminAI

A Python terminal chatbot for conversation and coding help.

## Features
- Chat with a local terminal interface
- Coding assistance and explanation
- Conversation memory within the session
- Easy setup with an OpenAI API key

## Run

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

3. Set your API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

4. Start the app:
   ```bash
   python terminai.py
   ```

Use `/clear` to reset the conversation and `/exit` to quit.
