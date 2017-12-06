from discord.ext import commands
import discord
import json
import random
import requests

class Moderation:
    """Commands for moderating your server."""
    def __init__(self, bot):
        self.bot = bot
    @commands.has_permissions(manage_messages=True)
    @commands.command(no_pm=True, pass_contex=True, aliases=['prune', 'bulk', 'bulkdelete', 'bulkremove', 'clean'])
    async def purge(self,ctx,amount=None):
        """Clears messages."""
        message = ctx.message
        if amount is None:
            await message.channel.send(f'If you want to purge messages, you need to enter a value for me to purge.')
            return
        try:
            amount = int(amount)
        except:
            await message.channel.send(f'Did you really attempt to purge ``{amount}`` messages?')
            return
        
        if amount > 300:
            await message.channel.send(f'You\'re really pushing my buttons. No bigger than 300!')
            return

        try:
            await message.channel.purge(limit = int(amount), bulk = True)
            await message.channel.send(f'I successfully purged ``{amount}`` messages! Can I get a cookie? :cookie:')
        except:
            await message.channel.send(f'I\'m sorry I failed to purge ``{amount}`` messages. Please don\'t hurt me!')
            return

    @commands.has_permissions(kick_members=True)
    @commands.command(no_pm=True, pass_contex=True, aliases=['delete'])
    async def kick(self,ctx):
        """Kicks a member from the discord server."""
        message = ctx.message
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

    @commands.has_permissions(ban_members=True)
    @commands.command(no_pm=True, pass_contex=True, aliases=['permdelete'])
    async def ban(self,ctx):
        """Bans a member from the discord server."""
        message = ctx.message
        if message.content.startswith("oof "):
            if len(message.mentions) <= 0:
                await message.channel.send('Do you mind adding someone for me to ban?')
                return
            member = message.mentions[0]
        try:
            await member.ban()
            await message.channel.send(f'I have successfully deleted {member.mention}')
        except:
            await message.channel.send(f'Well, that could of went better than expected. I wasn\'t able to ban {member.name}..')
            return



def setup(bot):
    p = Moderation(bot)
    bot.add_cog(p)
