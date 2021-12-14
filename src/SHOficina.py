import json

def autenticacao(cpf):
    with open("../clientes.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)

    for id_user in dados:
        if (id_user['id'] == cpf):
            return True
    return False