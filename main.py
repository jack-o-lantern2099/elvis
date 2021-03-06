"""
Created By Jivansh Sharma 
September 2020
@parzuko

"""

import discord
import os 
from get_token import token as TOKEN
from discord.ext import commands

elvis = commands.Bot(command_prefix = ".")
elvis.remove_command("help")

for cog in os.listdir("./cogs"):
    if cog.endswith('.py'):
        elvis.load_extension(f"cogs.{cog[:-3]}")

elvis.run(TOKEN)
