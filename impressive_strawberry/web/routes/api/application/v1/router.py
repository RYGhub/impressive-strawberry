import fastapi.routing
from sqlalchemy.orm import Session

from impressive_strawberry.database import tables
from impressive_strawberry.web import crud
from impressive_strawberry.web import deps
from impressive_strawberry.web import models
from impressive_strawberry.web import responses

router = fastapi.routing.APIRouter(
    prefix="/api/application/v1",
    tags=[
        "Application v1",
    ],
)


@router.post(
    "/",
    summary="Create a new application, and get a token.",
    response_model=models.full.ApplicationFull,
)
async def application_create(
        *,
        data: models.edit.ApplicationEdit,
        session: Session = fastapi.Depends(deps.dep_session)
):
    return crud.quick_create(session, tables.Application(name=data.name, description=data.description, webhook=data.webhook))


@router.get(
    "/this",
    summary="Get the application you're authenticating as.",
    response_model=models.full.ApplicationFull,
)
async def application_this_retrieve(
        *,
        application: tables.Application = fastapi.Depends(deps.dep_application),
):
    return application


@router.put(
    "/this",
    summary="Change the details of the application you're authenticating as.",
    response_model=models.full.ApplicationFull,
)
async def application_this_update(
        *,
        application: tables.Application = fastapi.Depends(deps.dep_application),
        data: models.edit.ApplicationEdit,
        session: Session = fastapi.Depends(deps.dep_session)
):
    return crud.quick_update(session=session, obj=application, data=data)


@router.delete(
    "/this",
    summary="Delete the application you're authenticating as.",
    status_code=204,
)
async def application_this_delete(
        *,
        application: tables.Application = fastapi.Depends(deps.dep_application),
        session: Session = fastapi.Depends(deps.dep_session),
):
    session.delete(application)
    session.commit()
    return responses.raw.NO_CONTENT