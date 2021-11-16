import os

import dotenv

dotenv.load_dotenv(".env", override=True)
dotenv.load_dotenv(".env.local", override=True)

import uvicorn
from impressive_strawberry.web.app import app

uvicorn.run(app, port=int(os.environ["IS_WEB_PORT"]))
