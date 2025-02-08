import os
import time
import logging
import asyncio
from telegram import Bot
from datetime import datetime, timedelta

# Token do seu bot (substitua pelo token gerado pelo BotFather)
TOKEN = "7620534813:AAHcBSowzuDOZV3zmuXdmT7jLoba_O8cU0U"
CHAT_ID = "-1002397537980"  # Coloque o ID do grupo ou usuário que receberá as mensagens

# Configuração do bot
bot = Bot(token=TOKEN)

# Lista de 21 receitas para enviar (7 dias x 3 receitas por dia)
receitas = [
    # Receitas do dia 1
    {
        "nome": "Bolinho de maçã 🍏",
        "ingredientes": [
            "1 maçã grande ralada grosseiramente (pode ralar com a casca)",
            "2 colheres (sopa) de aveia em flocos finos",
            "2 colheres (sopa) de farinha da preferência (pode ser de arroz ou trigo)",
            "1 ovo",
            "1 colher (sopa) de uvas passas previamente hidratadas (opcional)",
            "1 pitada de canela em pó",
            "1 colher (chá) de fermento em pó",
            "Semente de chia e linhaça a gosto"
        ],
        "modo_preparo": "Misture todos os ingredientes (deixando o fermento por último) até a massa ficar bem consistente. Despeje-a em forminhas de cupcake e asse por 15 a 20 minutos ou até dourar. Os bolinhos também podem ser congelados, com validade de 3 meses no freezer."
    },
    {
        "nome": "Papinha de banana 🍌",
        "ingredientes": [
            "1 banana madura",
            "Leite materno ou fórmula",
            "1 colher (sopa) de aveia (opcional)"
        ],
        "modo_preparo": "Amasse bem a banana e misture com o leite materno ou fórmula. Se desejar, adicione aveia para dar mais consistência."
    },
    {
        "nome": "Purê de abóbora 🎃",
        "ingredientes": [
            "1 fatia de abóbora",
            "1 colher (sopa) de azeite",
            "1 pitada de sal (opcional)"
        ],
        "modo_preparo": "Cozinhe a abóbora até ficar bem macia. Amasse bem e adicione azeite e sal a gosto. Pode ser servido com arroz ou como acompanhamento."
    },
    # Receitas do dia 2
    {
        "nome": "Mingau de aveia 🥣",
        "ingredientes": [
            "2 colheres (sopa) de aveia",
            "200 ml de leite",
            "1 colher (sopa) de mel ou açúcar mascavo (opcional)"
        ],
        "modo_preparo": "Misture a aveia no leite e cozinhe até ficar bem cremoso. Adicione mel ou açúcar a gosto para adoçar."
    },
    {
        "nome": "Purê de batata doce 🍠",
        "ingredientes": [
            "1 batata doce média",
            "1 colher (sopa) de azeite",
            "1 pitada de sal (opcional)"
        ],
        "modo_preparo": "Cozinhe a batata doce até ficar macia, depois amasse bem. Adicione azeite e sal a gosto."
    },
    {
        "nome": "Mingau de arroz 🌾",
        "ingredientes": [
            "2 colheres (sopa) de arroz",
            "200 ml de leite",
            "1 colher (sopa) de mel (opcional)"
        ],
        "modo_preparo": "Misture o arroz no leite e cozinhe até ficar cremoso. Adoce com mel se desejar."
    },
    # Receitas do dia 3
    {
        "nome": "Papinha de cenoura 🥕",
        "ingredientes": [
            "1 cenoura média",
            "1 colher (sopa) de azeite",
            "1 pitada de sal (opcional)"
        ],
        "modo_preparo": "Cozinhe a cenoura até ficar bem macia e amasse. Adicione azeite e sal a gosto."
    },
    {
        "nome": "Bolinho de cenoura 🧁",
        "ingredientes": [
            "2 cenouras médias raladas",
            "1 xícara de farinha de trigo",
            "2 ovos",
            "1 colher (chá) de fermento em pó",
            "1 colher (sopa) de açúcar mascavo",
            "1 pitada de sal"
        ],
        "modo_preparo": "Bata tudo no liquidificador até obter uma massa homogênea. Coloque em forminhas de cupcake e asse por 25 minutos ou até dourar."
    },
    {
        "nome": "Purê de mandioquinha 🥔",
        "ingredientes": [
            "4 mandioquinhas médias",
            "1 colher (sopa) de azeite",
            "1 pitada de sal (opcional)"
        ],
        "modo_preparo": "Cozinhe a mandioquinha até ficar bem macia, depois amasse bem. Adicione azeite e sal a gosto."
    },
    # Continuar com mais receitas até completar 21
]

# Função para enviar receitas no horário correto
async def enviar_receitas():
    # Horários para envio (6h, 11h, 20h)
    horarios = [6, 11, 20]
    
    # A partir de agora, enviar uma receita a cada 8 horas
    start_time = datetime.now()

    receita_index = 0  # Para selecionar as receitas

    for i in range(7):  # Para os 7 dias de receitas
        for h in horarios:
            # Calcula o horário de envio para cada dia
            envio_time = start_time.replace(hour=h, minute=0, second=0, microsecond=0) + timedelta(days=i)
            if envio_time < datetime.now():
                envio_time += timedelta(days=1)  # Caso o horário já tenha passado, envia no próximo dia

            # Espera até o horário correto para enviar a receita
            await asyncio.sleep((envio_time - datetime.now()).total_seconds())

            # Envia a receita do dia
            receita = receitas[receita_index]
            mensagem = f"Receita {receita_index+1}: **{receita['nome']}**\n\n**Ingredientes:**\n" + "\n".join([f"- {ing}" for ing in receita['ingredientes']]) + f"\n\n**Modo de preparo:**\n{receita['modo_preparo']}"
            await bot.send_message(chat_id=CHAT_ID, text=mensagem)
            
            # Incrementa o índice para a próxima receita
            receita_index += 1
            if receita_index >= len(receitas):  # Reinicia o ciclo de receitas após 21 receitas
                receita_index = 0

# Inicia o envio das receitas
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(enviar_receitas())  # Inicia a função assíncrona
