import discord
from discord.ext import commands
import os
import requests

TOKEN = '' # Paste token here

bot = commands.Bot(command_prefix = '.')

def tell_joke():
	url = 'https://icanhazdadjoke.com/'
	response = requests.get(url, headers={"Accept": "application/json"})
	data = response.json()
	return str(data['joke'])

@bot.event
async def on_ready():
	print("Let's go!")

# Prints the joke
@bot.event
async def on_message(message):
	channel = message.channel
	content = message.content
	if content == '.joke':
		joke = tell_joke()
		await channel.send(joke)

bot.run(TOKEN)

