
# importando bibliotecas
import os

# Criando listas de restaurantes com python
restaurantes = [
                {'nome': 'Praça', 'categoria':'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria':'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria':'Italiana ', 'ativo': False}
]

def exibir_nome_do_programa(): 
    print(""" 
    
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar Novo Restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)

    print(f'O resutarante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_princial()

def listar_restaurantes():
    exibir_subtitulo('Listando os Restaurantes Cadastrados')


    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']

        print(f' - {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_princial()


def exibir_opcoes():
    print('1. Cadastrar Restaurante \n')
    print('2. Listar Restaurante \n')
    print('3. Ativar Restaurante \n')
    print('4. Sair \n')


def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_princial()

def escolher_opcao():
    try:
        # Declarando variaveis
        opcao_escolhida = int(input('Escolha uma opção: '))
        # print('Você escolheu a opção', opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            print('Ativar Restaurante')

        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
def voltar_ao_menu_princial():
    input('\nDigite uma tecla para voltar ao menu')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    
# Utilizando interpolação no python
#  print(f'Você escolheu a opção {opcao_escolhida}')

# Criando funções em python
def finalizar_app():
    exibir_subtitulo('Finaizando o Programa')


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
     


if __name__ == '__main__':
    main()




