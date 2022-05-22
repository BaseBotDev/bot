import nextcord
from nextcord.ext import commands 
import random
from configs.list import titles, pp, size

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

def setup(bot):
    bot.add_cog(Fun(bot))