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
    
    while True:
        nome = input("Digite o nome: ").strip()
        if nome:
            break
        print("O nome não pode ficar vazio!")

    while True:
        try:
            idade = int(input("Digite a idade: "))
            
            if idade <= 0:
                print("A idade deve ser maior que zero!")
               
                continue

            break

        except ValueError:
            print("Digite apenas números!")
    while True:    
        modalidade = str(input("Digite a modalidade: ")).strip()
        if modalidade:
            break
        print("A modalidade não pode ficar vazia!")
        
    while True:
        telefone = input("Digite seu telefone: ").strip()
        if not telefone:
            print("O telefone não pode ficar vazio!")
            continue
        
        if not telefone.isdigit():
            print("Digite apenas números!")
            continue
        
        break

    aluno = {
            "id": proximo_id,
            "nome": nome,
            "idade": idade,
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
        print(f"Idade: {aluno['idade']}")
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
            
            while True:
                novo_nome = input("Digite o novo nome: ").strip()
                if novo_nome:
                    break
                print("O novo nome não pode ficar vazio!")
                continue

            aluno["nome"] = novo_nome
            encontrado = True

            print("Nome alterado com sucesso!")
            
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
            print(f"id: {aluno['id']}")
            print(f"aluno: {aluno['nome']}")
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
        