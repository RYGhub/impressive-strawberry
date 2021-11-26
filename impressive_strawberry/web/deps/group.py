from uuid import UUID

import fastapi

from impressive_strawberry.database import tables, engine
from impressive_strawberry.web import crud
from impressive_strawberry.web.deps.application import dep_application
from impressive_strawberry.web.deps.database import dep_session

__all__ = (
    "dep_group",
)


def dep_group(
        session: engine.Session = fastapi.Depends(dep_session),
        application: tables.Application = fastapi.Depends(dep_application),
        group: str = fastapi.Query(...)
):
    try:
        uuid = UUID(group)
    except ValueError:
        return crud.quick_retrieve(session, tables.Group, application=application, crystal=group)
    else:
        return crud.quick_retrieve(session, tables.Group, application=application, id=uuid)
