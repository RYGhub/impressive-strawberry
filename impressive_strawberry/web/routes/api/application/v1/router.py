import fastapi.routing
from sqlalchemy.orm import Session

from impressive_strawberry.database import tables
from impressive_strawberry.database.deps import dep_session
from impressive_strawberry.web import response_schema, models, responses
from impressive_strawberry.web.auth.deps import dep_application
from impressive_strawberry.web.quick import quick_create, quick_update

router = fastapi.routing.APIRouter(
    tags=[
        "Application",
    ],
)


@router.post(
    "/",
    summary="Create a new application, and get a token.",
    response_model=models.ApplicationFull,
)
async def application_post(
        *,
        data: models.ApplicationCreate,
        session: Session = fastapi.Depends(dep_session)
):
    return quick_create(session, tables.Application(name=data.name, description=data.description, webhook=data.webhook))


@router.get(
    "/me",
    summary="Get the application you're authenticating as.",
    response_model=models.ApplicationFull,
    responses={
        **response_schema.UNAUTHORIZED,
        **response_schema.NOT_FOUND,
    },
)
async def application_get(
        *,
        application: tables.Application = fastapi.Depends(dep_application),
):
    return application


@router.put(
    "/me",
    summary="Change the details of the application you're authenticating as.",
    response_model=models.ApplicationFull,
)
async def application_put(
        *,
        application: tables.Application = fastapi.Depends(dep_application),
        data: models.ApplicationCreate,
        session: Session = fastapi.Depends(dep_session)
):
    return quick_update(session=session, obj=application, data=data)


@router.delete(
    "/me",
    summary="Delete the application you're authenticating as.",
    status_code=204,
)
async def application_delete(
        *,
        application: tables.Application = fastapi.Depends(dep_application),
        session: Session = fastapi.Depends(dep_session),
):
    session.delete(application)
    session.commit()
    return responses.NO_CONTENT
