import nextcord
from nextcord.ext import commands 
import random
from configs.list import titles, pp, size, death_ways, crewmate_colors, empty, player, item1, vehicle, vehicleInside, item2
import aiohttp
from bs4 import BeautifulSoup
import urllib
import json
from nextcord import Interaction, Button
import asyncio

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(help = "How horny are you?")
    async def horny(self, ctx):
        embed = nextcord.Embed(
            title = f"{random.choice(titles)}",
            description = f"**Results**\n{random.randint(1, 100)}% horny",
            color = nextcord.Color.red()
        )

        await ctx.send(embed = embed)

    @commands.command(help = "Big PP", aliases = ["pprate", "ppsize"])
    async def pp(self, ctx):
        embed = nextcord.Embed(
            title = f"{random.choice(pp)}",
            description = f"**Results**\n{random.choice(size)}",
            color = nextcord.Color.red()
        )

        await ctx.send(embed = embed)

    async def web_scrape(text):
        async with aiohttp.CLientSession() as session:
            async with session.get(text) as r:
                if r.status == 200:
                    text = r.text()
                    return text
                

    @commands.command(help = "What would you do?")
    async def wyr(self, ctx):

        async def web_scrape(text):
            async with aiohttp.ClientSession() as session:
                async with session.get(text) as r:
                    if r.status == 200:
                        text = await r.text()
                        return text

        text = await web_scrape("https://either.io/")
        soup = BeautifulSoup(text, 'lxml')
        l = []
        for choice in soup.find_all("span", {"class":"option-text"}):
            l.append(choice.text)

        embed = nextcord.Embed(
            color = nextcord.Color.random()
        )

        embed.set_author(name = "Would you rather...", url = "https://either.io/", icon_url = self.bot.user.avatar.url)
        embed.add_field(name = "Either...", value = f":regional_indicator_a: {l[0]}", inline = False)
        embed.add_field(name = "Or...", value = f":regional_indicator_b: {l[1]}")
        message = await ctx.send(embed=embed)

        await message.add_reaction("🇦")
        await message.add_reaction("🇧")

    @commands.command(help = "Will you die as a virgin? :eyes:")
    async def virgin(self, ctx, member : nextcord.Member = None):
        if member == None:
            member = ctx.author

        answers = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        ]

        embed = nextcord.Embed(
            title = f"Will {member.name} die as a virgin?",
            color = nextcord.Color.random()
        )

        embed.add_field(
            name = "Results",
            value = f"{random.choice(answers)}"
        )

        await ctx.send(embed=embed)
    
    @commands.command(help = "Damn bro, you are sus af")
    async def rate(self, ctx, member : nextcord.Member = None):
        if member == None:
            member = ctx.author

        embed = nextcord.Embed(
            title = "Sus?!?!?",
            description = f"**Results**\n{random.randint(1, 100)}% sus!",
            color = nextcord.Color.red()
        )

        await ctx.send(embed=embed)
    
    @commands.command(help = "Sends a random meme using an API")
    async def meme(self, ctx):
        memeAPI = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

        memeData = json.load(memeAPI)

        memeURL = memeData['url']
        memeName = memeData['title']
        memePost = memeData['author']
        memeSub = memeData['subreddit']
        memeLink = memeData['postLink']

        embed = nextcord.Embed(
            title = f"{memeName}",
            color = nextcord.Color.blurple(),
            url = f"{memeURL}"
        )

        embed.set_image(url = memeURL)
        embed.set_footer(text = f"r/{memeSub}")
        await ctx.send(embed = embed)

    @commands.command()
    async def amongus(self, ctx):


        class AmongUsMove(nextcord.ui.View):
            def __init__(self):
                super().__init__()

            @nextcord.ui.button(label = "east", style = nextcord.ButtonStyle.blurple)
            async def east(self, button : nextcord.ui.Button, interaction: nextcord.Interaction): 

                gameEmbed = nextcord.Embed(
                    title = "You found a knife",
                    description = "Probably a knife from a ship wreck that an impostor left when they died. You can't collect this. It's damaged. **You will now float in 5s!**",
                    color = nextcord.Color.red()
                )

                gameEmbed.add_field(name = "**SPACE**\n*Explorer Mode*", value = f"""
                                    {empty} {empty} {empty} {empty} {empty}
                                    {empty} {empty} {empty} {empty} {empty}
                                    {empty} {empty} {empty} {player} {item1}
                                    {empty} {empty} {empty} {empty} {empty}
                                    {empty} {empty} {empty} {empty} {empty}""", inline = False)

                gameEmbed.add_field(name = "Task", value = "Go explore the galaxy using `north` to go up, `east` to go to the right, `south` to go down or `west` to go left.", inline = False)

                await interaction.edit(embed = gameEmbed)

                await asyncio.sleep(5)

                gameEmbed = nextcord.Embed(
                    title = "Floated",
                    description = "You floated right past the knife. Wait, what's this? You're right in front of a rocket. How 'bout you do a lil `?aurocketpeek`?",
                    color = nextcord.Color.red()
                )

                gameEmbed.add_field(name = "**SPACE**\n*Explorer Mode*", value = f"""
                                    {empty} {empty} {empty} {empty} {empty}
                                    {empty} {empty} {empty} {empty} {empty}
                                    {empty} {empty} {item1} {player} {vehicle}
                                    {empty} {empty} {empty} {empty} {empty}
                                    {empty} {empty} {empty} {empty} {empty}""", inline = False)

                gameEmbed.add_field(name = "Task", value = "Get inside the rocket", inline = False)

                await interaction.edit(embed = gameEmbed)


            action = ["rocket peek.views quick"]

            if action == "rocket peek.views quick":    

                class commDev(nextcord.ui.View):
                        def __init__(self):
                            super().__init__()

                        @nextcord.ui.button(label = "use comm device", style = nextcord.ButtonStyle.blurple)
                        async def comm(self, button : nextcord.ui.Button, interaction: nextcord.Interaction): 
                            commDevice = nextcord.Embed(
                                title = "Contacting nearby ships",
                                description = "Please stand by!",
                                color = nextcord.Color.red()
                            )

                            await interaction.edit(embed = commDevice)

                            await asyncio.sleep(3)

                            endEmbed = nextcord.Embed(
                                title = "VICTORY (East ending)",
                                description = "**You won!**\n\nA nearby ship picked you up and the crewmates welcomed you.",
                                color = nextcord.Color.green()
                            )   

                            await interaction.edit(embed = endEmbed)
                            self.stop()

                view = commDev()

                startEmbed = nextcord.Embed(
                        title = "You find something helpful",
                        description = "You have access to a communication device! You contact nearby ships.",
                        color = nextcord.Color.red()
                )

                startEmbed.add_field(name = "**VEHICLE - ROCKET**\n*Exploring*", value = f"""
                    {vehicleInside} {vehicleInside} {vehicleInside} {vehicleInside} {vehicleInside}
                    {item2} {player} {vehicleInside} {vehicleInside} {vehicleInside}
                    {vehicleInside} {vehicleInside} {vehicleInside} {vehicleInside} {vehicleInside}
                    {vehicleInside} {vehicleInside} {vehicleInside} {vehicleInside} {vehicleInside}
                    {vehicleInside} {vehicleInside} {vehicleInside} {vehicleInside} {vehicleInside}""", inline = False)

                startEmbed.add_field(name = "Task", value = "Contact a nearby ship", inline = False)

                #await interaction.edit(embed = startEmbed, view = view)

        view = AmongUsMove()

        startEmbed = nextcord.Embed(
            title = "You find yourself in the darkness...",
            description = "... and you just got ejected because you were accused of being the impostor.",
            color = nextcord.Color.red()
        )

        startEmbed.add_field(name = "**SPACE**\n*Just floating around*", value = f"""
        {empty} {empty} {empty} {empty} {empty}
        {empty} {empty} {empty} {empty} {empty}
        {empty} {empty} {player} {empty} {empty}
        {empty} {empty} {empty} {empty} {empty}
        {empty} {empty} {empty} {empty} {empty}""", inline = False)

        startEmbed.add_field(name = "Task", value = "Go explore the galaxy using `north` to go up, `east` to go to the right, `south` to go down or `west` to go left.", inline = False)

        await ctx.send(embed = startEmbed, view = view)

def setup(bot):
    bot.add_cog(Fun(bot))