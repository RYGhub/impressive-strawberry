import httpx

from impressive_strawberry.database import tables

ALLOY_EMOJI = {
    tables.Alloy.BRONZE: ":third_place:",
    tables.Alloy.SILVER: ":second_place:",
    tables.Alloy.GOLD: ":first_place:",
}

ALLOY_NAMES = {
    tables.Alloy.BRONZE: "Bronze",
    tables.Alloy.SILVER: "Silver",
    tables.Alloy.GOLD: "Gold",
}

ALLOY_COLORS = {
    tables.Alloy.BRONZE: 0xff8a3b,
    tables.Alloy.SILVER: 0xccd6dd,
    tables.Alloy.GOLD: 0xffac33,
}


def build_spoiler_row(r: str) -> str:
    if r:
        return f"||{r}||"
    else:
        return ""


def build_spoiler_description(s: str) -> str:
    return "\n".join(map(build_spoiler_row, s.split("\n")))


def build_description(ach: tables.Achievement) -> str:
    if ach.secret:
        return build_spoiler_description(ach.description)
    else:
        return ach.description


def build_obtainability_field(ach: tables.Achievement) -> dict:
    if ach.repeatable:
        value = ":repeat: Multiple times"
    else:
        value = ":one: Once"

    return {
        "name": "Obtainable",
        "value": value,
        "inline": True,
    }


def build_rarity_field(ach: tables.Achievement) -> dict:
    return {
        "name": "Rarity",
        "value": f"{ALLOY_EMOJI[ach.alloy]} {ALLOY_NAMES[ach.alloy]}",
        "inline": True,
    }


def build_icon_thumbnail(ach: tables.Achievement) -> dict:
    if ach.icon:
        return {
            "thumbnail": {
                "url": "https://example.org/a.png"
            }
        }
    else:
        return {}


def build_embed(ach: tables.Achievement) -> dict:
    return {
        "title": ach.name,
        "description": ach.description,
        "color": ALLOY_COLORS[ach.alloy],
        "fields": [
            build_rarity_field(ach),
            build_obtainability_field(ach),
        ],
        **build_icon_thumbnail(ach),
    }


def build_notify_unlock_payload(unlock: tables.Unlock) -> dict:
    return {
        "content": f"<@{unlock.user.crystal}> achieved **{ALLOY_EMOJI[unlock.achievement.alloy]} {unlock.achievement.name}**!",
        "embeds": [
            build_embed(unlock.achievement),
        ],
    }


async def notify_unlock(url: str, unlock: tables.Unlock) -> None:
    # Send the post request
    async with httpx.AsyncClient() as c:
        response: httpx.Response = await c.post(url, params={"wait": True}, json=build_notify_unlock_payload(unlock))
    # Raise if the request fails
    response.raise_for_status()
