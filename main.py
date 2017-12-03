# Next-gen Ro-Verify
# host on heroku? yeah. what the heck is heroku :joy: . a free place to host the bot online
# where to store data though? -->
import requests
import asyncio
import discord
from discord.ext import commands
import os
import json
import random

cmds = []
path = os.listdir('cogs')
for file in path:
    if file.endswith('.py'):
        cmds.append(file.replace('.py', ''))



client = commands.Bot(description="A bot. What do you expect this description to say?!?!",command_prefix=["oof ", "oof"],game=discord.Game(name=f"oof help 👍"))
client.remove_command("help")
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("This command requires more permissions.")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send('Ahhh!! I\'m missing permissions to use this command!!')
    else:
        print(error)

@client.event
async def on_ready():
    #await client.user.edit(username='Patrick Star', avatar=open('patrick.jpg', 'rb').read())
    if __name__ == "__main__":
        for extension in cmds:
            try:
                client.load_extension("cogs." + extension)
                print(extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))
    print("LOADED!")

  
@client.event
async def on_message(message):
    if message.author.bot == True:
        return
    if not message.guild is None:
        await client.process_commands(message)
        pass
    else:
        return

@client.event
async def on_guild_join(guild):
    for channel in guild.channels:
        try:
            await channel.send("I sexually identify as a discord bot.")
            return
        except:
            continue
  
  
client.run(str(os.environ.get('TOKEN')))
