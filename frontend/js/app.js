const sessionId = "test-session";
const ws = new WebSocket(`ws://localhost:8000/ws/${sessionId}`);

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

    ws.onmessage = function(event)
    {
        const message =
            JSON.parse(event.data);

        if (message.type === "code_update")
        {
            editor.setValue(
                message.code
            );
        }
    };

    editor.onDidChangeModelContent(() => {

        ws.send(
            JSON.stringify({
                type: "code_update",
                code: editor.getValue()
            })
        );

    });
});