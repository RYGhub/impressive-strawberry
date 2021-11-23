import fastapi.routing
from sqlalchemy.orm import Session

from impressive_strawberry.database import tables
from impressive_strawberry.web import crud
from impressive_strawberry.web import deps
from impressive_strawberry.web import models
from impressive_strawberry.web import responses

router = fastapi.routing.APIRouter(
    prefix="/api/application/v1/this/group/v1",
    tags=[
        "Group v1",
    ],
)


@router.get(
    "/",
    summary="Get the groups of the application you're authenticating as.",
    response_model=list[models.read.GroupRead],
)
async def group_list(
        *,
        application: tables.Application = fastapi.Depends(deps.dep_application),
):
    return application.groups


@router.get(
    "/{group_crystal}",
    summary="Get a specific group that exists within the application you're authenticating as.",
    response_model=models.full.GroupFull
)
async def group_retrieve(
        *,
        group: tables.Group = fastapi.Depends(deps.dep_group),
):
    return group


@router.post(
    "/",
    summary="Add a group to the application you're authenticating as.",
    response_model=models.full.GroupFull
)
async def group_create(
        *,
        data: models.edit.GroupEdit,
        session: Session = fastapi.Depends(deps.dep_session),
        application: tables.Application = fastapi.Depends(deps.dep_application)
):
    return crud.quick_create(session, tables.Group(crystal=data.crystal, application_id=application.id))


@router.put(
    "/{group_crystal}",
    summary="Update a group within the application you're authenticating as.",
    response_model=models.full.GroupFull
)
async def group_update(
        *,
        data: models.edit.GroupEdit,
        session: Session = fastapi.Depends(deps.dep_session),
        group: tables.Group = fastapi.Depends(deps.dep_group),
):
    return crud.quick_update(session, group, data)


@router.delete(
    "/{group_crystal}",
    summary="Delete a group within the application you're authenticating as.",
    status_code=204
)
async def group_delete(
        *,
        session: Session = fastapi.Depends(deps.dep_session),
        group: tables.Group = fastapi.Depends(deps.dep_group),
):
    session.delete(group)
    session.commit()
    return responses.raw.NO_CONTENT
