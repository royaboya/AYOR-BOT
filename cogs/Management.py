import discord
from discord.ext import commands

class Management(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["mention"])
    async def ping(self, ctx, member:discord.Member):
        await ctx.send(member.mention, delete_after=10)

def setup(client):
    client.add_cog(Management(client))