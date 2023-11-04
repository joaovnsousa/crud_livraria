from classes import *

class DeleteCRUD:
    def __init__(self, gerencia_livraria):
        self.gerencia_livraria = gerencia_livraria
        
    def remove_autor(self, idautor):
        self.remove_autor_de_livroAutores(idautor)
        consulta = f'DELETE FROM autores WHERE idautores = {idautor}'
        self.gerencia_livraria.cursor.execute(consulta)
        self.gerencia_livraria.conexao.commit()
    
    def remove_genero(self, idgenero):
        self.remove_genero_de_livroGenero(idgenero)
        consulta = f'DELETE FROM generos WHERE idgeneros = {idgenero}'
        self.gerencia_livraria.cursor.execute(consulta)
        self.gerencia_livraria.conexao.commit()

    def remove_livro_(self, id):
        self.remove_livro_de_livroAutores(id)
        self.remove_livro_de_livroGenero(id)
        consulta = f'DELETE FROM livros WHERE idLivros = {id}'
        self.gerencia_livraria.cursor.execute(consulta)
        self.gerencia_livraria.conexao.commit()

    def remove_livro_de_livroAutores(self, id):
        consulta = f'DELETE FROM livro_autores WHERE fk_idlivros = {id}'
        self.gerencia_livraria.cursor.execute(consulta)
        self.gerencia_livraria.conexao.commit()

    def remove_autor_de_livroAutores(self, id):
        consulta = f'DELETE FROM livro_autores WHERE fk_idautores = {id}'
        self.gerencia_livraria.cursor.execute(consulta)
        self.gerencia_livraria.conexao.commit()
    
    def remove_livro_de_livroGenero(self, id):
        consulta = f'DELETE FROM livro_generos WHERE f_idlivros = {id}'
        self.gerencia_livraria.cursor.execute(consulta)
        self.gerencia_livraria.conexao.commit()
    
    def remove_genero_de_livroGenero(self, id):
        consulta = f'DELETE FROM livro_generos WHERE f_idgeneros = {id}'
        self.gerencia_livraria.cursor.execute(consulta)
        self.gerencia_livraria.conexao.commit()