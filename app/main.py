from fastapi import FastAPI, HTTPException
import uuid

from app.models.session import Session
from app.models.update_code_request import UpdateCodeRequest

app = FastAPI()


sessions: dict[str, Session] = {}

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/sessions")
def create_session():
    session = Session(
        id=str(uuid.uuid4()),
        code=""
    )
    sessions[session.id] = session

    return {"id": session.id}

@app.get("/sessions/{id}")
def get_session(id: str):
    session = sessions.get(id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    return session

@app.put("/sessions/{id}/code")
def update_code(id: str, request: UpdateCodeRequest):
    session = sessions.get(id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )
    
    session.code = request.code

    return session