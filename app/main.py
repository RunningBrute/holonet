from fastapi import FastAPI, WebSocket

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

@app.get("/sessions")
def get_sessions():
    return session_manager.get_sessions()

@app.put("/sessions/{id}/code")
def update_code(id: str, request: UpdateCodeRequest):
    return session_manager.update_code(id, request.code)

@app.delete("/sessions/{id}")
def delete_session(id: str):
    session_manager.delete_session(id)

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()

    while True:
        message = await ws.receive_text()

        await ws.send_text(f"Echo: {message}")