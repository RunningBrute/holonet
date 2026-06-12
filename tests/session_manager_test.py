from app.services.session_manager import SessionManager

def test_create_new_session():
    manager = SessionManager()
    session = manager.create_session()

    assert session.id is not None
    assert session.code == ""