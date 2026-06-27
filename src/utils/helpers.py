"""
Aqui ficarão as funções que são repetidas várias vezes
para terem facil acesso

"""
import datetime


def validar_nome():
     while True:
        nome = input("Digite o nome: ").strip()
        if nome:
            return nome
    
        print("O nome não pode ficar vazio!")

def validar_data_nascimento():
    while True: 
        data = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()

        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Data inválida! Digite no formato: dd/mm/aaaa")

def validar_telefone():
    while True:
        telefone = input("Digite seu telefone: ").strip()
        if not telefone:
            print("O telefone não pode ficar vazio!")
            continue
        
        if not telefone.isdigit():
            print("Digite apenas números!")
            continue
        
        return telefone
    
def validar_id(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas números!")

def validar_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
        except ValueError:
            print("Digite apenas números!")
            continue

        if valor <= 0:
            print("O valor precisa ser maior que zero!")
            continue

        return valor