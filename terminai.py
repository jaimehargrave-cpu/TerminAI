import os

from openai import OpenAI, OpenAIError

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
SYSTEM_PROMPT = (
    "You are TerminAI, a friendly and practical assistant for conversation "
    "and coding help. Explain code clearly, ask clarifying questions when "
    "needed, and never claim you ran code or tests unless you actually did."
)


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Missing OPENAI_API_KEY.")
        print("Set it in your environment, then run TerminAI again.")
        return

    client = OpenAI(api_key=api_key)
    conversation = [{"role": "developer", "content": SYSTEM_PROMPT}]

    print(f"TerminAI — chat and coding help ({MODEL})")
    print("Type /clear to start a new conversation or /exit to quit.\n")

    while True:
        try:
            message = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nTerminAI: Goodbye!")
            break

        if not message:
            continue

        if message.lower() in {"/exit", "/quit"}:
            print("TerminAI: Goodbye!")
            break

        if message.lower() == "/clear":
            conversation = [{"role": "developer", "content": SYSTEM_PROMPT}]
            print("TerminAI: Conversation cleared.\n")
            continue

        conversation.append({"role": "user", "content": message})

        try:
            response = client.responses.create(
                model=MODEL,
                input=conversation,
            )
            answer = response.output_text.strip()
            print(f"\nTerminAI: {answer}\n")
            conversation.append({"role": "assistant", "content": answer})
        except OpenAIError as error:
            conversation.pop()
            print(f"\nTerminAI: The API request failed: {error}\n")


if __name__ == "__main__":
    main()
