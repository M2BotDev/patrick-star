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
    async def help(self,ctx, cmdname = None):
        """Displays this message."""
        message = ctx.message
        colors = [0x6699ff, 0xffccff, 0x99ffcc, 0xff9966, 0xffff99, 0xff0066, 0xcc00ff, 0x66ffff]
        if cmdname == None:
            for cog in self.bot.cogs:
                x = ""
                if str(cog).lower() == 'creator' and message.author.id != 264312374931095552:
                    continue
                for cmd in self.bot.get_cog_commands(cog):
                    cogcmd = self.bot.get_command(str(cmd))
                    x += f"**{str(cmd)}** | ``{str(cogcmd.help)}``\n"
                embed = discord.Embed(title = str(cog), description = self.bot.cogs[cog].__doc__+f"\n\n{x}", color = random.choice(colors))
                await message.author.send(embed=embed)
            await message.channel.send('Check your DMs :mailbox_with_mail:')
        else:
            cmdname = str(cmdname).lower()
            cog = self.bot.get_command(cmdname)
            if cog == None:
                await message.channel.send('That command doesn\'t exist! Do **oof help** to see all commands.')
                return
            w = ""
            for x in cog.aliases:
                w += x+" "
            embed = discord.Embed(color = random.choice(colors), description = f"This command is part of {str(cog.cog_name) or 'no category'}.", title="Help")
            wo = f"**NAME** >> {cog.name}\n**DESCRIPTION** >> {cog.help}"
            if w != "":
                wo += f"\n**ALIASES** >> {w}"
            embed.add_field(name="Cog Information", value=wo)
            await message.channel.send(embed=embed)

    @commands.command(no_pm=True, pass_context=True)
    async def invite(self,ctx):
        """Discord invite to my rock and the link to invite me!"""
        message = ctx.message
        await message.channel.send(embed=discord.Embed(
            title="Bot Invite",
            description="Click [here](https://discord.gg/p8BXGM7) to join my server :heart:\n\nClick [here](https://discordapp.com/oauth2/authorize?client_id=376808047064121354&scope=bot&permissions=8) to invite me to your discord! :cookie:",
            color=0xffccff
        ))

    @commands.command(no_pm=True, pass_context=True)
    async def ping(self,ctx):
        """Checks the bots response time!"""
        message = ctx.message
        await message.channel.send("Pong!")
        
def setup(bot):
    p = Utility(bot)
    bot.add_cog(p)
