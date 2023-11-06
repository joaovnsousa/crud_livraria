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
            print('------------------------------------------------------------------------------------------------')
            retorno = True
            while retorno:
                if loginVendedor() != None:
                    retorno = False
                else:
                    retorno = True
            cpf = input('Digite o CPF do cliente: ')
            cliente = transforma_tupla_objeto(read.pesquisa_cliente(cpf), 'cliente')
            print(cliente[0])
            
        case 3:
            carrinho(lista_carrinho)
        
        case 4:
            escolha = menu_vendedor(create, read, update, delete)

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

def carrinho(lista_carrinho):
    print('Aqui está o seu carrinho: ')
    livros_carrinho = []
    for ids in lista_carrinho:
        livros_carrinho.append(read.pesquisa_titulo_id_livro_por_id(ids))
    tabela_nome_id(livros_carrinho)
    print('------------------------------------------------------------------------------------------------')
    escolha = input(('Digite remover para remover algo do carrinho, digite finalizar para terminar a compra: '))
    print('------------------------------------------------------------------------------------------------')
    if escolha == 'remover':
        remover_do_carrinho(lista_carrinho)
        return
    elif escolha == 'finalizar':
        print('Você tem cadastro no sistema?')
        resposta_cadastro = input('Digite sim ou não: ')
        if resposta_cadastro == 'sim':
            cpf = input('Digite seu CPF com todos os pontos e traços: ')
            cliente = read.pesquisa_cliente(cpf)
            transforma_tupla_objeto(cliente, 'cliente')
            finaliza_compra(cliente, lista_carrinho)
        if resposta_cadastro == 'não':
            #AQUI
            cadastro_cliente()
            return


def cadastro_cliente():
    nome = input('Digite seu primeiro nome: ')
    sobrenome = input('Digite o seu sobrenome: ')
    valida_cpf = False
    cpf = ''
    while valida_cpf == False:
        cpf = input('Digite o seu CPF: ')
        valida_cpf = instancia_livraria.verifica_cpf(cpf)
        if valida_cpf:
            print('Seu CPF é válido!')
            print('------------------------------------------------------------------------------------------------')
        else:
            print('CPF inválido. Tente novamente')
            print('------------------------------------------------------------------------------------------------')
    prim_telefone = input('Digite o seu primeiro telefone: ')
    print('------------------------------------------------------------------------------------------------')
    seg_telefone = input('Digite o seu segundo telefone; se não tiver, coloque 00000: ')
    print('------------------------------------------------------------------------------------------------')
    if seg_telefone == '00000':
        seg_telefone = None
    isFlamengo = input('Diga sim se é fã do flamengo ou não se contrário: ')
    print('------------------------------------------------------------------------------------------------')
    isFlamengo = resposta_booleana(isFlamengo)
    isFromSousa = input('Diga sim se é de Sousa ou não se o contrário: ')
    print('------------------------------------------------------------------------------------------------')
    isFromSousa = resposta_booleana(isFromSousa)
    isOnePieceFan = input('Diga sim se é fã de One Piece ou não caso contrário: ')
    print('------------------------------------------------------------------------------------------------')
    isOnePieceFan = resposta_booleana(isOnePieceFan)
    novoCliente = Cliente(nome, sobrenome, cpf, prim_telefone, seg_telefone, isFlamengo, isFromSousa, isOnePieceFan)
    print(novoCliente)
    create.insere_novo_cliente(novoCliente)
    novoCliente.set_idcliente(instancia_livraria.cursor.lastrowid)
    finaliza_compra(novoCliente, lista_carrinho)

