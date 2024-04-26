import functions

from conexao import db_produtos, db_usuario, fechar_conexao


conexao_produtos = db_produtos()
conexao_usuarios = db_usuario()

def mais_operacao():
    opc = input("DESEJA FAZER MAIS ALGUMA OPERAÇÃO? [S/N] ").upper()
    if opc == "S":
        client_menu()
    elif opc == "N":
        print("FINALIZANDO PROGRAMA...")
        functions.visualizar_tela()
    else:
        print("ERRO, OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
        mais_operacao()


def client_screen():
    functions.limpar_tela()
    print("**********************************")
    print("             | MENU |             ")
    print("**********************************")
    print("| 1. VER PRODUTOS NO ESTOQUE")
    print("| 2. COMPRAR")
    print("| 3. LOGOUT\n")


def mostrar_produtos(conexao):
    try:
        functions.limpar_tela()
        print("********************************************")
        print("                  PRODUTOS                  ")
        print("********************************************")
        
        with conexao.cursor() as cursor:
            cursor.execute("SELECT Nome, Quantidade, Preco_venda, Descricao FROM Produto")
            produtos = cursor.fetchall()

            for nome, quantidade, preco_venda, descricao in produtos:
                print(f"DEBUG: Produto: {nome}, Quantidade: {quantidade}, Preço: {preco_venda}, Descrição: {descricao}")
                if quantidade is not None and quantidade > 0:
                    print(f"PRODUTO: {nome}, DESCRIÇÃO: {descricao}, QUANTIDADE: {quantidade}, PREÇO: R$ {preco_venda:.2f}")
                else:
                    print(f"PRODUTO: {nome} - ESGOTADO")
                    
        functions.visualizar_tela()
        client_menu()
        
    except Exception as e:
        print(f"ERRO AO MOSTRAR PRODUTOS: {str(e)}")


def comprar_produto(conexao):
    try:
        print("********************************************")
        print("                  COMPRAR                   ")
        print("********************************************")
        
        with conexao.cursor() as cursor:
            cursor.execute("SELECT Nome, Quantidade, Preco_venda, Descricao FROM Produto")
            produtos = cursor.fetchall()
            
            produtos_disponiveis = []
            for nome, quantidade, preco_venda, descricao in produtos:
                if quantidade is not None and quantidade > 0:
                    produtos_disponiveis.append((nome, quantidade, preco_venda, descricao))
                else:
                    produtos_disponiveis.append((nome, "ESGOTADO", preco_venda, descricao))
            
            if produtos_disponiveis:
                print("PRODUTOS DISPONÍVEIS PARA COMPRA:")
                for produto in produtos_disponiveis:
                    nome, quantidade, preco_venda, descricao = produto
                    if quantidade != "ESGOTADO":
                        print(f"PRODUTO: {nome}, DESCRIÇÃO: {descricao}, QUANTIDADE: {quantidade}, PREÇO: R$ {preco_venda:.2f}")
                    else:
                        print(f"PRODUTO: {nome} - {quantidade}")
                
                esc = input("QUAL PRODUTO DESEJA COMPRAR? ")

                for produto in produtos_disponiveis:
                    if esc == produto[0]:
                        if produto[1] != "ESGOTADO":
                            qntd = input("QUAL A QUANTIDADE QUE DESEJA COMPRAR? ")
                            if functions.checagem_numero(qntd):
                                qntd = int(qntd)
                                if produto[1] >= qntd:
                                    preco_compra = produto[2] * qntd
                                    confirmar_compra = input(
                                        f"DESEJA COMPRAR {qntd} UNIDADES DO PRODUTO {esc} POR R$ {preco_compra:.2f}? ").upper()
                                    if confirmar_compra == 'SIM':
                                        with conexao.cursor() as cursor:
                                            cursor.execute("UPDATE Produto SET Quantidade = Quantidade - :1 WHERE Nome = :2",
                                                           (qntd, esc))
                                            conexao.commit()
                                        print("COMPRA REALIZADA COM SUCESSO!")
                                        mais_operacao()
                                    elif confirmar_compra == 'NAO':
                                        print("CANCELANDO SUA COMPRA...")
                                        mais_operacao()
                                    else:
                                        print("OPÇÃO INVÁLIDA!")
                                        mais_operacao()
                                else:
                                    print("NÃO TEMOS ESTOQUE SUFICIENTE PARA SUA COMPRA.")
                                    mais_operacao()
                        else:
                            print("ESTE PRODUTO ESTÁ ESGOTADO. POR FAVOR, ESCOLHA OUTRO.")
                            mais_operacao()
            else:
                print("NENHUM PRODUTO DISPONÍVEL PARA COMPRA NO MOMENTO.")
                mais_operacao()
    except Exception as e:
        print(f"ERRO AO REALIZAR A COMPRA: {str(e)}")


def client_menu():
    while True:
        functions.limpar_tela()
        client_screen()
        esc = input("DIGITE O QUE DESEJA FAZER: ")
        match esc:
            case '1':
                mostrar_produtos(conexao_produtos)
                break
            case '2':
                comprar_produto(conexao_produtos)
                break
            case '3':
                print("FINALIZANDO SESSÃO...")
                functions.visualizar_tela()
                fechar_conexao(conexao_produtos, conexao_usuarios)
                break
            case _:
                print("OPÇÃO INVÁLIDA")
