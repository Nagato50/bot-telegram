import os
import time
import logging
import asyncio
from telegram import Bot

# Token do seu bot (substitua pelo token gerado pelo BotFather)
TOKEN = "7620534813:AAHcBSowzuDOZV3zmuXdmT7jLoba_O8cU0U"
CHAT_ID = "-1002397537980"  # Coloque o ID do grupo ou usuário que receberá as mensagens

# Configuração do bot
bot = Bot(token=TOKEN)

# Lista de receitas para enviar diariamente
receitas = [
    "Receita 1: Papinha de banana 🍌\nAmasse uma banana e misture com um pouco de leite materno ou fórmula.",
    "Receita 2: Purê de abóbora 🎃\nCozinhe a abóbora e amasse bem antes de servir.",
    "Receita 3: Mingau de aveia 🥣\nMisture aveia com leite e cozinhe até ficar cremoso.",
    "Receita 4: Bolinho de maçã 🍏\nMisture maçã, aveia, farinha, ovo e canela. Asse até dourar.",
    "Receita 5: Papinha de cenoura 🥕\nCozinhe a cenoura e amasse bem.",
    "Receita 6: Mingau de arroz 🌾\nMisture arroz com leite e cozinhe até ficar cremoso.",
    "Receita 7: Purê de batata doce 🍠\nCozinhe a batata doce e amasse bem antes de servir."
]

# Função assíncrona para enviar receitas diariamente
async def enviar_receitas():
    while True:
        for receita in receitas:
            await bot.send_message(chat_id=CHAT_ID, text=receita)
            await asyncio.sleep(86400)  # Espera 24 horas (86400 segundos) antes de enviar a próxima receita

# Inicia o envio das receitas
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(enviar_receitas())  # Inicia a função assíncrona
