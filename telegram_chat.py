import telebot
import os
from dotenv import load_dotenv
import time
from openai_API import response


load_dotenv()

telegram_token = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(telegram_token, parse_mode=None)

context = {}  # Dicionário para armazenar o contexto

def get_previous_response(chat_id, message):
    if chat_id in context:
        previous_context = context[chat_id]
    else:
        previous_context = ""

    context[chat_id] = previous_context + " " + message  # Atualiza o contexto com a nova mensagem

    resposta = response(context[chat_id])  # Gera a resposta com base no contexto atualizado

    return resposta


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Olá, bem vindo ao Helport, como posso ajudar? Para ver o menu de comandos digite '/help'")

@bot.message_handler(commands=['help'])
def handle_help(message):
    commands = [
        "/help - Exibir esta mensagem de ajuda",
        "/clear - Limpar o contexto da conversa"
    ]
    help_message = "Comandos disponíveis:\n\n"
    help_message += "\n".join(commands)
    bot.send_message(message.chat.id, help_message)

@bot.message_handler(commands=['clear'])
def handle_clear(message):
    chat_id = message.chat.id
    if chat_id in context:
        del context[chat_id]
        bot.send_message(chat_id, "O contexto foi limpo.")
    else:
        bot.send_message(chat_id, "Não há contexto para limpar.")

@bot.message_handler(content_types=['text'])
def handle_message(message):
    msg = bot.send_message(message.chat.id, "Escrevendo...")
    print("Usuário:", message.text)
    resposta = get_previous_response(message.chat.id, message.text)
    context[message.chat.id] = ""  # Limpa o contexto anterior após gerar a resposta
    bot.edit_message_text(resposta, message.chat.id, msg.message_id)
    print("ChatGPT:", resposta)















