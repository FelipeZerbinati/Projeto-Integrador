import functions
continuar = True

user = ['admin']
pswd = ['admin']
def cadastro():
    user_input = input("DIGITE O NOME DE USUÁRIO: ")
    pswd_input = input("DIGITE SUA SENHA: ")
    if(user_input not in user):
        user.append(user_input)
        pswd.append(pswd_input)
        print("CADASTRADO COM SUCESSO!")
        
    else:
        print("NOME DE USUÁRIO JÁ ESTÁ EM USO.")

def login():
    user_input = input('DIGITE O NOME DE USUÁRIO: ')
    pswd_input = input('DIGITE SUA SENHA: ')
    if(user_input in user):
        if(pswd_input in pswd):
            print("LOGIN FEITO COM SUCESSO!")
            
        else:
            print("NOME DE USUÁRIO E/OU SENHA INVÁLIDOS.")   
    else:
        print("NOME DE USUÁRIO E/OU SENHA INVÁLIDOS.")

  
while(continuar):
    print("**************************************************************************************************")
    print("\t\t\t\t    | 1. LOGIN | 2. CADASTRO |")
    print("**************************************************************************************************")

    escolha = input("ESCOLHA UMA OPÇÃO: ")
    if(functions.checagem_numero(escolha)):
        if(escolha == '1'):
            login()
            
        elif(escolha == '2'):
            cadastro()
        else:
            print("ESCOLHA INVÁLIDA!")
        