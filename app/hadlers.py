from app import bot
from app.games import kanobu, return_knb
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


state = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
	user_id = message.from_user.id
	state[user_id] = "start"
	bot.reply_to(message, "Давай сыграем в Камень, Ножницы, Бумага")
	

@bot.message_handler(commands=["games"])
def send_games(message):
	print(message)
	chat_id = message.chat.id
	bot.send_message(chat_id, "Для игры в КНБ отправь команду /КНБ")

@bot.message_handler(commands=["КНБ"])
def set_state_knb(message):
	user_id = message.from_user.id
	state[user_id] = "knb"
	bot.send_message(message.chat.id, "Теперь играем в КМБ!")

@bot.message_handler(commands=["exit"])
def set_state_exit(message):
	user_id = message.from_user.id
	state[user_id] = "start"
	bot.send_message(message.chat.id, "Хорошо сыграли!")

@bot.message_handler(text=["игра", "Игра", "Games"])
def show_games(message):
	markup = InlineKeyboardMarkup()
	markup.add(InlineKeyboardButton("Играем!", callback_data="game"))
	markup.add(InlineKeyboardButton("Не хочу", callback_data="no"))
	bot.send_message(message.chat.id, "Давай сыграем!", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def game_all(message):
	user_state = state[message.from_user.id]
	
	if user_state == "knb":
		player = message.text
		if player in return_knb():
			comp_choice, who_win = kanobu(player)
			reply_text = f"{comp_choice}\n{who_win}"
			bot.reply_to(message, reply_text)
		else:
			bot.reply_to(message, "Выбери: Камень Ножницы Бамага")
	elif user_state == "start":
		bot.reply_to(message,"Для выбора игры введите команду /games")