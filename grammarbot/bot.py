from __future__ import annotations

import crescent
import language_tool_python

from .config import CONFIG


class GrammarBot(crescent.Bot):
    def __init__(self) -> None:
        super().__init__(CONFIG.discord_token)

        self.tool = language_tool_python.LanguageTool("en-US")
        self.plugins.load("grammarbot.plugin")
