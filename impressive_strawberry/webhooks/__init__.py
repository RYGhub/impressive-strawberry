from impressive_strawberry.database import tables

from . import discord
from . import strawberry

__all__ = (
    "notify_unlock",
)

module_map = {
    tables.WebhookType.STRAWBERRY: strawberry,
    tables.WebhookType.DISCORD: discord,
}


async def notify_unlock(application: tables.Application, unlock: tables.Unlock) -> None:
    return await module_map[application.webhook_type].notify_unlock(url=application.webhook_url, unlock=unlock)
