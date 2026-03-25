import requests
import json

chat_history = []

def ask_ai():
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3:8b",
            "prompt": "\n".join(chat_history),
            "stream": False
        }
    )

    return response.json()["response"]

def save_history(history):
    with open("memory.json", "w") as file:
        json.dump(history, file)

def load_history():
    try:
        with open("memory.json", "r") as file:
            return json.load(file)
    except:
        return []
    
def main():
    print("Animal Guessing Game - type 'quit' to exit")

    chat_history = load_history()

    if not chat_history:
        system_prompt = """THIS IS A GAME:
You choose ONE secret animal and remember it.
DO NOT change the animal.
DO NOT tell me what it is.

I will try to guess it.

If I guess correctly, say ONLY: "YOU WON!"
Otherwise, give hints."""

        chat_history.append(system_prompt)

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            save_history(chat_history)
            print("Game saved. Bye!")
            break

        chat_history.append("User: " + user_input)

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": "\n".join(chat_history),
                "stream": False
            }
        )

        reply = response.json()["response"]

        chat_history.append("Bot: " + reply)

        print("Bot:", reply)


main()