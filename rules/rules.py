import asyncio
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class Rules(commands.Cog):
    """
    A sample set of rules you can use when your first starting your server to save time.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["rulesloose", "lrules", "rulesl"])
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def postrulesloose(self, ctx):
        """Send preconfigured rules - loose."""
        embed = discord.Embed(
            title="Server Rules"
        )
        embed.description="""
                > ``1.`` No Spamming. 
                • This will result in a kick.
                > ``2.`` No Trolling.
                • This will result in an instant ban.
                > ``3.`` Do NOT mass ping any group of users or roles.
                • Pinging a role counts as mass pinging
                > ``4.`` Respect All Members.
                • Staff and Members, everyone deserves respect.
                > ``5.`` Any form of NSFW content is prohibited in any and all channels within this server.
                • A ban will be coming your way for violating this.
                > ``6.`` You are REQUIRED to follow Discord Terms of Service (Discord TOS).
                • https://www.discordapp.com/tos
                > ``7.`` You are REQUIRED to follow Discord's Community Guidelines.
            • https://www.discordapp.com/guidelines
            """
        embed.color=self.bot.main_color
        return await ctx.send(embed=embed)

    @commands.command(aliases=["rulesnormal", "nrules", "rulesn"])
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def postrulesnormal(self, ctx):
        """Send preconfigured rules - normal."""
        embed = discord.Embed(
            title="Server Rules"
        )
        embed.description="""
                > ``1.`` No Spamming. 
                • This will result in a kick.
                
                > ``2.`` No Trolling.
                • This will result in an instant ban.
                
                > ``3.`` Do not beg for staff roles.
                • It will make your chances of becoming staff 2000 time harder.

                > ``4.`` Do NOT mass ping any group of users or roles.
                • Pinging a role counts as mass pinging

                > ``5.`` Any offensive usernames or nicknames will be changed to an appropriate name by use of the nicknaming feature.

                > ``6.`` Respect All Members.
                • Staff and Members, everyone deserves respect.

                > ``7.`` Any form of NSFW content is prohibited in any and all channels within this server.
                • A ban will be coming your way for violating this.

                > ``8.`` You are REQUIRED to follow Discord Terms of Service (Discord TOS).
                • https://www.discordapp.com/tos

                > ``9.`` You are REQUIRED to follow Discord's Community Guidelines.
                • https://www.discordapp.com/guidelines
            """
        embed.color=self.bot.main_color
        return await ctx.send(embed=embed)

    @commands.command(aliases=["rulesstrict", "srules", "ruless"])
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def postrulesstrict(self, ctx):
        """Send preconfigured rules - strict."""
        embed = discord.Embed(
            title="Server Rules"
        )
        embed.description = """
                > ``1.`` No Spamming. 
                • This will result in a kick.

                > ``2.`` No Trolling.
                • This will result in an instant ban.

                > ``3.`` Do not beg for staff roles.
                • It will make your chances of becoming staff 2000 time harder.

                > ``4.`` Do NOT mass ping any group of users or roles.
                • Pinging a role counts as mass pinging

                > ``5.`` You must do anything and everything staff members tell you to do.
                
                > ``6.`` Respect All Members.
                • Staff and Members, everyone deserves respect.

                > ``7.`` Any form of NSFW content is prohibited in any and all channels within this server.
                • A ban will be coming your way for violating this.

                > ``8.`` You are REQUIRED to follow Discord Terms of Service (Discord TOS).
                • https://www.discordapp.com/tos

                > ``9.`` You are REQUIRED to follow Discord's Community Guidelines.
                • https://www.discordapp.com/guidelines
                
                > ``10.`` All nicknames must be approved by the Staff Team, DM this bot for approval.
                
                > ``11.`` You may not lie to anyone, else you will receive punishment.
                
                > ``12.`` Posting any content in this server, outside of the server without the express consent of the owner is prohibited.
                • ie. You can not post a picture of general chat outside of the server.
                
                > ``13.`` You may not use any word in which is defined as mean or inappropriate in any text or voice channel.
                • Therefore, the f word, s word, d word, or any other word a Kindergartner isn't supposed to say is prohibited.
                
                > ``14.`` Mention of any outside resource not in this server will count as advertising.
            """

        embed.color = self.bot.main_color
        return await ctx.send(embed=embed)

    @commands.command(aliases=["rulessuggest", "fixthesethings"])
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def suggestrules(self, ctx):
        """Learn about how to suggest changes to this plugin and its pre-made set of rules"""
        embed = discord.Embed(
            title="Suggestion Instructions"
        )
        embed.description="""
                If you'd like to suggest something for this plugin (anything, formatting changes, or rule changes)
                join the plugin server [https://discord.gg/4JE4XSW](https://discord.gg/4JE4XSW) and make contact with ``Stephen#2806``
            """
        embed.color=self.bot.main_color
        return await ctx.send(embed=embed)

# piyush is the only reason this works

def setup(bot):
    bot.add_cog(Rules(bot))
