"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Victor Santana de Jesus
2 - Lucas Pereira da Silva
"""


import os

# Limpa o terminal.
os.system("cls || clear")

# opcao_escolhida = input('Escolha uma opção: ')
#print(opcao_escolhida == 1)
#print(type(opcao_escolhida))
#print(type(1))

import os
os.system("cls || clear")

def exibir_nome_do_programa():
    print("""
ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear') 
    print('Finalizando o app')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    # opcao_escolhida = int(opcao_escolhida)

    if opcao_escolhida == 1: 
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2: 
        print('Listar restaurantes')
    elif opcao_escolhida == 3: 
        print('Ativar restaurante')
    else: 
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()