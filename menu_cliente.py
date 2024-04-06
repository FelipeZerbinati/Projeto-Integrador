import functions
import menu_adm as adm


def mais_opercao():
    opc = input("DESEJA FAZER MAIS ALGUMA OPERAÇÃO? [S/N] ").upper()
    if opc == "S":
        client_menu()
    elif opc == "N":
        print("FINALIZANDO PROGRAMA...")
        functions.visualizar_tela()
    else:
        print("ERROR, OPÇAO INVALIDA! TENTE NOVAMENTE.")
        mais_opercao()


def client_screen():
    print("******************************************")
    print("| 1. VER PRODUTOS | 2. COMPRAR | 3. LOGOUT |")
    print("******************************************")


def mostrar_produtos():
    for prod in adm.produtos:
        print("PRODUTO: {0}, QUANTIDADE: {1}, PREÇO: R$ {2:.2f}".format(prod['produto'], prod['quantidade'],
                                                                        prod['preco']))
    functions.visualizar_tela()
    client_menu()


def comprar_produto():
    for prod in adm.produtos:
        print("PRODUTO: {0}, QUANTIDADE: {1:.0f}, PREÇO: R$ {2:.2f}".format(prod['produto'], prod['quantidade'],
                                                                            prod['preco']))
    esc = input("Que produto deseja comprar?").upper()
    for prod in adm.produtos:
        if esc == prod['produto']:
            qntd = input("Qual a quantidade que deseja comprar? ")
            if functions.checagem_numero(qntd):
                qntd = int(qntd)
                if prod['quantidade'] >= qntd:
                    preco_compra = prod['preco'] * qntd
                    confirmar_compra = input(
                        "Deseja comprar {0:.0f} unidades do produto {1} por R$ {2:.2f}?".format(qntd, prod['produto'],
                                                                                                preco_compra)).upper()
                    if confirmar_compra == 'SIM':
                        prod['quantidade'] -= qntd
                        print("COMPRA REALIZADA COM SUCESSO!")
                        functions.visualizar_tela()
                        mais_opercao()
                    elif confirmar_compra == 'NAO':
                        print("CANCELANDO SUA COMPRA...")
                        functions.visualizar_tela()
                        mais_opercao()

                    else:
                        print("ERRO, OPÇÃO INVÁLIDA.")
                        functions.visualizar_tela()
                        mais_opercao()
                else:
                    print("Não temos estoque suficiente para sua compra.")
                    functions.visualizar_tela()
                    mais_opercao()


def client_menu():
    while True:
        functions.limpar_tela()
        client_screen()
        esc = input("DIGITE O QUE DESEJA FAZER: ")
        if functions.checagem_numero(esc):
            if esc == '1':
                mostrar_produtos()
            elif esc == '2':
                comprar_produto()
            elif esc == '3':
                print("FINALIZANDO SESSÃO...")
                functions.visualizar_tela()

                break
            else:
                print("OPÇÃO INVÁLIDA")
