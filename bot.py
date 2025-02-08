import logging
import asyncio
from telegram import Bot

# Token do seu bot (substitua pelo token gerado pelo BotFather)
TOKEN = "7620534813:AAHcBSowzuDOZV3zmuXdmT7jLoba_O8cU0U"
CHAT_ID = "-1002397537980"  # Coloque o ID do grupo ou usuário que receberá as mensagens

# Configuração do bot (utilizando a versão assíncrona)
bot = Bot(token=TOKEN)

# Lista de receitas para enviar diariamente
receitas = [
    "Receita 1: **Bolinho de maçã 🍏**\n\n**Ingredientes:**\n- 1 maçã grande ralada grosseiramente (pode ralar com a casca)\n- 2 colheres (sopa) de aveia em flocos finos\n- 2 colheres (sopa) de farinha da preferência (pode ser de arroz ou trigo)\n- 1 ovo\n- 1 colher (sopa) de uvas passas previamente hidratadas (opcional)\n- 1 pitada de canela em pó\n- 1 colher (chá) de fermento em pó\n- Semente de chia e linhaça a gosto\n\n**Modo de preparo:**\nMisture todos os ingredientes (deixando o fermento por último) até a massa ficar bem consistente. Despeje-a em forminhas de cupcake e asse por 15 a 20 minutos ou até dourar. Os bolinhos também podem ser congelados, com validade de 3 meses no freezer.",
    
    "Receita 2: **Papinha de abóbora e cenoura 🎃🥕**\n\n**Ingredientes:**\n- 1/2 abóbora cabotiá descascada e cortada em pedaços\n- 1 cenoura média, cortada em rodelas\n- 1 colher (sopa) de azeite de oliva\n- 1 pitada de sal (opcional)\n- Água para cozinhar\n\n**Modo de preparo:**\nCozinhe a abóbora e a cenoura até ficarem bem macias. Após o cozimento, bata tudo no liquidificador com um pouco da água do cozimento para obter a consistência desejada. Sirva com uma pitada de azeite.",
    
    "Receita 3: **Mingau de aveia com maçã 🥣🍏**\n\n**Ingredientes:**\n- 3 colheres (sopa) de aveia em flocos finos\n- 1 maçã pequena ralada\n- 1 xícara de leite materno ou fórmula (ou leite de amêndoas)\n- 1 colher (chá) de mel (opcional, para bebês maiores de 1 ano)\n\n**Modo de preparo:**\nEm uma panela, cozinhe a aveia com o leite até que ela esteja bem cozida e cremosa. Adicione a maçã ralada e cozinhe por mais 2 minutos. Se for usar mel, adicione no final. Deixe esfriar antes de servir ao bebê.",
    
    "Receita 4: **Papinha de pêra e banana 🍐🍌**\n\n**Ingredientes:**\n- 1 pêra madura cortada em pedaços pequenos\n- 1 banana média\n- 1 colher (chá) de suco de limão (opcional)\n\n**Modo de preparo:**\nAmasse a banana com um garfo e reserve. Cozinhe a pêra até ficar bem macia, depois amasse-a também. Misture as duas frutas e adicione o suco de limão, se desejado, para evitar que a pêra oxide.",
    
    "Receita 5: **Purê de batata-doce e frango 🍠🍗**\n\n**Ingredientes:**\n- 1 batata-doce média\n- 1 peito de frango cozido e desfiado\n- 1 colher (sopa) de azeite de oliva\n- Água para cozimento\n\n**Modo de preparo:**\nCozinhe a batata-doce até ficar bem macia. Em seguida, amasse-a até obter um purê. Misture o frango desfiado e acrescente um pouco de azeite de oliva. Caso precise, adicione um pouco da água do cozimento da batata-doce para ajustar a consistência.",
    
    "Receita 6: **Papinha de abacate 🥑**\n\n**Ingredientes:**\n- 1 abacate maduro\n- 1 colher (sopa) de leite materno ou fórmula\n- 1 pitada de canela em pó (opcional)\n\n**Modo de preparo:**\nAmasse o abacate com um garfo até obter um purê bem macio. Se necessário, adicione um pouco de leite materno ou fórmula para deixar a papinha mais cremosa. Se o bebê já tiver mais de 1 ano, pode adicionar uma pitada de canela.",
    
    "Receita 7: **Mingau de arroz com banana 🍌🍚**\n\n**Ingredientes:**\n- 2 colheres (sopa) de arroz cozido\n- 1 banana madura amassada\n- 1/2 xícara de leite materno ou fórmula\n\n**Modo de preparo:**\nCozinhe o arroz até ele estar bem macio. Em uma panela, misture o arroz cozido com o leite e cozinhe até o mingau ficar bem cremoso. Depois, adicione a banana amassada e misture bem. Deixe esfriar antes de servir.",
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
