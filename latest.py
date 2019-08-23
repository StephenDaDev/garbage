import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, "Cog", object)


class latest(Cog):
    """Find out whats the latest plugin to come to the market!
    """


    @commands.command(aliases=["helpers", "supporters", "supportmembers"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def support(self, ctx):
        """Send an embed with all the support members."""
          


def setup(bot):
    bot.add_cog(latest(bot))
