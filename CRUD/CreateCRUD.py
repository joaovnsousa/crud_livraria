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
    
    def insere_nova_compra(self, compra):
        insercao = f'INSERT INTO compra(forma_pagamento, status_confirmação, data_compra, idclientes, idvendedor) VALUES ("{compra.forma_pagamento}", "{compra.status}", "{compra.data_compra}", {compra.cliente.get_idcliente()}, {compra.vendedor})'
        self.gerencia_livraria.executa_commit(insercao)
    
    def insere_compra_livros(self, idcompra, idlivro):
        insercao = f'INSERT INTO compra_livros(idcompra, idlivros) VALUES ({idcompra}, {idlivro})'
        self.gerencia_livraria.executa_commit(insercao)

    def insere_novo_cliente(self, cliente):
        insercao = f'INSERT INTO pessoa(nome, sobrenome, cpf, prim_telefone, seg_telefone) VALUES ("{cliente.get_nome()}", "{cliente.get_sobrenome()}", "{cliente.get_cpf()}", "{cliente.get_prim_telefone()}", "{cliente.get_seg_telefone()}")'
        self.gerencia_livraria.executa_commit(insercao)
        idpessoa = self.gerencia_livraria.cursor.lastrowid
        insercao = f'INSERT INTO clientes(idpessoa, isFlamengo, isFromSousa, isOnePieceFan) VALUES ({idpessoa}, {cliente.get_isFlamengo()}, {cliente.get_isFromSousa()}, {cliente.get_isOnePieceFan()})'
        self.gerencia_livraria.executa_commit(insercao)

    def insere_nova_pessoa(self, pessoa):
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
