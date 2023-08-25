"""Global ORM base."""


import uuid

import sqlalchemy
from sqlalchemy.ext import declarative
from sqlalchemy.sql import functions


@declarative.as_declarative()
class Base:
    """Global ORM base.

    Attributes:
        id: The UUID primary key.
        created_at: An ISO-8601 timestamp of creation.
        updated_at: An ISO-8601 timestamp of most recent update.
    """

    __abstract__ = True

    id = sqlalchemy.Column(
        sqlalchemy.Uuid,
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
    )
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        nullable=False,
        default=functions.func.current_timestamp(),
    )
    updated_at = sqlalchemy.Column(
        sqlalchemy.DateTime,
        nullable=False,
        default=functions.func.current_timestamp(),
        onupdate=functions.func.current_timestamp(),
    )
