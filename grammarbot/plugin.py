from __future__ import annotations

from typing import TYPE_CHECKING, cast

import crescent
import hikari
import language_tool_python

if TYPE_CHECKING:
    from .bot import GrammarBot


plugin = crescent.Plugin()


@plugin.include
@crescent.event
async def on_message(event: hikari.GuildMessageCreateEvent) -> None:
    bot = cast(GrammarBot, event.app)

    if event.author.is_bot:
        return

    if event.content is None:
        return

    errors: list[language_tool_python.Match] = bot.tool.check(event.content)
    if not errors:
        return

    embed = hikari.Embed(description=f"Found {len(errors)} possible error(s).")
    for error in errors[0:25]:
        embed.add_field(
            name=error.ruleId,
            value=error.message
            + '\n"'
            + error.context
            + '"\n->'
            + ", ".join(error.replacements[0:5]),
        )

    await event.message.respond(embed=embed, reply=True)
