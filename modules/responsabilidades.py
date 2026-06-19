"""REGRAS

- Um aluno pode possuir vários responsáveis legais.

- Um aluno pode possuir apenas um responsável financeiro.

- Uma pessoa pode ser responsável por vários alunos.

- Uma mesma pessoa pode ser responsável legal e financeiro do mesmo aluno.

- Não permitir responsabilidades duplicadas."""

import modules.alunos as alunos
import database.conexao as conexao


def menu_resp():
    print("=" * 50)
    print("1 - Vincular responsabilidade")
    print("2 - Listar responsabilidades")
    print("3 - Alterar responsabilidade")
    print("4 - Remover responsabilidade")
    print("5 - Sair")
    print("=" * 50)

def vincular_resp():
    alunos.listar_resumo_nome()

    aluno_id = validar_id("Digite o id do aluno:")

    listar_pessoas()

    responsavel_id = validar_id("Digite o id do responsável: ")

    while True:
            tipo_resp = str(input("Qual o tipo de responsabilidade: FINANCEIRO/LEGAL: ")).strip().upper()

            if tipo_resp not in ("FINANCEIRO", "LEGAL"):
                print("Digite apenas FINANCEIRO ou LEGAL!")
                continue
            break
    
    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    cursor.execute("""
                SELECT COUNT(*)
                FROM responsabilidades
                WHERE alunoID = %s
                AND responsavelID = %s
                AND tipo_responsabilidade = %s
    """, (aluno_id, responsavel_id, tipo_resp))

    resultado = cursor.fetchone()[0]

    if resultado > 0:
        print("Essa responsabilidade já está cadastrada!")

        cursor.close()
        conexao_db.close()
        return
    
    elif tipo_resp == "LEGAL":
        cursor.execute("""
                    INSERT INTO responsabilidades(alunoID, responsavelID, tipo_responsabilidade)
                    VALUES (%s, %s, %s)
                    """, (aluno_id, responsavel_id, tipo_resp))
        
        conexao_db.commit()

        cursor.close()
        conexao_db.close()
        return

    elif tipo_resp == "FINANCEIRO":
        cursor.execute("""
                    SELECT COUNT(*)
                    FROM responsabilidades
                    WHERE alunoID = %s
                    AND tipo_responsabilidade = 'FINANCEIRO'
                """, (aluno_id,))
        resultado_finan = cursor.fetchone()[0]

        if resultado_finan > 0:
            print("Já existe um responsável financeiro!")
            
            cursor.close()
            conexao_db.close()
            print("Responsabilidade vinculada com sucesso!")
            return

        elif resultado_finan == 0:
            cursor.execute("""
                        INSERT INTO responsabilidades(alunoID, responsavelID, tipo_responsabilidade)
                        VALUES (%s, %s, %s)
                        """, (aluno_id, responsavel_id, tipo_resp))
            
            conexao_db.commit()

            cursor.close()
            conexao_db.close()

            print("Responsabilidade vinculada com sucesso!")
            return

def listar_resp():
    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    cursor.execute("""
                SELECT
                    pa.nome,
                    pr.nome,
                    r.tipo_responsabilidade
                    FROM responsabilidades r
                    JOIN alunos a
                    ON r.alunoID = a.IDaluno
                    JOIN pessoas pa
                    ON a.pessoaID = pa.IDpessoa
                    JOIN pessoas pr
                    ON r.responsavelID = pr.IDpessoa
                    """)
    responsabilidades = cursor.fetchall()
    if not responsabilidades:
        print("Não há nenhum vinculo de responsabilidade")

        cursor.close()
        conexao_db.close()

        return
    
    for responsabilidade in responsabilidades:
        print("-" * 30)
        print(f"Aluno: {responsabilidade[0]}")
        print(f"Responsável: {responsabilidade[1]}")
        print(f"Tipo: {responsabilidade[2]}")

    cursor.close()
    conexao_db.close()

