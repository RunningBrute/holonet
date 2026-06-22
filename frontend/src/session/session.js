export function getSessionId()
{
    const sessionId = window.location.pathname
        .split("/")
        .pop();
    return sessionId;
}

export function showSessionId()
{
    document
        .getElementById("session-id")
        .textContent = `Session: ${getSessionId()}`;
}