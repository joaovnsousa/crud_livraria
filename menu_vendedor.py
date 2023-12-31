from classes import *
from prettytable import PrettyTable
import datetime
from CRUD.CreateCRUD import *
from CRUD.DeleteCRUD import *
from CRUD.ReadCRUD import *
from CRUD.UpdateCRUD import *


instancia_livraria = GerenciaLivraria()
create = CreateCRUD(instancia_livraria)
read = ReadCRUD(instancia_livraria)
update = UpdateCRUD(instancia_livraria)
delete = DeleteCRUD(instancia_livraria)


def menu_vendedor(create, read, update, delete):
    todos_os_livros = read.pesquisa_geral()
    todos_os_livros = lista_de_livros(todos_os_livros)
    tabelao2(todos_os_livros)
    print('Olá! Seja bem-vindo ao Los Libros Hermanos.')
    print('-------------------------------------------')
    print('Digite o número correspondente às seguintes opções:')
    print('1: Inserir')
    print('2: Atualizar os dados de algum livro')
    print('3: Consultar um livro')
    print('4: Remover um livro')
    print('5: Atualizar os dados de algum cliente')
    print('6: Mostrar as vendas de um vendedor')
    print('0: Sair do sistema')
    escolha = int(input('Digite sua escolha: '))
    match escolha:
        case 1:
            print('-------------------------------------------')
            menu_inserir_geral(create, read)
            return True

        case 2:
            print('-------------------------------------------')
            menu_atualizar(read, update)
        case 3:
            print('-------------------------------------------')
            
            menu_escolha_consulta(read)
            return True

        case 4:
            print('-------------------------------------------')
            menu_remocoes(read, delete)

        case 5:
            print('-------------------------------------------')
            menu_atualizar_cliente(read, update)
        case 6:
            print('-------------------------------------------')
            mostra_vendas_vendedores(read)

        case 0:
            return True

        case _:
            return False
        
#AHAHAHAHAHA
#Cria uma lista de livros passada através de uma lista de tuplas após uma consulta
def lista_de_livros(livros):
    lista_livros = []
    for livro in livros:
        instancia_livro = Livros(livro[1], livro[2], livro[3], livro[4], livro[5], livro[6], livro[7], livro[8], livro[9], livro[10], livro[11], livro[12], livro[13])
        instancia_livro.set_id(livro[0])
        lista_livros.append(instancia_livro)
    return lista_livros

def mostra_vendas_vendedores(read):
    consulta = read.consulta_vendas_vendedor()
    table_rows = ['ID da Compra', 'ID do Cliente', 'Nome do Cliente', 'ID do Vendedor', 'Nome do Vendedor', 'Data da compra']
    tabela = PrettyTable(table_rows)
    for elemento in consulta:
        tabela.add_row([elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5]])
    print(tabela)
    idCompra = int(input('Digite o número do ID da compra que você deseja ver quais livros foram comprados: '))
    dados = read.consulta_livros_compra_id(idCompra)
    print(dados)
    dados = lista_de_livros(dados)
    tabelao2(dados)

def verifica_livros_em_estoque(livros):
    lista_nova_livros = []
    for livro in livros:
        if livro.get_data_saida() == None:
            lista_nova_livros.append(livro)
    return lista_nova_livros
