import discord
from discord.ext import commands
import asyncio
import random as rand
from utils import misc

class BauCua(commands.Cog):
    """ Commands related to bot utilities."""
    def __init__(self, bot):
        self.bot = bot
        self.dice_emojis = {
            'Bầu': "<:bau:960662361381945344>",
            'Cua': "<:cua:960662361331617812>",
            'Tôm': "<:tom:960662361629397073>",
            'Cá': "<:ca:960662360996065361>",
            'Gà': "<:ga:960662361478406154>",
            'Nai': "<:nai:960662361428074516>"
        }
        self.extra_emojis = {
            'bell': '\N{bell}', 
            'check': '✅'
        }

    def game_begin_embed_message(self, ctx):
        message = discord.Embed(title="Bầu cua", description="", color=0xdc1d24)
        message.set_image(url = "https://cdn.discordapp.com/attachments/883724601090273291/895123475163934790/dung-cu-choi-bau-cua-tom-ca.png")
        message.add_field(name="Hướng dẫn", value = "React emoji tương ứng \nChủ ván bấm :bell: để chốt")
        message.set_footer(text=f"Chủ ván {ctx.author}", icon_url=ctx.author.avatar_url)
        return message

    def get_game_confirm_embed_message(self, ctx, reaction_groups):
        message = discord.Embed(title="Bầu Cua", description="", color=0xdc1d24)
        for emoji_name, emoji in self.dice_emojis.items():
            message.add_field(name=f"{emoji} {emoji_name}", value=f":point_right: {' '.join(reaction_groups[emoji])}", inline=False)
        message.add_field(name="Hướng dẫn", value = "Chủ ván bấm ✅ để nhận kết quả")
        message.set_footer(text=f"Chủ ván {ctx.author}", icon_url=ctx.author.avatar_url)
        return message
    
    def edited_game_begin_embed_message(self, ctx):
        message = discord.Embed(title = 'Bầu Cua', description = "Bắt đầu", colour = 0xdc1d24)
        message.set_footer(text=f"Chủ ván {ctx.author}", icon_url=ctx.author.avatar_url)
        return message

    def get_result_embed_message(self, ctx, reaction_groups):
        result = [rand.choice(list(self.dice_emojis.values())),rand.choice(list(self.dice_emojis.values())),rand.choice(list(self.dice_emojis.values()))]
        message = discord.Embed(title="Bầu Cua", description="", color=0xdc1d24)
        for emoji_name, emoji in self.dice_emojis.items():
            message.add_field(name=f"{emoji} {emoji_name}", value=f"{':green_circle:' if emoji in result else ':point_right: '}{' '.join(reaction_groups[emoji])}", inline=False)
        message.add_field(name="Kết quả", value = " ".join(result))
        message.set_footer(text=f"Chủ ván {ctx.author}", icon_url=ctx.author.avatar_url)
        return message

    @commands.Cog.listener()
    async def on_ready(self):
        print("BauCua Cog Loaded Succesfully")

    @commands.command(name="roll", aliases=[])
    async def random(self, ctx):
        """ Đổ bầu cua nhanh """
        await ctx.send(f"{rand.choice(list(self.dice_emojis.values()))} {rand.choice(list(self.dice_emojis.values()))} {rand.choice(list(self.dice_emojis.values()))}")
    
    @commands.command(name="baucua", aliases=[])
    async def start(self, ctx):
        """ Bắt đầu game Bầu Cua """
        game = await ctx.send(embed = self.game_begin_embed_message(ctx))
        for emoji in self.dice_emojis:
            await game.add_reaction(self.dice_emojis[emoji])
        await game.add_reaction(self.extra_emojis['bell'])

        def check1(reaction, user):
            return user == ctx.author and str(reaction.emoji) == self.extra_emojis['bell']

        try:
            await self.bot.wait_for('reaction_add', timeout=120.0, check = check1)
        except asyncio.TimeoutError:
            pass

        cache_game_begin_message = await ctx.channel.fetch_message(game.id)
        reacts = cache_game_begin_message.reactions
        updating_message = await ctx.send(embed = discord.Embed(title = 'Bầu cua', description = 'Đang chốt các lựa chọn...', colour = 0xdc1d24))

        reaction_groups = {key : [] for key in self.dice_emojis.values()}
        for emoji in reaction_groups.keys():
            for reaction in reacts:
                if str(reaction.emoji) == emoji:
                    async for user in reaction.users():
                        if user.bot != True:
                            reaction_groups[emoji].append(user.mention)

        await cache_game_begin_message.edit(embed = self.edited_game_begin_embed_message(ctx))
        confirm_message = await ctx.send(embed = self.get_game_confirm_embed_message(ctx, reaction_groups))
        await confirm_message.add_reaction(self.extra_emojis['check'])

        def check2(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'
        try:
            await self.bot.wait_for('reaction_add', timeout=15.0, check = check2)
        except asyncio.TimeoutError:
            pass
        
        await ctx.send(embed = self.get_result_embed_message(ctx, reaction_groups))
        await game.delete()
        await updating_message.delete()
        await confirm_message.delete()

def setup(bot):
    bot.add_cog(BauCua(bot))