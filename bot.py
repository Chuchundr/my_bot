import os
import telebot
import random

from dotenv import load_dotenv
from telebot import types

from os.path import join, dirname


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


bot = telebot.TeleBot(os.environ.get('TOKEN'))
