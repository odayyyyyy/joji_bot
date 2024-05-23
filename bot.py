import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv('TOKEN')
FONT_PATH = "MOBO-Bold.otf"
FONT_SIZE = 40
IMAGE_PATH = "joji.jpeg"
OUTPUT_PATH = "kikikan.jpg"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def textimage(ctx, *, text: str):
    image = Image.open(IMAGE_PATH)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    text_width, text_height = draw.textsize(text, font=font)
    width, height = image.size
    position = ((width - text_width) / 2, (height - text_height) / 2)
    draw.text(position, text, (255, 255, 255), font=font)
    image.save(OUTPUT_PATH)
    await ctx.send(file=discord.File(OUTPUT_PATH))

bot.run(TOKEN)
