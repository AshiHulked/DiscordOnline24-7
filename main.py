import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Aktifkan jika butuh akses ke isi pesan

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Jalankan bot
bot.run(os.getenv("DISCORD_TOKEN"))
