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

    #Insere um livro com todas as informações tirando o autor e o gênero
    def inserir_livros(self, livro):
        insercao = "INSERT INTO livros(titulo, editora, preco, data_publicacao, edicao, isbn, volume, idioma) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        parametros = (
            livro.get_titulo(),
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

    #Insere o autor na tabela autores
    def insere_autor(self, autor):
        consulta = f"INSERT INTO autores(nome) VALUES ('{autor}')"
        self.cursor.execute(consulta)
        self.conexao.commit()

    def insere_livro_genero(self, id_livro, id_genero):
        consulta = f"INSERT INTO livro_generos (f_idlivros, f_idgeneros) VALUES ('{id_livro}', '{id_genero}')"
        self.cursor.execute(consulta)
        self.conexao.commit()

    #Insere o gênero do livro na tabela gênero
    def insere_genero(self, genero):
        consulta = f"INSERT INTO generos(nome) VALUES ('{genero}')"
        self.cursor.execute(consulta)
        self.conexao.commit()

    def atualiza_titulo_livro(self, idlivro, valor):
        consulta = f'UPDATE livros SET titulo = "{valor}" WHERE idlivros = {idlivro}'
        self.cursor.execute(consulta)
        self.conexao.commit()

    #Relaciona o id do autor com o id do livro na tabela livro_autores e insere ambos os ids.
    def insere_livro_autores(self, idLivro, idAutor):
        consulta = f"INSERT INTO livro_autores (fk_idlivros, fk_idautores) VALUES ('{idLivro}', '{idAutor}')"
        self.cursor.execute(consulta)
        self.conexao.commit()

    #Consulta os autores de um livro e retorna um objeto com o nome dos livros
    def consulta_autores_de_um_livro(self, idLivro):
        consulta = f'SELECT autores.nome FROM autores JOIN livro_autores ON autores.idautores = livro_autores.fk_idautores WHERE livro_autores.fk_idlivros = {idLivro}'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
    
    def consulta_generos_de_um_livro(self, idLivro):
        consulta = f'SELECT generos.nome FROM generos JOIN livro_generos ON generos.idgeneros = livro_generos.f_idgeneros WHERE livro_generos.f_idlivros = {idLivro}'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
    
    
    #Consulta os livros de um determinado autor e retorna um objeto com o nome dos livros
    def consulta_livros_de_um_autor(self, idAutor):
        consulta = f'SELECT * FROM livros JOIN livro_autores ON livros.idlivros = livro_autores.fk_idlivros WHERE livro_autores.fk_idautores = {idAutor}'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
    
    def consulta_geral(self):
        consulta = f'''SELECT livros.idlivros AS "ID do Livro",
    GROUP_CONCAT(DISTINCT autores.nome SEPARATOR ', ') AS "Autores",
    livros.idioma AS "Idioma",
    livros.isbn AS "ISBN",
    livros.edicao AS "Edição",
    livros.volume AS "Volume",
    GROUP_CONCAT(DISTINCT generos.nome SEPARATOR ', ') AS "Gêneros",
    livros.titulo AS "Título do Livro"
FROM
    livros
LEFT JOIN
    livro_autores ON livros.idlivros = livro_autores.fk_idlivros
LEFT JOIN
    autores ON livro_autores.fk_idautores = autores.idautores
LEFT JOIN
    livro_generos ON livros.idlivros = livro_generos.f_idlivros
LEFT JOIN
    generos ON livro_generos.f_idgeneros = generos.idgeneros
GROUP BY 
    livros.idlivros '''
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados

    def encontrar_genero_por_autor(self, autor):
        consulta_autor = f'SELECT idautores FROM autores WHERE nome = "{autor}"'
        self.cursor.execute(consulta_autor)
        resultados_autor = self.cursor.fetchone()

        id_autor = resultados_autor[0]

        consulta_livros = f'SELECT fk_idlivros FROM livro_autores WHERE fk_idautores = {id_autor}'
        self.cursor.execute(consulta_livros)
        resultados_livros = self.cursor.fetchall()

        print(resultados_livros)

        for resultado_livro in resultados_livros:
            id_livro = resultado_livro[0]
            consulta_generos = f'SELECT nome FROM generos INNER JOIN livro_generos ON livro_generos.f_idgeneros = generos.idgeneros WHERE f_idlivros = {id_livro}'
            self.cursor.execute(consulta_generos)
            resultados_generos = self.cursor.fetchall()


        return resultados_generos



    def encontrar_autor_por_genero(self, genero):
            consulta_genero = f'SELECT idgeneros FROM generos WHERE nome = "{genero}"'
            self.cursor.execute(consulta_genero)
            resultado_genero = self.cursor.fetchone()

            id_genero = resultado_genero[0]

            consulta_livros = f'SELECT f_idlivros FROM livro_generos WHERE f_idgeneros = {id_genero}'
            self.cursor.execute(consulta_livros)
            resultados_livros = self.cursor.fetchall()

            print(resultados_livros)

            for resultado_livro in resultados_livros:
                id_livro = resultado_livro[0]
                consulta_autores = f'SELECT nome FROM autores INNER JOIN livro_autores ON livro_autores.fk_idautores = autores.idautores WHERE fk_idlivros = {id_livro}'
                                   #f'SELECT nome FROM generos INNER JOIN livro_generos ON livro_generos.f_idgeneros = generos.idgeneros WHERE f_idlivros = {id_livro}'
                                   #f'SELECT autores.nome FROM autores INNER JOIN livro_autores ON livro_autores.fk_idautores = autores.idautores WHERE livro_autores.fk_idlivros = {id_livro}'
                self.cursor.execute(consulta_autores)
                resultados_autores = self.cursor.fetchall()

            
            return resultados_autores



    #Pesquisa por título de livro
    def pesquisa_por_titulo(self, titulo):
        consulta = f'SELECT * FROM livros WHERE titulo = "{titulo}"'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
    
    def pesquisa_todos_os_livros(self):
        consulta = f'SELECT * FROM livros'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados

    #Pesquisa o nome de todos os autores (pode ser que seja deletado)
    def pesquisa_por_autor(self, idAutores):
        consulta = f'SELECT DISTINCT livros.idlivros, livros.titulo, livros.editora, livros.preco, livros.data_publicacao, livros.edicao, livros.isbn, livros.volume, livros.idioma FROM livros JOIN livro_autores ON livros.idlivros = livro_autores.fk_idlivros WHERE livro_autores.fk_idautores = "{idAutores}"'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
    
    def pesquisa_todos_os_autores(self):
        consulta = f'SELECT * FROM autores'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados

    def pesquisa_id_autor(self, autor):
        consulta = f'SELECT idautores FROM autores WHERE nome = "{autor}"'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados

    def pesquisa_nome_autor_idlivro(self, idlivro):
        consulta = f'SELECT fk_idautores FROM livro_autores WHERE livro_autores.fk_idlivro = {idlivro} JOIN '
    
    #Pesquisa o nome de todos os gêneros (pode ser que seja deletado)
    def pesquisa_por_genero(self, idGenero):
        consulta = f'SELECT DISTINCT livros.idlivros, livros.titulo, livros.editora, livros.preco, livros.data_publicacao, livros.edicao, livros.isbn, livros.volume, livros.idioma FROM livros JOIN livro_generos ON livros.idlivros = livro_generos.f_idlivros WHERE livro_generos.f_idgeneros = "{idGenero}"'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
    
    def pesquisa_todos_os_generos(self):
        consulta = f'SELECT * FROM generos'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados    

    def pesquisa_id_genero(self, genero):
        consulta = f'SELECT idgeneros FROM generos WHERE nome = "{genero}"'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
    
    #def get_autor(self, autor):
        #consulta = f'SELECT autor FROM autores JOIN livro_autores ON livros.idautores = livro_autores.fk_idlivros WHERE livro_autores.fk_idautores = {idAutor}''
    
    #Pesquisa todas as editoras
    def pesquisa_por_editora(self, editora):
        consulta = f'SELECT * FROM livros WHERE editora = "{editora}"'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
    
    #Remove o livro recebendo o id como parâmetro e utilizando o mesmo para remover
    def remove_livro_(self, id):
        self.remove_livro_de_livroAutores(id)
        self.remove_livro_de_livroGenero(id)
        consulta = f'DELETE FROM livros WHERE idLivros = {id}'
        self.cursor.execute(consulta)
        self.conexao.commit()

    def remove_livro_de_livroAutores(self, id):
        consulta = f'DELETE FROM livro_autores WHERE fk_idlivros = {id}'
        self.cursor.execute(consulta)
        self.conexao.commit()
    
    def remove_livro_de_livroGenero(self, id):
        consulta = f'DELETE FROM livro_generos WHERE f_idlivros = {id}'
        self.cursor.execute(consulta)
        self.conexao.commit()
    #Pesquisa um livro específico por id
    def pesquisa_por_id(self, id):
        consulta = f'SELECT * FROM livros WHERE idLivros = {id}'
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchall()
        return resultados
    
