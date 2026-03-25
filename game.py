import requests

chat_history = []

def ask_ai():
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": "\n".join(chat_history),
            "stream": False
        }
    )

    return response.json()["response"]


def main():
    print("Animal Guessing Game - type 'quit' to exit")

    # Initial instruction (ONLY ONCE)
    system_prompt = """THIS IS A GAME:
You choose ONE secret animal and remember it.
DO NOT change the animal.
DO NOT tell me what it is.
I will try to guess it.

If I guess correctly, say ONLY: "YOU WON!"
Otherwise, give hints.
KEEP answers short (1 sentence max)"""

    chat_history.append(system_prompt)

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        chat_history.append("User: " + user_input)

        reply = ask_ai()

        chat_history.append("Bot: " + reply)

        print("Bot:", reply)


main()