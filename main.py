from discord.ext import commands
import discord
import json
from pathlib import Path

bot = commands.Bot(command_prefix=">")
config = json.load(open("config.json"))

@bot.event
async def on_ready():
    print("Bot is ready")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{file[:-3]}")
            print(f"{file} is loaded")
        except:
            print(f"Error occured while loading {file}")



bot.run(config["token"])
