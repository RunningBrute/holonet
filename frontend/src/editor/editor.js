import * as monaco from 'monaco-editor';

export function createEditor()
{
    return monaco.editor.create(
        document.getElementById("editor"),
        {
            value: `#include <iostream>

int main()
{
    std::cout << "Hello";
}
`,
            language: "cpp",
            automaticLayout: true
        }
    );
}

export function setupEditor(editor, ws, state)
{
    editor.onDidChangeModelContent(() => {
        console.log("sending");

        if (state.updatingFromRemote)
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
}