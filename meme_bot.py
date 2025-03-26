import discord
from discord.ext import commands
import os, random
import requests
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Cada vez que se llama a la solicitud de pato, el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def mem(ctx):
    '''Envía mem1 hasta mem5 uno por uno'''
    for i in range(1, 6):
        filepath = f'Images/mem{i}.jpg'
        print(f"Intentando abrir: {filepath}")  # Depuración
        if os.path.exists(filepath):
            try:
                with open(filepath, 'rb') as f:
                    picture = discord.File(f)
                    await ctx.send(file=picture)
            except Exception as e:
                await ctx.send(f"❌ Error al enviar el archivo: {e}")
        else:
            await ctx.send(f"❌ No se encontró el archivo: {filepath}")
bot.run("MTM1MTcyNjM1MzUzNTIwNTM3Ng.GiHU70._mCkOu6UtKcgj5o1wcgqdYqDb6R9v8NNAjUSfM")