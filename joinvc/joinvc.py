"""
Join VC plugin for Modmail.
Command Written By: "JakeCodes" on stackoverflow
Compiled for Modmail Plugin Usage by Stephen.
"""

from discord import Embed
from discord.ext.commands import Bot, Cog, Context, command

from core.checks import has_permissions
from core.models import PermissionLevel


class joinVC(Cog):
    """
    Join VC plugin for Modmail.
    Command Written By: "JakeCodes" on stackoverflow
    Compiled for Modmail Plugin Usage by Stephen.
    """

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command(aliases=["joinvc", "j", "joining"])
    @has_permissions(PermissionLevel.REGULAR)
    async def join(self, ctx: Context) -> None:
        """Send an embed with all the support members."""
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")





def setup(bot: Bot) -> None:
    """Bot cog load."""
    bot.add_cog(joinVC(bot))
