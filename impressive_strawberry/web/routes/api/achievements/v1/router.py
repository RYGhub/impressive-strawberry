from uuid import UUID

import fastapi.routing
from sqlalchemy.orm import Session

from impressive_strawberry.database import tables
from impressive_strawberry.web import crud
from impressive_strawberry.web import deps
from impressive_strawberry.web import models
from impressive_strawberry.web import responses

router = fastapi.routing.APIRouter(
    prefix="/api/application/this/group/{group_id}/achievements/v1",
    tags=[
        "Achievements v1",
    ],
)


@router.get(
    "/",
    summary="Get the achievements of a certain group within the application you're authenticating as.",
    response_model=list[models.read.AchievementRead]
)
async def achievements_this_retrieve(
        *,
        group_id: UUID,
        application: tables.Application = fastapi.Depends(deps.dep_application),
        session: Session = fastapi.Depends(deps.dep_session)
):
    group = crud.quick_retrieve(session, tables.Group, application_id=application.id, id=group_id)
    return group.achievements


@router.get(
    "/{achievement_id}",
    summary="Get the details of an achievement belonging to a certain group within the application you're authenticating as.",
    response_model=models.full.AchievementFull
)
async def achievement_retrieve(
        *,
        group_id: UUID,
        achievement_id: UUID,
        application: tables.Application = fastapi.Depends(deps.dep_application),
        session: Session = fastapi.Depends(deps.dep_session)
):
    group = crud.quick_retrieve(session, tables.Group, application_id=application.id, id=group_id)

    return crud.quick_retrieve(session, tables.Achievement, group_id=group.id, id=achievement_id)


@router.post(
    "/",
    summary="Create a new achievement belonging to a certain group within the application you're authenticating as.",
    response_model=models.full.AchievementFull
)
async def achievement_create(
        *,
        group_id: UUID,
        data: models.edit.AchievementEdit,
        application: tables.Application = fastapi.Depends(deps.dep_application),
        session: Session = fastapi.Depends(deps.dep_session)
):
    group = crud.quick_retrieve(session, tables.Group, application_id=application.id, id=group_id)
    return crud.quick_create(session, tables.Achievement(name=data.name, description=data.description,
                                                         alloy=data.alloy, secret=data.secret, icon=data.icon,
                                                         repeatable=data.repeatable, group_id=group.id))
