import discord
import random
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

    # if message.author.name == 'killerkrok':
    #    await message.channel.send("https://tenor.com/view/horny-jail-bonk-dog-hit-head-stop-being-horny-gif-17298755")

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

    """
    elif message.content.startswith("&roll"):
        dice_text = message.content.split()
        dice_limit = int(dice_text[1])
        print(dice_text)
        print(dice_limit)
        if dice_limit < 1 or dice_limit > 200:
            await message.channel.send(code_formating_string("Error: Must be in range 2 - 200"))
        else:
            dice_roll = random.randint(1, dice_limit)
            print(dice_roll)
            discord_tag = message.author.name
            await message.channel.send(f"{discord_tag} s roll: {dice_roll}")
    """


client.run(os.environ['AUTH_TOKEN'])
