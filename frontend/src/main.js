import { createEditor, setupEditor } from './editor/editor.js';
import { createTerminal } from './terminal/terminal.js';
import { createWebSocket, setupWebSocket } from './websocket/websocket.js';
import { setupCompileButton } from './ui/compileButton.js';
import { setupClearTerminalButton } from './ui/clearTerminalButton.js'
import { getSessionId, showSessionId } from './session/session.js';

import './styles/style.css';

const editor = createEditor();
const terminal = createTerminal();
const socket = createWebSocket(getSessionId());

const state = { updatingFromRemote: false };

setupEditor(editor, socket, state);
setupWebSocket(editor, terminal, socket, state);
setupCompileButton(terminal, socket);
setupClearTerminalButton(terminal, socket);
showSessionId();
