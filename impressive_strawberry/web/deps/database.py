import logging

import sqlalchemy.orm

from impressive_strawberry.database import engine

log = logging.getLogger(__name__)

__all__ = (
    "dep_session",
)


def dep_session() -> sqlalchemy.orm.Session:
    log.debug("Creating database session...")
    with engine.Session(future=True) as session:
        log.debug("Yielding control of the database session...")
        yield session
        log.debug("Closing database session...")
    log.debug("Closed database session!")
