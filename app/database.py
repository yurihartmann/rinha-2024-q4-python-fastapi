from sqlmodel import create_engine, Session

_engine = create_engine(
    url=u"postgresql://admin:123@localhost:5432/rinha",
)


def get_session():
    with Session(_engine) as session:
        yield session
