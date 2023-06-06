import telebot
import os
from dotenv import load_dotenv
import time
from openai_API import response

load_dotenv()

telegram_token = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(telegram_token, parse_mode=None)

@bot.message_handler(content_types=['text'])
def start(message):
    start = message.text
    if start == '/start':
        bot.send_message(message.chat.id, "Olá, como posso ajudar?")
    else:
        msg = bot.send_message(message.chat.id, "Escrevendo...")
        # print("Usuário:", message.text)
        chat_response = response(message.text)        
        bot.edit_message_text(chat_response, message.chat.id, msg.message_id)
        # print("ChatGPT:", chat_response)