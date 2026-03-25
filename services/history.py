import json

def save_history(history):
    with open("memory.json", "w") as file:
        json.dump(history, file)

def load_history():
    try:
        with open("memory.json", "r") as file:
            return json.load(file)
    except:
        return []