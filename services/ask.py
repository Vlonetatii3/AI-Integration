import requests

def ask_ollama(history):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": "\n".join(history),
            "stream": False
        },
        timeout=60
    )

    response.raise_for_status()
    data = response.json()
    return data["response"]