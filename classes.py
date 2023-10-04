from APIkeys import *
import mysql.connector
from CreateCRUD import *
from DeleteCRUD import *
from ReadCRUD import *
from UpdateCRUD import *

class Livros:
    def __init__(self, titulo, autor, genero, editora, preco, data_publicacao, edicao, isbn, volume, idioma):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__editora = editora
        self.__preco = preco
        self.__data_publicacao = data_publicacao
        self.__edicao = edicao
        self.__isbn = isbn
        self.__volume = volume
        self.__idioma = idioma

    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_genero(self):
        return self.__genero

    def get_editora(self):
        return self.__editora

    def get_preco(self):
        return self.__preco

    def get_data_publicacao(self):
        return self.__data_publicacao

    def get_edicao(self):
        return self.__edicao

    def get_isbn(self):
        return self.__isbn

    def get_volume(self):
        return self.__volume

    def get_idioma(self):
        return self.__idioma
    
class GerenciaLivraria:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GerenciaLivraria, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.conexao = mysql.connector.connect (
            host = credencial_nome,
            user = credencial_user,
            password = credencial_passwd,
            database = credencial_database,
        )
        self.cursor = self.conexao.cursor()

    def executa_commit(self, consulta):
        self.cursor.execute(consulta)
        self.conexao.commit()

    def executa_fetch(self, consulta):
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
