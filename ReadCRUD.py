from classes import *

class ReadCRUD:
    def __init__(self, gerencia_livraria):
        self.gerencia_livraria = gerencia_livraria

    def consulta_autores_de_um_livro(self, idLivro):
        consulta = f'SELECT autores.nome FROM autores JOIN livro_autores ON autores.idautores = livro_autores.fk_idautores WHERE livro_autores.fk_idlivros = {idLivro}'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def consulta_livros_de_um_autor(self, idAutor):
        consulta = f'SELECT * FROM livros JOIN livro_autores ON livros.idlivros = livro_autores.fk_idlivros WHERE livro_autores.fk_idautores = {idAutor}'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def consulta_generos_de_um_livro(self, idLivro):
        consulta = f'SELECT generos.nome FROM generos JOIN livro_generos ON generos.idgeneros = livro_generos.f_idgeneros WHERE livro_generos.f_idlivros = {idLivro}'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_por_titulo(self, titulo):
        consulta = f'SELECT * FROM livros WHERE titulo = "{titulo}"'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_todos_os_livros(self):
        consulta = f'SELECT * FROM livros'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado

    def pesquisa_por_autor(self, idAutores):
        consulta = f'SELECT DISTINCT livros.idlivros, livros.titulo, livros.editora, livros.preco, livros.data_publicacao, livros.edicao, livros.isbn, livros.volume, livros.idioma FROM livros JOIN livro_autores ON livros.idlivros = livro_autores.fk_idlivros WHERE livro_autores.fk_idautores = "{idAutores}"'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_todos_os_autores(self):
        consulta = f'SELECT * FROM autores'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado

    def pesquisa_id_autor(self, autor):
        consulta = f'SELECT idautores FROM autores WHERE nome = "{autor}"'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_por_genero(self, idGenero):
        consulta = f'SELECT DISTINCT livros.idlivros, livros.titulo, livros.editora, livros.preco, livros.data_publicacao, livros.edicao, livros.isbn, livros.volume, livros.idioma FROM livros JOIN livro_generos ON livros.idlivros = livro_generos.f_idlivros WHERE livro_generos.f_idgeneros = "{idGenero}"'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_todos_os_generos(self):
        consulta = f'SELECT * FROM generos'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado   

    def pesquisa_id_genero(self, genero):
        consulta = f'SELECT idgeneros FROM generos WHERE nome = "{genero}"'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_por_editora(self, editora):
        consulta = f'SELECT * FROM livros WHERE editora = "{editora}"'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_por_id(self, id):
        consulta = f'SELECT * FROM livros WHERE idLivros = {id}'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_geral(self):
        consulta = f'''SELECT livros.idlivros AS IDLivro, livros.titulo AS Livro, 
    GROUP_CONCAT(DISTINCT autores.nome SEPARATOR ', ') AS Autores,
    GROUP_CONCAT(DISTINCT generos.nome SEPARATOR ', ') AS Generos,
    livros.editora AS Editora,
    livros.preco AS Preco,
    livros.data_publicacao AS DataDePublicação,
    livros.edicao AS Edição,
    livros.isbn AS ISBN,
    livros.volume AS Volume,
    livros.idioma AS Idioma
FROM
    livros
LEFT JOIN livro_autores ON livros.idlivros = livro_autores.fk_idlivros
LEFT JOIN autores ON livro_autores.fk_idautores = autores.idautores
LEFT JOIN livro_generos ON livros.idlivros = livro_generos.f_idlivros
LEFT JOIN generos ON livro_generos.f_idgeneros = generos.idgeneros
GROUP BY
    livros.idlivros;'''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado