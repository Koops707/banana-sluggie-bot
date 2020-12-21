import discord
import os


def code_formating_string(in_string):
    return "```" + in_string + "```"


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # c4.printHello()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.name == 'killerkrok':
        await message.channel.send("https://tenor.com/view/horny-jail-bonk-dog-hit-head-stop-being-horny-gif-17298755")

    elif message.content.startswith('&hello'):
        string_to_send = "Hello " + message.author.mention + " !"
        await message.channel.send(string_to_send)

    elif message.content.startswith("&connect4"):
        await message.channel.send(code_formating_string("Connect 4 in progress - Stay Tuned!"))

    elif message.content.startswith("&opgg"):
        summoner_name = message.content.split()
        if len(summoner_name) != 2:
            await message.channel.send(code_formating_string("Invalid Format: format as \"&opgg <summoner_name>\""))
        else:
            # await message.channel.send(league.report_league_stats(summoner_name[1]))
            if summoner_name[1] == "killerkrok":
                await message.channel.send(code_formating_string("Doo Doo Player"))
            else:
                await message.channel.send(code_formating_string("Functionality not implemented yet"))

client.run(os.environ['AUTH_TOKEN'])
