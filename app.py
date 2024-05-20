
# importando bibliotecas
import os

# Criando listas de restaurantes com python
restaurantes = []

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
    os.system('cls')
    print('Cadastro de novo restaurantes\n')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    restaurantes.append(nome_do_restaurante)

    print(f'O resutarante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def exibir_opcoes():
    print('1. Cadastrar Restaurante \n')
    print('2. Listar Restaurante \n')
    print('3. Ativar Restaurante \n')
    print('4. Sair \n')


def opcao_invalida():
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        # Declarando variaveis
        opcao_escolhida = int(input('Escolha uma opção: '))
        # print('Você escolheu a opção', opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            print('Listar Restaurante')

        elif opcao_escolhida == 3:
            print('Ativar Restaurante')

        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
# Utilizando interpolação no python
#  print(f'Você escolheu a opção {opcao_escolhida}')

# Criando funções em python
def finalizar_app():
    os.system('cls')
    print('Finalizando o app')


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
     


if __name__ == '__main__':
    main()




