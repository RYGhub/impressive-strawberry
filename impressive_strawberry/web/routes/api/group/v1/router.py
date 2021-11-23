from uuid import UUID

import fastapi.routing
from sqlalchemy.orm import Session

from impressive_strawberry.database import tables
from impressive_strawberry.web import crud
from impressive_strawberry.web import deps
from impressive_strawberry.web import models
from impressive_strawberry.web import responses

router = fastapi.routing.APIRouter(
    prefix="/api/application/this/group/v1",
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
    "/{group_id}",
    summary="Get a specific group that exists within your application.",
    response_model=models.full.GroupFull
)
async def group_retrieve(
        *,
        group_id: UUID,
        application: tables.Application = fastapi.Depends(deps.dep_application),
        session: Session = fastapi.Depends(deps.dep_session),
):
    return crud.quick_retrieve(session, tables.Group, application_id=application.id, id=group_id)


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
    "/{group_id}",
    summary="Update a group within the application you're authenticating as.",
    response_model=models.full.GroupFull
)
async def group_update(
        *,
        group_id: UUID,
        data: models.edit.GroupEdit,
        session: Session = fastapi.Depends(deps.dep_session),
        application: tables.Application = fastapi.Depends(deps.dep_application)
):
    return crud.quick_update(session, group, data)


@router.delete(
    "/{group_id}",
    summary="Delete a group within the application you're authenticating as.",
    status_code=204
)
async def group_delete(
        *,
        group_id: UUID,
        session: Session = fastapi.Depends(deps.dep_session),
        application: tables.Application = fastapi.Depends(deps.dep_application)
):
    group = crud.quick_retrieve(session, tables.Group, application_id=application.id, id=group_id)
    session.delete(group)
    session.commit()
    return responses.raw.NO_CONTENT
