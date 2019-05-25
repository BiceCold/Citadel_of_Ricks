from os.path import join, dirname

import os
from dotenv import load_dotenv

# load the .env file from project root
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
print('Init! Load dotenv.')


def get_config(name: str):
    return os.environ.get(name)
