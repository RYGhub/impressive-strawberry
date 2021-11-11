from __future__ import annotations
from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from uuid import UUID
from impressive_strawberry.database.tables import Alloy
from datetime import datetime
from abc import ABCMeta


class StrawberryModel(BaseModel, metaclass=ABCMeta):
    """
    Base model for :mod:`impressive_strawberry`\\ 's :mod:`pydantic` models.
    """

    class Config(BaseModel.Config):
        json_encoders = {
            datetime: lambda obj: obj.timestamp(),
            Alloy: lambda obj: obj.name,
        }


class StrawberryORMModel(StrawberryModel, metaclass=ABCMeta):
    """
    Extension to :class:`.StrawberryModel` which enables the :attr:`.StrawberryModel.Config.orm_mode`.
    """

    class Config(StrawberryModel.Config):
        orm_mode = True


class ApplicationCreate(StrawberryORMModel):
    """
    **Creation** model for :class:`.database.tables.Application`.
    """

    name: str
    description: str
    webhook: HttpUrl

    class Config(StrawberryORMModel.Config):
        schema_extra = {
            "example": {
                "name": "Strawberry Bot",
                "description": "A bot to integrate achievements in Discord servers.",
                "webhook": "https://discord.com/api/webhooks/123123123123123123/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            },
        }


class GroupCreate(StrawberryORMModel):
    """
    **Creation** model for :class:`.database.tables.Group`.
    """

    application_id: UUID
    crystal: str

    class Config(StrawberryORMModel.Config):
        schema_extra = {
            "example": {
                "application_id": "971851d4-b41f-46e1-a884-5b5e84a276f8",
                "crystal": "176353500710699008",
            },
        }


class AchievementCreate(StrawberryORMModel):
    """
    **Creation** model for :class:`.database.tables.Achievement`.
    """

    name: str
    description: str
    alloy: Alloy
    secret: bool
    icon: Optional[str]
    repeatable: bool
    group_id: UUID

    class Config(StrawberryORMModel.Config):
        schema_extra = {
            "example": {
                "name": "My First Achievement",
                "description": "Create your first acheivement on Strawberry!",
                "alloy": "BRONZE",
                "secret": False,
                "icon": None,
                "repeatable": False,
                "group_id": "70fd1bf3-69dd-4cde-9d41-42368221849f",
            },
        }


class UnlockCreate(StrawberryORMModel):
    """
    **Creation** model for :class:`.database.tables.Unlock`.
    """

    achievement_id: UUID
    user_id: UUID

    class Config(StrawberryORMModel.Config):
        schema_extra = {
            "example": {
                "achievement_id": "a0da6178-d1d3-48ef-984c-7bb8a75c6d3b",
                "user_id": "ee4855c6-5690-4a88-9999-950b3ae92473",
            },
        }


class UserCreate(StrawberryORMModel):
    """
    **Creation** model for :class:`.database.tables.User`.
    """

    application_id: UUID
    crystal: str

    class Config(StrawberryORMModel.Config):
        schema_extra = {
            "example": {
                "application_id": "971851d4-b41f-46e1-a884-5b5e84a276f8",
                "crystal": "77703771181817856",
            },
        }


class ApplicationRead(ApplicationCreate):
    """
    **Read** model for :class:`.database.tables.Application`.
    """

    id: UUID
    token: str

    class Config(ApplicationCreate.Config):
        schema_extra = {
            "example": {
                **ApplicationCreate.Config.schema_extra["example"],
                "id": "971851d4-b41f-46e1-a884-5b5e84a276f8",
                "token": "tLsk16aJojijZkuLQqJ-pVHnnBPVAl-G0HYavFkfmk4",
            },
        }


class GroupRead(GroupCreate):
    """
    **Read** model for :class:`.database.tables.Group`.
    """

    id: UUID

    class Config(GroupCreate.Config):
        schema_extra = {
            "example": {
                **GroupCreate.Config.schema_extra["example"],
                "id": "70fd1bf3-69dd-4cde-9d41-42368221849f",
            },
        }


class AchievementRead(AchievementCreate):
    """
    **Read** model for :class:`.database.tables.Achievement`.
    """

    id: UUID

    class Config(AchievementCreate.Config):
        schema_extra = {
            "example": {
                **AchievementCreate.Config.schema_extra["example"],
                "id": "a0da6178-d1d3-48ef-984c-7bb8a75c6d3b",
            },
        }


class UnlockRead(UnlockCreate):
    """
    **Read** model for :class:`.database.tables.Unlock`.
    """

    id: UUID
    timestamp: datetime

    class Config(UnlockCreate.Config):
        schema_extra = {
            "example": {
                **UnlockCreate.Config.schema_extra["example"],
                "id": "15e5bdfb-1b5d-4de2-acc6-fc45b01a503e",
                "timestamp": 1636600556.251724,
            },
        }


class UserRead(UserCreate):
    """
    **Read** model for :class:`.database.tables.User`.
    """

    id: UUID

    class Config(UserCreate.Config):
        schema_extra = {
            "example": {
                **UserCreate.Config.schema_extra["example"],
                "id": "ee4855c6-5690-4a88-9999-950b3ae92473",
            },
        }


class ApplicationFull(ApplicationRead):
    """
    **Full** model (with expanded relationships) for :class:`.database.tables.Application`.
    """

    groups: List[GroupRead]
    users: List[UserRead]

    class Config(ApplicationRead.Config):
        schema_extra = {
            "example": {
                **ApplicationRead.Config.schema_extra["example"],
                "groups": [
                    GroupRead.Config.schema_extra["example"],
                ],
                "users": [
                    UserRead.Config.schema_extra["example"],
                ],
            },
        }


class GroupFull(GroupRead):
    """
    **Full** model (with expanded relationships) for :class:`.database.tables.Group`.
    """

    application: ApplicationRead
    achievements: List[AchievementRead]

    class Config(GroupRead.Config):
        schema_extra = {
            "example": {
                **GroupRead.Config.schema_extra["example"],
                "application": ApplicationRead.Config.schema_extra["example"],
                "achievements": [
                    AchievementRead.Config.schema_extra["example"],
                ],
            },
        }


class AchievementFull(AchievementRead):
    """
    **Full** model (with expanded relationships) for :class:`.database.tables.Achievement`.
    """

    group: GroupRead
    unlocks: List[UnlockRead]

    class Config(AchievementRead.Config):
        schema_extra = {
            "example": {
                **AchievementRead.Config.schema_extra["example"],
                "group": GroupRead.Config.schema_extra["example"],
                "unlocks": [
                    UnlockRead.Config.schema_extra["example"],
                ],
            },
        }


class UnlockFull(UnlockRead):
    """
    **Full** model (with expanded relationships) for :class:`.database.tables.Unlock`.
    """

    achievement: AchievementRead
    user: UserRead

    class Config(UnlockRead.Config):
        schema_extra = {
            "example": {
                **UnlockRead.Config.schema_extra["example"],
                "achievement": AchievementRead.Config.schema_extra["example"],
                "user": UserRead.Config.schema_extra["example"],
            },
        }


class UserFull(UserRead):
    """
    **Full** model (with expanded relationships) for :class:`.database.tables.User`.
    """

    application: List[ApplicationRead]
    unlocks: List[AchievementRead]

    class Config(UserRead.Config):
        schema_extra = {
            "example": {
                **UserRead.Config.schema_extra["example"],
                "application": ApplicationRead.Config.schema_extra["example"],
                "unlocks": [
                    UnlockRead.Config.schema_extra["example"],
                ],
            },
        }
