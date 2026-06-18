export function setupCompileButton(terminal, socket)
{
    document
        .getElementById("compile-button")
        .addEventListener("click", () => {
                terminal.writeln("$ Compile requested");
                socket.send(JSON.stringify({type: "compile"}));
            });
}