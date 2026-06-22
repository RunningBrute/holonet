import { Terminal } from '@xterm/xterm';
import '@xterm/xterm/css/xterm.css';

export function createTerminal()
{
    const terminal = new Terminal({
        cursorBlink: true,
        scrollback: 5000
    });

    terminal.open(document.getElementById("terminal"));
    terminal.writeln("$ Ready");

    return terminal;
}