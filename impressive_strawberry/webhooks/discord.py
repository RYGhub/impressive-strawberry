import httpx

from impressive_strawberry.database import tables

ALLOY_EMOJI = {
    tables.Alloy.BRONZE: ":third_place:",
    tables.Alloy.SILVER: ":second_place:",
    tables.Alloy.GOLD: ":first_place:",
}


async def notify_unlock(url: str, unlock: tables.Unlock) -> None:
    json = {
        "content": f"<@{unlock.user.crystal}> achieved **{alloy_emoji[unlock.achievement.alloy]} {unlock.achievement.name}**!"
    }

    # Send the post request
    async with httpx.AsyncClient() as c:
        response: httpx.Response = await c.post(url, params={"wait": True}, json=json)
    # Raise if the request fails
    response.raise_for_status()