def alterar_resp():
    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    cursor.execute("""
                SELECT
                    r.IDresponsabilidade,
                    r.alunoID,
                    r.responsavelID,
                    pa.nome,
                    pr.nome,
                    r.tipo_responsabilidade
                    FROM responsabilidades r
                    JOIN alunos a
                    ON r.alunoID = a.IDaluno
                    JOIN pessoas pa
                    ON a.pessoaID = pa.IDpessoa
                    JOIN pessoas pr
                    ON r.responsavelID = pr.IDpessoa
                    """)
    responsabilidades = cursor.fetchall()
    if not responsabilidades:
        print("Não há nenhum vinculo de responsabilidade")

        cursor.close()
        conexao_db.close()

        return
    
    for responsabilidade in responsabilidades:
        print("-" * 30)
        print(f"ID: {responsabilidade[0]}")
        print(f"Aluno: {responsabilidade[3]}")
        print(f"Responsável: {responsabilidade[4]}")
        print(f"Tipo: {responsabilidade[5]}")
        
    id_resp = validar_id("Digite o id da responsabilidade: ")

    responsabilidade_escolhida = None

    for responsabilidade in responsabilidades:
        if responsabilidade[0] == id_resp:
            responsabilidade_escolhida = responsabilidade
            break

    if responsabilidade_escolhida is None:
        print("Responsabilidade não encontrada!")
        
        cursor.close()
        conexao_db.close()
        return
    
    print("-" * 30)
    print(f"ID responsabilidade: {responsabilidade_escolhida[0]}")
    print(f"ID aluno: {responsabilidade_escolhida[1]}")
    print(f"ID responsável: {responsabilidade_escolhida[2]}")
    print(f"Aluno: {responsabilidade_escolhida[3]}")
    print(f"Responsável: {responsabilidade_escolhida[4]}")
    print(f"Tipo: {responsabilidade_escolhida[5]}")
    print("-" * 30)
    print(" ")
    print("=" * 30)
    print("1 - Alterar responsável")
    print("2 - Alterar tipo")
    print("3 - Alterar ambos")
    print("=" * 30)

    opcao = validar_id("Escolha a opção: ")

    if opcao == 1:
        listar_pessoas()

        novo_responsavel_id = validar_id("Digite o ID do novo responsável: ")

        cursor.execute("""
                SELECT COUNT(*)
                FROM pessoas
                WHERE IDpessoa = %s
                    """, (novo_responsavel_id,))
        
        resultado_pessoa = cursor.fetchone()[0]
        
        if resultado_pessoa == 0:
            print("Responsável não encontrado!")
            
            cursor.close()
            conexao_db.close()
            return
        
        cursor.execute("""
                    SELECT COUNT(*)
                    FROM responsabilidades
                    WHERE alunoID = %s
                    AND responsavelID = %s
                    AND tipo_responsabilidade = %s
                    """, (responsabilidade_escolhida[1], novo_responsavel_id, responsabilidade_escolhida[5]))
        
        resultado_duplicidade = cursor.fetchone()[0]

        if resultado_duplicidade > 0:
            print("Esse vínculo já existe!")

            cursor.close()
            conexao_db.close()
            return

        cursor.execute("""
                UPDATE responsabilidades
                SET responsavelID = %s
                WHERE IDresponsabilidade = %s
                    """, (novo_responsavel_id, id_resp))
        
        conexao_db.commit()

        print("Responsável alterado com sucesso")

        cursor.close()
        conexao_db.close()
        
        return
    
    elif opcao == 2:
        pass
    
    elif opcao == 3:
        pass
    
    else:
        print("Opção inválida")

        cursor.close()
        conexao_db.close()

        return
    
def remover_resp():
    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    cursor.execute("""
                SELECT
                    r.IDresponsabilidade,
                    pa.nome,
                    pr.nome,
                    r.tipo_responsabilidade
                    FROM responsabilidades r
                    JOIN alunos a
                    ON r.alunoID = a.IDaluno
                    JOIN pessoas pa
                    ON a.pessoaID = pa.IDpessoa
                    JOIN pessoas pr
                    ON r.responsavelID = pr.IDpessoa
                    """)
    responsabilidades = cursor.fetchall()
    if not responsabilidades:
        print("Não há nenhum vinculo de responsabilidade")

        cursor.close()
        conexao_db.close()

        return
    
    for responsabilidade in responsabilidades:
        print("-" * 30)
        print(f"ID: {responsabilidade[0]}")
        print(f"Aluno: {responsabilidade[1]}")
        print(f"Responsável: {responsabilidade[2]}")
        print(f"Tipo: {responsabilidade[3]}")
        
    id_resp = validar_id("Digite o id da responsabilidade: ")

    responsabilidade_escolhida = None

    for responsabilidade in responsabilidades:
        if responsabilidade[0] == id_resp:
            responsabilidade_escolhida = responsabilidade
            break

    if responsabilidade_escolhida is None:
        print("Responsabilidade não encontrada!")
        
        cursor.close()
        conexao_db.close()
        return
    
    print("-" * 30)
    print(f"Aluno: {responsabilidade_escolhida[1]}")
    print(f"Responsável: {responsabilidade_escolhida[2]}")
    print(f"Tipo: {responsabilidade_escolhida[3]}")

    while True:
        confirmacao = str(input("Tem certeza que deseja excluir? S/N: ")).strip().upper()

        if confirmacao not in ("S", "N"):
            print("Digite apenas S ou N por favor!")
            continue
        break
    
    if confirmacao == "S":
        cursor.execute("""
                    DELETE FROM responsabilidades
                    WHERE IDresponsabilidade = %s
                    """, (id_resp,))
    
        conexao_db.commit()

        print("Responsabilidade excluída com sucesso!")

        cursor.close()
        conexao_db.close()
        return
    
    if confirmacao == "N":
        print("Operação cancelada!")

        cursor.close()
        conexao_db.close()
        return

def listar_pessoas():
    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    cursor.execute("""
            SELECT
                p.IDpessoa,
                p.nome,
                t.numero
                   FROM pessoas p
                   JOIN telefones t
                   ON t.pessoaID = p.IDpessoa
""")
    
    pessoas = cursor.fetchall()
    if not pessoas:
        print("Nenhuma pessoa encontrada!")

        cursor.close()
        conexao_db.close()

        return

    for pessoa in pessoas:
        print("-" * 30)
        print(f"ID: {pessoa[0]}")
        print(f"Nome: {pessoa[1]}")
        print(f"Número: {pessoa[2]}")

    cursor.close()
    conexao_db.close()

def validar_id(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas números!")