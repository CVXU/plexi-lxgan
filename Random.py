#DISCORD
import discord
from discord.ext import commands

#RANDOM
import random
from random import randint

#DATETIME
from datetime import datetime

#COG SETUP
class plexi:
    def __init__(self, bot):
        self.bot = bot
    
    #COMMAND
    @commands.command()
    async def random(self, ctx, arg1: int = None):
        now = datetime.now()
        time_now = now.strftime("%H:%M")
        try:
            if not arg1:
                embed = discord.Embed(
                    colour = discord.Colour.blurple()
                )
                random_number = random.randint(0, 1000)
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/478598485172813832/487964413324820502/image0.png')
                embed.set_author(name=f'Random number for {ctx.author.name}')
                embed.add_field(name='Capped at:', value='`No input given, so 1000`', inline=False)
                embed.add_field(name='Your number:', value=f'`{random_number}`', inline=False)
                embed.set_footer(text=f'Today at {time_now}', icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    colour = discord.Colour.blurple()
                )
                random_number = random.randint(0, arg1)
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/478598485172813832/487964413324820502/image0.png')
                embed.set_author(name=f'Random number for {ctx.author.name}')
                embed.add_field(name='Capped at:', value=f'`{arg1}`', inline=False)
                embed.add_field(name='Your number:', value=f'`{random_number}`', inline=False)
                embed.set_footer(text=f'Today at {time_now}', icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
        except Exception as error:
            await ctx.send(error)
          
def setup(bot):
    bot.add_cog(plexi(bot))
