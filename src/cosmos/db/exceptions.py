"""Database-related exceptions."""


from typing import Type, TypeVar
import uuid


_ModelType = TypeVar("_ModelType")


class NotFoundException(Exception):
    """Resource is not accessible."""

    def __init__(self, resource_type: Type[TypeVar], resource_id: uuid.UUID):
        """Constructor.

        resource_type: The type of object attempting to be accessed.
        resource_id: The id of the object attempting to be accessed.
        """
        super().__init__(f"{resource_type.__name__} '{resource_id}' not found.")
