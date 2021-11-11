import sqlalchemy.orm
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, Enum, Boolean, DateTime, Text
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
    description = Column(Text, nullable=False, default="")
    token = Column(String, nullable=False, default=secrets.token_urlsafe)
    webhook = Column(String, nullable=False)

    groups = relationship("Group", back_populates="application")
    users = relationship("User", back_populates="application")


class Group(Base):
    """
    A :class:`.Group` represents a grouping of :class:`.Achievement`\\ s in an :class:`.Application`.

    If, for example, the application is a Discord Bot, the :class:`.Group` represents the Discord Guild / Server.
    """

    __tablename__ = "groups"
    __table_args__ = (
        # To avoid an application having the same server over and over, uniqueness between the crystal and the application_id is needed
        UniqueConstraint('application_id', 'crystal'),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    application_id = Column(UUID(as_uuid=True), ForeignKey("applications.id"), nullable=False)

    crystal = Column(String, nullable=False)
    """
    :class:`Application`\\ s can identify :class:`.Group`\\ s through a custom identifier, the :attr:`.crystal`, which is specified on creation.
    """

    application = relationship("Application", back_populates="groups")
    achievements = relationship("Achievement", back_populates="group")


class Achievement(Base):
    """
    An :class:`.Achievement` represents an award that can be bestowed by an :class:`.Application` to an :class:`.User`.

    All :class:`.Achievement`\\ s belong to a :class:`.Group`.
    """

    __tablename__ = "achievements"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False, default="")
    alloy = Column(Enum(Alloy), nullable=False)
    secret = Column(Boolean, nullable=False, default=False)
    icon = Column(String)
    repeatable = Column(Boolean, nullable=False, default=False)
    group_id = Column(UUID(as_uuid=True), ForeignKey("groups.id"), nullable=False)

    group = relationship("Group", back_populates="achievements")
    unlocks = relationship("Unlock", back_populates="achievement")


class Unlock(Base):
    """
    An :class:`.Unlock` represents the bestowing of an :class:`.Achievement` to an :class:`.User`.

    If the achievement is :attr:`~.Achievement.repeatable`, multiple :class:`.Unlock`\\ s for it can exist.
    """

    __tablename__ = "unlocks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column(DateTime, nullable=False, default=datetime.datetime.now)
    achievement_id = Column(UUID(as_uuid=True), ForeignKey("achievements.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    achievement = relationship("Achievement", back_populates="unlocks")
    user = relationship("User", back_populates="unlocks")


class User(Base):
    """
    An :class:`.User` is the representation of a person in an :class:`.Application`.

    If, for example, the application is a Discord Bot, the :class:`.User` represents the corresponding Discord User.
    """

    __tablename__ = "users"
    __table_args__ = (
        # To avoid an user registered to the same server over and over, uniqueness between the crystal
        # and the application_id is needed
        UniqueConstraint('application_id', 'crystal'),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    application_id = Column(UUID(as_uuid=True), ForeignKey("application.id"), nullable=False)

    crystal = Column(String, nullable=False)
    """
    :class:`Application`\\ s can identify :class:`.Group`\\ s through a custom identifier, the :attr:`.crystal`, which is specified on creation.
    """

    application = relationship("Application", back_populates="groups")
    unlocks = relationship("User", back_populates="user")
