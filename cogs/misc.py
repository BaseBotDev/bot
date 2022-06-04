from nextcord.ext import commands 
from configs.data.data import version

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Gets the latest BaseBot version", aliases = ["build", "b", "v", "ver"])
    async def version(self, ctx):
        await ctx.send(f"Porov is currently on version **{version}**")
    
    @commands.command(help = "Gets the current bot latency", aliases = ["latency", "l"])
    async def ping(self, ctx):
            await ctx.send(f"**:ping_pong: Pong!** It took {round(self.bot.latency * 1000)} ms for me to respond!")

def setup(bot):
    bot.add_cog(Misc(bot))