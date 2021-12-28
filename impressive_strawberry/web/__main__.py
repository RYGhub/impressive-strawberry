import logging
import os

import alembic.config
import dotenv
import uvicorn

logging.basicConfig(level="DEBUG")
log = logging.getLogger(__name__)

dotenv.load_dotenv(".env", override=True)
dotenv.load_dotenv(".env.local", override=True)

from impressive_strawberry.web.app import app

log.info("Running migrations with Alembic...")
alembic.config.main(argv=["--raiseerr", "upgrade", "head"])
log.info("Running impressive_strawberry with Uvicorn...")
uvicorn.run(app, port=int(os.environ["IS_WEB_PORT"]))
