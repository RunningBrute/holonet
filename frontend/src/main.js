import { createEditor, setupEditor } from './editor/editor.js';
import { createTerminal } from './terminal/terminal.js';
import { createWebSocket, setupWebSocket } from './websocket/websocket.js';
import { setupCompileButton } from './ui/compileButton.js';

import './styles/style.css';

const editor = createEditor();
const terminal = createTerminal();
const params = new URLSearchParams(window.location.search);
const sessionId = params.get("session") ?? "default";
const socket = createWebSocket(sessionId);

const state = { updatingFromRemote: false };

setupEditor(editor, socket, state);
setupWebSocket(editor, socket, state);
setupCompileButton(terminal, socket);