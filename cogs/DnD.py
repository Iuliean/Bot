import discord
from .utils import name_generator
from numpy import random
from discord.ext import commands

class DnD(commands.Cog):
    
    def __init__(self,client):
        self.client = client
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print ('DnD is live')
    #Commands
    @commands.command(brief = 'Flips a coin for you.')
    async def coinflip(self,ctx):
        if random.randint(100)%2==0 : await ctx.send("It's Heads Boss")
        else : await ctx.send("It's Tails Boss")
    
    @commands.command(brief = 'Rolls a dice for you.Example of usage: #roll 2d20+1')
    async def roll(self,ctx,dice):
        print("He tried to roll a "+dice)
        dice = dice.lower()
        dices = []
        message = ""
        sum_of_dices = 0
        try:
            temp = dice.split("d")
            print (temp)
            multiplyer = int(temp[0])
            print("multiplyer is ok and it's value is:"+str(multiplyer))
            if temp[1].find("+") >=0:
                temp = temp[1].split("+")
                dice_type = int(temp[0])
                print ("dice type is ok and it's value is:"+str(dice_type))
                adder = int(temp[1])
                print ("adder is ok and it's value is:"+str(adder))
            else:
                dice_type = int(temp[1])
                print ("dice type is ok and it's value is:"+str(dice_type))
                adder = 0
                print("adder is ok and it's value is:"+str(adder))

        except:
            print ("Character cannot be converted")
            await ctx.send("Sorry boss something went wrong.Make sure you used this format: 2d20+2 .:heart:")
    
        for i in range(0,multiplyer):
            dices.append(random.randint(1,dice_type+1))
            print ("Genterating dices")

        message = "You Rolled a "+dice+" and got:\n"+"Split:"
        for n in dices:
            message = message +", " +str(n+adder)
            print ("Calcuating split dices")

        message = message + "\nAddded: "
        for n in dices:
            sum_of_dices +=n
            print("Calculateing added dices")
            
        message = message + str(sum_of_dices+adder)
        print (message)
        await ctx.send(message)
    
    @commands.command(brief = 'Generates a female or male name.Example: #namepls m or #namepls f')
    async def namepls(self,ctx,gender):
        if gender == 'm':
            await ctx.send(name_generator.generate_male())
        elif gender == 'f':
            await ctx.send(name_generator.generate_female())
        else:
            await ctx.send("Sorry Boss i don't know the gender "+'"'+str(gender)+'"'+" but you can try f(for female) or m(for male) like this : #namepls f or #namepls m")
      
        

            

    
    
def setup (client):
    client.add_cog(DnD(client))