import os
import discord
from discord.ext import commands
from utils import misc

class About(commands.Cog):
    """ Commands related to bot information."""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("About Cog Loaded Succesfully")

    @commands.command(name="info", aliases=[])
    async def info(self, ctx):
        """ Displays information about the bot."""
        message = discord.Embed(title="Info", description=f"{self.bot.description}", color=0xdc1d24)
        message.add_field(name="Author", value=f"{await self.bot.fetch_user(self.bot.owner_id)}")
        message.add_field(name="Version", value="1.0.0")
        message.add_field(name="Prefix", value="!")
        message.add_field(name="Source Code", value="<blank>")
        message.add_field(name="GitHub", value="<blank>")
        message.add_field(name="Discord", value="<blank>")
        message.add_field(name="Support Server", value="<blank>")
        message.add_field(name="Invite", value="<blank>")
        message.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=message)
    
    @commands.command(name="author", aliases=[])
    async def author(self, ctx):
        author = await self.bot.fetch_user(self.bot.owner_id)
        message = discord.Embed(title="Author", description=f"{author}", color=0xdc1d24)
        message.set_thumbnail(url=author.avatar_url)
        message.add_field(name="ID", value=f"{author.id}")
        message.add_field(name="Facebook", value=f"{misc.author_facebook()}")
        message.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=message)

def setup(bot):
    bot.add_cog(About(bot))