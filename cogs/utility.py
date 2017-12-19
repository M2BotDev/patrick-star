from discord.ext import commands
import discord
import json
import random
import requests
import os

class Utility:
    """Other commands."""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(no_pm=True, pass_contex=True, aliases=['halp', 'cmds', 'cmdz', 'commands', 'commandz'])
    async def help(self,ctx):
        """Gives you help."""
        message = ctx.message
        strng = ""
        try:
            for cog in self.bot.cogs:
                if str(cog).lower() == "creator" and message.author.id != 264312374931095552:
                    continue
                print(cog)
                strng += f"\n***__{cog}__***\n\n"
                for command in self.bot.get_cog_commands(cog):
                    strng += f"**{str(command)}** : *{self.bot.get_command(str(command)).help}*\n"
            await message.author.send(strng)
            await message.channel.send(":mailbox: Commands in your messages!")
        except:
            await message.channel.send("I wasn't able to DM you! Please enable dms from server members.")
        
                
    @commands.command(no_pm=True, pass_context=True)
    async def invite(self,ctx):
        """Gives you an invite."""
        message = ctx.message
        await message.channel.send(embed=discord.Embed(
            title="Bot Invite",
            description="Click [here](https://discord.gg/p8BXGM7) to join my server :heart:\n\nClick [here](https://discordapp.com/oauth2/authorize?client_id=376808047064121354&scope=bot&permissions=8) to invite me to your discord! :cookie:",
            color=0xffccff
        ))

    @commands.command(no_pm=True, pass_context=True)
    async def ping(self,ctx):
        """Pong!"""
        message = ctx.message
        await message.channel.send("Pong!")
        
def setup(bot):
    p = Utility(bot)
    bot.add_cog(p)
