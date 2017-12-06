from discord.ext import commands
import discord
import json
import random
import requests
import os
import re
import sys
import contextlib
import io as StringIO

class Creator:
    """Commands only the bot creator can use."""
    def __init__(self, bot):
        self.bot = bot
        self.quotes = []

    @commands.command(no_pm=True, pass_context=True, aliases=['code'])
    async def eval(self,ctx,*,code=None):
        """Executes code."""
        message = ctx.message
        if message.author.id != 264312374931095552:
            return
	code = f"""{code}"""
        try:
            thetext = str(eval(code))
        except Exception as e:
            thetext = e
        if thetext == "":
            thetext = None
        await message.channel.send(f"``{thetext}``")

    @commands.command(no_pm=True, pass_context=True)
    async def reload(self,ctx):
        """Reloads cogs."""
        message = ctx.message
        if message.author.id != 264312374931095552:
            return
        cmds = []
        path = os.listdir('cogs')
        for file in path:
            if file.endswith('.py'):
                cmds.append(file.replace('.py', ''))

        for cog in cmds:
            self.bot.unload_extension("cogs."+cog)
            print('unloaded ' + cog)
        for extension in cmds:
            try:
                self.bot.load_extension("cogs." + extension)
                print(extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))
        await message.channel.send("OOF, successfully reloaded cogs!")
    @commands.command(no_pm=True, pass_contex=True, aliases=["servers", "discords"])
    async def guilds(self,ctx):
        """Servers the bot is in."""
        message = ctx.message
        if message.author.id != 264312374931095552:
            return
        info = "List of all the bots servers!"
        g = ""
        x = len(self.bot.guilds)
        if x >= 50:
            info = f"Only showing 50 out of {x} servers."
            x = 50
        for guild in self.bot.guilds[:x]:
            g += f'\n**{guild.name}** :  ``{len(guild.members)}`` members.'
            try:
                x = await guild.invites()
                g += f" [INVITE](https://discord.gg/{x[0].code})"
            except:
                pass
        embed = discord.Embed(title="Creator", description=info+"\n"+g, color=0x99ffcc)
        await message.author.send(embed=embed)
        await message.channel.send(":mailbox: check your messages!")
            
def setup(bot):
    p = Creator(bot)
    bot.add_cog(p)
