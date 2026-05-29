cadastro_aluno = []

proximo_id = 1
def cadastrar_alunos(cadastro_aluno):
    
    global proximo_id
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cpf = int(input("Digite o cpf: "))
    cadastro = {
            "id": proximo_id,
            "nome": nome,
                "idade": idade,
                "cpf": cpf,
                }
    cadastro_aluno.append(cadastro)
    proximo_id += 1
    
def listar_alunos(cadastro_aluno):
    for aluno in cadastro_aluno:
        print(aluno["id"], "-", aluno["nome"])
def alterar_alunos(cadastro_aluno):
    for aluno in cadastro_aluno:
        print(aluno["id"], "-", aluno["nome"])
        
    opcao = int(input("Escolha o id do aluno: "))
    
    novo_nome = input("Digite o novo nome: ")

    for aluno in cadastro_aluno:

        if aluno["id"] == opcao:

            aluno["nome"] = novo_nome

            print("Nome alterado com sucesso!")        
def remover_aluno(cadastro_aluno):
    for aluno in cadastro_aluno:
        print(aluno["id"], "-", aluno["nome"])
    opcao = int(input("Digite o id do cadastro a ser excluído: "))
    for aluno in cadastro_aluno:
        if aluno["id"] == opcao:
            cadastro_aluno.remove(aluno)
            print("Cadastro excluído com sucesso!")
            
            break