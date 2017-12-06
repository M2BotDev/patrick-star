from discord.ext import commands
import discord
import json
import random
import requests
import os
import re
import math

class Fun:
    """Fun commands!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, pass_context=True, aliases=['startvote', 'createvote', 'poll'])
    async def vote(self,ctx,*,votetext=None):
        """Creates a vote!"""
        message = ctx.message
        if votetext == None:
            await message.channel.send('I need something to say!')
            return
        embed = discord.Embed(tile="Vote", description=votetext,color=0xff0066)
        embed.set_footer(text='Vote created by '+message.author.name+"#"+message.author.discriminator, icon_url=message.author.avatar_url)
        xmsg = await message.channel.send(embed=embed)
        try:
            em1 = "\U00002705"
            em2 = "\U0000274e"
            await xmsg.add_reaction(em1)
            await xmsg.add_reaction(em2)
        except:
            await message.channel.send('Couldn\'t add reactions.. :sob:')
        try:
            await message.delete()
        except:
            pass

    @commands.command(no_pm=True, pass_context=True, aliases=['userinformation', 'user'])
    async def userinfo(self,ctx):
        """Gets a user information."""
        message = ctx.message
        user = message.author
        if len(message.mentions) >= 1:
            user = message.mentions[0]
        name = user.name
        fullname = user.name+"#"+user.discriminator
        mention = user.mention
        id_ = user.id
        nick = user.display_name
        bot = "No"
        created = user.created_at
        if user.bot:
            bot="Yes"
        if nick == name:
            nick = "No nickname"
        roles = "|"
        for role in user.roles:
            roles += f" {role.mention} |"
        highest_role = user.roles[len(user.roles)-1].mention
        embed=discord.Embed(title="Fun", description=f"Information for {name}", color=0xff0066)
        embed.add_field(name='User', value=f'**NAME** >> {name}\n**TAG** >> {fullname}\n**MENTION** >> {mention}\n**ID** >> {id_}\n**BOT** >> {bot}\n**CREATED** >> {created}', inline=False)
        embed.add_field(name='Server', value=f'**ROLES** >> {roles}\n**HIGHEST ROLE** >> {highest_role}\n**NICKNAME** >> {nick}', inline=False)
        embed.set_image(url=user.avatar_url)
        await message.channel.send(embed=embed)
        
    @commands.command(no_pm=True, pass_context=True, aliases=['choice', 'choose'])
    async def pick(self,ctx,*,choices=None):
        """Picks a random choice. Splits by comma"""
        message = ctx.message
        if choices==None:
            await message.channel.send("Give me something to choose!")
            return
        choices = str(choices)
        choices = choices.split(',')
        if len(choices) <= 1:
            await message.channel.send("More than one item please. Remember you split them by comma.")
            return
        await message.channel.send(f"I choose.....**{random.choice(choices)}**")
        
    @commands.command(no_pm=True, pass_context=True)
    async def rate(self,ctx, am=None):
        """Rates you out of stars!"""
        message = ctx.message
        if am == None:
            am = 5
        try:
            am = int(am)
            am -= 0
        except:
            am = 5

        if am > 20 or am <= 0:
            await message.channel.send("Please, no bigger than 20 and no less than 1!")
            return
        ampicked = random.randint(0, am)
        lol = ""
        for z in range(ampicked):
            lol += ":star: "
        if am - ampicked > 0:
            for w in range(am-ampicked):
                lol += "<:oof_blackstar:382273167068102656> "
                
        await message.channel.send(lol)
        
    @commands.command(no_pm=True, pass_context=True, aliases=['8ball', 'ask'])
    async def fortune(self,ctx,*,question=None):
        """Ask me anything!"""
        message = ctx.message
        if question == None:
            await message.channel.send("You must ask me something!")
            return
        fortunes = ["Yes", "No", "Uhh....yes?", "Well...uh....no", "Nope", "Yep"
                    ,"YES!!!!!", "NO!", "Yeah...no", "Mhm", "Obviously", "Obviously not", "Correct!", "Wrong!", "Peanut", "No.....no...no..no", "Uh ask again later.."]

        await message.channel.send(f":8ball: {random.choice(fortunes)}")

    @commands.command(no_pm=True, pass_context=True)
    async def say(self,ctx,*,text=None):
        """I'll repeat what you say! <3"""
        message = ctx.message
	    if not text:
		    await message.channel.send("I need something to say!")
		    return
        embed = discord.Embed(color=0xff0066, description=text)
        await message.channel.send(embed=embed)

    @commands.command(no_pm=True, pass_contex=True, aliases=['avatarurl', 'avatar_url'])
    async def avatar(self,ctx):
        """Gets the avatar of a user."""
        message = ctx.message
        if len(message.mentions) <= 0:
            user = message.author
        else:
            user = message.mentions[0]

        embed=discord.Embed(description=f"Avatar for {user.mention}", color=0xff0066)
        embed.set_image(url=user.avatar_url)
        await message.channel.send(embed=embed)
    
    @commands.command(no_pm=True, pass_contex=True)
    async def mock(self,ctx,*,text=None):
        """Mocks what you say!"""
        message = ctx.message
        if text != None:
            newtext = ""
            i = 0
            for x in text:
                i = i + 1
                if (i / 2) == math.floor(i/2):
                    newtext += x.upper()
                else:
                    newtext += x.lower()
            embed=discord.Embed(description=newtext, color=0xff0066)
            embed.set_image(url="http://i0.kym-cdn.com/entries/icons/original/000/022/940/spongebobicon.jpg")
            await message.channel.send(embed=embed)

    @commands.command(no_pm=True, pass_contex=True, aliases=['bigletters', 'bigwords', 'hugewords', 'bigtext', 'hugetext'])
    async def bigword(self,ctx,*,text=None):
        """Makes everything you said bigger"""
        message = ctx.message
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        if text != None:
            newtext = ""
            for letter in text:
                if letter.lower() in letters:
                    newtext += f":regional_indicator_{letter.lower()}: "
                elif letter.lower() == ">":
                    newtext += f":arrow_forward: "
                elif letter.lower() == "<":
                    newtext += f":arrow_backward: "
                elif letter.lower() == "#":
                    newtext += f":hash: "
                elif letter.lower() == " ":
                    newtext += f"     "
                elif letter.lower() == "!":
                    newtext += f":exclamation: "
                elif letter.lower() == "?":
                    newtext += f":question: "
                elif letter.lower() == "+":
                    newtext += f":heavy_plus_sign: "
                elif letter.lower() == "$":
                    newtext += f":heavy_dollar_sign: "
                elif letter.lower() == "-":
                    newtext += f":heavy_minus_sign: "
                else:
                    try:
                        newtext += f":{numbers[int(letter.lower())]}: "
                    except:
                         newtext += f"**{letter}** "
            embed=discord.Embed(description=newtext, color=0xff0066)
            await message.channel.send(embed=embed)

    @commands.command(no_pm=True, pass_contex=True)
    async def urban(self,ctx,*,word=None):
        """Gets results from urban dictionary!"""
        message = ctx.message
        if word == None:
            await message.channel.send("Please enter something for me to search!")
            return
        word = re.sub(" ", "+", word.lower())
        link = f"http://api.urbandictionary.com/v0/define?term={word}"
        source = requests.get(link)
        text = source.text
        jsonv = json.loads(text)
        if jsonv["result_type"] == "no_results":
            await message.channel.send("That word doesn't exist!")
            return
        first = jsonv["list"][0]
        print(first['definition'])
        try:
            embed=discord.Embed(color=0xff0066)
            embed.add_field(name=":book:", value=f"{first['definition']}", inline=False)
            embed.add_field(name=":scroll:", value=f"{first['example']}", inline=False)
            embed.add_field(name=":thumbsup: ", value=f"{first['thumbs_up']}", inline=True)
            embed.add_field(name=":thumbsdown: ", value=f"{first['thumbs_down']}", inline=True)
            embed.add_field(name=":pen_ballpoint:", value=f"{first['author']}", inline=False)
            embed.set_author(name=f"Urban - {first['word']}", url=link, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
        except:
            embed=discord.Embed(color=0xff0066)
            embed.add_field(name=":book:", value=f"{first['definition'][:201]}...[click here for the rest](https://www.urbandictionary.com/define.php?term={word})", inline=False)
            embed.add_field(name=":scroll:", value=f"{first['example']}", inline=False)
            embed.add_field(name=":thumbsup: ", value=f"{first['thumbs_up']}", inline=True)
            embed.add_field(name=":thumbsdown: ", value=f"{first['thumbs_down']}", inline=True)
            embed.add_field(name=":pen_ballpoint:", value=f"{first['author']}", inline=False)
            embed.set_author(name=f"Urban - {first['word']}", url=link, icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)  
def setup(bot):
    p = Fun(bot)
    bot.add_cog(p)
