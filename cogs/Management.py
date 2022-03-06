import discord
from discord.ext import commands

class Management(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["mention"])
    async def ping(self, ctx, member:discord.Member):
        await ctx.send(member.mention, delete_after=10)

    @commands.command(aliases=["move"])
    async def move_all(self, ctx, current : discord.VoiceChannel=None, destination : discord.VoiceChannel=None):
        for member_id in current.voice_states.keys():
            memb = ctx.guild.get_member(member_id)
            await memb.move_to(destination)

def setup(client):
    client.add_cog(Management(client))