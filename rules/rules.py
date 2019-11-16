import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, "Cog", object)


class sRules(Cog):
    """
    A sample set of rules you can use when your first starting your server to save time.
    """
    @commands.command(aliases=["rolesloose", "lrules", "rulesl"])
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def postrulesloose(self, ctx):
        """Send preconfigured rules - loose."""
        embed = discord.Embed(
            title="Server Rules"
            description="> ``1.`` No Spamming.\nThis will result in a kick.\n\n > ``2.`` No Trolling. This will result in an instant ban.\n\n > ``3.`` Do NOT mass ping any group of users or roles. Pinging a role counts as mass pinging.\n\n > ``4.`` Respect All Members. Staff and Members, everyone deserves respect.\n\n > ``5.`` Any form of NSFW content is prohibited in any and all channels within this server. A ban will be coming your way for violating this.\n\n > ``6.`` You are REQUIRED to follow Discord Terms of Service [Discord TOS](https://www.discordapp.com/tos) > ``7.`` You are REQUIRED to follow Discord's Community [Guidelines](https://www.discordapp.com/guidelines)",
            color=self.bot.main_color,
        )
        return await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(sRules(bot))
