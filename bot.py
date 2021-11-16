import os
import telebot
import random

from dotenv import load_dotenv
from telebot import types

from os.path import join, dirname


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


bot = telebot.TeleBot(os.environ.get('TOKEN'))


@bot.message_handler(commands=['start'])
def welcome (message):
	sti = open('images/111.jpg', 'rb')
	bot.send_photo(message.chat.id, sti, caption = 'Добро пожаловать')
# keybord
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Меню")
	item2 = types.KeyboardButton("Заказать")
	markup.add(item1, item2)
	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nМы готовы принять ваш заказ, \nДля ознакомления с меню нажмите на кнопку 'Меню'".format(message.from_user, bot.get_me()),
			parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Меню':
			bot.send_message(message.chat.id, '''Если у вас намечается мероприятие и вы думаете где вам приобрести корейские салаты?!🤔 
Мы можем вам помочь 😁 
Важно‼️‼️‼️
Принимаем  по предварительному заказу минимум 2 дня.
Меньше 1 кг заказ не принимается!
Контактные номера для заказа 📱 

+998 90-324-52-68
+998 91-137-88-05

Наш прайс лист 🙂
Рыба хе из судака 140,000 за 1 кг 
Мясо хе 180,000 за 1 кг 
Потрашки хе 65,000 за 1 кг 
Требуха хе 65,000 за 1 кг 
Юк хе 160,000 за 1 кг 
Хе из куриной грудки 75,000 за 1 кг 
Сердце хе 75,000 за 1 кг 
Салат из огурцов с мясом  (веча) 80,000 за 1 кг 
Вешенки с мясом жаренные 100,000 за 1 кг
Шампиньоны жаренные с мясом 160,000 за 1 кг 
Опята с мясом 110,000 за 1 кг 
Косари 140,000 за 1 кг 
Салат из водорослей (Меги ча) 60,000 за 1 кг 
Тиргум ча 65,000 за 1 кг 
Чапче 90,000 за 1 кг 
Кактуги 30,000 за 1 кг 
Панчани 110,000 за 1 кг
Кимчхи 50,000 за 1 кг 
Крахмальные Пегодя  5000 1 шт (минимальный заказ 30 шт)''' )
		elif message.text == 'Заказать':
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Кимчхи", callback_data='kim')
			item2 = types.InlineKeyboardButton("Панчани", callback_data='pan')
			markup.add(item1, item2)
			bot.send_message(message.chat.id, 'Что будете заказывать?',parse_mode='html', reply_markup=markup)
		else:
			pass


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'kim':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сколько кг?",
			reply_markup=None)
				bot.send_message(call.message.chat.id, 'Введите число')

				if message.text == 1:
					bot.send_message(call.message.chat.id, 'Ваш заказ принят')  # тут у меня ругается на NameError("name 'message' is not defined")
					#Тут наверное надо чтобы записывал куда то заказ
					markup = types.InlineKeyboardMarkup(row_width=2)
					item1 = types.InlineKeyboardButton("Главное меню", callback_data='mainm')
					item2 = types.InlineKeyboardButton("Ещё заказать", callback_data='zak')
					markup.add(item1,item2)
					bot.send_message(message.chat.id, 'Что-нибудь ещё',parse_mode='html', reply_markup=markup)
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Работать....')
	except Exception as e:
		print(repr(e))
#RUN
bot.polling(none_stop=True)