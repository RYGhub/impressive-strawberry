import os
import uvicorn
import dotenv
from impressive_strawberry.web.app import app


dotenv.load_dotenv(".env")
dotenv.load_dotenv(".env.local")


uvicorn.run(app, port=os.environ["IS_WEB_PORT"])
