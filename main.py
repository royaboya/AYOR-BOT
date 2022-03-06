import discord
from discord.ext import commands
import os

TOKEN = '' # idc lol

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='~', intents=intents)


# class Help(commands.MinimalHelpCommand):
#     async def send_pages(self):
#         destination = self.get_destination()
#         for page in self.paginator.pages:
#             emby = discord.Embed(description=page)
#             await destination.send(embed=emby)

# client.help_command = Help()

for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')

if __name__ == '__main__':
    client.run(TOKEN)



