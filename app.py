import os
import telebot

from kanobu import kanobu, knb_list
from random import choice
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

bot = telebot.TeleBot(token, parse_mode=None) 


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Давай сыграем в Камень, Ножницы, Бумага")
	

@bot.message_handler(func=lambda m: True)
def game_all(message):
	player = message.text
	if player in knb_list:
		computer = choice(knb_list)
		reply_text = f"Компьютер выбрал {computer}\n{kanobu(player=player, computer=computer)}"
		bot.reply_to(message, reply_text)
	else:
		bot.reply_to(message, "Выбери: Камень Ножницы Бамага")

bot.infinity_polling()