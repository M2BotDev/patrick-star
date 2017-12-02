from discord.ext import commands
import discord
import json
import random
import requests

class Server:
    """Commands for the discord server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, pass_contex=True, aliases=['serverusers', 'users'])
    async def susers(self,ctx):
        """Shows how many members are in your discord."""
        message = ctx.message
        await message.channel.send(f'``{message.guild.name}`` has ``{len(message.guild.members)}`` members! :thinking:')

    @commands.command(no_pm=True, pass_context=True, aliases=['serverinfo', 'guild'])
    async def server(self,ctx):
        """Displays information about the discord server."""
        guild = ctx.guild
        message = ctx.message
        y = ""
        for x in message.guild.emojis:
            y += f"<:{x.name.lower()}:{x.id}>"
        if y == "": y = "This discord has no emojis."
        embed = discord.Embed(color = 0xff99cc, title = "Server", description = f"Basic information about {message.guild.name}")
        embed.add_field(name="Server Information", value=f"**ID** >> {guild.id}\n**REGION** >> {guild.region}\n**CREATED** >> {str(guild.created_at)[:10]}\n**MEMBERS** >> {len(guild.members)}\n**ROLES** >> {len(guild.roles)}", inline=False)
        embed.add_field(name="Extra Information", value=f"**CHANNELS** >> {len(guild.channels)}\n**EMOJIS** >> {y}\n**OWNER** >> {guild.owner.mention}", inline=False)
        embed.set_thumbnail(url=message.guild.icon_url)
        await message.channel.send(embed=embed)
    @commands.command(no_pm=True, pass_context=True, aliases=['serveremojis', 'emojis'])
    async def semojis(self, ctx):
        """Shows all the emojis in the discord!"""
        message = ctx.message
        y = ""
        for x in message.guild.emojis:
            y += f"<:{x.name.lower()}:{x.id}>"
        if y == "": y = "This discord has no emojis."
        await message.channel.send(y)

def setup(bot):
    p = Server(bot)
    bot.add_cog(p)
