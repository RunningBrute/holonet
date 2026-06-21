from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse, Response

from app.services.session_manager import SessionManager
from app.services.connection_manager import ConnectionManager
from app.services.compiler_service import CompilerService
from app.models.update_code_request import UpdateCodeRequest

app = FastAPI()
session_manager = SessionManager()
connection_manager = ConnectionManager()
compiler_service = CompilerService()

app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

#@app.get("/")
#def index():
#    return FileResponse("frontend/dist/index.html")

@app.get("/")
def index():
    session = session_manager.create_session()
    return RedirectResponse(url=f"/session/{session.id}")

@app.get("/session/{session_id}")
def session_page(session_id: str):
    if not session_manager.session_exist(session_id):
        return Response(status_code=404)

    return FileResponse("frontend/dist/index.html")

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

#@app.get("/sessions")
#def get_sessions():
#    return session_manager.get_sessions()

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
    if not session_manager.session_exist(session_id):
        await ws.close()
        return
    
    await connection_manager.connect(ws, session_id)
    
    session = session_manager.get_session(session_id)
    await ws.send_json({"type": "initial_code", "code": session.code})
    
    try:
        while True:
            message = await ws.receive_json()
            if message["type"] == "compile":
                output = compiler_service.compile(session.code)
                await connection_manager.broadcast(session_id, {
                    "type": "terminal",
                    "text": output
                }, None)
            await connection_manager.broadcast(session_id, message, ws)
    except WebSocketDisconnect:
        connection_manager.disconnect(ws, session_id)