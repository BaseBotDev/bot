from nextcord.ext import commands 
from configs.data.data import version

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Gets the latest BaseBot version", aliases = ["build", "b", "v", "ver"])
    async def version(self, ctx):
        await ctx.send(f"Base Bot is currently on version **{version}**")

def setup(bot):
    bot.add_cog(Misc(bot))