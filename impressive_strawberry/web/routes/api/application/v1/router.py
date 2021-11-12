from uuid import UUID

import fastapi.routing
from sqlalchemy.orm import Session

from impressive_strawberry.database import tables
from impressive_strawberry.database.deps import dep_session
from impressive_strawberry.web import response_schema, models, responses
from impressive_strawberry.web.quick import quick_create, quick_retrieve, quick_update

app_router = fastapi.routing.APIRouter(
    tags=[
        "application",
    ],
)


# FIXME: Either add a check to enforce only the currently logged in application to be read or remove the identifier.


@app_router.get(
    "/{id_}",
    response_model=models.ApplicationFull,
    responses={
        **response_schema.NOT_FOUND
    },
)
async def application_get(
        id_: UUID,
        session: Session = fastapi.Depends(dep_session)
):
    return quick_retrieve(session=session, table=tables.Application, id=id_)


@app_router.post(
    "/",
    response_model=models.ApplicationFull,
)
async def application_post(
        data: models.ApplicationCreate,
        session: Session = fastapi.Depends(dep_session)
):
    return quick_create(session, tables.Application(name=data.name, description=data.description, webhook=data.webhook))


@app_router.put(
    "/{id_}",
    response_model=models.ApplicationFull,
)
async def application_put(
        id_: UUID,
        data: models.ApplicationCreate,
        session: Session = fastapi.Depends(dep_session)
):
    application: tables.Application = quick_retrieve(session=session, table=tables.Application, id=id_)
    return quick_update(session=session, obj=application, data=data)


@app_router.delete(
    "/{id_}",
    status_code=204,
)
async def application_patch(id_: UUID, session: Session = fastapi.Depends(dep_session)):
    application: tables.Application = quick_retrieve(session=session, table=tables.Application, id=id_)
    session.delete(application)
    session.commit()
    return responses.NO_CONTENT
