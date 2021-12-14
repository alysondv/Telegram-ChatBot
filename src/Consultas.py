from datetime import datetime
from Key import bot
import json

def getOrdens(cid, cpf):
    with open("../clientes.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)

    for id_user in dados:
        if (id_user['id'] == cpf):
            for obj in id_user['ordens']: 
                ord = f"""
                    id: {obj['id']}
                    data: {obj['data']}
                    produto: {obj['produto']}
                """
                bot.send_message(cid, ord)
            break

def getStatus(status, cpf):
    cont = 0
    with open("../clientes.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    for id_user in dados:
        if (id_user['id'] == cpf):
            for obj in id_user['ordens']: 
                if(obj['id'] == status.text):
                    stat = f"status: {obj['status']}"
                    bot.send_message(status.chat.id, stat)
                    cont += 1
            if(cont == 0):
                bot.send_message(status.chat.id, "Sem ordem com esse ID")
            break

def getOrcamento(orcamento, cpf):
    cont = 0
    with open("../clientes.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    for id_user in dados:
        if (id_user['id'] == cpf):
            for obj in id_user['ordens']: 
                if(obj['id'] == orcamento.text):
                    stat = f"orcamento: R${obj['orcamento']}"
                    bot.send_message(orcamento.chat.id, stat)
                    cont += 1
            if(cont == 0):
                bot.send_message(orcamento.chat.id, "Sem ordem com esse ID")
            break

def getRecibo(recibo, cpf):
    cont = 0
    with open("../clientes.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    for id_user in dados:
        if (id_user['id'] == cpf):
            for obj in id_user['ordens']: 
                if(obj['id'] == recibo.text):
                    stat = f"""
                    \tProduto: {obj['produto']}
                    data: {obj['data']}
                    Orçamento: R${obj['orcamento']}

                    Cod. Recibo: {obj['recibo']}
                    """
                    bot.send_message(recibo.chat.id, stat)
                    cont += 1
            if(cont == 0):
                bot.send_message(recibo.chat.id, "Sem ordem com esse ID")
            break

def setFeedback(feedback, cpf):
    cont = 0
    with open("../clientes.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    for id_user in dados:
        if (id_user['id'] == cpf):
            for obj in id_user['ordens']: 
                if(obj['id'] == feedback.text):
                    cid = feedback.chat.id
                    setFeedb = bot.send_message(cid, 'Envie seu feedback:')
                    bot.register_next_step_handler(setFeedb , registerFeedback)
                    cont += 1
            if(cont == 0):
                bot.send_message(feedback.chat.id, "Sem ordem com esse ID")
            break

    
            
def registerFeedback(message):
    cid = message.chat.id
    feedback = message.text
    arquivo = f"{cid}_feedback.txt" 

    with open(arquivo, 'a', encoding='utf-8') as arq:
        arq.write(f"user: {cid} - {datetime.now()}")
        arq.write("\n")
        arq.write(feedback)
        arq.write("\n")
        # send_to_db(f"{cid}_feedback.txt")
        # dados armazenados em feedback que seriam enviados para o db 

    bot.send_message(cid, "Obrigado pelo feedback!")