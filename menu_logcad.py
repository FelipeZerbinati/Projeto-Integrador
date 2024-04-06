import functions
import menu_adm as adm
import menu_cliente as clt

continuar = True

db = [{'nome': 'admin', 'senha': 'admin', 'adm_priveleges': 'sim'}]


def menu_logcad():
    while continuar:
        print("**************************************************************************************************")
        print("\t\t\t\t    | 1. LOGIN | 2. CADASTRO |")
        print("**************************************************************************************************")

        escolha = input("ESCOLHA UMA OPÇÃO: ")
        if functions.checagem_numero(escolha):
            if escolha == '1':
                login()
                break
            elif escolha == '2':
                cadastro()
                break
            else:
                print("ESCOLHA INVÁLIDA!")


def cadastro():
    user_input = input("DIGITE O NOME DE USUÁRIO: ")
    pswd_input = input("DIGITE SUA SENHA: ")
    for pessoa in db:
        if pessoa['nome'] == user_input:
            print("NOME DE USUÁRIO JÁ ESTÁ EM USO.")
            menu_logcad()
            return

    cad = {'nome': user_input, 'senha': pswd_input, 'adm_priveleges': 'nao'}
    db.append(cad)
    print("CADASTRADO COM SUCESSO!")
    menu_logcad()

def login():
    user_input = input('DIGITE O NOME DE USUÁRIO: ')
    pswd_input = input('DIGITE SUA SENHA: ')
    for pessoa in db:
        if pessoa['nome'] == user_input and pessoa['senha'] == pswd_input:
            if pessoa['adm_priveleges'] == 'sim':
                adm.main_menu()
            print("LOGIN FEITO COM SUCESSO!")
            functions.limpar_tela()
            clt.client_menu()
            return
    print("NOME DE USUÁRIO E/OU SENHA INVÁLIDOS.")
    menu_logcad()

menu_logcad()
