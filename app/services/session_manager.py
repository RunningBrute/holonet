from fastapi import HTTPException
import uuid

from app.models.session import Session

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