import typing as t
from uuid import UUID

from pydantic import HttpUrl

from impressive_strawberry.database import tables
from impressive_strawberry.web.models import base

__all__ = (
    "ApplicationEdit",
    "GroupEdit",
    "AchievementEdit",
    "UnlockEdit",
    "UserEdit",
)


class ApplicationEdit(base.StrawberryORMModel):
    """
    **Edit** model for :class:`.database.tables.Application`.
    """

    name: str
    description: str
    webhook: HttpUrl

    class Config(base.StrawberryORMModel.Config):
        schema_extra = {
            "example": {
                "name": "Strawberry Bot",
                "description": "A bot to integrate achievements in Discord servers.",
                "webhook": "https://discord.com/api/webhooks/123123123123123123/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            },
        }


class GroupEdit(base.StrawberryORMModel):
    """
    **Edit** model for :class:`.database.tables.Group`.
    """

    crystal: str

    class Config(base.StrawberryORMModel.Config):
        schema_extra = {
            "example": {
                "crystal": "176353500710699008",
            },
        }


class AchievementEdit(base.StrawberryORMModel):
    """
    **Edit** model for :class:`.database.tables.Achievement`.
    """

    name: str
    description: str
    alloy: tables.Alloy
    secret: bool
    icon: t.Optional[str]
    repeatable: bool
    crystal: str

    class Config(base.StrawberryORMModel.Config):
        schema_extra = {
            "example": {
                "name": "My First Achievement",
                "description": "Edit your first acheivement on Strawberry!",
                "alloy": "BRONZE",
                "secret": False,
                "icon": None,
                "repeatable": False,
                "crystal": "my-first-achievement"
            },
        }


class UnlockEdit(base.StrawberryORMModel):
    """
    **Edit** model for :class:`.database.tables.Unlock`.
    """

    achievement_id: UUID
    user_id: UUID

    class Config(base.StrawberryORMModel.Config):
        schema_extra = {
            "example": {
                "achievement_id": "a0da6178-d1d3-48ef-984c-7bb8a75c6d3b",
                "user_id": "ee4855c6-5690-4a88-9999-950b3ae92473",
            },
        }


class UserEdit(base.StrawberryORMModel):
    """
    **Edit** model for :class:`.database.tables.User`.
    """

    application_id: UUID
    crystal: str

    class Config(base.StrawberryORMModel.Config):
        schema_extra = {
            "example": {
                "application_id": "971851d4-b41f-46e1-a884-5b5e84a276f8",
                "crystal": "77703771181817856",
            },
        }
