import pydantic
from typing import List, Optional
import uuid
from impressive_strawberry.database.tables import AlloyEnum
from datetime import datetime


class StrawberryModel(pydantic.BaseModel):
    pass


class StrawberryORMModel(StrawberryModel):
    class Config(StrawberryModel.Config):
        orm_mode = True


# I might have overdone this

class ApplicationCreate(StrawberryORMModel):
    """
    Application creation schema
    """
    name: str
    webhook: str


class Application(ApplicationCreate):
    """
    Application schema
    """
    id: uuid
    token: str


class GroupCreate(StrawberryORMModel):
    """
    Group creation schema
    """
    crystal: str
    application_id: uuid


class Group(GroupCreate):
    """
    Group schema
    """
    id: uuid


class AchievementCreate(StrawberryORMModel):
    """
    Achievement creation schema
    """
    name: str
    description: str
    alloy: AlloyEnum
    secret: bool
    icon: str
    repeatable: bool


class Achievement(AchievementCreate):
    """
    Achievement schema
    """
    id: uuid


class GroupFull(Group):
    """
    Group schema with expanded relationships
    """
    application: Application
    achievements: Optional[List[Achievement]]


class AchievementFull(Achievement):
    """
    Achievement schema with expanded relationships
    """
    unlocks: List[Optional["Unlock"]]


class UnlockCreate(StrawberryORMModel):
    """
    Unlock creation schema
    """
    achievement_id = uuid
    user_id = uuid


class Unlock(UnlockCreate):
    """
    Unlock schema
    """
    id = uuid
    unlocked_on: datetime


class UserCreate(StrawberryORMModel):
    """
    User creation schema
    """
    crystal: str
    application_id: uuid


class User(UserCreate):
    """
    User schema
    """
    id: uuid


class UnlockFull(Unlock):
    """
    Unlock schema with expanded relationships
    """
    achievement: Achievement
    user: User


class UserFull(User):
    """
    User schema with expanded relationships
    """
    application = Optional[List[Application]]
    unlocks = Optional[List[Achievement]]


class ApplicationFull(Application):
    """
    Application schema with expanded relationships
    """
    groups: Optional[List[Group]]
    users: Optional[List[User]]
