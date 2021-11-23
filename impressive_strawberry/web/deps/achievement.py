import fastapi

from impressive_strawberry.database import tables, engine
from impressive_strawberry.web import crud
from impressive_strawberry.web.deps.database import dep_session
from impressive_strawberry.web.deps.group import dep_group


def dep_achievement(
        session: engine.Session = fastapi.Depends(dep_session),
        group: tables.Group = fastapi.Depends(dep_group),
        achievement_crystal: str = fastapi.Path(...)
):
    return crud.quick_retrieve(session, tables.Group, group=group, crystal=achievement_crystal)
