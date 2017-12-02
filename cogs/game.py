import discord
from discord.ext import commands
import requests
import json
import re
from bs4 import BeautifulSoup

class Game:
    """Commands for games such as Minecraft, Roblox, & more!"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(no_pm=True, pass_contex=True, aliases=['rowiki'])
    async def robloxwiki(self,ctx,*,arguments=None):
        """Searches the roblox wiki."""
        message = ctx.message
        if arguments == None:
            await message.channel.send("Listen buddy, I need something to search for.")
            return
        arguments = arguments.replace(" ", "%20")
        response = requests.get("https://www.google.com/search?safe=on&q=site%3Awiki.roblox.com%20"+arguments.lower())
        soup = BeautifulSoup(response.text, "html.parser")
        delivered = soup.find_all(class_="r")
        links = soup.find_all('cite')
        try:
            string = ""
            y = 0
            for x in delivered[:5]:
                try:
                    string += f"\n [{delivered[y].get_text()}]({'http://'+links[y].text.replace('(', '%28').replace(')', '%29')})".replace('/url?q=', '')
                except Exception as e:
                    pass
                y+=1
            if y == 0:
                await message.channel.send("Welp, I didn't find anything.")
                return
        except Exception as e:
            await message.channel.send("Welp, I didn't find anything.")
            return

        await message.channel.send(embed=discord.Embed(
            title="Roblox Wiki",
            description="Is this not what you're looking for? Search again noob!\n" + string,
            color=0x0BFFF
        ))

    @commands.command(no_pm=True, pass_context=True, aliases=['minecrafthistory'])
    async def mchistory(self,ctx, mcname=None):
        """Gets a users name history."""
        message = ctx.message
        if mcname == None:
            await message.channel.send("Enter a ***current*** minecraft name first!")
            return
        try:
            uuid = json.loads(requests.get(f'https://api.mojang.com/users/profiles/minecraft/{mcname}').text)['id']
            api = json.loads(requests.get(f'https://api.mojang.com/user/profiles/{uuid}/names').text)
            embed = discord.Embed(description = f'Username history of {mcname}', color=0x0BFFF)
            embed.add_field(name="Times Changed", value=f"{len(api)-1}", inline=True)
            embed.add_field(name="First Name", value=f"{api[0]['name']}", inline=True)
            embed.add_field(name="Current Name", value=f"{api[-1]['name']}", inline=True)
            embed.set_image(url=f"https://crafatar.com/avatars/{uuid}")
            await message.channel.send(embed=embed)
        except:
            await message.channel.send("Invalid username! Make sure the username is ***current***")


def setup(bot):
    p = Game(bot)
    bot.add_cog(p)
