import discord
from discord.ext import commands

class xo(commands.Cog):

    #x=':x:'
    #o=':o:'
    #empty=':black_large_square:'
    
    def __init__(self,player1,player2,name1,name2):
        self.player1 = player1
        self.player2 = player2
        self.name1 = name1
        self.name2 = name2
        self.finnished = False
        self.isplayer2 = True
        self.table =[
           [':black_large_square:',':black_large_square:',':black_large_square:'],
           [':black_large_square:',':black_large_square:',':black_large_square:'],
           [':black_large_square:',':black_large_square:',':black_large_square:']
        ]
        print ('The game has begun')

    def table_to_string(self):
        msg='\n'
        for i in range(0,3):
            for j in range(0,3):
                msg= msg + self.table[i][j]
            msg=msg+'\n'
        return msg
    
    def place_o(self,position):
       
        if position == 'a1' and self.table[0][0] == ':black_large_square:':
            self.table[0][0]=':o:'
        
        if position == 'a2' and self.table[0][1] == ':black_large_square:':
            self.table[0][1]=':o:'
        
        if position == 'a3' and self.table[0][2] == ':black_large_square:':
            self.table[0][2]=':o:'
        
        if position == 'b1' and self.table[1][0] == ':black_large_square:':
            self.table[1][0]=':o:'
        
        if position == 'b2' and self.table[1][1] == ':black_large_square:':
            self.table[1][1]=':o:'
        
        if position == 'b3' and self.table[1][2] == ':black_large_square:':
            self.table[1][2]=':o:'
        
        if position == 'c1' and self.table[2][0] == ':black_large_square:':
            self.table[2][0]=':o:'
        
        if position == 'c2' and self.table[2][1] == ':black_large_square:':
            self.table[2][1]=':o:'
        
        if position == 'c3' and self.table[2][2] == ':black_large_square:':
            self.table[2][2]=':o:'

    def place_x(self,position):
       
        if position == 'a1' and self.table[0][0] == ':black_large_square:':
            self.table[0][0]=':x:'
        
        if position == 'a2' and self.table[0][1] == ':black_large_square:':
            self.table[0][1]=':x:'
        
        if position == 'a3' and self.table[0][2] == ':black_large_square:':
            self.table[0][2]=':x:'
        
        if position == 'b1' and self.table[1][0] == ':black_large_square:':
            self.table[1][0]=':x:'
        
        if position == 'b2' and self.table[1][1] == ':black_large_square:':
            self.table[1][1]=':x:'
        
        if position == 'b3' and self.table[1][2] == ':black_large_square:':
            self.table[1][2]=':x:'
        
        if position == 'c1' and self.table[2][0] == ':black_large_square:':
            self.table[2][0]=':x:'
        
        if position == 'c2' and self.table[2][1] == ':black_large_square:':
            self.table[2][1]=':x:'
        
        if position == 'c3' and self.table[2][2] == ':black_large_square:':
            self.table[2][2]=':x:'
    
    def x_won(self):

        if self.table[0][0] == ':x:' and self.table[0][1] == ':x:' and self.table[0][2] == ':x:':
            return True
        
        elif self.table[1][0] == ':x:' and self.table[1][1] == ':x:' and self.table[1][2] == ':x:':
            return True
        
        elif  self.table[2][0] == ':x:' and self.table[2][1] == ':x:' and self.table[2][2] == ':x:':
            return True
        
        elif  self.table[0][0] == ':x:' and self.table[1][0] == ':x:' and self.table[2][0] == ':x:':
            return True
        
        elif  self.table[0][1] == ':x:' and self.table[1][1] == ':x:' and self.table[2][1] == ':x:':
            return True

        elif  self.table[0][2] == ':x:' and self.table[1][2] == ':x:' and self.table[2][2] == ':x:':
            return True

        elif  self.table[0][0] == ':x:' and self.table[1][1] == ':x:' and self.table[2][2] == ':x:':
            return True
        
        elif  self.table[2][0] == ':x:' and self.table[1][1] == ':x:' and self.table[0][2] == ':x:':
            return True
        
        else :
            return False

    def o_won(self):

        if self.table[0][0] == ':o:' and self.table[0][1] == ':o:' and self.table[0][2] == ':o:':
            return True
        
        elif self.table[1][0] == ':o:' and self.table[1][1] == ':o:' and self.table[1][2] == ':o:':
            return True
        
        elif  self.table[2][0] == ':o:' and self.table[2][1] == ':o:' and self.table[2][2] == ':o:':
            return True
        
        elif  self.table[0][0] == ':o:' and self.table[1][0] == ':o:' and self.table[2][0] == ':o:':
            return True
        
        elif  self.table[0][1] == ':o:' and self.table[1][1] == ':o:' and self.table[2][1] == ':o:':
            return True

        elif  self.table[0][2] == ':o:' and self.table[1][2] == ':o:' and self.table[2][2] == ':o:':
            return True

        elif  self.table[0][0] == ':o:' and self.table[1][1] == ':o:' and self.table[2][2] == ':o:':
            return True
        
        elif  self.table[2][0] == ':o:' and self.table[1][1] == ':o:' and self.table[0][2] == ':o:':
            return True
        
        else :
            return False

    def is_draw(self):
        found = False

        for i in range(0,3):
           for j in range(0,3):
               if self.table[i][j] == ':black_large_square:':
                   found = True  
        return found

    async def start_game(self,client,ctx):
        
        await ctx.send(f'The current game is between '+str(self.player1) + ' and '+ str(self.player2))
        title = self.name1 + ' vs ' + self.name2
        legal_moves = 'a1 a2 a3 b1 b2 b3 c1 c2 c3'

        embeded = discord.Embed(
            color = discord.Colour(23)
        )
        embeded.add_field(name = title ,value = self.table_to_string() ,inline=False)
        await ctx.send(embed = embeded)
        embeded.remove_field(0)
        
        while not self.finnished:
            msg = await client.wait_for('message')
            
            if self.isplayer2:
                
                if '<@!'+str(msg.author.id)+'>' == self.player2 and legal_moves.find(msg.content) >= 0:
                    
                    print('player2')
                    self.place_o(msg.content)
                    
                    embeded.add_field(name = title ,value = self.table_to_string() ,inline=False)
                    await ctx.send(embed = embeded)
                    embeded.remove_field(0)
                    
                    self.isplayer2 = False

            elif not self.isplayer2:
                
                if '<@!'+str(msg.author.id)+">" == self.player1 and legal_moves.find(msg.content) >=0:
                    
                    print ('player1')
                    self.place_x(msg.content)
                    
                    embeded.add_field(name = title ,value = self.table_to_string() ,inline=False)
                    await ctx.send(embed = embeded)
                    embeded.remove_field(0)
                    
                    self.isplayer2 = True

            if self.x_won():
                await ctx.send(str(self.player1)+' won!!!!')
                break
            
            if self.o_won():
                await ctx.send(str(self.player2)+' won!!!!')
                break
            
            if not self.is_draw() and not (self.x_won() or self.o_won()):
                await ctx.send("""It's a draw :(""")
                break


            if ('<@!'+str(msg.author.id)+'>' == self.player2 or '<@!'+str(msg.author.id)+'>' == self.player1) and msg.content == 'end':
                await ctx.send ('The game has ended nobody won :(')
                break
        print ('The loop has been escaped')
