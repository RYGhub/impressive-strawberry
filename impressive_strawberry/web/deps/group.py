from uuid import UUID

import fastapi

from impressive_strawberry.database import tables, engine
from impressive_strawberry.web import crud
from impressive_strawberry.web.deps.application import dep_application
from impressive_strawberry.web.deps.database import dep_session


def dep_group(
        session: engine.Session = fastapi.Depends(dep_session),
        application: tables.Application = fastapi.Depends(dep_application),
        group_id: UUID = fastapi.Path(...)
):
    return crud.quick_retrieve(session, tables.Group, application_id=application.id, id=group_id)
