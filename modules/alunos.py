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
    
    nome = input("Digite o nome: ")
    while True:
        try:
            idade = int(input("Digite a idade: "))
            break

        except ValueError:
            print("Digite apenas números!")
        
    modalidade = str(input("Digite a modalidade: "))
    telefone = input("Digite seu telefone: ")
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
            
            novo_nome = input("Digite o novo nome: ")

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
            lista_alunos.remove(aluno)
           
            encontrado = True

            print("Cadastro excluído com sucesso!")
            
            break
    if not encontrado:
        print("ID inexistente")

def listar_resumo_nome(lista_alunos):
    for aluno in lista_alunos:
        print(aluno["id"], "-",aluno["nome"])