#Importando bibliotecas
import os

#Usando dicionários e listas
restaurantes = [{"nome": "Praça", "categoria": "Japonesa", "ativo" : False}, {"nome": "Pizza Suprema", "categoria": "Pizza", "ativo" : True}, {"nome": "Cantina Italiana", "categoria": "Italiano", "ativo" : False}]


#Função para exibir o nome do programa (título do programa extraído do fsymbols)
def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")



#Função para exibir as opções do app
def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estados de restaurante")
    print("4. Sair\n")



#Função para finalizar o app
def finalizar_app():
    exibir_subtitulo("Finalizando o app")


#Verificando a validade das opções escolhidas
def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()



#Voltando para o menu principal
def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal")
    main()



#Exibindo os subtítulos referentes a cada funcionalidade do programa
def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha) 
    print(texto)
    print(linha)
    print()


#Cadastrando restaurantes
def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de restaurantes")

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')

    #Dicionário com os dados dos restaurantes
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()



#Listando restaurantes com o laço de repetição for
def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes cadastrados: ")
    
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"} ')
    for restaurante in restaurantes:
        #Pegando informações dos dicionários
        nome_restaurante = restaurante["nome"]

        categoria = restaurante["categoria"] 

        ativo = "Ativado" if restaurante["ativo"] else "Desativado"

        print(f".{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

#Função para ativar e desativar restaurantes
def alternar_estado_do_restaurante():
    exibir_subtitulo("Alternando o estado do restaurante\n")

    voltar_ao_menu_principal()

    nome_restaurante = input("Digite o nome do restaurante a partir do qual deseja alterar o estado: ")

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True

            restaurante["ativo"] = not restaurante ["ativo"]

            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"

            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante informado não foi encontrado!")

            

#Função com as opções a serem escolhidas
def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        #print(type(opcao_escolhida))

        #Verificando as opções escolhidas em estruturas comdicionais
        if(opcao_escolhida == 1):
            cadastrar_novo_restaurante()


        elif(opcao_escolhida == 2):
            listar_restaurantes()


        elif(opcao_escolhida == 3):
            alternar_estado_do_restaurante()
        

        elif(opcao_escolhida == 4):
            finalizar_app()


        else:
            opcao_invalida()

    except:
        opcao_invalida
            



#Definindo este arquivo .py como principal
def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()

