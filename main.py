from src.utils.interface import titulo
from src.utils.interface import menu
import src.modules.alunos as alunos
import src.modules.responsabilidades as resp
import src.modules.planos as planos

titulo("CT BRAGA SYSTEM")
menu("MENU PRINCIPAL", ["1 - Alunos", "2 - Responsabilidades", "3 - Planos", "4 - Sair"])

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
        while True:
            planos.menu_planos()
            try:
                escolha = int(input("Digite uma das opções numéricas: "))
            except ValueError:
                print("Digite apenas números!")
                continue

            if escolha == 1:
                planos.cadastrar_plano()
            elif escolha == 2:
                planos.listar_plano()
                input("Aperte enter pra continuar...")
            elif escolha == 3:
                planos.alterar_plano()
            elif escolha == 4:
                planos.remover_plano()
            elif escolha == 5:
                print("Finalizando sistema...")

                break

            else:
                print("Opção inválida!")
        break


    if escolha == 4:
        print("Finalizando o sistema...")

        break