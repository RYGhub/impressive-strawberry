from uuid import UUID

import fastapi

from impressive_strawberry.database import tables, engine
from impressive_strawberry.web import crud
from impressive_strawberry.web.deps.application import dep_application_this
from impressive_strawberry.web.deps.database import dep_session

__all__ = (
    "dep_user_thisapp",
)


def dep_user_thisapp(
        session: engine.Session = fastapi.Depends(dep_session),
        application: tables.Application = fastapi.Depends(dep_application_this),
        user: str = fastapi.Query(...)
) -> tables.User:
    """
    Dependency which parses the ``user`` query parameter into a :class:`.tables.User`, trying to parse it as a UUID first, then falling back to using it as the crystal.

    It is limited to the users accessible to the application the request is being performed as.
    """
    try:
        uuid = UUID(user)
    except ValueError:
        return crud.quick_retrieve(session, tables.User, application=application, crystal=user)
    else:
        return crud.quick_retrieve(session, tables.User, application=application, id=uuid)
