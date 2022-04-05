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
        """ Hiển thị thông tin Bot."""
        message = discord.Embed(title="Thông tin", description=f"{self.bot.description}", color=0xdc1d24)
        message.add_field(name="Tác giả", value=f"{await self.bot.fetch_user(self.bot.owner_id)}")
        message.add_field(name="Phiên bản", value="1.0.0")
        message.add_field(name="Prefix", value="!")
        message.add_field(name="Source Code", value="https://github.com/dxl-1805/Bau-Cua-Hoo-Hey-How-DISCORD-BOT")
        message.add_field(name="GitHub", value="https://github.com/dxl-1805")
        message.add_field(name="Discord", value="<blank>")
        message.set_footer(text=f"Yêu cầu bởi {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=message)
    
    @commands.command(name="author", aliases=[])
    async def author(self, ctx):
        """ Hiển thị thông tin tác giả."""
        author = await self.bot.fetch_user(self.bot.owner_id)
        message = discord.Embed(title="Tác giả", description=f"{author}", color=0xdc1d24)
        message.set_thumbnail(url=author.avatar_url)
        message.add_field(name="ID", value=f"{author.id}")
        message.add_field(name="Facebook", value=f"{misc.author_facebook()}")
        message.set_footer(text=f"Yêu cầu bởi {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=message)

def setup(bot):
    bot.add_cog(About(bot))