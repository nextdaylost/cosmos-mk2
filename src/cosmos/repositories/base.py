"""Global repository base."""


from typing import Generic, Type, TypeVar
import uuid

import pydantic
from sqlalchemy import orm

from cosmos.db import (
    base as db_base,
    exceptions as db_exceptions,
    session as db_session,
)
from cosmos.models import base as imm_base


_ModelType = TypeVar("_ModelType", bound=imm_base.Base)
_ModelOrmType = TypeVar("_ModelOrmType", bound=db_base.Base)
_CreateDtoType = TypeVar("_CreateDtoType", bound=pydantic.BaseModel)
_UpdateDtoType = TypeVar("_UpdateDtoType", bound=pydantic.BaseModel)


class RepositoryBase(
    Generic[_ModelType, _ModelOrmType, _CreateDtoType, _UpdateDtoType]
):
    """Global repository base.

    _model: The type of object used in application memory.
    _model_orm: The type of object stored in the database.
    _session_factory: A database session factory.
    """

    def __init__(
        self,
        model: Type[_ModelType],
        model_orm: Type[_ModelOrmType],
        session_factory: db_session.SessionFactory,
    ) -> None:
        """Constructor.

        model: The type of object used in application memory.
        model_orm: The type of object stored in the database.
        session_factory: A database session factory.
        """
        self._model = model
        self._model_orm = model_orm
        self._session_factory = session_factory

    def _create(
        self,
        session: orm.Session,
        dto: Type[_CreateDtoType],
    ) -> Type[_ModelOrmType]:
        """Creates a resource in the database.

        Used for intra-repository operations.

        Returns:
            The ORM representation of the specified resource.
        """
        obj_orm = self._model_orm(**dto.model_dump())
        session.add(obj_orm)
        return obj_orm

    def _delete_by_id(
        self,
        session: orm.Session,
        resource_id: uuid.UUID,
    ) -> None:
        """Deletes a resource in the database.

        Used for intra-repository operations.
        """
        obj_orm = self._get_by_id(session, resource_id)
        session.delete(obj_orm)

    def _get_by_id(
        self,
        session: orm.Session,
        resource_id: uuid.UUID,
    ) -> Type[_ModelOrmType]:
        """Retrieves a resource in the database.

        Used for intra-repository operations.

        Returns:
            The ORM representation of the specified resource.
        """
        obj_orm = session.query(self._model_orm).get(resource_id)
        if not obj_orm:
            raise db_exceptions.NotFoundException(Type[self._model_orm], resource_id)
        return obj_orm

    def create(self, dto: Type[_CreateDtoType]) -> _ModelType:
        """Creates a resource in the database.

        Returns:
            The in-memory representation of the specified resource.
        """
        with self._session_factory() as session:
            obj_orm = self._create(session, dto)
            session.commit()
            session.refresh(obj_orm)
            return self._model.model_validate(obj_orm)

    def delete(self, resource_id: uuid.UUID) -> None:
        """Creates a resource in the database."""
        with self._session_factory() as session:
            self._delete_by_id(session, resource_id)
            session.commit()

    def get(self, resource_id: uuid.UUID) -> _ModelType:
        """Creates a resource in the database.

        Returns:
            The in-memory representation of the specified resource.
        """
        with self._session_factory() as session:
            obj_orm = self._get_by_id(session, resource_id)
            return self._model.model_validate(obj_orm)

    def list(
        self,
        *,
        limit: pydantic.NonNegativeInt = 100,
        offset: pydantic.NonNegativeInt = 0,
    ) -> list[_ModelType]:
        """Creates a resource in the database.

        Returns:
            A list of in-memory representations for the resource type.
        """
        with self._session_factory() as session:
            obj_orm_list = (
                session.query(self._model_orm).offset(offset).limit(limit).all()
            )
            return [self._model.model_validate(obj_orm) for obj_orm in obj_orm_list]

    def update(self, resource_id: uuid.UUID, dto: Type[_UpdateDtoType]) -> _ModelType:
        """Creates a resource in the database.

        Returns:
            The in-memory representation of the specified resource.
        """
        with self._session_factory() as session:
            obj_orm = self._get_by_id(session, resource_id)
            for k, v in dto.model_dump().items():
                setattr(obj_orm, k, v)
            session.commit()
            session.refresh(obj_orm)
            return self._model.model_validate(obj_orm)
