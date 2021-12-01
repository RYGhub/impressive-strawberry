from uuid import UUID

import fastapi

from impressive_strawberry.database import tables, engine
from impressive_strawberry.web import crud
from impressive_strawberry.web.deps.application import dep_application
from impressive_strawberry.web.deps.database import dep_session
from impressive_strawberry.web.deps.group import dep_group
from impressive_strawberry.web.errors import ResourceNotFound

__all__ = (
    "dep_achievement",
    "dep_achievement_basic"
)


def dep_achievement(
        session: engine.Session = fastapi.Depends(dep_session),
        group: tables.Group = fastapi.Depends(dep_group),
        achievement: str = fastapi.Path(...)
):
    try:
        uuid = UUID(achievement)
    except ValueError:
        return crud.quick_retrieve(session, tables.Achievement, group=group, crystal=achievement)
    else:
        return crud.quick_retrieve(session, tables.Achievement, group=group, id=uuid)


def dep_achievement_basic(
        achievement: UUID,
        session: engine.Session = fastapi.Depends(dep_session),
        application: tables.Application = fastapi.Depends(dep_application),
):
    result = crud.quick_retrieve(session, tables.Achievement, id=achievement)
    if result.group.application != application:
        raise ResourceNotFound()
    return result
