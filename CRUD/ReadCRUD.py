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
    
    def pesquisa_todos_os_livros(self):
        consulta = f'SELECT * FROM livros'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        print(resultado)
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

    def pesquisa_titulo_id_livro_por_id(self, id):
        consulta = f'SELECT idlivros, titulo FROM view_estoque WHERE idLivros = {id}'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado  
    
    def consulta_login_senha(self, login, senha):
        consulta = f'SELECT * FROM vendedor WHERE login = "{login}" AND senha = "{senha}"'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_livros_em_estoque(self):
        consulta = f'SELECT * FROM view_estoque WHERE data_saida = NULL'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    #Pesquisa o cliente por nome e sobrenome
    def pesquisa_cliente(self, cpf):
        consulta = f'''SELECT DISTINCT clientes.idclientes, pessoa.nome, pessoa.sobrenome, pessoa.cpf, pessoa.prim_telefone, pessoa.seg_telefone,
                    clientes.isFlamengo, clientes.isFromSousa, clientes.isOnePieceFan
                    FROM clientes INNER JOIN pessoa ON pessoa.idpessoa = clientes.idpessoa WHERE pessoa.cpf = "{cpf}" '''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_cliente_geral(self):
        consulta = f'''SELECT * FROM pessoa INNER JOIN clientes ON pessoa.idpessoa = clientes.id_pessoa '''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_vendedor_por_id(self, idvendedor):
        consulta = f'SELECT nome FROM pessoa JOIN vendedor ON pessoa.idpessoa = vendedor.idpessoa WHERE vendedor.idvendedor = {idvendedor}'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado

    def pesquisa_livro_por_id(self, idlivro):
        consulta = f'SELECT * FROM view_estoque WHERE idlivros = {idlivro}'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def consulta_livros_compra_id(self, idcompra):
        consulta = f''' SELECT livros.idlivros AS IDLivro, 
       livros.titulo AS Livro, 
       GROUP_CONCAT(DISTINCT autores.nome SEPARATOR ', ') AS Autores,
       GROUP_CONCAT(DISTINCT generos.nome SEPARATOR ', ') AS Generos,
       livros.editora AS Editora,
       livros.preco AS Preco,
       livros.data_publicacao AS DataDePublicação,
       livros.edicao AS Edição,
       livros.isbn AS ISBN,
       livros.volume AS Volume,
       livros.idioma AS Idioma,
       livros.data_entrada AS DataEntrada,
       livros.data_saida AS DataSaida,
       livros.isFromMari AS isFromMari
FROM compra_livros
LEFT JOIN livros ON compra_livros.idlivros = livros.idlivros
LEFT JOIN livro_autores ON livros.idlivros = livro_autores.fk_idlivros
LEFT JOIN autores ON livro_autores.fk_idautores = autores.idautores
LEFT JOIN livro_generos ON livros.idlivros = livro_generos.f_idlivros
LEFT JOIN generos ON livro_generos.f_idgeneros = generos.idgeneros
WHERE compra_livros.idcompra = {idcompra}
GROUP BY livros.idlivros;'''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado

    def consulta_vendas_vendedor(self):
        consulta = f'''SELECT compra.idcompra, 
       clientes.idClientes AS idCliente, 
       CONCAT(pessoa_cliente.nome, ' ', pessoa_cliente.sobrenome) AS nomeCliente, 
       vendedor.idVendedor AS idVendedor, 
       CONCAT(pessoa_vendedor.nome, ' ', pessoa_vendedor.sobrenome) AS nomeVendedor,
       compra.data_compra
FROM compra
JOIN clientes ON compra.idclientes = clientes.idClientes
JOIN vendedor ON compra.idvendedor = vendedor.idVendedor
JOIN pessoa AS pessoa_cliente ON clientes.idPessoa = pessoa_cliente.idPessoa
JOIN pessoa AS pessoa_vendedor ON vendedor.idPessoa = pessoa_vendedor.idPessoa; '''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    #Pesquisa os livros que o cliente comprou através de seu id
    def pesquisa_compras_de_cliente(self, idcliente):
        consulta = f'''SELECT livros.*, clientes.* FROM clientes
                LEFT JOIN compra ON compra.idclientes = clientes.idclientes
                LEFT JOIN compra_livros ON compra_livros.idcompra = compra.idcompra
                LEFT JOIN livros ON livros.idlivros = compra_livros.idlivros
                WHERE clientes.idclientes = {idcliente}'''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado

    def consulta_faixa_de_preco(self, preco1, preco2):
        consulta = f'SELECT * FROM view_estoque WHERE preco > {preco1} and preco < {preco2}'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    #Seleciona todos os livros, generos e autores; autores e gêneros são passados cada um como uma string
    def pesquisa_geral(self):
        consulta = f'''SELECT * FROM view_estoque;'''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado

    def pesquisa_livro_por_titulo(self, titulo):
        consulta = f'''SELECT * FROM view_estoque
    WHERE view_estoque.titulo like "%{titulo}%"
    GROUP BY view_estoque.idlivros;'''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_livros_de_editora(self, editora):
        consulta = f'''SELECT * FROM view_estoque
    WHERE view_estoque.editora like "%{editora}%"
    GROUP BY view_estoque.idlivros;'''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_livros_por_genero(self, genero):
        consulta = f'''SELECT * FROM view_estoque
    WHERE view_estoque.genero like "%{genero}%"
    GROUP BY view_estoque.idlivros;'''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_livros_fabricados_em_mari(self):
        consulta = f'SELECT * FROM view_estoque WHERE isFromMari = 1'
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado
    
    def pesquisa_livros_de_um_autor(self, autor):
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
    FROM livros
    LEFT JOIN livro_autores ON livros.idlivros = livro_autores.fk_idlivros
    LEFT JOIN autores ON livro_autores.fk_idautores = autores.idautores
    LEFT JOIN livro_generos ON livros.idlivros = livro_generos.f_idlivros
    LEFT JOIN generos ON livro_generos.f_idgeneros = generos.idgeneros
    WHERE autores.nome = "{autor}"
    GROUP BY livros.idlivros;'''
        resultado = self.gerencia_livraria.executa_fetch(consulta)
        return resultado