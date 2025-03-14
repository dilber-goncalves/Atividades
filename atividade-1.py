#codigo sem função

fluxo_caixa = []

print ("==============================")
print ("= Sistema de Fluxo de Caixa =")
print ("==============================")
print ("1--adicionar receita")
print ("2--adicionar despesa")
print ("\n# digite outro numero para encerrar #\n")

def adicionar_transacao():
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor
    })

while True:
    opcao = int(input("Digite uma opção: "))
    
    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break

#nota fiscal
total = 0 
for fc in fluxo_caixa:
    print(fc["nome"], ":", fc["valor"])
    total += fc["valor"]

print("\nSaldo autal: ", total)