import os
import discord
from discord.ext import commands

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Error: BOT_TOKEN variable is not set.")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_error(event, *args, **kwargs):
    # Implement error handling logic here
    print(f"An error occurred during {event}: {sys.exc_info()}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send("Choo choo! 🚅")

if __name__ == "__main__":
    bot.run(BOT_TOKEN)
