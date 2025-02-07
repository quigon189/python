import os
import telebot
from telebot import custom_filters

from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

bot = telebot.TeleBot(token, parse_mode=None) 

from app import hadlers

bot.add_custom_filter(custom_filters.TextMatchFilter())