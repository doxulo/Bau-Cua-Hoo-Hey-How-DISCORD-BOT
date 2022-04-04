import os
import discord
from discord.ext import commands
import random as rand
from utils import misc

class BauCua(commands.Cog):
    """ Commands related to bot utilities."""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("BauCua Cog Loaded Succesfully")

    @commands.command(name="roll", aliases=[])
    async def random(self, ctx):
        """ blank """
        dice = ['bau', 'cua', 'tom', 'ca', 'ga', 'nai']
        await ctx.send(f"{dice[rand.randint(0, 5)]} {dice[rand.randint(0, 5)]} {dice[rand.randint(0, 5)]}")
    
    @commands.command(name="start", aliases=[])
    async def start(self, ctx):
        """ Begin a game of Bau Cua """
        message = discord.Embed(title="Bau Cua", description="Bau Cua Game", color=0xdc1d24)
        message.add_field(name="Rules", value="1. Roll 3 times.\n2. If you win, you get 1 point.\n3. If you lose, you lose 1 point.\n4. If you draw, you get nothing.\n5. If you have 0 point, you lose the game.")
        message.set_footer(text=f"Started by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=message)
def setup(bot):
    bot.add_cog(BauCua(bot))