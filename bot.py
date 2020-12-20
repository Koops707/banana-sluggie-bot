import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # c4.printHello()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        string_to_send = "Hello " + message.author.mention + " !"
        await message.channel.send(string_to_send)

    elif message.content.startswith("$connect4"):
        await message.channel.send("Connect 4 in progress - Stay Tuned!")

client.run(os.environ['AUTH_TOKEN'])
