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
import time
time.sleep

def limpa_terminal():
    os.system("cls || clear") 

lista_pratos = []    
while True:
    numero = int(input(f"Digite a numeração do prato desejado:  "))
    limpa_terminal()
    match (numero):
        case 1 | 2 | 3 | 4 | 5 | 6 | 7:
            lista_pratos.append(numero)
            
        case _:
            print("Número inválido! \nTente novamente.")   


