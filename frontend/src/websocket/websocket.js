export function createWebSocket(sessionId)
{
    const ws = new WebSocket(`ws://localhost:8000/ws/${sessionId}`);
    
    ws.onopen = () => { console.log("connected"); };

    return ws;
}

export function setupWebSocket(editor, terminal, ws, state)
{
    ws.onmessage = (event) => {
        
        console.log("received");
        const message = JSON.parse(event.data);

        if (message.type === "initial_code")
        {
            state.updatingFromRemote = true;
            editor.setValue(message.code);
            state.updatingFromRemote = false;
        }
        else if (message.type === "code_update")
        {
            state.updatingFromRemote = true;
            editor.setValue(message.code);
            state.updatingFromRemote = false;
        }
        else if (message.type === "terminal")
        {
            state.updatingFromRemote = true;
            terminal.writeln(message.text);
            state.updatingFromRemote = false;
        }
        else if (message.type === "terminal_clear")
        {
            state.updatingFromRemote = true;
            terminal.clear();
            state.updatingFromRemote = false;
        }
    };
}