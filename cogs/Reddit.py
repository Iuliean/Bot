import discord
from discord.ext import commands
from numpy import random
import praw

class Reddit (commands.Cog):
    def __init__(self,client):
        self.client = client
        self.reddit = praw.Reddit(client_id = "",
                                  client_secret = "",
                                  user_agent="")        

    @commands.command()
    async def reddit_ok(self,ctx):
        await ctx.send(self.reddit.read_only)
    
    @commands.command()
    async def reddit(self,ctx,subreddit,tag):
        posts = []
        try:
            if tag == "new":
                for submission in self.reddit.subreddit(subreddit).new(limit =100):
                    print(submission.url)
                    posts.append(submission.url)
        
            elif tag == "hot":
                for submission in self.reddit.subreddit(subreddit).hot(limit =100):
                    print(submission.url)
                    posts.append(submission.url)
           
            elif tag == "top":
                for submission in self.reddit.subreddit(subreddit).top(limit =100):
                    print(submission.url)
                    posts.append(submission.url)
            
            elif tag == "controversial":
                for submission in self.reddit.subreddit(subreddit).controversial(limit =100):
                    print(submission.url)
                    posts.append(submission.url)
            
            elif tag == "rising":
                for submission in self.reddit.subreddit(subreddit).rising(limit =100):
                    print(submission.url)
                    posts.append(submission.url)
            
            await ctx.send(posts[random.randint(0,len(posts))])
            
        except:
            await ctx.send("Something went wrong BOSS")

def setup (client):
    client.add_cog(Reddit(client))