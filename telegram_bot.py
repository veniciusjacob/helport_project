import telebot
import openai_api
import support_database

telegram_token = '6196110344:AAHmhS4iXHeRO73hdElgjVQyVU_r2gSJYLo'
bot = telebot.TeleBot(telegram_token)

@bot.message_handler(commands=['start'])
def start(message):
    # Mensagem de boas-vindas
    welcome_message = "Bem-vindo ao Helport! Como posso ajudar você?"

    bot.reply_to(message, welcome_message)

@bot.message_handler(func=lambda message: True)
@bot.message_handler(func=lambda message: True)
def responder_mensagem(message):
    if message.from_user is not None:
        input_text = message.text

        # Exibir mensagem "digitando"
        bot.send_chat_action(message.chat.id, 'typing')

        # Verifica se a resposta está no banco de dados
        response = support_database.search_database(input_text)

        if response is not None:
            # Resposta encontrada no banco de dados
            bot.reply_to(message, response)
        else:
            # Se a resposta não estiver no banco de dados, usa a API do ChatGPT
            reply = openai_api.generate_response(input_text)

            # Adiciona a entrada e a resposta ao banco de dados
            support_database.add_to_database(input_text, reply)

            bot.reply_to(message, reply)
print("Bot is now running")
bot.polling()
