import os

import requests

MODEL = os.getenv("TERMINAI_MODEL", "llama3.1")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434").rstrip("/")
SYSTEM_PROMPT = (
    "You are TerminAI, a friendly and practical assistant for conversation "
    "and coding help. Explain code clearly, ask clarifying questions when "
    "needed, and never claim you ran code or tests unless you actually did."
)


def ask_ollama(history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}, *history]
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={"model": MODEL, "messages": messages, "stream": False},
            timeout=300,
        )
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"].strip()
    except requests.ConnectionError as exc:
        raise RuntimeError(
            f"Can't reach Ollama at {OLLAMA_URL}. Make sure Ollama is installed "
            "and running."
        ) from exc
    except requests.Timeout as exc:
        raise RuntimeError("Ollama took too long to respond; try again.") from exc
    except requests.HTTPError as exc:
        detail = exc.response.text if exc.response is not None else str(exc)
        raise RuntimeError(f"Ollama request failed: {detail}") from exc
    except (requests.RequestException, ValueError, KeyError) as exc:
        raise RuntimeError(f"Couldn't read Ollama's response: {exc}") from exc


def main():
    history = []
    print(f"TerminAI — local Ollama chat ({MODEL})")
    print("No API key needed. Type /clear to reset or /exit to quit.\n")

    while True:
        try:
            text = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nTerminAI: Goodbye!")
            break

        if not text:
            continue
        if text.lower() in {"/exit", "/quit"}:
            print("TerminAI: Goodbye!")
            break
        if text.lower() == "/clear":
            history.clear()
            print("TerminAI: Conversation cleared.\n")
            continue

        history.append({"role": "user", "content": text})
        try:
            answer = ask_ollama(history)
        except RuntimeError as exc:
            history.pop()
            print(f"\nTerminAI: {exc}\n")
            continue

        history.append({"role": "assistant", "content": answer})
        print(f"\nTerminAI: {answer}\n")


if __name__ == "__main__":
    main()
