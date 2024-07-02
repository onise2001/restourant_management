from .session import Session

def get_session():
    session = Session()
    return session


session = get_session()