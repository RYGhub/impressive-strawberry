from uuid import UUID

import fastapi

from impressive_strawberry.database import tables, engine
from impressive_strawberry.web import crud
from impressive_strawberry.web.deps.application import dep_application
from impressive_strawberry.web.deps.database import dep_session

__all__ = (
    "dep_user",
)


def dep_user(
        session: engine.Session = fastapi.Depends(dep_session),
        application: tables.Application = fastapi.Depends(dep_application),
        user: str = fastapi.Query(...)
):
    try:
        uuid = UUID(user)
    except ValueError:
        return crud.quick_retrieve(session, tables.User, application=application, crystal=user)
    else:
        return crud.quick_retrieve(session, tables.User, application=application, id=uuid)
