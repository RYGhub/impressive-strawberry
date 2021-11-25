import fastapi.routing
from sqlalchemy.orm import Session

from impressive_strawberry.database import tables
from impressive_strawberry.web import crud
from impressive_strawberry.web import deps
from impressive_strawberry.web import models
from impressive_strawberry.web import responses
from impressive_strawberry.web.errors import DuplicatingUnrepeatableUnlock

router = fastapi.routing.APIRouter(
    prefix="/api/application/v1/this/user/v1/{user}/achievement/v1/{achievement}/unlocks/v1",
    tags=[
        "Unlock v1",
    ],
)


@router.post(
    "/",
    summary="Adds a certain achievement of a group to a user, " +
            "both belonging to the same application you're authenticating as.",
    response_model=models.full.UserFull,
)
async def unlock_create(
        *,
        session: Session = fastapi.Depends(deps.dep_session),
        achievement: tables.Achievement = fastapi.Depends(deps.dep_achievement_basic),
        user: tables.User = fastapi.Depends(deps.dep_user)
):
    if achievement in [u.achievement for u in user.unlocks] and not achievement.repeatable:
        raise DuplicatingUnrepeatableUnlock
    crud.quick_create(session, tables.Unlock(achievement_id=achievement.id, user_id=user.id))
    return user


@router.delete(
    "/{unlock}",
    summary="Removes an unlock of an user belonging to the application you're authenticating as.",
    status_code=204
)
async def unlock_delete(
        *,
        unlock: tables.Unlock = fastapi.Depends(deps.dep_unlock),
        session: Session = fastapi.Depends(deps.dep_session)
):
    session.delete(unlock)
    session.commit()
    return responses.raw.NO_CONTENT
