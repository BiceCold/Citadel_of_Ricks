# Citadel_of_Ricks
The citadel is a place for Ricks to hang out and wait to be summoned. Each Rick will be callable in a discord bot.

In order for Anti-Politics Rick to work properly you must include a .env file in your project containing keys for imgur 
and discord. the format is:

client_id = 'xxxxxxxxxxxxx'
client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
refresh_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
discord_token = "xxxxxxxxxxxxxxxxxxxxxxxx.xxxxxxxxx.xxxxxxxxxxxxxxxxxxx"

### anti politics rick
This module is designed to read messages posted in channels that the counsel has access to. It then checks for words in
the list of political topics and if one is in the message it posts a gif meant to deter this kind of discussion.

### gif rick
This module connects to an Imgur account dedicated to hosting random Rick and Morty gifs. When called, it looks through
the account and selects a random gif to post to the channel.

### counsel of ricks
This module reads messages in the channel and responds using the methods in the other modules.

### random rick message
This module contains a list of random Rick quotes and returns a random one from the list. The reason it is broken into
it's own module is because the list is unwieldy and I may want to use it somewhere else later.

### environment handlers
This module maintains access to private keys and tokens for accessing your own accounts and API's