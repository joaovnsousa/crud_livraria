from classes import *
from menu_vendedor import *
from prettytable import PrettyTable
from CRUD.CreateCRUD import *
from CRUD.DeleteCRUD import *
from CRUD.ReadCRUD import *
from CRUD.UpdateCRUD import *

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
            procura_livros()
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

