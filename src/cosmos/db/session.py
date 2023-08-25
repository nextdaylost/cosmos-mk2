"""Database session."""


import contextlib
from typing import Annotated, Callable, ContextManager, Generator

import fastapi
import sqlalchemy
from sqlalchemy import orm

from cosmos.core import config


_engine = sqlalchemy.create_engine(config.settings.sqlalchemy_uri)
_session_factory = orm.scoped_session(orm.sessionmaker(autoflush=False, bind=_engine))


def session_factory() -> Generator[orm.Session, None, None]:
    """Database session factory.

    Yields:
        A SQLAlchemy ORM session.
    """
    session = _session_factory()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


SessionFactory = Annotated[
    Callable[..., ContextManager[orm.Session]],
    fastapi.Depends(lambda: contextlib.contextmanager(session_factory)),
]
