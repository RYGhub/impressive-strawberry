import httpx
from impressive_strawberry.database import tables

alloy_emoji = {
    tables.Alloy.BRONZE: "🥉",
    tables.Alloy.SILVER: "🥈",
    tables.Alloy.GOLD: "🥇",
}


async def notify_unlock(url: str, unlock: tables.Unlock) -> None:
    json = {
        "content": f"<@{unlock.user.crystal}> achieved **{alloy_emoji[unlock.achievement.alloy]} {unlock.achievement.name}**!"
    }

    # Send the post request
    response: httpx.Response = await httpx.post(url, params={"wait": True}, json=json)
    # Raise if the request fails
    response.raise_for_status()
