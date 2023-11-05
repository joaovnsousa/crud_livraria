from classes import *

class CreateCRUD:
    def __init__(self, gerencia_livraria):
        self.gerencia_livraria = gerencia_livraria

    def inserir_livros(self, livro):
        insercao = "INSERT INTO livros(titulo, editora, preco, data_publicacao, edicao, isbn, volume, idioma, data_entrada, isFromMari) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        parametros = (
            livro.get_titulo(),
            livro.get_editora(),
            livro.get_preco(),
            livro.get_data_publicacao(),
            livro.get_edicao(),
            livro.get_isbn(),
            livro.get_volume(),
            livro.get_idioma(),
            livro.get_data_entrada(),
            livro.get_isFromMari()
        )

        self.gerencia_livraria.cursor.execute(insercao, parametros)
        self.gerencia_livraria.conexao.commit()   

    def insere_autor(self, autor):
        consulta = f"INSERT INTO autores(nome) VALUES ('{autor}')"
        self.gerencia_livraria.executa_commit(consulta)

    def insere_livro_genero(self, id_livro, id_genero):
        consulta = f"INSERT INTO livro_generos (f_idlivros, f_idgeneros) VALUES ('{id_livro}', '{id_genero}')"
        self.gerencia_livraria.executa_commit(consulta)


    #Insere o gênero do livro na tabela gênero
    def insere_genero(self, genero):
        consulta = f"INSERT INTO generos(nome) VALUES ('{genero}')"
        self.gerencia_livraria.executa_commit(consulta)

    
    def insere_livro_autores(self, idLivro, idAutor):
        consulta = f"INSERT INTO livro_autores (fk_idlivros, fk_idautores) VALUES ('{idLivro}', '{idAutor}')"
        self.gerencia_livraria.executa_commit(consulta)
