from uuid import UUID

import fastapi

from impressive_strawberry.database import tables, engine
from impressive_strawberry.web import crud
from impressive_strawberry.web.deps.application import dep_application_this
from impressive_strawberry.web.deps.database import dep_session
from impressive_strawberry.web.errors import ResourceNotFound

__all__ = (
    "dep_unlock_thisapp",
)


def dep_unlock_thisapp(
        unlock: UUID,
        session: engine.Session = fastapi.Depends(dep_session),
        application: tables.Application = fastapi.Depends(dep_application_this)
):
    result = crud.quick_retrieve(session, tables.Unlock, id=unlock)
    if result.user.application != application:
        raise ResourceNotFound()
    return result
