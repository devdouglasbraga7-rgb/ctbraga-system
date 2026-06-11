import database.conexao as conexao
from datetime import datetime

def menu():
    print("=" * 50)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Alterar aluno")
    print("4 - Remover aluno")
    print("5 - Sair")
    print("=" * 50)

def cadastrar_aluno():
    
    conexao_db = conexao.conectar()
    cursor = conexao_db.cursor()

    nome = validar_nome()

    data_nascimento = validar_data_nascimento()

    telefone = validar_telefone()

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

        if campo == 1:
            novo_nome = validar_nome()
            print(novo_nome)

        elif campo == 2:
            nova_data = validar_data_nascimento()
            print(nova_data)
        
        elif campo == 3:
            novo_numero = validar_telefone()
            print(novo_numero)

        else:
            print("Opção inválida!")
            continue            
        
        print("Campo alterado com sucesso!")
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
    for aluno in alunos:
        print(f"{aluno[0]} - {aluno[1]}")

    cursor.close()
    conexao_db.close()

def validar_nome():
     while True:
        nome = input("Digite o nome: ").strip()
        if nome:
            return nome
    
        print("O nome não pode ficar vazio!")

def validar_data_nascimento():
    while True:
            
            data = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()

            partes = data.split("/")

            if len(partes) != 3:
                print("Formato inválido!")
                continue
            
            dia, mes, ano = partes

            if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
                print("Digite apenas números!")
                continue

            return data

def validar_telefone():
    while True:
        telefone = input("Digite seu telefone: ").strip()
        if not telefone:
            print("O telefone não pode ficar vazio!")
            continue
        
        if not telefone.isdigit():
            print("Digite apenas números!")
            continue
        
        return telefone