#Essas linhas importam as bibliotecas necessárias, incluindo os, aiogram, openai e tokens.
import os
from aiogram import Bot, Dispatcher, executor, types
import openai
import tokens

#Aqui é definida uma classe chamada Reference que possui um atributo response vazio. Essa classe é 
#usada para armazenar a resposta anterior do modelo de linguagem.
class Reference:

    def __init__(self) -> None:
        self.response = ""

#Essa linha configura a chave de API do OpenAI para acessar a API do Chat GPT. O valor da chave é obtido do arquivo tokens.py, da variável token_chatGPT
openai.api_key = tokens.token_chatGPT

#Aqui é criado um objeto reference da classe Reference para armazenar a resposta anterior do modelo de linguagem.
reference = Reference()

#A variável TOKEN é definida com o valor da chave do token do bot do Telegram, obtido do arquivo tokens.py, da variável token_telegramBot.
TOKEN = tokens.token_telegramBot

# A variável MODEL_NAME é definida com o nome do modelo usado pelo Chat GPT. Nesse caso, o modelo é "gpt-3.5-turbo".
MODEL_NAME = "gpt-3.5-turbo"

#O objeto bot é inicializado com o token do bot do Telegram e o objeto dispatcher é inicializado com o objeto bot.
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

# Essa função clear_past() é definida para limpar a conversa e o contexto anterior. Ela define o atributo response do objeto reference como uma string vazia.
def clear_past():

    reference.response = ""

# Esse é um tratador de eventos para o comando /start. Quando um usuário envia esse comando, a função welcome() é chamada. Ela limpa a conversa anterior chamando clear_past() e envia uma mensagem de boas-vindas ao usuário.
@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    clear_past()
    await message.reply("Bem vindo ao ChatGPT Bot. This is a test! Como posso ajudar você?")


# A handler to clear the previous message

    
# Esse é um tratador de eventos para o comando /help. Quando um usuário envia esse comando, a função helper() é chamada. Ela define a variável help_command com uma string contendo os comandos disponíveis e envia essa mensagem ao usuário.
@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    help_command = """
    Comandos disponíveis:
/start - Inicia a conversa
/clear - Limpa a conversa
/help - Exibe este menu    
    """
    await message.reply(help_command)

#Esse é um tratador de eventos para qualquer mensagem recebida. Quando uma mensagem é recebida, a função welcome() é chamada. Ela utiliza a API do Chat GPT para gerar uma resposta com base na mensagem do usuário e na resposta anterior armazenada em reference.response. A resposta gerada é armazenada em reference.response para ser usada como referência na próxima iteração. A resposta também é enviada como mensagem para o usuário.
@dispatcher.message_handler()
async def welcome(message: types.Message):
    #print(f">> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = MODEL_NAME,
        messages=[
            {"role": "assistant", "content": reference.response},
            {"role": "user", "content": message.text} #our query
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    
    #print(f">> Chat GPT: \n\t{reference.response}")

    await bot.send_message(chat_id=message.chat.id, text=reference.response)

#main()
if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)