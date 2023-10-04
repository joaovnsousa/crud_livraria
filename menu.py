from classes import *
from prettytable import PrettyTable
from CreateCRUD import *
from DeleteCRUD import *
from ReadCRUD import *
from UpdateCRUD import *

instancia_livraria = GerenciaLivraria()
create = CreateCRUD(instancia_livraria)
read = ReadCRUD(instancia_livraria)
update = UpdateCRUD(instancia_livraria)
delete = DeleteCRUD(instancia_livraria)

def menu(create, read, update, delete):
    print('Olá! Seja bem-vindo ao Los Libros Hermanos.')
    print('-------------------------------------------')
    print('Digite o número correspondente às seguintes opções:')
    print('1: Inserir')
    print('2: Atualizar os dados de algum livro')
    print('3: Consultar um livro')
    print('4: Remover um livro')
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
        case 0:
            return False

        case _:
            return False
        
def tabelao(read):
    table_rows = ['id', 'Título', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma']
    tabela = PrettyTable(table_rows)
    consulta_livros = read.pesquisa_todos_os_livros()
    consulta_autores = []
    idlivros = []
    for objeto in consulta_livros:
        idlivros.append(objeto[0])
        tabela.add_row(objeto)
    for id in idlivros:
        consulta_autores.append(read.consulta_autores_de_um_livro(id))
    tabela.add_column('Autores', consulta_autores)
    consulta_generos = []
    idlivros2 = []
    for objeto in consulta_livros:
        idlivros2.append(objeto[0])
    for id in idlivros2:
        consulta_generos.append(read.consulta_generos_de_um_livro(id))
    tabela.add_column('Gêneros', consulta_generos)

    print(tabela)

def menu_atualizar(read, update):
    tabelao(read)
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
    table_rows = ['id', 'Título', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma']
    tabela = PrettyTable(table_rows)
    consulta_livros_nome = read.pesquisa_por_titulo(titulo)
    consulta_autores = []
    idlivros = []
    for objeto in consulta_livros_nome:
        idlivros.append(objeto[0])
        tabela.add_row(objeto)
    for id in idlivros:
        consulta_autores.append(read.consulta_autores_de_um_livro(id))
    tabela.add_column('Autores', consulta_autores)
    consulta_generos = []
    idlivros2 = []
    for objeto in consulta_livros_nome:
        idlivros2.append(objeto[0])
    for id in idlivros2:
        consulta_generos.append(read.consulta_generos_de_um_livro(id))
    tabela.add_column('Gêneros', consulta_generos)
    print(tabela)
    return

def consulta_editora(read):
    editora = (input('Digite a editora do livro: '))
    table_rows = ['id', 'Título', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma']
    tabela = PrettyTable(table_rows)
    consulta_livros_nome = read.pesquisa_por_editora(editora)
    consulta_autores = []
    idlivros = []
    for objeto in consulta_livros_nome:
        idlivros.append(objeto[0])
        tabela.add_row(objeto)
    for id in idlivros:
        consulta_autores.append(read.consulta_autores_de_um_livro(id))
    tabela.add_column('Autores', consulta_autores)
    consulta_generos = []
    idlivros2 = []
    for objeto in consulta_livros_nome:
        idlivros2.append(objeto[0])
    for id in idlivros2:
        consulta_generos.append(read.consulta_generos_de_um_livro(id))
    tabela.add_column('Gêneros', consulta_generos)
    print(tabela)
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
    table_rows = ['id', 'Título', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma']
    tabela = PrettyTable(table_rows)

    get_id = read.pesquisa_id_genero(genero)
    get_id = get_id[0][0]

    consulta_livros_nome = read.pesquisa_por_genero(get_id)
    consulta_autores = []
    idlivros = []
    
    
    for objeto in consulta_livros_nome:
        idlivros.append(objeto[0])
        tabela.add_row(objeto)

    for id in idlivros:
        consulta_autores.append(read.consulta_autores_de_um_livro(id))
    tabela.add_column('Autores', consulta_autores)
    consulta_generos = []
    idlivros2 = []
    for objeto in consulta_livros_nome:
        idlivros2.append(objeto[0])
    for id in idlivros2:
        consulta_generos.append(read.consulta_generos_de_um_livro(id))
    tabela.add_column('Gêneros', consulta_generos)
    print(tabela)
    return

def consulta_livro_autor(read):
    autor = (input('Digite o autor do livro: '))
    table_rows = ['id', 'Título', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma']
    tabela = PrettyTable(table_rows)

    get_id = read.pesquisa_id_autor(autor)
    get_id = get_id[0][0]

    consulta_livros_nome = read.pesquisa_por_autor(get_id)
    consulta_autores = []
    idlivros = []
    
    
    for objeto in consulta_livros_nome:
        idlivros.append(objeto[0])
        tabela.add_row(objeto)

    for id in idlivros:
        consulta_autores.append(read.consulta_autores_de_um_livro(id))
    tabela.add_column('Autores', consulta_autores)
    consulta_generos = []
    idlivros2 = []
    for objeto in consulta_livros_nome:
        idlivros2.append(objeto[0])
    for id in idlivros2:
        consulta_generos.append(read.consulta_generos_de_um_livro(id))
    tabela.add_column('Gêneros', consulta_generos)
    return
    
def menu_inserir_geral(create, read):
    while True:
            print("1: Livro\n2: Autor\n3: Gênero\n0: Sair")
            escolha = int(input('Escolha'))


            match escolha:
                case 1:
                    menu_inserir_livro(create, read)
                    return True
                    

                case 2:
                    menu_inserir_autor(create, read)
                    return True                

                case 3:
                    menu_inserir_genero(create, read)
                    return True

                case 0:
                    return False

def menu_inserir_autor(create, read):
        
        condicao = False
        consulta_autores = read.pesquisa_todos_os_autores()
        id_autor_novo = 0

        input_autor = input("Digite o nome do autor: ")
        print('Caso deseje parar de inserir um autor, digite "Acabou"')
        if any(input_autor in tupla for _, tupla in consulta_autores):
            condicao = False
        elif not any(input_autor in tupla for _, tupla in consulta_autores) and input_autor != 'Acabou':
            condicao = True
            create.insere_autor(input_autor)
            id_autor_novo = create.gerencia_livraria.cursor.lastrowid
            
        elif input_autor == 'Acabou':
            condicao = False

        while condicao == True:
            
            escolha = input('Existe algum livro relacionado a esse autor na base dados? ')
            if escolha == 'sim' or escolha == 'Sim':
                tabelao(read)
                id_livro_relacionado = input('Digite o id do livro: ')
                create.insere_livro_autores(id_livro_relacionado, id_autor_novo)
            if escolha == 'não' or escolha == 'Não':
                break

def menu_inserir_genero(create, read):

        condicao = False
        consulta_generos = read.pesquisa_todos_os_generos()
        id_genero_novo = 0

        input_genero = input("Digite o gênero do livro: ")
        print('Caso deseje parar de inserir um gênero, digite "Acabou"')

        if any(input_genero in tupla for _, tupla in consulta_generos):
            condicao = False
        elif not any(input_genero in tupla for _, tupla in consulta_generos) and input_genero != 'Acabou':
            condicao = True
            create.insere_genero(input_genero)
            id_genero_novo = create.gerencia_livraria.cursor.lastrowid
            
        elif input_genero == 'Acabou':
            condicao = False

        while condicao == True:
            
            escolha = input('Existe algum livro relacionado a esse gênero na base de dados? ')
            if escolha == 'sim' or escolha == 'Sim':
                tabelao(read)
                id_livro_relacionado = input('Digite o id do livro: ')
                create.insere_livro_genero(id_livro_relacionado, id_genero_novo)
                print("Inserido com sucesso!")
            if escolha == 'não' or escolha == 'Não':
                break




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
                idioma
            )

            instancia_livro_autor_genero(autores, novo_livro, genero, autores_existentes, generos_existentes, create, read)

            print('Livro inserido com sucesso!')

            return
        
        except ValueError as e:
            # Captura exceções ValueError quando as entradas são inválidas
            print(f"Erro: {e}")
            print("Por favor, forneça entradas válidas.")
        

            # solicita as informações do livro:
            

def menu_remocoes(read, delete):
            # solicita as informações do livro:
            tabelao(read)

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

tabelao(read)
while True:
    booleano = menu(create, read, update, delete)
    if booleano == False:
        break