const sessionId = "test-session";
const ws = new WebSocket(`ws://localhost:8000/ws/${sessionId}`);
const editor = document.getElementById("editor");

ws.onmessage = function(event)
{
    const message = JSON.parse(event.data);

    if (message.type === "code_update")
    {
        editor.value = message.code;
    }
};

editor.addEventListener("input", () => {
        ws.send(
            JSON.stringify({
                type: "code_update",
                code: editor.value
            })
        );
    }
);