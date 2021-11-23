from uuid import UUID

import fastapi

from impressive_strawberry.database import tables, engine
from impressive_strawberry.web import crud
from impressive_strawberry.web.deps.database import dep_session
from impressive_strawberry.web.deps.group import dep_group

__all__ = (
    "dep_achievement",
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
