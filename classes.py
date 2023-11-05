from APIkeys import *
import mysql.connector
import datetime
from prettytable import PrettyTable
from CRUD.CreateCRUD import *
from CRUD.DeleteCRUD import *
from CRUD.ReadCRUD import *
from CRUD.UpdateCRUD import *

class Livros:
    def __init__(self, titulo, autor, genero, editora, preco, data_publicacao, edicao, isbn, volume, idioma, data_entrada, data_saida, isFromMari):
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
        self.__data_entrada = data_entrada
        self.__data_saida = data_saida
        self.__isFromMari = isFromMari
        self.__id = 0

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
    
    def get_isFromMari(self):
        return self.__isFromMari

    def get_id(self):
        return self.__id
    
    def get_data_entrada(self):
        return self.__data_entrada

    def get_data_saida(self):
        return self.__data_saida

    def set_data_saida(self, data):
        self.__data_saida = data
    
    def set_id(self, id):
        self.__id = id
    
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

    def verifica_cpf(self, cpf):
        digito1 = False
        digito2 = False
        cpf = cpf.replace('-', ''.replace(' ', ''))
        cpf = cpf.replace('.', ''.replace(' ', ''))
        if len(cpf) < 11 or len(cpf) > 11:
            print('Inválido! O CPF deve ter exatamente 11 dígitos.')
            return
        
        #Verifica o primeiro dígito
        soma = 0
        for i in range (9):
            soma = soma + int (cpf[i]) * (10 - i)
        if soma % 11 == 0 or soma % 11 == 1:
            if int (cpf[9]) == 0: 
                digito1 = True
        else:
            if int (cpf[9]) == 11 - (soma % 11):
                digito1 = True
        
        #Verifica o segundo dígito
        soma = 0
        for i in range(10):
            soma = soma + int(cpf[i]) * (11 - i)
        if soma % 11 == 0 or soma % 11 == 1:
            if int(cpf[10] == 0):
                digito2 = True
        else:
            if int (cpf[10]) == 11 - (soma % 11):
                digito2 = True

        if digito1 and digito2:
            return True
    

class Cliente:
    def __init__(self, nome, sobrenome, cpf, prim_telefone, seg_telefone, isFlamengo, isFromSousa, isOnePieceFan):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__prim_telefone = prim_telefone
        self.__seg_telefone = seg_telefone
        self.__isFlamengo = isFlamengo
        self.__isFromSousa = isFromSousa
        self.__isOnePieceFan = isOnePieceFan
        self.__livros_comprados = None
        self.__id = 0

    def get_nome(self):
        return self.__nome
    
    def get_sobrenome(self):
        return self.__sobrenome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_prim_telefone(self):
        return self.__prim_telefone
    
    def get_seg_telefone(self):
        return self.__seg_telefone
    
    def get_isFlamengo(self):
        return self.__isFlamengo
    
    def get_isFromSousa(self):
        return self.__isFromSousa
    
    def get_isOnePieceFan(self):
        return self.__isOnePieceFan
    
    def get_livros_comprados(self):
        return self.__livros_comprados
    
    def set_livros_comprados(self):
        return self.__livros_comprados
    
    def __str__(self):
        table_rows = ['Nome', 'Sobrenome', 'CPF', 'Primeiro telefone', 'Segundo telefone', 'Flamengo', 'Sousa', 'One Piece']
        tabela = PrettyTable(table_rows)
        tabela.add_row([Cliente.get_nome(self), Cliente.get_sobrenome(self), Cliente.get_cpf(self), Cliente.get_prim_telefone(self), Cliente.get_seg_telefone(self), Cliente.get_isFlamengo(self), Cliente.get_isFromSousa(self), Cliente.get_isOnePieceFan(self)]) 
        print(tabela)
        return ""

#Sempre tem um vendedor, um cliente, uma lista de livros, uma forma de pagamento, e um status.
class Compra:
    def __init__(self, vendedor, cliente, livros, forma_pagamento, status):
        self.vendedor = vendedor
        self.cliente = cliente
        self.livros = livros
        self.forma_pagamento = forma_pagamento
        self.status = status
        self.data_compra = datetime.date.today()
        
    #Atualiza o status da compra. Também deve atualizar no banco de dados quando for pro menu
    def atualiza_status(self, atualizacao):
        if atualizacao == False:
            self.status = 'Congelada'
        else:
            if self.status == None:
                self.status = 'Em andamento'
            if self.status == 'Em andamento':
                self.status = 'Completa'

    #Calcula o total da compra de acordo com os descontos que o cliente tem.
    def total_compra(self):
        total = 0
        for livro in self.livros:
            total = total + livro.get_preco()
        if self.cliente.get_isFlamengo() or self.cliente.get_isFromSousa() or self.cliente.get_isOnePieceFan():
            desconto = total * 0.25
            total = total - desconto
        return total