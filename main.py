import modules.alunos as alunos

lista_alunos = []

while True:
    alunos.menu()
    try:
        escolha = int(input("Digite uma das opções numéricas: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if escolha == 1:
        alunos.cadastrar_aluno(lista_alunos)
    elif escolha == 2:
        alunos.listar_alunos(lista_alunos)
        input("Aperte enter para continuar...")
    elif escolha == 3:
        alunos.alterar_aluno(lista_alunos)
    elif escolha == 4:
        alunos.remover_aluno(lista_alunos)
    elif escolha == 5:
        print("Finalizando o sistema....")

        break

    else:
        print("Opção inválida!")