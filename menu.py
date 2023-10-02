from classes import Livros, GerenciaLivraria
#import requests

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
            case 4:
                print('-------------------------------------------')
            case 0:
                return False

            case _:
                return "Tente novamente."

    
    def menu_inserir(self):
        print('Insira abaixo as informações do livro: ')

        while True:
            try:
                # solicita as informações do livro:

                titulo = input('Título: ')
                autor = input('Autor: ')

                if not titulo.strip() or not autor.strip():
                    raise ValueError("Título e autor não podem ser vazios.")

                genero = input('Gênero: ')
                editora = input('Editora: ')

                preco = float(input('Preço: '))
                if preco < 0:
                    raise ValueError("o preço não pode ser um número negativo.")

                data_publicacao = input('Data de Publicação (AAAA-MM-DD): ')
                
                edicao = int(input('Edição: '))
                if edicao <= 0:
                    raise ValueError("o livro deve ter pelo menos uma edição.")
                

                isbn = input('ISBN: ')
                
                volume = int(input('Volume: '))
                if volume < 0:
                    raise ValueError("o volume não pode ser um número negativo. Digite 0 caso não haja volume.")
               
                idioma = input('Idioma: ')


                # tratamento de erros:

                if preco < 0:
                    raise ValueError("O preço não pode ser um número negativo.")
                
                if volume < 0:
                    raise ValueError("O volume não pode ser um número negativo. Digite 0 caso não haja volume.")
                
                if edicao <= 0:
                    raise ValueError("O livro deve ter pelo menos uma edição.")
                
                if self.checa_isbn() == False:
                    raise ValueError("O isbn deve ser inserido corretamente.")
                

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
            
                self.instancia_livraria.inserir_livros(novo_livro)


            
                print('Livro inserido com sucesso!')

                return
            

            except ValueError as e:
                # Captura exceções ValueError quando as entradas são inválidas
                print(f"Erro: {e}")
                print("Por favor, forneça entradas válidas.")


    def verifica_isbn_10(isbn):
        soma = 0
        for i in range(1, len(isbn) + 1):
            soma = soma + int (isbn[i-1])* i
        if soma % 11 == 0:
            return True
        else:
            return False

    def verifica_isbn_13(isbn):
        soma = (sum(int(isbn) for caractere in isbn[::2]) + sum(int(isbn) * 3 for caractere in isbn[1::2]))
        return soma % 10 == 0
    
    def checa_isbn(isbn, self):
        isbn = isbn.replace('-', '').replace(' ', '')
        if len(isbn) == 10:
            validacao = self.verifica_isbn_10(isbn)

        if len(isbn) == 13:
            validacao = self.verifica_isbn_13(isbn)
        else:
            print('O ISBN não pode ter menos de 10 ou 13 dígitos.')
        
        if validacao == True:
            print('ISBN válido!')
        else:
            print('ISBN não é válido. Tente novamente')

menu = Menu()
menu.menu()