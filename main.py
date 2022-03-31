import discord
from discord.ext import commands
import os

TOKEN = "ODAxMTk4NDI1NDUwMDg2NDQx.YAdMLg.4zdYOCzc-fFKm457PVNcfDjN4uw"  # idc lol

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="~", intents=intents)


# class Help(commands.MinimalHelpCommand):
#     async def send_pages(self):
#         destination = self.get_destination()
#         for page in self.paginator.pages:
#             emby = discord.Embed(description=page)
#             await destination.send(embed=emby)

# client.help_command = Help()

for file in os.listdir("./cogs"):
    if file.endswith(".py"):      
        client.load_extension("cogs." + file[:-3])

if __name__ == "__main__":
    client.run(TOKEN)
