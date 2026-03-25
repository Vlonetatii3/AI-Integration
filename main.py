from fastapi import FastAPI
from api.ask import router as AskRouter

app = FastAPI(title="AI GAME SERVICE",
              description="Guessing game",
              version= "1.0.1")

app.include_router(AskRouter)