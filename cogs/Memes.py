import discord
from discord.ext import commands

memes = './cogs/utils/resources/memes'

class Memes (commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def pepe(self,ctx,meme):
        await ctx.send(file=discord.File(memes+'/pepe/'+meme+'.jpg'))

def setup(client):
    client.add_cog(Memes(client))