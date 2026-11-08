# TerminAI

A Python terminal chatbot for conversation and coding help using a model running locally in Ollama. TerminAI does not need an API key.

## Setup

1. Install Ollama from https://ollama.com and start it.
2. Download a model (one-time download; choose a model supported by your computer):

   ```bash
   ollama pull llama3.1
   ```

3. Clone this repository, then create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # macOS/Linux
   source .venv/bin/activate
   # Windows PowerShell: .venv\\Scripts\\Activate.ps1
   ```

4. Install TerminAI's Python dependency and start it:

   ```bash
   python -m pip install -r requirements.txt
   python terminai.py
   ```

Ollama should be running locally at `http://localhost:11434`. To use another model, set `TERMINAI_MODEL` to its Ollama model name. To change the Ollama address, set `OLLAMA_URL`.

Use `/clear` to reset the current conversation and `/exit` to quit. After the model is downloaded, chats are processed by Ollama on your machine; the model download itself requires internet.
