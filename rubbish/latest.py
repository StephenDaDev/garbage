import discord
from discord.ext import commands

class latest(commands.Cog):
    """Find out whats the latest plugin to come to the market!
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["newest"])
    async def latest(self, ctx):
        """Send the latest plugin to be added to the registry"""
          await ctx.send("This doesn't work because they would need to update for it to work...")


def setup(bot):
    bot.add_cog(latest(bot))
