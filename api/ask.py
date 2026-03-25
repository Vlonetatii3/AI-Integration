from fastapi import APIRouter
from model.chat_request import ChatRequest
from model.chat_response import ChatResponse
from services.history import save_history, load_history
from services.ask import ask_ollama

router = APIRouter(tags=["Ask"])


MEMORY_FILE = "memory.json"

@router.post("/chat", response_model= ChatResponse)
def chat(request: ChatRequest):
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

    chat_history.append("User: " + request.message)

    reply = ask_ollama(chat_history)

    chat_history.append("Bot: " + reply)

    chat_history = chat_history[-20:]
    save_history(chat_history)

    return {"reply": reply}



@router.post("/reset")
def reset():
    system_prompt = """THIS IS A GAME:
You choose ONE secret animal and remember it.
DO NOT change the animal.
DO NOT tell me what it is.

I will try to guess it.

If I guess correctly, say ONLY: "YOU WON!"
Otherwise, give hints."""
    
    chat_history = [system_prompt]
    save_history(chat_history)

    return {"message": "Game reset successfully"}