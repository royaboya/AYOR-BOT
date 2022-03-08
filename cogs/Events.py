import discord
from discord.ext import commands

# stack over flow link because i forgot
# https://stackoverflow.com/questions/48038953/bot-event-in-a-cog-discord-py


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("it's on")
        await self.client.change_presence(activity=discord.Game(name = "with your mother"))


def setup(client):
    client.add_cog(Events(client))
