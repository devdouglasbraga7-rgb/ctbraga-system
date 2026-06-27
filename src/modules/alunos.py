import src.database.conexao as conexao
from datetime import datetime
from src.utils.interface import menu
import src.utils.helpers as help

#Mostra o menu de opções
def menu_alunos():
    menu("MENU ALUNOS", ["1 - Cadastrar aluno", "2 - Listar alunos", "3 - Alterar aluno", "4 - Remover aluno", "5 - Sair"])

def cadastrar_aluno():
    
    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    nome = help.validar_nome()

    data_nascimento = help.validar_data_nascimento()

    telefone = help.validar_telefone()

    data_mysql = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    cursor.execute("""
    INSERT INTO pessoas(nome, data_nascimento)
    VALUES (%s, %s)
    """, (nome, data_mysql)
        )
    
    id_pessoa = cursor.lastrowid

    cursor.execute("""
        INSERT INTO alunos(status_a, pessoaID)
        VALUES (%s, %s)
    """, ("ATIVO", id_pessoa)
        )

    cursor.execute("""
        INSERT INTO telefones(numero, pessoaID)
        VALUES (%s, %s)
    """, (telefone, id_pessoa))

    conexao_db.commit()

    print("Aluno cadastrado com sucesso!")
    cursor.close()
    conexao_db.close()
    
def listar_alunos():
    
    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    cursor.execute("""SELECT
                   a.IDaluno,
                   p.nome,
                   p.data_nascimento,
                   a.status_a,
                   t.numero
                   FROM alunos a
                   JOIN pessoas p
                   ON a.pessoaID = p.IDpessoa
                   JOIN telefones t
                   ON t.pessoaID = p.IDpessoa
                   """)
    alunos = cursor.fetchall()
    if not alunos:
        print("Nenhum aluno encontrado")

        cursor.close()
        conexao_db.close()
        
        return
    
    for aluno in alunos:
        print("-" * 50)
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Data de nascimento: {aluno[2]}")
        print(f"Status: {aluno[3]}")
        print(f"Número: {aluno[4]}")
    
    cursor.close()
    conexao_db.close()

def alterar_aluno():

    listar_resumo_nome()

    while True:    
        
        try:
            opcao = int(input("Escolha o id do aluno: "))
            break
        except ValueError:
            print("Digite apenas números!")


    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    cursor.execute("""
            SELECT
                p.IDpessoa,
                p.nome,
                p.data_nascimento,
                t.numero
                From alunos a
                JOIN pessoas p
                ON a.pessoaID = p.IDpessoa
                JOIN telefones t
                ON t.pessoaID = p.IDpessoa
                WHERE IDaluno = %s
                """, (opcao,))
    
    aluno = cursor.fetchone()
    
    if aluno is None:
        print("ID inexistente")
        
        cursor.close()
        conexao_db.close()
        
        return    

    print("=" * 50)
    print("1 - alterar nome")
    print("2 - alterar data de nascimento")
    print("3 - alterar telefone")
    print("=" * 50)
            
    while True:
        try:
            campo = int(input("Escolha a opção que deseja alterar: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if campo == 1:
            novo_nome = help.validar_nome()
            cursor.execute("""
                        UPDATE pessoas
                        SET nome = %s
                        WHERE IDpessoa = %s
                        """, (novo_nome, aluno[0]))
            
            conexao_db.commit()
            
            print("Nome alterado com sucesso!")

            cursor.close()
            conexao_db.close()

            return

        elif campo == 2:
            nova_data = help.validar_data_nascimento()
            
            nova_data_sql = datetime.strptime(nova_data, "%d/%m/%Y").date()
            
            cursor.execute("""
                        UPDATE pessoas
                        SET data_nascimento = %s
                        WHERE IDpessoa = %s
                    """, (nova_data_sql, aluno[0]))
            
            conexao_db.commit()

            print("Data alterada com sucesso!")

            cursor.close()
            conexao_db.close()        

            return
        
        elif campo == 3:
            novo_numero = help.validar_telefone()
            
            cursor.execute("""
                        UPDATE telefones
                        SET numero = %s
                        WHERE pessoaID = %s            
                        """, (novo_numero, aluno[0]))
            
            conexao_db.commit()

            print("Telefone alterado com sucesso!")

            cursor.close()
            conexao_db.close()

            return

        else:
            print("Opção inválida!")
            continue            
        
        break

def remover_aluno():
    
    listar_resumo_nome()

    while True:        
        try:
            opcao = int(input("Digite o id do cadastro a ser excluído: "))
            break
        except ValueError:
            print("Digite apenas números!")

    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    cursor.execute("""
            SELECT
                a.IDaluno,
                p.nome,
                p.data_nascimento,
                t.numero
                From alunos a
                JOIN pessoas p
                ON a.pessoaID = p.IDpessoa
                JOIN telefones t
                ON t.pessoaID = p.IDpessoa
                WHERE IDaluno = %s
                """, (opcao,))
    
    aluno = cursor.fetchone()
    
    if aluno is None:
        print("ID inexistente")
        
        cursor.close()
        conexao_db.close()
        
        return
    
    print("-" * 50)
    print(f"ID: {aluno[0]}")
    print(f"Aluno: {aluno[1]}")
    print(f"Data de nascimento: {aluno[2]}")
    print(f"Número: {aluno[3]}")
    print("-" * 50)
            
    while True:
        confirmacao = input("\nTem certeza? S/N: ").strip().upper()
        if confirmacao not in ["S", "N"]:
            print("Digite apenas S ou N.")
            continue
        
        elif confirmacao == "S":
            
            cursor.execute("""
                    DELETE FROM alunos
                    WHERE IDaluno = %s
                        """,(opcao,))
            conexao_db.commit()

            print("Cadastro excluído com sucesso!")

            cursor.close()
            conexao_db.close()

            return

        elif confirmacao == "N":
            print("Operação cancelada!")
            
            cursor.close()
            conexao_db.close()

            return

       
def listar_resumo_nome():
    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    cursor.execute("""
            SELECT 
                a.IDaluno,
                p.nome
            FROM alunos a
            JOIN pessoas p
                ON a.pessoaID = p.IDpessoa
    """)
    alunos = cursor.fetchall()
    if not alunos:
        print("Nenhum aluno encontrado")
        
        cursor.close()
        conexao_db.close()
        
        return
    
    for aluno in alunos:
        print(f"{aluno[0]} - {aluno[1]}")

    cursor.close()
    conexao_db.close()