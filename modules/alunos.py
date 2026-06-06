proximo_id = 1

def menu():
    print("=" * 50)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Alterar aluno")
    print("4 - Remover aluno")
    print("5 - Sair")
    print("=" * 50)

def cadastrar_aluno(lista_alunos):
    
    global proximo_id
    
    nome = validar_nome()

    data_nascimento = validar_data_nascimento()
    
    modalidade = validar_modalidade()
        
    telefone = validar_telefone()

    aluno = {
            "id": proximo_id,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "modalidade": modalidade,
            "telefone": telefone
                }
    lista_alunos.append(aluno)
    proximo_id += 1
    
def listar_alunos(lista_alunos):
    
    if not lista_alunos:
        print("Nenhum aluno encontrado")
        return
    
    for aluno in lista_alunos:
        print("-" * 50)
        print(f"ID: {aluno['id']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Data de nascimento: {aluno['data_nascimento']}")
        print(f"Modalidade: {aluno['modalidade']}")
        print(f"Telefone: {aluno['telefone']}")
def alterar_aluno(lista_alunos):
    
    if not lista_alunos:
        print("Nenhum aluno encontrado")
        return
    
    listar_resumo_nome(lista_alunos)

    while True:    
        
        try:
            opcao = int(input("Escolha o id do aluno: "))
            break
        except ValueError:
            print("Digite apenas números!")

    encontrado = False
    
    for aluno in lista_alunos:

        if aluno["id"] == opcao:
            encontrado = True

            print("=" * 50)
            print("1 - alterar nome")
            print("2 - alterar data de nascimento")
            print("3 - alterar modalidade")
            print("4 - alterar telefone")
            print("=" * 50)
            
            while True:
                try:
                    campo = int(input("Escolha a opção que deseja alterar: "))
                    break
                except ValueError:
                    print("Digite apenas números!")

            if campo == 1:
                aluno["nome"] = validar_nome()

            elif campo == 2:
                aluno["data_nascimento"] = validar_data_nascimento()

            elif campo == 3:
                aluno["modalidade"] = validar_modalidade()
            
            elif campo == 4:
                aluno["telefone"] = validar_telefone()
            
            else:
                print("Opção inválida!")
                continue            
            
            print("Campo alterado com sucesso!")
            break
    if not encontrado:
        print("ID inexistente")

def remover_aluno(lista_alunos):
    
    if not lista_alunos:
        print("Nenhum aluno encontrado")
        return
    
    listar_resumo_nome(lista_alunos)

    while True:        
        try:
            opcao = int(input("Digite o id do cadastro a ser excluído: "))
            break
        except ValueError:
            print("Digite apenas números!")
    
    encontrado = False

    for aluno in lista_alunos:
        if aluno["id"] == opcao:
            encontrado = True
            print("-" * 50)
            print(f"ID: {aluno['id']}")
            print(f"Aluno: {aluno['nome']}")
            print(f"Data de nascimento: {aluno['data_nascimento']}")
            print(f"Modalidade: {aluno['modalidade']}")
            print("-" * 50)
            
            while True:
                confirmacao = input("\nTem certeza? S/N: ").strip().upper()
                if confirmacao not in ["S", "N"]:
                    print("Digite apenas S ou N.")
                    continue
                
                elif confirmacao == "S":
                   lista_alunos.remove(aluno)
                   print("Cadastro excluído com sucesso!")

                elif confirmacao == "N":
                    print("Operação cancelada!")
                    break
            break

    if not encontrado:
        print("ID inexistente")

def listar_resumo_nome(lista_alunos):
    for aluno in lista_alunos:
        print(aluno["id"], "-",aluno["nome"])

def validar_nome():
     while True:
        nome = input("Digite o nome: ").strip()
        if nome:
            return nome
    
        print("O nome não pode ficar vazio!")

def validar_data_nascimento():
    while True:
            
            data = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()

            partes = data.split("/")

            if len(partes) != 3:
                print("Formato inválido!")
                continue
            
            dia, mes, ano = partes

            if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
                print("Digite apenas números!")
                continue

            return data
    
def validar_modalidade():
    while True:    
        modalidade = str(input("Digite a modalidade: ")).strip()
        if modalidade:
            return modalidade
        print("A modalidade não pode ficar vazia!")

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