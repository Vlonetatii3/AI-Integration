import requests

def ask_ai(message):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": message,
            "stream": False
        }
    )

    return response.json()["response"]

def check_prompt(prompt):
    response = f"GIVE ME A CLEAR ANSWER. THE USER INPUT IS: {prompt}"
    return response

def main():
    print("Local AI Chatbot - type 'quit' to exit")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        prompt = check_prompt(user_input)
        reply = ask_ai(prompt)
        print("Bot:", reply)


main()