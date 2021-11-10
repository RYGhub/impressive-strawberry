import sqlalchemy.orm
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, Enum, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
import secrets
import enum
import datetime

Base = sqlalchemy.orm.declarative_base()
TOKEN_LEN = 20


class Alloy(enum.IntEnum):
    """
    An alloy represents the rarity of an :class:`.Achievement`.

    :class:`int` values represent the rarity of the achievement; higher values represent rarer achievements.

    The rarity of alloys can be compared as if they were integers:

    >>> Alloy.BRONZE < Alloy.SILVER
    True
    >>> Alloy.SILVER < Alloy.GOLD
    True
    >>> Alloy.GOLD == Alloy.GOLD
    True
    """

    BRONZE = 100
    "A common :class:`.Achievement`."

    SILVER = 250
    "An uncommon :class:`.Achievement`."

    GOLD = 1000
    "A rare :class:`.Achievement`."


class Application(Base):
    """
    An :class:`.Application` represents an entity interacting with :mod:`impressive_strawberry`, such as a website or a bot.
    """

    __tablename__ = "applications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    token = Column(String, nullable=False, default=secrets.token_urlsafe)
    webhook = Column(String, nullable=False)

    groups = relationship("Group", backref="application")
    users = relationship("User", backref="application")


class Group(Base):
    """
    Group SQLAlchemy model.
    The Group is the entity that possesses achievements.
    It can be a Discord Server, or other kinds of stuff.
    """

    __tablename__ = "groups"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    crystal = Column(String, nullable=False)

    application_id = Column(UUID(as_uuid=True), ForeignKey("application.id"), nullable=False)
    achievements = relationship("Achievement", backref="group")
    # To avoid an application having the same server over and over, uniqueness between the crystal
    # and the application_id is needed
    __table_args__ = (UniqueConstraint('application_id', 'crystal'),)


class Achievement(Base):
    """
    Achievement SQLAlchemy model.
    """

    __tablename__ = "achievement"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = Column(String, nullable=False)
    description = Column(String)
    alloy = Column(Enum(Alloy), nullable=False, default=Alloy.bronze)
    secret = Column(Boolean, nullable=False, default=False)
    icon = Column(String)
    repeatable = Column(Boolean, nullable=False, default=False)

    group_id = Column(UUID(as_uuid=True), ForeignKey("group.id"), nullable=False)


class Unlock(Base):
    """
    Unlock SQLAlchemy model.
    Used to keep track of user's progress with achievements in a group.
    """

    __tablename__ = "unlock"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    unlocked_on = Column(DateTime, nullable=False)

    achievement_id = Column(UUID(as_uuid=True), ForeignKey("achievement.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    unlocked_by = relationship("User", backref="unlocks")
    achievement = relationship("Achievement", backref="unlocks")

    def __init__(self, **kwargs):
        super(Unlock, self).__init__(**kwargs)
        self.unlocked_on = datetime.datetime.now()


class User(Base):
    """
    User SQLAlchemy model.
    Contains unique external identifier of the user.
    """

    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    crystal = Column(String, nullable=False)

    application_id = Column(UUID(as_uuid=True), ForeignKey("application.id"), nullable=False)
    # To avoid an user registered to the same server over and over, uniqueness between the crystal
    # and the application_id is needed
    __table_args__ = (UniqueConstraint('application_id', 'crystal'),)
