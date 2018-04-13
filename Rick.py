import discord
import random


TOKEN = 'NDM0MTY0NjY2OTY1Njg4MzMx.DbGa9A.4Oj5lM-epxmzL_U36UYmQt-VIrI'
client = discord.Client()

def random_message():
    phrase = ["I'm sorry, but your opinion means very little to me.",
              "Ooh la la, someone's getting laid in college.",
              "wubalubadubdub!",
              "Don't break your arm jerking yourself off",
              "lick lick lick my balls",
              "let's get riggity riggity wrecked son!",
              "you're a piece of shit and I can prove it mathematically"
              "I'm pickle Rick!",
              "I'm going to need you to take these and shove 'em waaaay up inside your butthole.",
              "Let's get schwifty",
              "Don't hate the player, hate the game son",
              "You backed the wrong conceptual horse",
              "Weddings are basically funerals with cake",
              "It's like the N word and the C word had a baby and it was raised by all the bad words for Jews",
              "You're young, you have your whole life ahead of you, and your anal cavity is still taut yet malleable"
              ]
    return random.choice(phrase)


wayup_url = 'http://i0.kym-cdn.com/photos/images/original/000/703/020/271.gif'
embed = discord.Embed()
politic_words = ["gun", "guns", "housing", "homeless", "regulation"]

@client.event
async def on_message(message):
    #don't let Rick talk to himself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg1 = 'hey, hey there *brrrp* {0.author.mention} you fuckin little idiot.'.format(message)
        await client.send_message(message.channel, msg1)

    if message.content.startswith('!quote'):
        msg2 = random_message().format(message)
        await client.send_message(message.channel, msg2)

    if "gun" in message.content.lower():
        msg3 = embed.set_image(url=wayup_url)
        await client.send_message(message.channel, embed=embed)

    if "guns" in message.content.lower():
        msg3 = embed.set_image(url=wayup_url)
        await client.send_message(message.channel, embed=embed)

    if "assault" in message.content.lower():
        msg3 = embed.set_image(url=wayup_url)
        await client.send_message(message.channel, embed=embed)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run(TOKEN)
