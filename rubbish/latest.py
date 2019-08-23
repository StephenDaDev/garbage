import discord
from discord.ext import commands

class latest(Cog):
    """Find out whats the latest plugin to come to the market!
    """


    @commands.command(aliases=["newest"])
    async def latest(self, ctx):
        """Send the latest plugin to be added to the registry"""
          await ctx.send("The latest plugin is DAzVise's ServerStats Plugin!")


def setup(bot):
    bot.add_cog(latest(bot))
