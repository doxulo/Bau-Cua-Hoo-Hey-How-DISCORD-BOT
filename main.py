import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils import misc
from pretty_help import PrettyHelp, DefaultMenu

load_dotenv()

class BauCuaBot(commands.Bot):
    def __init__(self):
        self.description = "Bầu Cua Bot mô phỏng tựa game Bầu Cua Cá Cọp, hay còn có tên là Hoo Hey How."
        self.menu = DefaultMenu(delete_after_timeout=True)
        super().__init__(
            command_prefix = commands.when_mentioned_or('!'),
            owner_id = 476438504868544525,
            description = self.description,
            case_insensitive = True,
            activity = discord.Activity(name="!help", type=discord.ActivityType.listening),
            help_command = PrettyHelp(color = discord.Color(0xdc1d24), ending_note = "Yêu cầu bởi {ctx.author}", index_title = "Chức năng", menu = self.menu, no_category = "Khác")
        )

    async def on_ready(self):
        self.starttime = misc.get_raw_current_time()
        print(f'connected to discord as {self.user} at {misc.get_formated_ICT_time()}')

bot = BauCuaBot()

@bot.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Load {extension} Cog Successfully")

@bot.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unload {extension} Cog Successfully")

@bot.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Reload {extension} Cog Successfully")

@bot.command(hidden=True)
@commands.is_owner()
async def reloadall(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.unload_extension(f"cogs.{filename[:-3]}")
            bot.load_extension(f"cogs.{filename[:-3]}")
    await ctx.send(f"Reload All Cogs Successfully")

@bot.command(hidden=True)
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send(f"Shutdown Bot Successfully")
    await bot.close()

@bot.command(hidden=True)
@commands.is_owner()
async def updateactivity(ctx, activity_name):
    await bot.change_presence(activity=discord.Game(name=activity_name))
    await ctx.send(f"Update Activity Successfully")

@bot.command(hidden=True)
@commands.is_owner()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")

@bot.command(hidden = True)
@commands.is_owner()
async def checksv(ctx):
    result = ''
    activesv = bot.guilds
    count= 0
    for guild in activesv:
        count += 1
        result += 'NO.{0} | ID: {1} | Name: {2} | Member: {3}\n'.format(count, guild.id, guild.name, guild.member_count)
    await ctx.send(result)

@bot.command(hidden = True)
@commands.is_owner()
async def uptime(ctx):
    await ctx.send(f"{misc.get_formated_uptime(bot.starttime)}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(os.getenv('DISCORD_TOKEN'))