def finaliza_compra(novoCliente, lista_carrinho):
    autenticacao = True
    idvendedor = 0
    while autenticacao:
        idvendedor = loginVendedor()
        if idvendedor != None:
            autenticacao = False
        else:
            autenticacao = True
    forma_pagamento = input('Digite aqui sua forma de pagamento: ')
    print('------------------------------------------------------------------------------------------------')
    while forma_pagamento != 'berries' and 'cartão' and 'boleto' and 'pix' and 'Dinheiro':
        forma_pagamento = input('Digite aqui sua forma de pagamento: ')
    lista_livros1 = []
    for num in lista_carrinho:
        lista_livros1.append(read.pesquisa_livro_por_id(num))
    lista_livros1 = [tupla for sublist in lista_livros1 for tupla in sublist]
    lista_livros2 = []
    lista_livros2 = lista_de_livros(lista_livros1)
    compra_atual = Compra(idvendedor, novoCliente, lista_livros2, forma_pagamento, None)
    print(novoCliente)
    print(lista_livros2)
    print(compra_atual)
    print('O total da sua compra é: ', compra_atual.total_compra())
    print('------------------------------------------------------------------------------------------------')
    escolha = input('Deseja finalizar a compra? ')
    if escolha == 'sim':
        compra_atual.status = 'Concluída'
    elif escolha == 'não':
        compra_atual.status = 'Congelada'
        return
    create.insere_nova_compra(compra_atual)
    idcompra = instancia_livraria.cursor.lastrowid
    for livro in lista_livros2:
        create.insere_compra_livros(idcompra, livro.get_id())
        update.atualiza_data_saida_livro(livro.get_id(), compra_atual.data_compra)
    print('------------------------------------------------------------------------------------------------')
    tabela_compra(compra_atual, idcompra)


def tabela_compra(compra, idcompra):
    tabela_rows = ['ID Compra', 'Cliente', 'Vendedor']
    tabela1 = PrettyTable(tabela_rows)
    print(read.pesquisa_vendedor_por_id(8))
    tabela1.add_row([idcompra, compra.cliente.get_nome(), read.pesquisa_vendedor_por_id(8)])
    print(tabela1)
    print('------------------------------------------------------------------------------------------------')
    print('----------------------------------------COMPRAS-------------------------------------------------')
    tabela2_rows = ['idLivro', 'Livro', 'Preço']
    tabela2 = PrettyTable(tabela2_rows)
    for livro in compra.livros:
        tabela2.add_row([livro.get_id(), livro.get_titulo(), livro.get_preco()])
    print(tabela2)

def resposta_booleana(resposta):
    if resposta == 'sim':
        return True
    if resposta == 'não':
        return False
    
def tabela_nome_id(livros):
    table_rows = ['ID', 'Título']
    tabela = PrettyTable(table_rows)
    for obj in livros:
        for livro in obj:
            tabela.add_row([livro[0], livro[1]])
    print(tabela)


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
            menu_usuario()


def remover_do_carrinho(lista_carrinho):
    id_livro = int(input('Digite o ID do livro que você deseja remover do carrinho: '))
    lista_carrinho = [x for x in lista_carrinho if x != id_livro]
    print(lista_carrinho)

def loginVendedor():
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')
    consulta = read.consulta_login_senha(login, senha)
    if consulta != []:
        print('Seja bem-vindo ao sistema!')
        return consulta[0][0]
    else:
        print('Tente novamente.')
        return None

#clientez = Cliente('Rafael', 'Victor', '111.120.244-33', '(83)98694-4876', None, 1, 0, 1)
#clientez.set_idcliente(7)
lista = []
livro1 = Livros('Mitologia: Contos imortais de deuses e heróis', 'Edith Hamilton', 'Mitologia, Cultura, História', 'Sextante', 35.99, '2022-08-16', 1, '978-6555644074', 1, 'Português', '2022-08-16', '2022-08-16', 1)
livro1.set_id(11)
lista.append(livro1)
compra1 = Compra(2, Cliente('Rafael', 'Victor', '111.120.244-33', '(83)98694-4876', None, 1, 0, 1), lista, 'Dinheiro', 'Confirmado')
tabela_compra(compra1, 2)
#cadastro_cliente()
#finaliza_compra(clientez, [7, 8, 9])
menu_usuario()