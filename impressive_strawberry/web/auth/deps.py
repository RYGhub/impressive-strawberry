import re

import fastapi
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from impressive_strawberry.database.deps import dep_session
from impressive_strawberry.database.tables import Application

dep_application_token = APIKeyHeader(
    scheme_name="application_token",
    name="Authorization",
    description="The token of the application to authenticate as.",
)


def dep_application(
        session: Session = fastapi.Depends(dep_session),
        header: str = fastapi.Security(dep_application_token),
) -> Application:
    if not header:
        raise fastapi.HTTPException(status_code=401, detail="Missing authentication header")

    if match := re.match(r"^Bearer (.+)$", header):
        token = match.group(1)
    else:
        raise fastapi.HTTPException(status_code=401, detail="Invalid authentication header")

    app = session.execute(
        select(Application).where(Application.token == token)
    ).scalar()

    if not app:
        raise fastapi.HTTPException(status_code=401, detail="Token is invalid")

    return app
