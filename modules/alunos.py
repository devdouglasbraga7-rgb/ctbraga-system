alunos = []

def cadastrar_alunos():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cpf = int(input("Digite o cpf: "))
    cadastro = {"nome": nome,
                "idade": idade,
                "cpf": cpf,
                }
    alunos.append(cadastro)
    alunos.append(cadastro)
def listar_alunos():
    pass
def alterar_alunos():
    pass
def remover_aluno():
    pass