#Recebe uma lista de livros e passa seus dados para uma tabela, printando no final
def tabelao2(livros):
    table_rows = ['id', 'Título', 'Autores', 'Genero', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma', 'Data de Entrada', 'Data de Saída', 'isFromMari']
    tabela = PrettyTable(table_rows)
    for livro in livros:
        tabela.add_row([livro.get_id(), livro.get_titulo(), livro.get_autor(), livro.get_genero(), livro.get_editora(), livro.get_preco(), 
                        livro.get_data_publicacao(), livro.get_edicao(), livro.get_isbn(), livro.get_volume(), livro.get_idioma(), livro.get_data_entrada(), livro.get_data_saida(), livro.get_isFromMari()])
    print(tabela)

def menu_atualizar(read, update):
    tabelao2(todos_os_livros)
    idlivro = int(input('Escolha o id do livro que deseja atualizar dados: '))
    print('Por qual desses deseja fazer a atualização?\n1: Título\n2: Autor\n3: Gênero\n4: Editora\n5: Preço\n\
            6: Data de publicação\n7: Edição\n8: ISBN\n 9: Volume\n 10: Idioma\n0: Sair')
    escolha = int(input('Digite sua escolha: '))

    match escolha:
        case 1:
            titulo_atualizado = input('Digite o novo nome do título do livro: ')
            update.atualiza_titulo_livro(idlivro, titulo_atualizado)
            print("Título atualizado com sucesso!")
            return True
        
        case 2:
            atualiza_autor(read, update, idlivro)

        case 3:
            atualiza_genero(read, update, idlivro)

        case 4:
            preco_atualizado = input('Digite o novo nome da editora do livro: ')
            update.atualiza_editora_livro(idlivro, preco_atualizado)
            print("Editora atualizada com sucesso!")
            return True                

        case 5:
            preco_atualizado = float(input('Digite o novo preco do livro: '))
            update.atualiza_preco_livro(idlivro, preco_atualizado)
            print("Preco atualizado com sucesso!")
            return True

        case 6:
            data_atualizada = input('Digite a nova data de publicação (AAAA-MM-DD) do livro: ')
            update.atualiza_data_publicacao_livro(idlivro, data_atualizada)
            print("Data atualizada com sucesso!")
            return True
        
        case 7:
            edicao_atualizada = int(input('Digite a nova edição do livro: '))
            update.atualiza_edicao_livro(idlivro, edicao_atualizada)
            print("Edição atualizada com sucesso!")
            return True
        
        case 8:
            isbn_atualizado = input('Digite o isbn do livro: ')
            update.atualiza_isbn_livro(idlivro, isbn_atualizado)
            print("ISBN atualizado com sucesso!")
            return True
        
        case 9:
            volume_atualizado = int(input('Digite o novo volume do livro: '))
            update.atualiza_volume_livro(idlivro, volume_atualizado)
            print("Volume atualizado com sucesso!")
            return True
        
        case 10:
            idioma_atualizado = input('Digite o novo idioma do livro: ')
            update.atualiza_idioma_livro(idlivro, idioma_atualizado)
            print("Edição atualizada com sucesso!")
            return True
        
        case 0:
            return False
        

def menu_atualizar_cliente(read, update):
    todos_os_clientes = read.pesquisa_cliente_geral()
    print(todos_os_clientes)
    idcliente = int(input('Escolha o id do cliente que deseja atualizar dados: '))
    print('Por qual desses deseja fazer a atualização?\n1: Nome\n2: Sobrenome\n3: CPF\n4: Primeiro Telefone\n5: Segundo Telefone\n\
            6: Se é flamenguista\n7: Se é de Sousa\n8: Se é fã de One piece\n0: Sair')
    escolha = int(input('Digite sua escolha: '))

    match escolha:
        case 1:
            nome_atualizado = input('Digite o novo nome do cliente: ')
            update.atualiza_nome_cliente(idcliente, nome_atualizado)
            print("Nome atualizado com sucesso!")
            return True
        
        case 2:
            sobrenome_atualizado = input('Digite o novo sobrenome do cliente: ')
            update.atualiza_sobrenome_cliente(idcliente, sobrenome_atualizado)
            print("Sobrenome atualizado com sucesso!")
            return True

        case 3:
            cpf_atualizado = input('Digite o novo cpf do cliente: ')
            update.atualiza_cpf_cliente(idcliente, cpf_atualizado)
            print("CPF atualizado com sucesso!")
            return True

        case 4:
            ptelefone_atualizado = input('Digite o novo numero do telefone: ')
            update.atualiza_ptelefone_cliente(idcliente, ptelefone_atualizado)
            print("Telefone atualizado com sucesso!")
            return True                

        case 5:
            stelefone_atualizado = input('Digite o novo numero do telefone: ')
            update.atualiza_stelefone_cliente(idcliente, stelefone_atualizado)
            print("Telefone atualizado com sucesso!")
            return True                

        case 6:
            flamengo_atualizado = input('Digite 1 se o cliente for flamenguista, do contrário 0: ')
            update.atualiza_flamengo_cliente(idcliente, flamengo_atualizado)
            print("Usuário atualizado com sucesso!")
            return True
        
        case 7:
            sousa_atualizado = input('Digite 1 se o cliente for de Sousa, do contrário 0: ')
            update.atualiza_sousa_cliente(idcliente, sousa_atualizado)
            print("Usuário atualizado com sucesso!")
            return True
    
        case 8:
            onepiece_atualizado = input('Digite 1 se o cliente for fã de One Piece, do contrário 0: ')
            update.atualiza_onepiece_cliente(idcliente, onepiece_atualizado)
            print("Usuário atualizado com sucesso!")
            return True
        
                
        case 0:
            return False





def menu_escolha_consulta(read):
    print('Por qual desses deseja fazer a consulta?\n1: Título\n2: Autor\n3: Gênero\n4: Editora\n0: Voltar')
    escolha = int(input('Digite sua escolha: '))

    match escolha:
        case 1:
            consulta_titulo(read)
            return True
        
        case 2:
            consulta_livro_autor(read)
            return True
        case 3:
            consulta_genero(read)
            return True
        case 4:
            consulta_editora(read)
            return True

        case 0:
            return False
        
def consulta_titulo(read):
    titulo = (input('Digite o título do livro: '))
    tuplas_livros = read.pesquisa_livro_por_nome(titulo)
    lista_livros = lista_de_livros(tuplas_livros)
    tabelao2(lista_livros)
    return

def consulta_editora(read):
    editora = (input('Digite a editora do livro: '))
    tuplas_livros = read.pesquisa_livros_de_editora(editora)
    lista_livros = lista_de_livros(tuplas_livros)
    tabelao2(lista_livros)
    return

def atualiza_autor(read, update, idlivro):
    autores = read.consulta_autores_de_um_livro(idlivro)
    for autor in autores:
        nome_novo = input('Digite o novo nome do autor:')
        update.atualiza_nome_autor(nome_novo, autor[0])


def atualiza_genero(read, update, idlivro):
    generos = read.consulta_generos_de_um_livro(idlivro)
    for genero in generos:
        genero_novo = input("Digite o novo gênero: ")
        update.atualiza_nome_genero(genero_novo, genero[0])
        print("Dados atualizados!")

def consulta_genero(read):
    genero = (input('Digite o gênero do livro: '))
    tuplas_livros = read.pesquisa_livros_por_genero(genero)
    tabelao2(lista_de_livros(tuplas_livros))

def consulta_livro_autor(read):
    autor = (input('Digite o autor do livro: '))
    tuplas_livros = read.pesquisa_livros_de_um_autor(autor)
    tabelao2(lista_de_livros(tuplas_livros))
    
def menu_inserir_geral(create, read):
    menu_inserir_livro(create, read)

def menu_inserir_livro(create, read):
    while True:
        try:
            titulo = input('Título: ')
            
            autores = []
            autores_existentes = []
            consulta_autores = read.pesquisa_todos_os_autores()
            while True:
                input_autor = input('Autor: ')
                print('Caso deseje parar de inserir um autor, digite "Acabou"')
                if any(input_autor in tupla for _, tupla in consulta_autores):
                    autores_existentes.append(input_autor)
                elif not any(input_autor in tupla for _, tupla in consulta_autores) and input_autor != 'Acabou':
                    autores.append(input_autor)
                elif input_autor == 'Acabou':
                    break
            
            if not titulo.strip():
                raise ValueError("Título não pode ser vazios.")
            
            genero = []
            generos_existentes = []
            consulta_generos = read.pesquisa_todos_os_generos()
            while True:
                input_genero = input('Genero: ')
                print('Caso deseje parar de inserir um gênero, digite "Acabou"')
                if any(input_genero in tupla for _, tupla in consulta_generos):
                    generos_existentes.append(input_genero)
                elif not any(input_genero in tupla for _, tupla in consulta_generos) and input_genero != 'Acabou':
                    genero.append(input_genero)
                elif input_genero == 'Acabou':
                    break
            
            editora = input('Editora: ')

            preco = float(input('Preço: '))
            if preco < 0:
                raise ValueError("O preço não pode ser um número negativo.")

            data_publicacao = input('Data de Publicação (AAAA-MM-DD): ')
            
            edicao = int(input('Edição: '))
            if edicao <= 0:
                raise ValueError("O livro deve ter pelo menos uma edição.")
            

            isbn = input('ISBN: ')
            
            volume = int(input('Volume: '))

            if volume < 0:
                raise ValueError("O volume não pode ser um número negativo. Digite 0 caso não haja volume.")
            
            idioma = input('Idioma: ')

            data_entrada = datetime.date.today()
            data_entrada = data_entrada.strftime('%Y-%m-%d')

            data_saida = None

            isFromMari = int(input('É de Mari? 1 para sim e 0 para não:'))

            # tratamento de erros:

            if preco < 0:
                raise ValueError("O preço não pode ser um número negativo.")
            
            if volume < 0:
                raise ValueError("O volume não pode ser um número negativo. Digite 0 caso não haja volume.")
            
            if edicao <= 0:
                raise ValueError("O livro deve ter pelo menos uma edição.")
            
            if checa_isbn(isbn) == False:
                raise ValueError("O ISBN deve ser inserido corretamente.")
            
            novo_livro = Livros(
                titulo,
                autores,
                genero,
                editora,
                preco,
                data_publicacao,
                edicao,
                isbn,
                volume,
                idioma,
                data_entrada,
                data_saida,
                isFromMari
            )

            instancia_livro_autor_genero(autores, novo_livro, genero, autores_existentes, generos_existentes, create, read)
            print('Livro inserido com sucesso!')
            return
        
        except ValueError as e:
            # Captura exceções ValueError quando as entradas são inválidas
            print(f"Erro: {e}")
            print("Por favor, forneça entradas válidas.")
               

def menu_remocoes(read, delete):
            # solicita as informações do livro:

            print('O que deseja remover?\n1: Livro\n2: Autor\n3: Gênero\n0: Sair')
            
            escolha = int(input('Digite sua escolha: '))


            match escolha:
                case 1:
                    idlivro = input('Digite o nome do id do livro: ')
                    delete.remove_livro_(idlivro)
                    print("Título removido com sucesso!")
                    return True
                    

                case 2:
                    autor = input('Digite o nome do autor do livro: ')
                    idautor = read.pesquisa_id_autor(autor)
                    delete.remove_autor(idautor[0][0])
                    print("Autor removido com sucesso!")
                    return True                

                case 3:
                    genero = input('Digite o nome do gênero do livro: ')
                    idgenero = read.pesquisa_id_genero(genero)
                    delete.remove_genero(idgenero[0][0])
                    print("Gênero removido com sucesso!")
                    return True

                case 0:
                    return False


def verifica_isbn_10(isbn):
    soma = 0
    for i in range(1, len(isbn) + 1):
        soma = soma + int (isbn[i-1])* i
    return soma % 11 == 0

def verifica_isbn_13(isbn):
    soma = (sum(int(caractere) for caractere in isbn[::2]) + sum(int(caractere) * 3 for caractere in isbn[1::2]))
    return soma % 10 == 0

def checa_isbn(isbn):
    validacao = False
    isbn = isbn.replace('-', '').replace(' ', '')
    if len(isbn) == 10:
        validacao = verifica_isbn_10(isbn)

    elif len(isbn) == 13:
        validacao = verifica_isbn_13(isbn)
    
    else:
        print('O ISBN não pode ter menos de 10 ou 13 dígitos.')
    
    return validacao

def instancia_livro_autor_genero(autores, livro, generos, autores_existentes, generos_existentes, create, read):
    create.inserir_livros(livro)
    idLivro = create.gerencia_livraria.cursor.lastrowid
    for autor in autores:
        create.insere_autor(autor)
        idAutor = create.gerencia_livraria.cursor.lastrowid
        create.insere_livro_autores(idLivro, idAutor)
    for autor in autores_existentes:
        idAutor = read.pesquisa_id_autor(autor)
        create.insere_livro_autores(idLivro, idAutor[0][0])
    for genero in generos:
        create.insere_genero(genero)
        idGenero = create.gerencia_livraria.cursor.lastrowid
        create.insere_livro_genero(idLivro, idGenero)
    for genero in generos_existentes:
        idGenero = read.pesquisa_id_genero(genero)
        create.insere_livro_genero(idLivro, idGenero[0][0])

global todos_os_livros 
todos_os_livros = read.pesquisa_geral()
todos_os_livros = lista_de_livros(todos_os_livros)

#menu_vendedor(create, read, update, delete)