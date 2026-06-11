from fastapi import FastAPI

from app.services.session_manager import SessionManager
from app.models.update_code_request import UpdateCodeRequest

app = FastAPI()
session_manager = SessionManager()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/sessions")
def create_session():
    session = session_manager.create_session()
    return {"id": session.id}

@app.get("/sessions/{id}")
def get_session(id: str):
    return session_manager.get_session(id)

@app.put("/sessions/{id}/code")
def update_code(id: str, request: UpdateCodeRequest):
    return session_manager.update_code(id, request.code)