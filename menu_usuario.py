from classes import *
from menu_vendedor import *
from prettytable import PrettyTable
from CRUD.CreateCRUD import *
from CRUD.DeleteCRUD import *
from CRUD.ReadCRUD import *
from CRUD.UpdateCRUD import *

lista_carrinho = []

def menu_usuario():
    print('Seja bem-vindo à livraria Los Libros Hermanos! Selecione abaixo a função que você deseja fazer: ')
    print('------------------------------------------------------------------------------------------------')
    print('1: Procurar livros')
    print('------------------------------------------------------------------------------------------------')
    print('2: Verificar dados cadastrais')
    print('------------------------------------------------------------------------------------------------')
    print('3: Carrinho e confirmar compra')
    print('------------------------------------------------------------------------------------------------')
    print('4: Login como vendedor')
    print('------------------------------------------------------------------------------------------------')
    escolha = int(input('Digite sua escolha: '))
    
    match escolha:
        case 1:
            submenu_livros()
            return True
        case 2:
            print('Um vendedor será autenticado para verificar seus dados cadastrais.')
            retorno = True
            while retorno:
                retorno = loginVendedor()
            cpf = input('Digite o CPF do cliente: ')
            cliente = transforma_tupla_objeto(read.pesquisa_cliente(cpf), 'cliente')
            print(cliente[0])
            return True
            
        #case 3:

def transforma_tupla_objeto(tupla, param):
    lista_obj = []
    if param == 'cliente':
        for cliente in tupla:
            instancia_cliente = Cliente(cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6], cliente[7], cliente[8])
            lista_obj.append(instancia_cliente)
    #elif param == 'vendedor':

    return lista_obj


def submenu_livros():
    print('Deseja pesquisar livros e por quais parâmetros?')
    print('------------------------------------------------------------------------------------------------')
    print('1: Pesquisar todos os livros')
    print('2: Pesquisar por faixa de preço')
    print('3: Pesquisar por gênero')
    print('4: Pesquisar por livros fabricados em Mari')
    print('5: Pesquisar por nome')
    escolha = int(input('Digite o número da opção desejada: '))
    match escolha:
        case 1:
            livros_em_estoque = verifica_livros_em_estoque(todos_os_livros)
            lista_ids = id_lista_livros(livros_em_estoque)
            tabelao2(livros_em_estoque)
            print('Deseja adicionar algum livro no carrinho?')
            adicionar_no_carrinho(lista_ids)
        
        case 2:
            fronteira1 = float(input('Digite o primeiro valor da faixa de preço: '))
            fronteira2 = float(input('Digite o segundo valor da faixa de preço: '))
            livros_fronteira = verifica_livros_em_estoque(lista_de_livros(read.consulta_faixa_de_preco(fronteira1, fronteira2)))
            lista_ids = id_lista_livros(livros_fronteira)
            tabelao2(livros_fronteira)
            print('Deseja adicionar algum livro no carrinho?')
            adicionar_no_carrinho(lista_ids)

        case 3:
            genero = input('Digite o gênero dos livros: ')
            livros_generos = verifica_livros_em_estoque(lista_de_livros(read.pesquisa_livros_por_genero(genero)))
            lista_ids = id_lista_livros(livros_generos)
            tabelao2(livros_generos)
            print('Deseja adicionar algum livro no carrinho?')
            adicionar_no_carrinho(lista_ids)
        
        case 4:
            livros_mari = verifica_livros_em_estoque(lista_de_livros(read.pesquisa_livros_fabricados_em_mari()))
            lista_ids = id_lista_livros(livros_mari)
            tabelao2(livros_mari)
            print('Deseja adicionar algum livro no carrinho?')
            adicionar_no_carrinho(lista_ids)
        
        case 5:
            titulo = input('Digite o título do livro: ')
            livros_titulo = verifica_livros_em_estoque(lista_de_livros(read.pesquisa_livro_por_titulo(titulo)))
            lista_ids = id_lista_livros(livros_titulo)
            tabelao2(livros_titulo)
            print('Deseja adicionar algum livro no carrinho?')
            adicionar_no_carrinho(lista_ids)

def id_lista_livros(livros):
    lista_ids = []
    for livro in livros:
        lista_ids.append(livro.get_id())
    return lista_ids

def adicionar_no_carrinho(lista_idlivros):
    escolha = True
    while escolha: 
        id_livro = int(input('Digite o ID do livro que você deseja colocar no carrinho. Caso não queira colocar nenhum, digite 0: '))
        print('------------------------------------------------------------------------------------------------')
        if id_livro == 0:
            return
        if not any(id_livro == idlivro for idlivro in lista_idlivros):
            print('Digite um valor válido.')
            escolha = True
        else:
            lista_carrinho.append(id_livro)

def loginVendedor():
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')
    consulta = read.consulta_login_senha(login, senha)
    if consulta != []:
        print('Seja bem-vindo ao sistema!')
        return False
    else:
        print('Tente novamente.')
        return True

menu_usuario()