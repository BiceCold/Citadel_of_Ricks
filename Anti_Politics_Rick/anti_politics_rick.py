import discord
from Citadel_of_Ricks.Anti_Politics_Rick.random_message import random_message
from Gif_Rick.rick_random_gif import random_gif
from Environment_Handlers.configs import get_config


# attain access token
TOKEN = get_config("discord_token")
client = discord.Client()

politic_words = ["gun",
                 "housing",
                 "homeless",
                 "regulation",
                 "restriction",
                 "politic",
                 "assault",
                 "rifle",
                 "protest"
                 ]
embed = discord.Embed()
wayup_url = 'http://i0.kym-cdn.com/photos/images/original/000/703/020/271.gif'


@client.event
async def on_message(message):
    #don't let Rick talk to himself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        channel = message.channel
        msg1 = 'hey, hey there *brrrp* {0.author.mention} you fuckin little idiot.'.format(message)
        await channel.send(msg1)

    if message.content.startswith('!quote'):
        channel = message.channel
        msg2 = random_message().format(message)
        await channel.send(msg2)

    if message.content.startswith('!gif'):
        channel = message.channel
        msg3 = random_gif().format(message)
        await channel.send(msg3)

    message_string = message.content.lower()

    for word in politic_words:
        if message_string.find(word) != -1:
            channel = message.channel
            embed.set_image(url=wayup_url)
            await channel.send(embed=embed)

        else:
            #content is not matched, move on
            continue


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run(TOKEN)

