from classes import Livros, GerenciaLivraria
from prettytable import PrettyTable
class Menu:
    def __init__(self):
        self.livro_instanciado = None
        self.instancia_livraria = GerenciaLivraria()
    
    def menu(self):
        print('Olá! Seja bem-vindo ao Los Libros Hermanos.')
        print('-------------------------------------------')
        print('Digite o número correspondente às seguintes opções:')
        print('1: Inserir um novo livro')
        print('2: Atualizar os dados de algum livro')
        print('3: Consultar um livro')
        print('4: Remover um livro')
        print('0: Sair do sistema')
        escolha = int(input('Digite sua escolha: '))
        match escolha:
            case 1:
                print('-------------------------------------------')
                self.menu_inserir_geral()
                return True

            case 2:
                print('-------------------------------------------')
                self.menu_atualizar()
            case 3:
                print('-------------------------------------------')
                
                self.menu_escolha_consulta()
                return True

            case 4:
                print('-------------------------------------------')
                self.menu_remocoes()
            case 0:
                return False

            case _:
                return "Tente novamente."
    
                
    def tabelao(self):
        table_rows = ['id', 'Título', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma']
        tabela = PrettyTable(table_rows)
        consulta_livros = self.instancia_livraria.pesquisa_todos_os_livros()
        consulta_autores = []
        idlivros = []
        for objeto in consulta_livros:
            idlivros.append(objeto[0])
            tabela.add_row(objeto)
        for id in idlivros:
            consulta_autores.append(self.instancia_livraria.consulta_autores_de_um_livro(id))
        tabela.add_column('Autores', consulta_autores)
        consulta_generos = []
        idlivros2 = []
        for objeto in consulta_livros:
            idlivros2.append(objeto[0])
        for id in idlivros2:
            consulta_generos.append(self.instancia_livraria.consulta_generos_de_um_livro(id))
        tabela.add_column('Gêneros', consulta_generos)

        print(tabela)

    def menu_atualizar(self):
        self.tabelao()
        idlivro = int(input('Escolha o id do livro que deseja atualizar dados: '))
        print('Por qual desses deseja fazer a atualização?\n1: Título\n2: Autor\n3: Gênero\n4: Editora\n5: Preço\n\
              6: Data de publicação\n7: Edição\n8: ISBN\n 9: Volume\n 10: Idioma\n0: Sair')
        escolha = int(input('Digite sua escolha: '))

        match escolha:
            case 1:
                titulo_atualizado = input('Digite o novo nome do título do livro: ')
                self.instancia_livraria.atualiza_titulo_livro(idlivro, titulo_atualizado)
                print("Título atualizado com sucesso!")
                return True
            
            case 2:
                self.atualiza_autor(idlivro)

            case 3:
                self.atualiza_genero(idlivro)

            case 4:
                preco_atualizado = input('Digite o novo nome da editora do livro: ')
                self.instancia_livraria.atualiza_editora_livro(idlivro, preco_atualizado)
                print("Editora atualizada com sucesso!")
                return True                

            case 5:
                preco_atualizado = float(input('Digite o novo preco do livro: '))
                self.instancia_livraria.atualiza_preco_livro(idlivro, preco_atualizado)
                print("Preco atualizado com sucesso!")
                return True

            case 6:
                data_atualizada = input('Digite a nova data de publicação (AAAA-MM-DD) do livro: ')
                self.instancia_livraria.atualiza_data_publicacao_livro(idlivro, data_atualizada)
                print("Data atualizada com sucesso!")
                return True
            
            case 7:
                edicao_atualizada = int(input('Digite a nova edição do livro: '))
                self.instancia_livraria.atualiza_edicao_livro(idlivro, edicao_atualizada)
                print("Edição atualizada com sucesso!")
                return True
            
            case 8:
                isbn_atualizado = input('Digite o isbn do livro: ')
                self.instancia_livraria.atualiza_isbn_livro(idlivro, isbn_atualizado)
                print("ISBN atualizado com sucesso!")
                return True
            
            case 9:
                volume_atualizado = int(input('Digite o novo volume do livro: '))
                self.instancia_livraria.atualiza_volume_livro(idlivro, volume_atualizado)
                print("Volume atualizado com sucesso!")
                return True
            
            case 10:
                idioma_atualizado = input('Digite o novo idioma do livro: ')
                self.instancia_livraria.atualiza_idioma_livro(idlivro, idioma_atualizado)
                print("Edição atualizada com sucesso!")
                return True
            
            case 0:
                return False

    def menu_escolha_consulta(self):
        print('Por qual desses deseja fazer a consulta?\n1: Título\n2: Autor\n3: Gênero\n4: Editora\n0: Voltar')
        escolha = int(input('Digite sua escolha: '))

        match escolha:
            case 1:
                self.consulta_titulo()
                return True
            
            case 2:
                self.consulta_livro_autor()
                return True
            case 3:
                self.consulta_genero()
                return True
            case 4:
                self.consulta_editora()
                return True

            case 0:
                return False
        

    def consulta_titulo(self):
        titulo = (input('Digite o título do livro: '))
        table_rows = ['id', 'Título', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma']
        tabela = PrettyTable(table_rows)
        consulta_livros_nome = self.instancia_livraria.pesquisa_por_titulo(titulo)
        consulta_autores = []
        idlivros = []
        for objeto in consulta_livros_nome:
            idlivros.append(objeto[0])
            tabela.add_row(objeto)
        for id in idlivros:
            consulta_autores.append(self.instancia_livraria.consulta_autores_de_um_livro(id))
        tabela.add_column('Autores', consulta_autores)
        consulta_generos = []
        idlivros2 = []
        for objeto in consulta_livros_nome:
            idlivros2.append(objeto[0])
        for id in idlivros2:
            consulta_generos.append(self.instancia_livraria.consulta_generos_de_um_livro(id))
        tabela.add_column('Gêneros', consulta_generos)
        print(tabela)
        return
    
   # def get_autor(self):
        

    def consulta_editora(self):
        editora = (input('Digite a editora do livro: '))
        table_rows = ['id', 'Título', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma']
        tabela = PrettyTable(table_rows)
        consulta_livros_nome = self.instancia_livraria.pesquisa_por_editora(editora)
        consulta_autores = []
        idlivros = []
        for objeto in consulta_livros_nome:
            idlivros.append(objeto[0])
            tabela.add_row(objeto)
        for id in idlivros:
            consulta_autores.append(self.instancia_livraria.consulta_autores_de_um_livro(id))
        tabela.add_column('Autores', consulta_autores)
        consulta_generos = []
        idlivros2 = []
        for objeto in consulta_livros_nome:
            idlivros2.append(objeto[0])
        for id in idlivros2:
            consulta_generos.append(self.instancia_livraria.consulta_generos_de_um_livro(id))
        tabela.add_column('Gêneros', consulta_generos)
        print(tabela)
        return
    
    def atualiza_autor(self, idlivro):
        autores = self.instancia_livraria.consulta_autores_de_um_livro(idlivro)
        for autor in autores:
            nome_novo = input('Digite o novo nome do autor:')
            self.instancia_livraria.atualiza_nome_autor(nome_novo, autor[0])

    def atualiza_genero(self, idlivro):
        generos = self.instancia_livraria.consulta_generos_de_um_livro(idlivro)
        for genero in generos:
            genero_novo = input("Digite o novo gênero: ")
            self.instancia_livraria.atualiza_nome_genero(genero_novo, genero[0])
            print("Dados atualizados!")

    def consulta_genero(self):
        genero = (input('Digite o gênero do livro: '))
        #print(genero)
        table_rows = ['id', 'Título', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma']
        tabela = PrettyTable(table_rows)

        get_id = self.instancia_livraria.pesquisa_id_genero(genero)
        get_id = get_id[0][0]

        consulta_livros_nome = self.instancia_livraria.pesquisa_por_genero(get_id)
        consulta_autores = []
        idlivros = []
        
        
        for objeto in consulta_livros_nome:
            idlivros.append(objeto[0])
            tabela.add_row(objeto)

        for id in idlivros:
            consulta_autores.append(self.instancia_livraria.consulta_autores_de_um_livro(id))
        tabela.add_column('Autores', consulta_autores)
        consulta_generos = []
        idlivros2 = []
        for objeto in consulta_livros_nome:
            idlivros2.append(objeto[0])
        for id in idlivros2:
            consulta_generos.append(self.instancia_livraria.consulta_generos_de_um_livro(id))
        tabela.add_column('Gêneros', consulta_generos)
        print(tabela)
        return

    def consulta_livro_autor(self):
        autor = (input('Digite o autor do livro: '))
        table_rows = ['id', 'Título', 'Editora', 'Preço', 'Data de publicação', 'Edição', 'ISBN', 'Volume', 'Idioma']
        tabela = PrettyTable(table_rows)

        get_id = self.instancia_livraria.pesquisa_id_autor(autor)
        get_id = get_id[0][0]

        consulta_livros_nome = self.instancia_livraria.pesquisa_por_autor(get_id)
        consulta_autores = []
        idlivros = []
        
        
        for objeto in consulta_livros_nome:
            idlivros.append(objeto[0])
            tabela.add_row(objeto)

        for id in idlivros:
            consulta_autores.append(self.instancia_livraria.consulta_autores_de_um_livro(id))
        tabela.add_column('Autores', consulta_autores)
        consulta_generos = []
        idlivros2 = []
        for objeto in consulta_livros_nome:
            idlivros2.append(objeto[0])
        for id in idlivros2:
            consulta_generos.append(self.instancia_livraria.consulta_generos_de_um_livro(id))
        tabela.add_column('Gêneros', consulta_generos)
        return
        
    def menu_inserir_geral(self):
        while True:
                print("1: Livro\n2: Autor\n3: Gênero\n0: Sair")
                escolha = int(input('Escolha'))


                match escolha:
                    case 1:
                        self.menu_inserir_livro()
                        return True
                        

                    case 2:
                        self.menu_inserir_autor()
                        return True                

                    case 3:
                        self.menu_inserir_genero()
                        return True

                    case 0:
                        return False

    def menu_inserir_autor(self):
            
            condicao = False
            consulta_autores = self.instancia_livraria.pesquisa_todos_os_autores()
            id_autor_novo = 0

            input_autor = input("Digite o nome do autor: ")

            if any(input_autor in tupla for _, tupla in consulta_autores):
                condicao = False
            elif not any(input_autor in tupla for _, tupla in consulta_autores) and input_autor != '00000':
                condicao = True
                self.instancia_livraria.insere_autor(input_autor)
                id_autor_novo = self.instancia_livraria.cursor.lastrowid
                
            elif input_autor == '00000':
                condicao = False

            while condicao == True:
                
                escolha = input('Existe algum livro relacionado a esse autor na base dados? ')
                if escolha == 'sim' or escolha == 'Sim':
                    self.tabelao()
                    id_livro_relacionado = input('Digite o id do livro: ')
                    self.instancia_livraria.insere_livro_autores(id_livro_relacionado, id_autor_novo)
                if escolha == 'não' or escolha == 'Não':
                    break

    def menu_inserir_genero(self):

            condicao = False
            consulta_generos = self.instancia_livraria.pesquisa_todos_os_generos()
            id_genero_novo = 0

            input_genero = input("Digite o gênero do livro: ")

            if any(input_genero in tupla for _, tupla in consulta_generos):
                condicao = False
            elif not any(input_genero in tupla for _, tupla in consulta_generos) and input_genero != '00000':
                condicao = True
                self.instancia_livraria.insere_genero(input_genero)
                id_genero_novo = self.instancia_livraria.cursor.lastrowid
                
            elif input_genero == '00000':
                condicao = False

            while condicao == True:
                
                escolha = input('Existe algum livro relacionado a esse gênero na base de dados? ')
                if escolha == 'sim' or escolha == 'Sim':
                    self.tabelao()
                    id_livro_relacionado = input('Digite o id do livro: ')
                    self.instancia_livraria.insere_livro_genero(id_livro_relacionado, id_genero_novo)
                    print("Inserido com sucesso!")
                if escolha == 'não' or escolha == 'Não':
                    break




    def menu_inserir_livro(self):
        while True:
            try:
                titulo = input('Título: ')
                
                autores = []
                autores_existentes = []
                consulta_autores = self.instancia_livraria.pesquisa_todos_os_autores()
                while True:
                    input_autor = input('Autor: ')
                    if any(input_autor in tupla for _, tupla in consulta_autores):
                        autores_existentes.append(input_autor)
                    elif not any(input_autor in tupla for _, tupla in consulta_autores) and input_autor != '00000':
                        autores.append(input_autor)
                    elif input_autor == '00000':
                        break
                
                if not titulo.strip():
                    raise ValueError("Título não pode ser vazios.")
                
                genero = []
                generos_existentes = []
                consulta_generos = self.instancia_livraria.pesquisa_todos_os_generos()
                while True:
                    input_genero = input('Genero: ')
                    if any(input_genero in tupla for _, tupla in consulta_generos):
                        generos_existentes.append(input_genero)
                    elif not any(input_genero in tupla for _, tupla in consulta_generos) and input_genero != '00000':
                        genero.append(input_genero)
                    elif input_genero == '00000':
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
                
                if self.checa_isbn(isbn) == False:
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

                self.instancia_livro_autor_genero(autores, novo_livro, genero, autores_existentes, generos_existentes)

                print('Livro inserido com sucesso!')

                return
            
            except ValueError as e:
                # Captura exceções ValueError quando as entradas são inválidas
                print(f"Erro: {e}")
                print("Por favor, forneça entradas válidas.")
         

                # solicita as informações do livro:
               

    def menu_remocoes(self):
                # solicita as informações do livro:
                self.tabelao()

                print('O que deseja remover?\n1: Livro\n2: Autor\n3: Gênero\n0: Sair')
                
                escolha = int(input('Digite sua escolha: '))


                match escolha:
                    case 1:
                        idlivro = input('Digite o nome do id do livro: ')
                        self.instancia_livraria.remove_livro_(idlivro)
                        print("Título removido com sucesso!")
                        return True
                        

                    case 2:
                        autor = input('Digite o nome do autor do livro: ')
                        idautor = self.instancia_livraria.pesquisa_id_autor(autor)
                        self.instancia_livraria.remove_autor(idautor[0][0])
                        print("Autor removido com sucesso!")
                        return True                

                    case 3:
                        genero = input('Digite o nome do gênero do livro: ')
                        idgenero = self.instancia_livraria.pesquisa_id_genero(genero)
                        self.instancia_livraria.remove_genero(idgenero[0][0])
                        print("Gênero removido com sucesso!")
                        return True

                    case 0:
                        return False





    @staticmethod
    def verifica_isbn_10(isbn):
        soma = 0
        for i in range(1, len(isbn) + 1):
            soma = soma + int (isbn[i-1])* i
        return soma % 11 == 0

    @staticmethod
    def verifica_isbn_13(isbn):
        soma = (sum(int(caractere) for caractere in isbn[::2]) + sum(int(caractere) * 3 for caractere in isbn[1::2]))
        return soma % 10 == 0
    
    def checa_isbn(self, isbn):
        validacao = False
        isbn = isbn.replace('-', '').replace(' ', '')
        if len(isbn) == 10:
            validacao = self.verifica_isbn_10(isbn)

        elif len(isbn) == 13:
            validacao = self.verifica_isbn_13(isbn)
        
        else:
            print('O ISBN não pode ter menos de 10 ou 13 dígitos.')
        
        return validacao
    
    def instancia_livro_autor_genero(self, autores, livro, generos, autores_existentes, generos_existentes):
        self.instancia_livraria.inserir_livros(livro)
        idLivro = self.instancia_livraria.cursor.lastrowid
        for autor in autores:
            self.instancia_livraria.insere_autor(autor)
            idAutor = self.instancia_livraria.cursor.lastrowid
            self.instancia_livraria.insere_livro_autores(idLivro, idAutor)
        for autor in autores_existentes:
            idAutor = self.instancia_livraria.pesquisa_id_autor(autor)
            self.instancia_livraria.insere_livro_autores(idLivro, idAutor[0][0])
        for genero in generos:
            self.instancia_livraria.insere_genero(genero)
            idGenero = self.instancia_livraria.cursor.lastrowid
            self.instancia_livraria.insere_livro_genero(idLivro, idGenero)
        for genero in generos_existentes:
            idGenero = self.instancia_livraria.pesquisa_id_genero(genero)
            self.instancia_livraria.insere_livro_genero(idLivro, idGenero[0][0])
    
menu = Menu()
menu.tabelao()
menu.menu()