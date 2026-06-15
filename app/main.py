from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from app.services.session_manager import SessionManager
from app.services.connection_manager import ConnectionManager
from app.models.update_code_request import UpdateCodeRequest

app = FastAPI()
session_manager = SessionManager()
connection_manager = ConnectionManager()


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
        await ws.send_text(message)

@app.websocket("/ws/{session_id}")
async def websocket_endpoint(ws: WebSocket, session_id: str):
    await connection_manager.connect(ws, session_id)

    try:
        while True:
            message = await ws.receive_json()
            await connection_manager.broadcast(session_id, message, ws)
    except WebSocketDisconnect:
        connection_manager.disconnect(ws, session_id)