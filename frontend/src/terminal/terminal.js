import { FitAddon } from '@xterm/addon-fit'
import { Terminal } from '@xterm/xterm';
import '@xterm/xterm/css/xterm.css';

export function createTerminal()
{
    const terminal = new Terminal({
        cursorBlink: true,
        scrollback: 5000
    });

    const fitAddon = new FitAddon();
    
    terminal.loadAddon(fitAddon);
    terminal.open(document.getElementById("terminal"));
    fitAddon.fit();
    terminal.writeln("$ Ready");

    window.addEventListener("resize",
        () => fitAddon.fit()
    );

    return terminal;
}