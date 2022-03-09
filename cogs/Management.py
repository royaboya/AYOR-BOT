import discord
from discord.ext import commands


class Management(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["mention"])
    async def ping(self, ctx, member: discord.Member):
        for _ in range(5):
            await ctx.send(member.mention)

    @commands.command(aliases=["move"])
    async def move_all(
        self,
        ctx,
        current: discord.VoiceChannel = None,
        destination: discord.VoiceChannel = None,
    ):
        for member_id in current.voice_states.keys():
            memb = ctx.guild.get_member(member_id)
            await memb.move_to(destination)

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def silence(self, ctx, member_to_get: discord.Member):
        await member_to_get.edit(mute=True)


def setup(client):
    client.add_cog(Management(client))
