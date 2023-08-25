"""Local development database initialization helper."""


from cosmos.db import base, session


def initialize_db() -> None:
    """Creates database resources attached to the global ORM base class.

    Not for production use.
    """
    base.Base.metadata.create_all(session._engine)
