from fastapi import FastAPI, HTTPException
import uuid

from app.models.session import Session
from app.models.update_code_request import UpdateCodeRequest

app = FastAPI()

class SessionManager:
    def __init__(self):
        self.sessions: dict [str, Session] = {}

    def create_session(self) -> Session:
        session = Session(
            id=str(uuid.uuid4()),
            code=""
        )
        self.sessions[session.id] = session
        return session


    def get_session(self, id: str) -> Session:
        session = self.sessions.get(id)

        if session is None:
            raise HTTPException(
                status_code=404,
                detail="Session not found"
            )

        return session


    def update_code(self, id: str, code: str) -> Session:
        session = self.get_session(id)
        session.code = code
        return session


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