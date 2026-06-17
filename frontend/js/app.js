const sessionId = "test-session";
const ws = new WebSocket(`ws://localhost:8000/ws/${sessionId}`);
let updatingFromRemote = false;

ws.onopen = () => {
    console.log("connected");
};

ws.onerror = (e) => {
    console.log(e);
};

require.config({
    paths: {
        vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs'
    }
});

function appendTerminal(text)
{
    term.writeln(text);
}

require(['vs/editor/editor.main'], function () {

    const editor = monaco.editor.create(
        document.getElementById('editor'),
        {
            value: `#include <iostream>

int main()
{
    std::cout << "Hello";
}
`,
            language: 'cpp',
            automaticLayout: true
        }
    );

    const term = new Terminal({
        cursorBlink: true,
        theme: {
            background: "#1e1e1e",
            foreground: "#ffffff"
        }
    });

    term.open(document.getElementById("terminal"));
    term.writeln("Holonet Terminal");

    term.writeln("");
    term.writeln("$ Ready");

    const compileButton = document.getElementById("compile-button");
    compileButton.addEventListener("click", () => {
        term.writeln("$ Compile requested");
    });

    ws.onmessage = function(event)
    {
        const message =
            JSON.parse(event.data);

        if (message.type === "code_update")
        {
            updatingFromRemote = true;
            editor.setValue(message.code);
            updatingFromRemote = false;
        }
    };

    editor.onDidChangeModelContent(() => {

        if (updatingFromRemote)
        {
            return;
        }

        ws.send(
            JSON.stringify({
                type: "code_update",
                code: editor.getValue()
            })
        );

    });
});