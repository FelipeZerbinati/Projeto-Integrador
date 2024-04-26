import functions
import menu_adm as adm
import menu_cliente as clt

from conexao import db_usuario, fechar_conexao


conexao_usuario = db_usuario()


def menu_logcad():
    functions.limpar_tela()
    while True:
        print("**********************************")
        print("             | MENU |             ")
        print("**********************************")
        print("| 1. LOGIN")
        print("| 2. CADASTRO")
        print("| 3. SAIR\n")
        escolha = input("ESCOLHA UMA OPÇÃO: ")

        match escolha:
            case '1':
                functions.limpar_tela()
                login(conexao_usuario)
            case '2':
                functions.limpar_tela()
                cadastrar(conexao_usuario)
            case '3':

                print("FINALIZANDO PROGRAMA...")
                fechar_conexao(conexao_usuario)
                functions.visualizar_tela()
                break
            case _:
                print("ERROR!! OPÇÃO INVÁLIDA!!")




def cadastrar(conexao):
    try:
        cursor = conexao.cursor()
        
        print("**********************************")
        print("           | CADASTRO |           ")
        print("**********************************\n")
        
        nome_usuario = input("DIGITE O NOME DE USUÁRIO: ")
        senha = input("DIGITE A SENHA: ")
        email = input("DIGITE O EMAIL: ")
        num_telefone = input("DIGITE O NÚMERO DE TELEFONE: ")
        
        cursor.execute("SELECT COUNT(*) FROM CADASTRO WHERE EMAIL = :1 OR NUM_TELEFONE = :2",
                       (email, num_telefone))
        resultado = cursor.fetchone()
        if resultado[0] > 0:
            print("O E-MAIL ou NÚMERO DE TELEFONE JÁ FORAM CADASTRADOS EM OUTRO USUÁRIO.")
            return
        
        cursor.execute(f"INSERT INTO CADASTRO (NOME_USUARIO, SENHA, EMAIL, NUM_TELEFONE, ADMINISTRADOR) "
                       f"VALUES (:1, :2, :3, :4, 'NAO')",
                       (nome_usuario, senha, email, num_telefone))
        
        conexao.commit()
        print("USUÁRIO CADASTRADO COM SUCESSO!")
        
    except Exception as e:
        print("ERRO AO CADASTRAR USUÁRIO:", e)
    finally:
        cursor.close()



def login(conexao):
    global cursor
    functions.limpar_tela()
            
    print("***********************************")
    print("             | LOGIN |             ")
    print("***********************************\n")
    user_input = input('DIGITE O NOME DE USUÁRIO: ')
    pswd_input = input('DIGITE SUA SENHA: ')

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT administrador FROM CADASTRO WHERE nome_usuario = :1 AND senha = :2",
                       (user_input, pswd_input))
        resultado = cursor.fetchone()
        if resultado:
            administrador = resultado[0]
            if administrador == 'sim':
                print("LOGIN FEITO COM SUCESSO!")
                functions.visualizar_tela()
                adm.main_menu()
                return True
            else:
                print("LOGIN FEITO COM SUCESSO!")
                functions.visualizar_tela()
                clt.client_menu()
                return True
        else:
            print("NOME DE USUÁRIO OU SENHA INCORRETOS.")
            return False
    except Exception as error:
        print("ERRO AO REALIZAR LOGIN:", error)
    finally:
        cursor.close()



menu_logcad()
