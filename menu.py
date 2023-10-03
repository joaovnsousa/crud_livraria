from classes import Livros, GerenciaLivraria

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
                self.menu_inserir()
                return True

            case 2:
                print('-------------------------------------------')
            case 3:
                print('-------------------------------------------')
                
                self.menu_escolha_consulta()
                return True

            case 4:
                print('-------------------------------------------')
            case 0:
                return False

            case _:
                return "Tente novamente."
             
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

        self.instancia_livraria.pesquisa_por_titulo(titulo)
        return
    
   # def get_autor(self):
        

    def consulta_editora(self):
        editora = (input('Digite o nome da editora: '))

        livros_obj = self.instancia_livraria.pesquisa_por_editora(editora)

        #idAutor = self.instancia_livraria.pesquisa_id_autor(editora)
        #idAutor = idAutor[0][0]
        self.printa_consulta(livros_obj, editora)
        
    def consulta_genero(self):
        genero = (input('Digite o gênero do livro: '))

        idGenero = self.instancia_livraria.pesquisa_id_genero(genero)
        idGenero = idGenero[0][0]

        idAutor = self.instancia_livraria.pesquisa_id_autor(genero)
        idAutor = idAutor[0][0]

        livro_obj = self.instancia_livraria.pesquisa_por_genero(idAutor)
        self.printa_consulta(livro_obj, genero)

        return
        
    def consulta_livro_autor(self):
        autor = (input('Digite o autor do livro: '))
        consulta_autores = self.instancia_livraria.pesquisa_todos_os_autores()
        if (any(autor in tupla for _, tupla in consulta_autores) == False):
            print('Esse autor não existe na base de dados!')
            return
        print('a')
        idAutor = self.instancia_livraria.pesquisa_id_autor(autor)
        idAutor = idAutor[0][0]
        print('b')
        livros_obj = self.instancia_livraria.consulta_livros_de_um_autor(idAutor)
        print('c')
        self.printa_consulta(livros_obj, autor, 1)


    def menu_inserir(self):
        print('Insira abaixo as informações do livro: ')

        while True:
            try:
                # solicita as informações do livro:

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
                
                print(autores)
                print(autores_existentes)
                
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
            
    def printa_consulta(self, livros_obj, parametro, inteiro):
        print('---------------------------------------------------------------------------------------------------------------------------')
        if inteiro == 1:
            for i in range (0, len(livros_obj)):
                print(f'id: {livros_obj[i][0]} |Título: {livros_obj[i][1]}| Autor: {parametro} | Gênero:  Editora: {livros_obj[i][2]} | Preço: R${livros_obj[i][3]} | Data de Publicação: {livros_obj[i][4]} | Edição: {livros_obj[i][5]}| ISBN: {livros_obj[i][6]}| Volume: {livros_obj[i][7]} | Idioma: {livros_obj[i][8]}')
                print('---------------------------------------------------------------------------------------------------------------------------')
        if inteiro == 2:
            for i in range (0, len(livros_obj)):
                print(f'id: {livros_obj[i][0]} |Título: {livros_obj[i][1]}| Autor: |Gênero: {parametro} Editora: {livros_obj[i][2]} | Preço: R${livros_obj[i][3]} | Data de Publicação: {livros_obj[i][4]} | Edição: {livros_obj[i][5]}| ISBN: {livros_obj[i][6]}| Volume: {livros_obj[i][7]} | Idioma: {livros_obj[i][8]}')
                print('---------------------------------------------------------------------------------------------------------------------------')


                

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
print(menu.instancia_livraria.consulta_geral())
menu.menu()