import mysql.connector
from APIkeys import *
    
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
        self.livro = None
        self.menu = None

    #1.1
    def inserir_livros(self, livro):
        insercao = "INSERT INTO livros(titulo, autor, genero, editora, preco, data_publicacao, edicao, isbn, volume, idioma) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        parametros = (
            livro.get_titulo(),
            livro.get_autor(),
            livro.get_genero(),
            livro.get_editora(),
            livro.get_preco(),
            livro.get_data_publicacao(),
            livro.get_edicao(),
            livro.get_isbn(),
            livro.get_volume(),
            livro.get_idioma()
        )

        self.cursor.execute(insercao, parametros)
        self.conexao.commit()

        print("Livro inserido com sucesso!")

    #1.2
    def atualiza_campo(self, id, campo, valor):
        consulta = f'UPDATE livros SET {campo} = {valor} WHERE idLivros = {id}'
        self.cursor.execute(consulta)
        self.conexao.commit()

    #1.3
    def pesquisa_por_titulo(self, titulo):
        consulta = f'SELECT * FROM livros WHERE titulo = "{titulo}"'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
    
    #1.4
    def remove_por_id(self, id):
        consulta = f'DELETE FROM livros WHERE idLivros = {id}'
        self.cursor.execute(consulta)
        self.conexao.commit()

    #1.5
    def consultar_livros(self):
        consulta = "SELECT * FROM livros"
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        print(resultados)

    #1.6
    def pesquisa_por_id(self, id):
        consulta = f'SELECT * FROM livros WHERE idLivros = {id}'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
        
    
