from __future__ import annotations

import crescent
import hikari

from .config import CONFIG


class GrammarBot(crescent.Bot):
    def __init__(self) -> None:
        super().__init__(CONFIG.discord_token)

        self.plugins.add_plugin(plugin)


plugin = crescent.Plugin("main-plugin")


@plugin.include
@crescent.event
async def on_message(event: hikari.GuildMessageCreateEvent) -> None:
    if event.author.is_bot:
        return

    await event.message.respond("Hello, world!")
