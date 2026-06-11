from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()


class Session(BaseModel):
    id: str
    code: str

sessions: dict[str, Session] = {}

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/sessions")
async def create_session():
    session = Session(
        id=str(uuid.uuid4()),
        code=""
    )
    sessions[session.id] = session

    return {"id": session.id}

@app.get("/sessions/{id}")
async def get_session(id: str):
    session = sessions.get(id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    return sessions