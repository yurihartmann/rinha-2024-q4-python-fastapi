import os

from sqlmodel import create_engine, Session


def get_db_url():
    if os.getenv("DB_HOSTNAME"):
        return f'postgresql://admin:123@{os.getenv("DB_HOSTNAME")}:5432/rinha'

    return u"postgresql://admin:123@localhost:5432/rinha"


_engine = create_engine(
    url=get_db_url(),
)


def get_session():
    with Session(_engine) as session:
        yield session
