import os
mensagens = []

nome = input("Digite seu nome: ")

while True:

    #limpar terminal
    os.system("cls")

    if len(mensagens) > 0:
        for msg in mensagens:
            print(msg['nome'], "-", msg['texto'])
    
    print("_________________________")

    #obtendo texto
    texto = input("Digite sua mensagem: ")
    if texto == "sair":
        break

    #adicionar mensagens na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })