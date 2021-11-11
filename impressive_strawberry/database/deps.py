import sqlalchemy.orm

import impressive_strawberry.database.engine
import logging


log = logging.getLogger(__name__)


def dep_session() -> sqlalchemy.orm.Session:
    log.debug("Creating database session...")
    with impressive_strawberry.database.engine.Session(future=True) as session:
        log.debug("Yielding control of the database session...")
        yield session
        log.debug("Closing database session...")
    log.debug("Closed database session!")