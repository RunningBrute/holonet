import pytest
from fastapi import HTTPException
from app.services.session_manager import SessionManager


def test_get_not_existing_session():
    manager = SessionManager()

    with pytest.raises(HTTPException) as exc_info:
        manager.get_session("absd-1234-wsad")

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Session not found"


def test_delete_not_existing_session():
    manager = SessionManager()

    with pytest.raises(HTTPException) as exc_info:
        manager.delete_session("absd-1234-wsad")

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Session not found"


def test_update_not_existing_session_code():
    manager = SessionManager()

    with pytest.raises(HTTPException) as exc_info:
        manager.update_code("absd-1234-wsad", "new code;")

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Session not found"


def test_get_empty_sessions():
    manager = SessionManager()

    sessions = manager.get_sessions()
    assert len(sessions) == 0


def test_create_new_session():
    manager = SessionManager()
    session = manager.create_session()

    assert session.id is not None
    assert session.code == ""


def test_get_session():
    manager = SessionManager()
    session = manager.create_session()

    assert session.id is not None
    assert session.code == ""

    the_same_session = manager.get_session(session.id)
    assert session.id == the_same_session.id
    assert session.code == the_same_session.code


def test_get_all_sessions():
    manager = SessionManager()
    session = manager.create_session()
    next_session = manager.create_session()
    another_session = manager.create_session()

    sessions = manager.get_sessions()
    assert len(sessions) == 3
    assert session.id == sessions[0].id
    assert next_session.id == sessions[1].id
    assert another_session.id == sessions[2].id


def test_update_session_code():
    manager = SessionManager()
    session = manager.create_session()
    next_session = manager.create_session()

    assert session.code == ""
    assert next_session.code == ""

    new_code: str = "int main();"
    manager.update_code(next_session.id, new_code)
    updated_session = manager.get_session(next_session.id)
    assert updated_session.code == new_code
    assert session.code == ""


def test_delete_session():
    manager = SessionManager()
    session = manager.create_session()
    next_session = manager.create_session()

    assert len(manager.get_sessions()) == 2

    manager.delete_session(next_session.id)
    sessions = manager.get_sessions()
    assert len(sessions) == 1
    assert sessions[0].id == session.id
