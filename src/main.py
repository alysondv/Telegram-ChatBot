from Key import bot
from datetime import datetime
from SHOficina import autenticacao
from Consultas import getOrdens, getStatus, getOrcamento, getRecibo, setFeedback

def verificaCPF(message, opcao):
    cid = message.chat.id
    cpf = message.text
    if(not(autenticacao(cpf))):
        bot.send_message(cid, "Cliente não encontrado!")
    else:
        if(opcao == 1):
            getOrdens(cid, cpf)
        elif(opcao == 2):
            setOrdem = bot.send_message(message.chat.id, "ID da Ordem de serviço: ")
            bot.register_next_step_handler(setOrdem , getStatus, cpf)
        elif(opcao == 3):
            setOrdem = bot.send_message(message.chat.id, "ID da Ordem de serviço: ")
            bot.register_next_step_handler(setOrdem , getOrcamento, cpf)
        elif(opcao == 4):
            setOrdem = bot.send_message(message.chat.id, "ID da Ordem de serviço: ")
            bot.register_next_step_handler(setOrdem , getRecibo, cpf)
        elif(opcao == 6):
            setOrdem = bot.send_message(message.chat.id, "ID da Ordem de serviço: ")
            bot.register_next_step_handler(setOrdem , setFeedback, cpf)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    setLogin = bot.send_message(mensagem.chat.id, "Envie seu CPF/CNPJ:")
    bot.register_next_step_handler(setLogin , verificaCPF, 1)


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    setLogin = bot.send_message(mensagem.chat.id, "Envie seu CPF/CNPJ:")
    bot.register_next_step_handler(setLogin , verificaCPF, 2)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    setLogin = bot.send_message(mensagem.chat.id, "Envie seu CPF/CNPJ:")
    bot.register_next_step_handler(setLogin , verificaCPF, 3)

@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    setLogin = bot.send_message(mensagem.chat.id, "Envie seu CPF/CNPJ:")
    bot.register_next_step_handler(setLogin , verificaCPF, 4)

@bot.message_handler(commands=["opcao5"])
def opcao5(mensagem):
    bot.send_contact(mensagem.chat.id, +551112345678, "Eletro", "Marques")


@bot.message_handler(commands=["opcao6"])
def opcao6(mensagem):
    setLogin = bot.send_message(mensagem.chat.id, "Envie seu CPF/CNPJ:")
    bot.register_next_step_handler(setLogin , verificaCPF, 6)
    

@bot.message_handler(commands=["opcao7"])
def opcao7(mensagem):
    texto = """
        Atendimento encerrado!

        Se precisar é só entrar em contato novamente, até 😀
    """
    bot.send_message(mensagem.chat.id, texto)
    #quit()



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá, eu sou o Assistente virtual da Eletrônica Marques. Esse é o nosso canal Oficial no Telegram✔
    
    Estou aqui para te dar suporte com alguns dos nossos principais serviços☺
    """

    texto2 = """
        Primeiro, escolha qual serviço deseja utilizar:
        
        /opcao1-Consultar cadastro
        /opcao2-Consultar status/andamento de um serviço através da OS
        /opcao3-Consultar orçamento detalhado
        /opcao4-Emitir Recibo
        /opcao5-Falar com um atendente
        /opcao6-Feedback
        /opcao7-Encerrar atendimento
    """

    bot.reply_to(mensagem, texto)
    bot.send_message(mensagem.chat.id, texto2)

def main():
    bot.polling()

if __name__ == "__main__":
    main()