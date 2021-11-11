import fastapi
from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

import impressive_strawberry.web.models as models
import impressive_strawberry.database.tables as tables
from impressive_strawberry.database.deps import dep_session

app_router = fastapi.routing.APIRouter(
    prefix="/api/v1/application",
    tags=["application", ],
    responses={404: {"description": "Not found"}, 403: {"description": "Access Denied"},
               401: {"description": "Unauthorized"}}
)


# Not sure where to put this
def quick_save(session: Session, data):
    """
    **Quick_save** function that adds an object (data) to the session, commits it and refreshes before sending it back.
    """
    session.add(data)
    session.commit()
    session.refresh(data)
    return data


# Not sure where to put this
def get_or_404(session: Session, class_: object, id_: UUID):
    """
    **Get_or_404** function that performs a query in the database. If there's none, raises a 404 error.
    """
    result = session.query(class_).filter_by(id=id_).first()
    if not result:
        raise HTTPException(404)
    return result


@app_router.get("/{id_}", response_model=models.ApplicationFull)
async def application_get(id_: UUID, session: Session = fastapi.Depends(dep_session)):
    # Either add a check to enforce only the currently logged in application to be read or remove the identifier.
    return get_or_404(session, tables.Application, id_)


@app_router.post("/", response_model=models.ApplicationRead)
async def application_post(json: models.ApplicationCreate, session: Session = fastapi.Depends(dep_session)):
    return quick_save(session, tables.Application(name=json.name, description=json.description, webhook=json.webhook))


@app_router.patch("/{id_}", response_model=models.ApplicationRead)
async def application_patch(id_: UUID, json: models.ApplicationCreate, session: Session = fastapi.Depends(dep_session)):
    # Either add a check to enforce only the currently logged in application to be patched or remove the identifier.
    application: tables.Application = get_or_404(session, tables.Application, id_)
    application.name = json.name
    application.description = json.description
    application.webhook = json.webhook
    session.commit()
    return application


@app_router.delete("/{id_}")
async def application_patch(id_: UUID, session: Session = fastapi.Depends(dep_session)):
    # Either add a check to enforce only the currently logged in application to be deleted or remove the identifier.ù
    application: tables.Application = get_or_404(session, tables.Application, id_)
    session.delete(application)
    session.commit()
    raise HTTPException(204)
    # this return may seem useless, but if I don't do that fastapi gets mad. There's probably a better way to do this.
    return
