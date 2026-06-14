require.config({
    paths: {
        vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs'
    }
});

require(['vs/editor/editor.main'], function () {

    window.editor = monaco.editor.create(
        document.getElementById('editor'),
        {
            value:
`#include <iostream>

int main()
{
    std::cout << "Hello";
}
`,
            language: 'cpp',
            automaticLayout: true
        }
    );
});