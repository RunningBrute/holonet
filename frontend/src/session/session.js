export function getSessionId()
{
    const sessionId = window.location.pathname
        .split("/")
        .pop();
}