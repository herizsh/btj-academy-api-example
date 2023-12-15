from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "postgresql://username:password@localhost/dbname"

engine = create_engine(DATABASE_URI, echo=True)

Session = sessionmaker(bind=engine)


@contextmanager
def get_session(autocommit=True):
    """Context manager for database sessions."""
    session = Session()
    try:
        yield session
        if autocommit:
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
