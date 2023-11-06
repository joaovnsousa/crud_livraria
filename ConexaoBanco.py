import mysql.connector
from APIKeys import *

class ConexaoBanco:
    def __init__(self):
        self.conexao = mysql.connector.connect (
            host = credencial_nome,
            user = credencial_user,
            password = credencial_passwd,
            database = credencial_database,
            pool_recycle = 3600,
            pool_size = 5
        )
        self.cursor = self.conexao.cursor()
