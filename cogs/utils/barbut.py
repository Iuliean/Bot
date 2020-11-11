import discord
from numpy import random
from discord.ext import commands
from .sql_handler import sql_handler as sql

class BarBut ():

    def __init__(self,player1,player2,name1,name2,channel,bet):
        self.player1 = player1
        self.player2 = player2
        self.name1 = name1
        self.name2 = name2
        self.channel = channel
        self.bet = bet
        self.db =sql()

    async def barbut_start(self,client,ctx):
        
        await ctx.send("Barbut between "+self.player1+" and "+self.player2+"""\nType "roll" to throw the dice""")
        print(self.name1,self.name2)
        player1_roll = -1
        player2_roll = -1

        while True:
            msg = await client.wait_for('message')

            if msg.channel == self.channel and '<@!'+str(msg.author.id)+'>' == self.player1 and msg.content == 'roll':
                player1_roll = random.randint(0,7)
                await ctx.send(self.player1+' rolled:'+str(player1_roll))

            if msg.channel == self.channel and '<@!'+str(msg.author.id)+'>' == self.player2 and msg.content == 'roll':
                player2_roll = random.randint(0,7)
                await ctx.send(self.player2+' rolled:'+str(player2_roll))
            
            if player1_roll != -1 and player2_roll != -1:
                
                if player1_roll > player2_roll:
                    self.db.add_money(ctx.message.guild.id,self.player1[3:-1],self.bet*2)
                    await ctx.send(self.player1+' won !!!!!')
                    break

                elif player2_roll > player1_roll:
                    self.db.add_money(ctx.message.guild.id,self.player2[3:-1],self.bet*2)
                    await ctx.send(self.player2+' won !!!!!')
                    break
                else :
                    self.db.add_money(ctx.message.guild.id,self.player1[3:-1],self.bet)
                    self.db.add_money(ctx.message.guild.id,self.player2[3:-1],self.bet)
                    await ctx.send('Draw :(')
                    break
            
        
        print ('The loop has been escaped')