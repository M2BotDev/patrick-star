from discord.ext import commands
import discord
import json
import random
import requests

class Moderation:
    """Commands for moderating your server."""
    def __init__(self, bot):
        self.bot = bot

    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @commands.command(no_pm=True, pass_contex=True, aliases=['prune', 'bulk', 'bulkdelete', 'bulkremove', 'clean'])
    async def purge(self,ctx,amount=None):
        """Purges messages."""
        message = ctx.message
        try:
            amount = int(amount)
        except:
            pass
        if amount is None or not isinstance(amount, int):
            embed_cmdname = "purge"
            embed_cmdexample = "oof purge 12"

            embed_cmd = self.bot.get_command(embed_cmdname)
            aliases = ""
            for alias in embed_cmd.aliases:
                aliases += "-"+alias+" "
            if aliases == " ":
                aliases = ':no_entry_sign:'
            text = f"**ALIASES** {aliases}\n**DESCRIPTION** {embed_cmd.help}\n**USAGE**\n{embed_cmdexample}"
            embed = discord.Embed(title=f"Command: -{embed_cmdname}", description = text, color=0xff0066)
            await message.channel.send(embed=embed)
            return
        
        if amount > 100:
            await message.channel.send(f':rage: It can\'t be anymore than 100!!')
            return
        if amount < 2:
            await message.channel.send(f':rage: It can\'t be anyless than 2!!')
            return

        try:
            await message.channel.purge(limit = int(amount), bulk = True)
            await message.channel.send(f':raised_hand: :weary: :ok_hand: Purged!')
        except:
            await message.channel.send(f':sweat_drops: I couldn\'t purge!')
            return

    @commands.bot_has_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    @commands.command(no_pm=True, pass_contex=True, aliases=['delete'])
    async def kick(self,ctx):
        """Kicks a user from the discord."""
        message = ctx.message
        if len(message.mentions) <= 0:
            embed_cmdname = "kick"
            embed_cmdexample = "oof kick @someguy#1234"

            embed_cmd = self.bot.get_command(embed_cmdname)
            aliases = ""
            for alias in embed_cmd.aliases:
                aliases += "-"+alias+" "
            if aliases == " ":
                aliases = ':no_entry_sign:'
            text = f"**ALIASES** {aliases}\n**DESCRIPTION** {embed_cmd.help}\n**USAGE**\n{embed_cmdexample}"
            embed = discord.Embed(title=f"Command: -{embed_cmdname}", description = text, color=0xff0066)
            await message.channel.send(embed=embed)
            return
        if message.content.startswith("oof "):
            if len(message.mentions) <= 0:
                await message.channel.send('Do you mind adding someone for me to kick?')
                return
            member = message.mentions[0]
        try:
            await member.kick()
            await message.channel.send(f'I have successfully removed {member.mention}')
        except:
            await message.channel.send(f'Well, that could of went better than expected. I wasn\'t able to kick {member.name}..')
            return

    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    @commands.command(no_pm=True, pass_contex=True, aliases=['permdelete'])
    async def ban(self,ctx):
        """Bans a user from the discord."""
        message = ctx.message
        if len(message.mentions) <= 0:
            embed_cmdname = "ban"
            embed_cmdexample = "oof ban @someguy#1234"

            embed_cmd = self.bot.get_command(embed_cmdname)
            aliases = ""
            for alias in embed_cmd.aliases:
                aliases += "-"+alias+" "
            if aliases == " ":
                aliases = ':no_entry_sign:'
            text = f"**ALIASES** {aliases}\n**DESCRIPTION** {embed_cmd.help}\n**USAGE**\n{embed_cmdexample}"
            embed = discord.Embed(title=f"Command: -{embed_cmdname}", description = text, color=0xff0066)
            await message.channel.send(embed=embed)
            return

        try:
            await member.ban()
            await message.channel.send(f'I have successfully deleted {member.mention}')
        except:
            await message.channel.send(f'Well, that could of went better than expected. I wasn\'t able to ban {member.name}..')
            return



def setup(bot):
    p = Moderation(bot)
    bot.add_cog(p)
