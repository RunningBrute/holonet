export function createWebSocket(sessionId)
{
    const protocol = window.location.protocol === "https:" ? "wss" : "ws";
    const ws = new WebSocket(`${protocol}://${window.location.host}/ws/${sessionId}`);

    console.log("WS URL:", ws.url);
    
    ws.onopen = () => console.log("WS OPEN");
    ws.onerror = (e) => console.error("WS ERROR", e);
    ws.onclose = (e) => console.log("WS CLOSE", e.code, e.reason);

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
            const output = message.text
                .replace(/\r\n/g, "\n")
                .replace(/\r/g, "\n")
                .replace(/\n/g, "\r\n");

            terminal.reset();
            terminal.write(output);
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