import nextcord
from configs.cfg import PREFIX, TOKEN
from nextcord.ext import commands
import os

intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix = PREFIX, intents=intents, help_command=commands.DefaultHelpCommand())
bot.help_command = commands.MinimalHelpCommand()

class Help(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            destem = nextcord.Embed(
                description = page,
                color = nextcord.Color.green()
            )
            await destination.send(embed = destem)

    async def send_bot_help(self, mapping):
        embed = nextcord.Embed(
            title = "Help",
            color = nextcord.Color.green()
        )
        for cog, commands in mapping.items():
           filtered = await self.filter_commands(commands, sort = True)
           command_signatures = [self.get_command_signature(c) for c in commands]
           if command_signatures:
                cog_name = getattr(cog, "qualified_name", "Uncategorized")
                embed.add_field(name = cog_name, value = "`" + "\n".join(command_signatures) + "`", inline = False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = nextcord.Embed(
            title = self.get_command_signature(command),
            color = nextcord.Color.green()
        )
        embed.add_field(
            name = "Help", 
            value = command.help
        )
        alias = command.aliases
        if alias:
            embed.add_field(name = "Aliases", value = "``" + ", ".join(alias) + "``", inline = False)

        channel = self.get_destination()
        await channel.send(embed = embed)

    async def send_error_message(self, error):
        embed = nextcord.Embed(
            title = "Error", 
            description = error,
            color = nextcord.Color.red()
        )
        channel = self.get_destination()
        await channel.send(embed = embed)

    def get_command_brief(self, command):
            return command.short_doc or "Command is not documented."

bot.help_command = Help()

@bot.event
async def on_ready():
    print("Base Bot has been launched.")
    print("GitHub: https://github.com/BaseBotDev")

    await bot.change_presence(activity = nextcord.Game(name = "Base Bot"))

@bot.command(help = "Loads a command.")
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

    embed = nextcord.Embed(
        description=f"Loaded ``{extension}.py`` with success",
        color=nextcord.Color.blurple()
    )
    await ctx.send(embed=embed)


@bot.command(help = "Unloads a command.")
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

    embed = nextcord.Embed(
        description=f"Unloaded ``{extension}.py`` with success",
        color=nextcord.Color.blurple()
    )
    await ctx.send(embed=embed)


@bot.command(help = "Reloads a command.")
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

    embed = nextcord.Embed(
        description=f"Reloaded ``{extension}.py`` with success",
        color=nextcord.Color.blurple()
    )
    await ctx.send(embed=embed)

@load.error 
async def load_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = nextcord.Embed(
            description = "Only the owner of this bot can perform this command!",
            color = nextcord.Color.red()
        )
        await ctx.send(embed=embed)

@unload.error 
async def unload_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = nextcord.Embed(
            description = "Only the owner of this bot can perform this command!",
            color = nextcord.Color.red()
        )
        await ctx.send(embed=embed)

@reload.error 
async def reload_error(ctx, error):
    if isinstance(error, commands.Guil):
        embed = nextcord.Embed(
            description = "Only the owner of this bot can perform this command!",
            color = nextcord.Color.red()
        )
        await ctx.send(embed=embed)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN) # Set your token in configs/cfg.py
