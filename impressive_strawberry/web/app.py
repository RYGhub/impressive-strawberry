import fastapi
import pkg_resources

from impressive_strawberry.web.routes.api.application.v1.router import router as router_api_application_v1

app = fastapi.FastAPI(
    debug=__debug__,
    title="Impressive Strawberry",
    description="""""",
    version=pkg_resources.get_distribution("impressive_strawberry").version,
)
app.include_router(
    router_api_application_v1,
    prefix="/api/application/v1",
)
