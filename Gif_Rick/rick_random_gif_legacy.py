import imgurpython
from Citadel_of_Ricks import ID
import random


client_id = ID.client_id
client_secret = ID.client_secret
client_refresh_token = ID.refresh_token
client_access_token = ID.access_token
username = 'antipoliticsrick'

client = imgurpython.ImgurClient(client_id, client_secret, client_access_token, client_refresh_token)

# album_ids = client.get_account_album_ids(username, page=0)
img_lst = client.get_album_images('GebVe10')

giflink = []

def random_gif():
    for gif in img_lst:
        giflink.append(gif.link)
    randomgif = random.choice(giflink)
    return(randomgif)
