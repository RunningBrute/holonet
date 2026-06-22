export function setupClearTerminalButton(terminal, socket)
{
    document
        .getElementById("clear-terminal-button")
        .addEventListener("click", () => { terminal.clear(); });
}