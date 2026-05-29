cadastro_aluno = []
def cadastrar_alunos(cadastro_aluno):
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
    for i, nome in enumerate(cadastro_aluno, start=1):
        print(i, "-", nome["nome"])
def alterar_alunos(cadastro_aluno):
    for i, nome in enumerate(cadastro_aluno, start=1):
        print(i, "-" , nome)
        opcao = int(input("Escolha a opção: "))
        novo_nome = input("Digite o novo nome: ")
            
        cadastro[opcao - 1]["nome"] = novo_nome
def remover_aluno():
    pass