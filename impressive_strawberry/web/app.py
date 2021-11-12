import fastapi
import pkg_resources

from impressive_strawberry.database.engine import engine
from impressive_strawberry.database.tables import Base
from impressive_strawberry.web.routes import app_router

app = fastapi.FastAPI(
    debug=__debug__,
    title="Impressive Strawberry",
    description="""""",
    version=pkg_resources.get_distribution("impressive_strawberry").version,
)
app.include_router(app_router)

Base.metadata.create_all(bind=engine)
