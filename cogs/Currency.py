import discord
from discord.ext import commands
import os
from .utils.sql_handler import sql_handler as sql



class Currency(commands.Cog):

    

    def __init__(self,client):
        self.client = client

        self.db= sql()
    
    @commands.Cog.listener()
    async def on_message(self,ctx):
        self.db.add_money(ctx.guild.id,ctx.author.id,0.1)
    
    @commands.command()
    async def balance(self,ctx):
          
        await ctx.send('You have ₿ {} Balaceni in the bank'.format(self.db.get_money(ctx.message.guild.id,ctx.message.author.id)))

    @commands.command()
    async def pay (self,ctx,tag,amount:float):
        recipient = ctx.message.mentions[0].id

        if recipient != ctx.message.author.id and self.db.remove_money(ctx.message.guild.id,ctx.message.author.id,amount):
            self.db.add_money(ctx.message.guild.id,recipient , amount)

def setup(client):
    client.add_cog(Currency(client))