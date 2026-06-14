from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.connections: dict[str, list[WebSocket]] = {}

    async def connect(self, ws: WebSocket, session_id: str):
        await ws.accept()

        if session_id not in self.connections:
            self.connections[session_id] = []

        self.connections[session_id].append(ws)

    def disconnect(self, ws: WebSocket, session_id: str):
        self.connections[session_id].remove(ws)

    async def broadcast(self, session_id: str, message):
        session_connections = self.connections[session_id]
        for session_connection in session_connections:
            await session_connection.send_json(message)

