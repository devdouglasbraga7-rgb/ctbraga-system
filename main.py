import modules.alunos as alunos


cadastro_aluno = []

proximo_id = 1

while True:
    print("=" * 50)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Alterar aluno")
    print("4 - Remover aluno")
    print("=" * 50)

    escolha = int(input("Digite uma das opções numéricas: "))

    if escolha == 1:
        alunos.cadastrar_alunos(cadastro_aluno)
    elif escolha == 2:
        alunos.listar_alunos(cadastro_aluno)
    elif escolha == 3:
        alunos.alterar_alunos(cadastro_aluno)
    else:
        alunos.remover_aluno(cadastro_aluno)