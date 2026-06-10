from database.conexao import conectar

conexao = conectar()

if conexao.is_connected():
    print("Conetado com sucesso!")

conexao.close()