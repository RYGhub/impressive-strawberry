import fastapi.routing
from sqlalchemy.orm import Session

from impressive_strawberry.database import tables
from impressive_strawberry.web import crud
from impressive_strawberry.web import deps
from impressive_strawberry.web import models
from impressive_strawberry.web import responses

router = fastapi.routing.APIRouter(
    prefix="/api/group/v1",
    tags=[
        "Group v1",
    ],
)

