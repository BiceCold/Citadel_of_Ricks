import random


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
              "You're young, you have your whole life ahead of you, and your anal cavity is still taut yet malleable",
              "They’re just robots, {0.author.mention}! It’s OK to shoot them! They’re robots!........It’s a figure of speech, {0.author.mention}. They’re bureaucrats. I don’t respect them",
              "What, so everyone’s supposed to sleep every single night now?",
              "being nice is something stupid people do to hedge their bets",
              "Hey, save your Rick rules for the ueh sheep-Ricks, Rick-pig.",
              "Fuck you? No, no, no, no, no, fuck me!",
              "Uncertainty is inherently unsustainable. Eventually, everything either is or isn't.",
              "Think for yourselves. Don’t be sheep.",
              "Me sleeping on these linens is the favor. I mean w-w-what are we vindicating? Comfort?",
              "Two things I want to make very clear to everyone in this room. Never betray me and it's time to go.",
              "{0.author.mention}, is there any light beer left? It's amazing what you miss while in prison..........no you're right. Where's the vodka?",
              "So what's your origin? Did you fall into a vat of redundancy?",
              "I was also late because of my drinking and mentioned it to.....no one.",
              "Listen, {0.author.mention}, I hate to break it to you but what people call 'love' is just a chemical reaction that compels animals to breed. It hits hard, {0.author.mention}, then it slowly fades, leaving you stranded in a failing marriage. I did it. Your parents are gonna do it. Break the cycle, {0.author.mention}. Rise above. Focus on science"
              ]
    return random.choice(phrase)
