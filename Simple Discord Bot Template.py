import discord
from discord.ext import commands

client = commands.Bot(command_prefix ="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def hello(ctx):
    await ctx.send("{custom text}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.attachments:
        for attachments in message.attachments:
            if attachments.filename.lower().endswith(('.png','.jpg','.jpeg','gif','.mp4')):
                await message.channel.send("[Custom Text Response]")
    await client.process_commands(message)

client.run("Bot Token")