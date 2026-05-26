from modules.alunos import cadastrar_alunos

alunos = []
while True:
    print("=" * 50)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Alterar aluno")
    print("4 - Remover aluno")
    print("=" * 50)

    escolha = int(input("Digite uma das opções numéricas: "))

    if escolha == 1:
        cadastrar_alunos()