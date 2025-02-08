import os
import logging
import asyncio
from telegram import Bot

# Token do seu bot e ID do grupo
TOKEN = "7620534813:AAHcBSowzuDOZV3zmuXdmT7jLoba_O8cU0U"
CHAT_ID = "-1002397537980"

# Configuração do bot
bot = Bot(token=TOKEN)

# Lista de receitas para enviar diariamente (1 por dia)
receitas = [
    "🍌 Receita 1: Papinha de banana\nAmasse uma banana e misture com leite materno ou fórmula.",
    "🎃 Receita 2: Purê de abóbora\nCozinhe a abóbora e amasse bem antes de servir.",
    "🥣 Receita 3: Mingau de aveia\nMisture aveia com leite e cozinhe até ficar cremoso.",
    "🍎 Receita 4: Bolinho de maçã\nMisture 1 maçã ralada, aveia, ovo, fermento e leve ao forno.",
    "🥑 Receita 5: Purê de abacate\nAmasse um abacate maduro e misture com leite materno.",
    "🥕 Receita 6: Papinha de cenoura\nCozinhe cenoura e bata com um pouco de água.",
    "🍠 Receita 7: Purê de batata-doce\nCozinhe batata-doce e amasse até ficar cremoso."
]

# Arquivo que salva o índice da última receita enviada
SAVE_FILE = "last_sent.json"

def get_last_index():
    """Lê o índice da última receita enviada do arquivo."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            return data.get("last_index", -1)
    return -1

def save_last_index(index):
    """Salva o índice da última receita enviada no arquivo."""
    with open(SAVE_FILE, "w") as f:
        json.dump({"last_index": index}, f)

def enviar_receita_diaria():
    """Envia uma receita por dia, sem repetir."""
    last_index = get_last_index()
    next_index = (last_index + 1) % len(receitas)  # Avança para a próxima receita

    receita = receitas[next_index]
    bot.send_message(chat_id=CHAT_ID, text=receita)

    save_last_index(next_index)  # Salva o índice da receita enviada
    print(f"✅ Receita enviada: {receita}")  # Apenas para verificação nos logs

# Roda apenas 1 vez ao executar o script
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    enviar_receita_diaria()
