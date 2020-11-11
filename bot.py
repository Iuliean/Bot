import discord
import os
from cogs.utils.sql_handler import sql_handler as sql
from discord.ext import commands

client = commands.Bot(command_prefix = '#')
client.remove_command('help')

@client.event
async def on_ready():
    print ("Let's gooo bois!!!")
   
    db = sql()
    
            
    for server in client.guilds:
        try:
            db.insert("Server",("ID","Server_Name"),(str(server.id),server.name))
        except:
            pass
        
    for server in client.guilds:
        for member in server.members:
            try:
                db.insert("Member",("ServerID","UserID","User_Name") ,(str(server.id),str(member.id),member.name))
            except:
                pass

@client.command()
async def test(ctx):
    db = sql()

    test =db.get_collumn("Member" , "Balaceni" , "UserID = "+str(ctx.message.author.id))
    
    print (ctx.message.guild.id)


@client.command()
async def latency(ctx):
    await ctx.send(client.latency*1000)

@client.command()
async def load (ctx,extension):
    
    client.load_extension(f'cogs.{extension}')
    print (f'Loading {extension}')
    await ctx.send(f'{extension} has been loaded Boss')

@client.command()
async def unload (ctx,extension):

    client.unload_extension(f'cogs.{extension}')
    print(f'Unloading {extension}')
    await ctx.send(f'{extension} has been unloaded Boss')

@client.command()
async def help(ctx):
    embeded = discord.Embed(
        colour = discord.Colour(233)
    )
    
    embeded.set_author(name='Help')
    
    embeded.add_field(name="""#help""",value='Returns this',inline=False)
    embeded.add_field(name="""#soundboard""",value='Shows the avalible sounds in the soundboard',inline=False)
    embeded.add_field(name="""#dnd""",value='Shows the commands avalible in the DnD module',inline=False)
    embeded.add_field(name="""#memes""",value='Shows the avalible memes',inline=False)
    embeded.add_field(name="""#games""",value='Shows the avalible games',inline=False)
    embeded.add_field(name="""#reddit""",value='Pulls a random post from reddit.Example:#reddit dankmemes hot',inline=False)
    embeded.add_field(name="""#currency""",value='Shous currency related commands',inline=False)

    await ctx.send(embed=embeded)

@client.command()
async def soundboard(ctx):
    embeded = discord.Embed(
        colour = discord.Colour(150)
    )
    
    embeded.set_author(name = 'Soundboard')
    
    sounds=[]
    message = ''
   
    for filename in os.listdir('./cogs/utils/resources/sounds'):
        sounds.append(filename[:-4])
    for sound in sounds:
        message= message+sound+','
    
    embeded.add_field(name="Avalible sounds",value = message[:-1],inline=False)

    await ctx.send (embed = embeded)

@client.command()
async def dnd(ctx):
    embeded = discord.Embed(
        colour = discord.Colour(150)
    )
    
    embeded.set_author(name = 'DnD')
    
    embeded.add_field(name="""#roll""",value="""Rolls any type of dice for you.Example:#roll 2d20+3 or #roll 4d8""",inline=False)
    embeded.add_field(name="""#namepls""",value="""Generates a female or male name for you.Example:#namepls f or namepls m""",inline = False)
    embeded.add_field(name="""#coinflip""",value='Flips a coin for you',inline=False)

    await ctx.send(embed = embeded)

@client.command()
async def memes(ctx):
    embeded = discord.Embed(
        colour = discord.Colour(150)
    )
    
    embeded.set_author(name = 'Memes')
    
    memes=[]
    message = ''
    
    for filename in os.listdir('./cogs/utils/resources/memes/pepe'):
        memes.append(filename[:-4])
    for meme in memes:
        message= message+meme+','
    embeded.add_field(name="Avalible pepe memes",value = message[:-1],inline=False)
   
    await ctx.send (embed = embeded)

@client.command()
async def games(ctx):
    embeded = discord.Embed(
        colour = discord.Colour(233)
        )
    
    embeded.set_author(name="Games")
    
    embeded.add_field(name="#barbut",value="""Let's you play barbut with someone else for balaceni.Example: #barbut @Player 40""" ,inline = False)
    embeded.add_field(name="#xo",value="""Let's you play tic-tac-toe with someone else .Example of use : #xo @Player""" ,inline = False)

    await ctx.send (embed = embeded)

@client.command()
async def currency(ctx):
    embeded = discord.Embed(colour = discord.Color(233))
    
    embeded.set_author(name='Currency')
    
    embeded.add_field(name="""#balance""",value='Returns the amount of money you have',inline=False)
    embeded.add_field(name="""#pay""",value='Sends money from you to another person.Example :pay @Person 100',inline=False)

    await ctx.send(embed = embeded)

@client.command()
async def mute(ctx):
    voiceChannel = ctx.author.voice.channel

    for member in voiceChannel.members:
        if member not in ctx.message.mentions:
            await member.edit(mute=True)
    
@client.command()
async def unmute(ctx):
    voiceChannel = ctx.author.voice.channel

    for member in voiceChannel.members:
        await member.edit(mute=False)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')





client.run('')