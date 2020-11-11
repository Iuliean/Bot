import discord
from .utils.xo import xo
from .utils.barbut import BarBut
from discord.ext import commands
from .utils.sql_handler import sql_handler as sql 


class Games(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.db = sql()
    
    @commands.Cog.listener()
    async def on_ready(self):
        print ('Games is live.')

    @commands.command(pass_context=True)
    async def xo(self,ctx,adversar):
        player1 = '<@!'+str(ctx.message.author.id)+'>'
        player2 = '<@!'+str(ctx.message.mentions[0].id)+'>'
        print (player1,player2)
        
        Game = xo(player1,player2,ctx.message.author.name,ctx.message.mentions[0].name)
        
        await Game.start_game(self.client,ctx)

    @commands.command(pass_context=True)
    async def barbut(self,ctx,adversar,bet:float):
        player1 = '<@!'+str(ctx.message.author.id)+'>'
        player1_name = ctx.message.author.name
        print(player1)
       
        player2 = '<@!'+str(ctx.message.mentions[0].id)+'>'
        player2_name = ctx.message.mentions[0].name
        print(player2)
        
        channel = ctx.message.channel
        
        if self.db.remove_money(ctx.message.guild.id ,ctx.message.author.id ,bet):
            
            await ctx.send(str(player2)+' type accept to confirm the match or decline to cancel the match.The bet amount is: ₿'+str(bet)) 
            
            
            while True:
                msg = await self.client.wait_for('message')
            
                if "<@!"+str(msg.author.id)+">" == str(player2) and msg.content == 'accept' and msg.channel == channel and self.db.remove_money(ctx.message.guild.id,ctx.message.mentions[0].id,bet):
                    if player1 != player2:    
                        
                        Game = BarBut (player1,player2,player1_name,player2_name,channel,bet)
                        await Game.barbut_start(self.client,ctx)
                        break 
                   
                    else:
                        
                        self.db.add_money(ctx.message.guild.id,ctx.message.author.id,bet)
                        await ctx.send('@everyone '+player1+' is trying to play alone LMAO')
                
                elif (msg.author.id == int(player2[3:-1]) and msg.content == 'decline' and msg.channel == channel) or not self.db.remove_money(ctx.message.guild.id,ctx.message.mentions[0].id,bet) :
                
                    self.db.add_money(ctx.message.guild.id,ctx.message.author.id,bet)
                    break
        
        else:
            await ctx.send ('''Sorry boss you don't have enough money''')
        
        
        print ('the loop is done ')

def setup(client):
    client.add_cog(Games(client))
