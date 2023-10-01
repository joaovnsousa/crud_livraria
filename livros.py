import mysql.connector
    
class Livros:
    def __init__(self, titulo, autor, genero, editora, preco, data_publicacao, edicao, isbn, volume):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__editora = editora
        self.__preco = preco
        self.__data_publicacao = data_publicacao
        self.__edicao = edicao
        self.__isbn = isbn
        self.__volume = volume

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

class GerenciaLivraria:
    def __init__(self, host, user, password, database):
        self.conexao = mysql.connector.connect (
            host = host,
            user = user,
            password = password,
            database = database,
        )
        self.cursor = self.conexao.cursor()
        self.livro = None
        self.menu = None

    #1.5
    def consultar_livros(self):
        consulta = "SELECT * FROM livros"
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        print(resultados)

    def inserir_livros(self, livro):
        insercao = "INSERT INTO livros(titulo, autor, genero, editora, preco, data_publicacao, edicao, isbn, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        parametros = (
            livro.get_titulo(),
            livro.get_autor(),
            livro.get_genero(),
            livro.get_editora(),
            livro.get_preco(),
            livro.get_data_publicacao(),
            livro.get_edicao(),
            livro.get_isbn(),
            livro.get_volume()
        )

        self.cursor.execute(insercao, parametros)
        self.conexao.commit()

        print("Livro inserido com sucesso!")

        
    
gerente = GerenciaLivraria(host="localhost", user="root", password="47Lasanha*", database="crud_livraria")

