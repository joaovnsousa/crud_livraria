from classes import *

class UpdateCRUD:
    def __init__(self, gerencia_livraria):
        self.gerencia_livraria = gerencia_livraria

    def atualiza_titulo_livro(self, idlivro, valor):
        consulta = f'UPDATE livros SET titulo = "{valor}" WHERE idlivros = {idlivro}'
        self.gerencia_livraria.executa_commit(consulta)


    def atualiza_isbn_livro(self, idlivro, valor):
        consulta = f'UPDATE livros SET isbn = "{valor}" WHERE idlivros = {idlivro}'
        self.gerencia_livraria.executa_commit(consulta)


    def atualiza_data_publicacao_livro(self, idlivro, valor):
        consulta = f'UPDATE livros SET data_publicacao = "{valor}" WHERE idlivros = {idlivro}'
        self.gerencia_livraria.executa_commit(consulta)


    def atualiza_volume_livro(self, idlivro, valor):
        consulta = f'UPDATE livros SET volume = {valor} WHERE idlivros = {idlivro}'
        self.gerencia_livraria.executa_commit(consulta)


    def atualiza_idioma_livro(self, idlivro, valor):
        consulta = f'UPDATE livros SET idioma = "{valor}" WHERE idlivros = {idlivro}'
        self.gerencia_livraria.executa_commit(consulta)


    def atualiza_editora_livro(self, idlivro, valor):
        consulta = f'UPDATE livros SET editora = "{valor}" WHERE idlivros = {idlivro}'
        self.gerencia_livraria.executa_commit(consulta)


    def atualiza_preco_livro(self, idlivro, valor):
        consulta = f'UPDATE livros SET preco = {valor} WHERE idlivros = {idlivro}'
        self.gerencia_livraria.executa_commit(consulta)


    def atualiza_edicao_livro(self, idlivro, valor):
        consulta = f'UPDATE livros SET edicao = {valor} WHERE idlivros = {idlivro}'
        self.gerencia_livraria.executa_commit(consulta)


    def atualiza_nome_autor(self, nome, nome_antigo):
        consulta = f'UPDATE autores SET nome = "{nome}" WHERE nome = "{nome_antigo}"'
        self.gerencia_livraria.executa_commit(consulta)


    def atualiza_nome_genero(self, nome, nome_antigo):
        consulta = f'UPDATE generos SET nome = "{nome}" WHERE nome = "{nome_antigo}"'
        self.gerencia_livraria.executa_commit(consulta)
