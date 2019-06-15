import discord
from Gif_Rick.rick_random_gif import random_gif
from Environment_Handlers.configs import get_config
from Anti_Politics_Rick.anti_politics_rick import politics_words, way_up_there
from Random_Rick_Message.random_message import random_message

# attain access token
TOKEN = get_config("discord_token")
embed = discord.Embed()
client = discord.Client()


@client.event
async def on_message(message):
    # don't let Rick talk to himself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg1 = 'hey, hey there *brrrp* {0.author.mention} you fuckin little idiot.'.format(message)
        await message.channel.send(msg1)

    if message.content.startswith('!quote'):
        msg2 = random_message().format(message)
        await message.channel.send(msg2)

    if message.content.startswith('!gif'):
        msg3 = random_gif().format(message)
        await message.channel.send(msg3)

    message_string = message.content.lower()

    for word in politics_words():
        if message_string.find(word) != -1:
            embed.set_image(url=way_up_there())
            await message.channel.send(message.channel, embed=embed)

        else:
            # content is not matched, move on
            continue


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


def give_him_life():
    try:
        client.run(TOKEN)
    except KeyboardInterrupt:
        print("you killed me")
        client.logout()
    finally:
        client.close()


if __name__ == "__main__":

    give_him_life()
