from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app import agent
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

class ChatRequest(BaseModel):
    message: str
    lat: float = 12.9716
    lng: float = 77.5946

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/chat")
def chat(req: ChatRequest):
    query = f"""
User message: {req.message}
User location: ({req.lat}, {req.lng})
Default city: Bengaluru (use this if user doesn't mention a city)
"""
    result = agent.invoke({
        "messages": [{"role": "user", "content": query}]
    })
    return {"reply": result["messages"][-1].content}