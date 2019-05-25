import imgurpython
from Environment_Handlers.configs import get_config
import random


client_id = get_config("client_id")
client_secret = get_config("client_secret")
client_refresh_token = get_config("client_refresh")
client_access_token = get_config("client_access_token")
username = 'antipoliticsrick'

client = imgurpython.ImgurClient(client_id, client_secret, client_access_token, client_refresh_token)

# album_ids = client.get_account_album_ids(username, page=0)
img_lst = client.get_album_images('GebVe10')

giflink = []


def random_gif():
    for gif in img_lst:
        giflink.append(gif.link)
    randomgif = random.choice(giflink)
    return randomgif
