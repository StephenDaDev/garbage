import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, "Cog", object)


class latest(Cog):
    """Find out whats the latest plugin to come to the market!
    """


    @commands.command(aliases=["newest"])
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def latest(self, ctx):
        """Send the latest plugin to be added to the registry"""
          await bot.say("The latest plugin is DAzVise's ServerStats Plugin!")


def setup(bot):
    bot.add_cog(latest(bot))
