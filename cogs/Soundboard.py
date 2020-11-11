import discord
from discord.ext import commands
resources ='./cogs/utils/resources/sounds/'
class Soundboard(commands.Cog):
    
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Soundboard is live')

    @commands.command(pass_context=True)
    async def nuke(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'nuke.mp3'),after=lambda e:print('done',e))

            while True:
                if not voice.is_playing():
                    await voice.disconnect()
                    break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in a voice channel.')

    @commands.command(pass_context=True)
    async def boom(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'boom.mp3'),after=lambda e:print('done',e))

            while True:
                if not voice.is_playing():
                    await voice.disconnect()
                    break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in a voice channel.')
    
    @commands.command(pass_context=True)
    async def really(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'really.mp3'),after=lambda e:print('done',e))
            while True:
                if not voice.is_playing():
                    await voice.disconnect()
                    break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in a voice channel.')

    @commands.command(pass_context=True)
    async def infrangeri(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'infrangeri.mp3'),after=lambda e:print('done',e))
            while True:
                if not voice.is_playing():
                    await voice.disconnect()
                    break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in a voice channel.')
    
    @commands.command(pass_context=True)
    async def talent(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'talent.mp3'),after=lambda e:print('done',e))
            while True:
                if not voice.is_playing():
                    await voice.disconnect()
                    break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in a voice channel.')

    @commands.command(pass_context=True)
    async def gardamea(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'gardamea.mp3'),after=lambda e:print('done',e))
            while True:
                if not voice.is_playing():
                    await voice.disconnect()
                    break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in a voice channel.')

    @commands.command(pass_context=True)
    async def hehe(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'hehe.mp3'),after=lambda e:print('done',e))
            while True:
                if not voice.is_playing():
                    await voice.disconnect()
                    break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def hatz(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'hatz.mp3'),after=lambda e:print('done',e))
            while True:
                if not voice.is_playing():
                    await voice.disconnect()
                    break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def chelutu(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'chelutu.mp3'),after=lambda e:print('done',e))
            while True:
                if not voice.is_playing():
                    await voice.disconnect()
                    break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def apamare(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'apamare.mp3'),after=lambda e:print('done',e))
            while True:
                if not voice.is_playing():
                    await voice.disconnect()
                    break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def ping(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'ping.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def respect(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'respect.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def kekw(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'kekw.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def damage(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'damage.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def why(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'why.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def heheboy(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'heheboy.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def omg(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'omg.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def bully(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'bully.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def cena(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'cena.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')
            
    @commands.command(pass_context=True)
    async def default(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'default.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')

    @commands.command(pass_context=True)
    async def disconnected(self,ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            voice.play(discord.FFmpegPCMAudio(source = resources+'disconnected.mp3'),after=lambda e:print('done',e))
            while True:
               if not voice.is_playing():
                   await voice.disconnect()
                   break
        except:
            await ctx.send('Something went wrong boss.Make sure you are in voice channel.')
   
def setup(client):
    client.add_cog(Soundboard(client))
