import mysql.connector


def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='', 
        database='ctbraga',
        port=3308
    )
    return conexao
