"""Global in-memory model base."""


import datetime
import uuid

import pydantic

from cosmos.utils import transform


class Base(pydantic.BaseModel):
    """Global in-memory model base.

    Attributes:
        id: The UUID primary key.
        created_at: A datetime of creation.
        updated_at: A datetime of most recent update.
    """

    model_config = pydantic.ConfigDict(
        alias_generator=transform.to_camel,
        from_attributes=True,
        populate_by_name=True,
    )

    id: uuid.UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
