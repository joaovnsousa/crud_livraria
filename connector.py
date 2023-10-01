import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '47Lasanha*',
    database= 'crud_livraria',
)

cursor = conexao.cursor()


cursor.close()
conexao.close()