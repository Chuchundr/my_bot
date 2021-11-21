import os
import json
import logging

from dotenv import load_dotenv

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Handler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler, DictPersistence

from os.path import join, dirname

from data import Data

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

admins = Data(table='admins', columns=['name', 'chat_id'])
general = Data(table='general_info', columns=['name', 'text'])

updater = Updater(token=os.environ.get('TOKEN'), use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    start_message = general.to_dict().get('start_message').encode('utf8')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=start_message.decode('utf8')
    )


start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()