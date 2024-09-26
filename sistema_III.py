import os
import time

# Listas dos nomes e preços dos pratos
nomes_pratos = ["Miojo", "Coxinha", "Hambúrguer", "Churros", "X Tudo", "Feijoada", "Acarajé"]
precos_pratos = [5.00, 10.00, 15.00, 20.00, 25.00, 30.00, 35.00]

# Função para limpar o terminal
def limpa_terminal():
    os.system("cls || clear")

#Função para montar o cardápio.
def exibir_cardapio(nomes_pratos, precos_pratos):
    print("\nCardápio:")
    
    for i, nome in enumerate(nomes_pratos, 1):
        print(f"{i}° Prato – {nome} – R$ {precos_pratos[i-1]:.2f}")
    time.sleep(1)

# Função para solicitar o prato
def solicitar_prato(nomes_pratos, precos_pratos):
    pratos_selecionados = []
    precos_selecionados = []

    while True:
        limpa_terminal()
        exibir_cardapio(nomes_pratos, precos_pratos)
        
        numero = int(input("Digite a numeração do prato desejado: "))
        limpa_terminal()

        match numero:
            case 0: 
                break
            case 1 | 2 | 3 | 4 | 5 | 6 | 7:
                pratos_selecionados.append(nomes_pratos[numero - 1])
                precos_selecionados.append(precos_pratos[numero - 1])
                print(f"Prato {nomes_pratos[numero - 1]} adicionado!")
                time.sleep(1)
            case _:  
                print("Número inválido! Tente novamente.")
                time.sleep(1)
        limpa_terminal()
       
        while True:
            limpa_terminal()
            continuar = input("Deseja adicionar outro prato? Se sim, digite 's', se não, digite '0': ").strip().lower()
            limpa_terminal()
            if continuar == '0':
                return pratos_selecionados, precos_selecionados
            elif continuar == 's':
                break
            else:
                print("Opção inválida! Tente novamente.")
                time.sleep(1)
                
limpa_terminal()
# Função para solicitar a forma de pagamento
def solicitar_pagamento():
    print("\nFormas de pagamento:")
    print("1 - À vista (10% de desconto)")
    print("2 - Cartão de crédito (10% de acréscimo)")
    time.sleep(0.5)

    while True:
        forma_pagamento = int(input("\nEscolha a forma de pagamento: "))
        limpa_terminal()
        match forma_pagamento:
            case 1:
                print("Forma de pagamento selecionada: À vista")
                time.sleep(1)
                limpa_terminal()
                return forma_pagamento
            case 2:
                print("Forma de pagamento selecionada: Cartão de crédito")
                time.sleep(1)
                limpa_terminal()
                return forma_pagamento
            case _:
                print("Opção inválida! Escolha 1 ou 2.")
                time.sleep(0.5)
                limpa_terminal()

# Função para somar os preços dos pratos
def somar_precos(precos_selecionados):
    soma_total = 0
    for preco in precos_selecionados:
        soma_total += preco
    return soma_total

# Função para calcular o desconto ou acréscimo
def calcular_desconto_ou_acrescimo(soma_total, forma_pagamento):
    match forma_pagamento:
        case 1:
            desconto_ou_acrescimo = soma_total * 0.10 
            total = soma_total - desconto_ou_acrescimo
        case 2:
            desconto_ou_acrescimo = soma_total * 0.10
            total = soma_total + desconto_ou_acrescimo
    return desconto_ou_acrescimo, total

# Processamento de dados
lista_pratos, lista_precos = solicitar_prato(nomes_pratos, precos_pratos)

forma_pagamento = solicitar_pagamento()  
   
soma_total = somar_precos(lista_precos)
    
desconto_ou_acrescimo, total = calcular_desconto_ou_acrescimo(soma_total, forma_pagamento)

# Saída de Dados
print("Seu pedido foi:\n")
time.sleep(0.5)

for i, prato in enumerate(lista_pratos):
    print(f"{i+1}° Prato: {prato}")
    time.sleep(0.5)

print(f"\nTotal sem desconto ou acréscimo: R$ {soma_total:.2f}")
time.sleep(0.5)

match forma_pagamento:
    case 1:
        print("\nForma de pagamento: À vista")
    case 2:
        print("\nForma de pagamento: Cartão de crédito")
time.sleep(0.5)
         
print(f"\nDesconto ou Acréscimo: R$ {desconto_ou_acrescimo:.2f}")
time.sleep(0.5)

print(f"\nTotal a pagar: R$ {total:.2f}")