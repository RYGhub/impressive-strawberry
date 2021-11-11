import fastapi
import pkg_resources
import uvicorn
import os

from impressive_strawberry.web.routes import app_router
from impressive_strawberry.database.tables import Base
from impressive_strawberry.database.engine import engine
from impressive_strawberry.database.deps import dep_session
from impressive_strawberry.database.tables import Application


app = fastapi.FastAPI(
    debug=__debug__,
    title="Impressive Strawberry",
    description="""""",
    version=pkg_resources.get_distribution("impressive_strawberry").version,
)
app.include_router(app_router)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("IS_PORT")))