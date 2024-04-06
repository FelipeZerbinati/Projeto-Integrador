import functions
import menu_adm as adm
import menu_cliente as clt

db = [{'nome': 'admin', 'senha': 'admin', 'adm_priveleges': 'sim'},
      {'nome': 'marcelo', 'senha': '02072004', 'adm_priveleges': 'nao'}]

def menu_logcad():
    while True:
        print("**************************************************************************************************")
        print("\t\t\t\t    | 1. LOGIN | 2. CADASTRO | 3. FECHAR |")
        print("**************************************************************************************************")

        escolha = input("ESCOLHA UMA OPÇÃO: ")
        if functions.checagem_numero(escolha):
            if escolha == '1':
                if login():
                    return
            elif escolha == '2':
                cadastro()
            elif escolha == '3':
                print("FINALIZANDO PROGRAMA...")
                break
            else:
                print("ESCOLHA INVÁLIDA!")

def cadastro():
    user_input = input("DIGITE O NOME DE USUÁRIO: ")
    pswd_input = input("DIGITE SUA SENHA: ")

    for pessoa in db:
        if pessoa['nome'] == user_input:
            print("NOME DE USUÁRIO JÁ ESTÁ EM USO. TENTE NOVAMENTE!")
            return

    cad = {'nome': user_input, 'senha': pswd_input, 'adm_priveleges': 'nao'}
    db.append(cad)
    print("CADASTRADO COM SUCESSO!")

def login():
    user_input = input('DIGITE O NOME DE USUÁRIO: ')
    pswd_input = input('DIGITE SUA SENHA: ')

    for pessoa in db:
        if pessoa['nome'] == user_input and pessoa['senha'] == pswd_input:
            if pessoa['adm_priveleges'] == 'sim':
                print("LOGIN FEITO COM SUCESSO!")
                adm.main_menu()
            else:
                print("LOGIN FEITO COM SUCESSO!")
                clt.client_menu()
            return True

    print("NOME DE USUÁRIO E/OU SENHA INVÁLIDOS. TENTE NOVAMENTE!")
    return False

menu_logcad()
