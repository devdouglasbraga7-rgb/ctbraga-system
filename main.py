import modules.alunos as alunos
import modules.responsabilidades as resp


print("=" * 50)
print("                  CT BRAGA SYSTEM")
print("=" * 50)
print("1 - Alunos")
print("2 - Responsabilidades")
print("3 - Sair")
print("=" * 50)
while True:
    try:
        escolha = int(input("Digite uma das opções numéricas: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if escolha == 1:
        while True:
            alunos.menu_alunos()
            try:
                escolha = int(input("Digite uma das opções numéricas: "))
            except ValueError:
                print("Digite apenas números!")
                continue

            if escolha == 1:
                alunos.cadastrar_aluno()
            elif escolha == 2:
                alunos.listar_alunos()
                input("Aperte enter para continuar...")
            elif escolha == 3:
                alunos.alterar_aluno()
            elif escolha == 4:
                alunos.remover_aluno()
            elif escolha == 5:
                print("Finalizando o sistema....")

                break

            else:
                print("Opção inválida!")
        break
    if escolha == 2:
        while True:
            resp.menu_resp()
            try:
                escolha = int(input("Digite uma das opções numéricas: "))
            except ValueError:
                print("Digite apenas números!")
                continue

            if escolha == 1:
                resp.vincular_resp()
            elif escolha == 2:
                resp.listar_resp()
                input("Aperte enter pra continuar...")
            elif escolha == 3:
                resp.alterar_resp()
            elif escolha == 4:
                resp.remover_resp()
            elif escolha == 5:
                print("Finalizando sistema...")

                break

            else:
                print("Opção inválida!")
        break

    if escolha == 3:
        print("Finalizando o sistema...")

        break