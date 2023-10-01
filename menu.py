from classes import Livros, GerenciaLivraria

class Menu:
    def __init__(self):
        self.livro = None
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
                Menu.menu_inserir()

            case 2:
                print('-------------------------------------------')
            case 3:
                print('-------------------------------------------')
            case 4:
                print('-------------------------------------------')
            case 0:
                return False

            case _:
                return "Tente novamente."

    
    def menu_inserir(self):
        print('Insira abaixo as informações do livro: ')

    
        # solicita as informações do livro:

        titulo = input('Título: ')
        autor = input('Autor: ')
        genero = input('Gênero: ')
        editora = input('Editora: ')
        preco = float(input('Preço: '))
        data_publicacao = input('Data de Publicação (AAAA-MM-DD): ')
        edicao = input('Edição: ')
        isbn = input('ISBN: ')
        volume = int(input('Volume: '))
        idioma = input('Idioma: ')

        novo_livro = Livros(
        titulo,
        autor,
        genero,
        editora,
        preco,
        data_publicacao,
        edicao,
        isbn,
        volume,
        idioma
        )
    
        # Chame o método criar_livro() para inserir o livro no banco de dados
        self.instancia_livraria.inserir_livros(novo_livro)


    
        print('Livro inserido com sucesso!')

        return


    def checa_isbn(isbn):
        if (len(isbn) < 13 or len(isbn) > 13):
            print('A quantidade de caracteres está errada. Tente novamente')
            return False
        soma = 0
        for i in range(0, len(isbn) - 1):
            if(i % 2 != 0):
                soma = soma + int (isbn[i])
            else:
                soma = soma + 3 * int (isbn[i])
        multiplo10Soma = soma
        while multiplo10Soma % 10 != 0:
            multiplo10Soma = multiplo10Soma + 1
        if multiplo10Soma - soma == int (isbn[12]):
            print('Sucesso!')
            return True
        else:
            print('ISBN inválido. Tente novamente')
            return False
        
menu = Menu()
menu.menu()