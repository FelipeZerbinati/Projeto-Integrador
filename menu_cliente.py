import functions, menu_adm as adm

def client_screen():
    print("**************************************")
    print("| 1. VER PRODUTOS | 2. COMPRAR |")
    print("**************************************")

def mostrar_produtos():
    for prod in adm.produtos:
        print("PRODUTO: {0}, QUANTIDADE: {1}, PREÇO: R$ {2:.2f}".format(prod['produto'], prod['quantidade'], prod['preco']))

def comprar_produto():
    for prod in adm.produtos:
        print("PRODUTO: {0}, QUANTIDADE: {1}, PREÇO: R$ {2:.2f}".format(prod['produto'], prod['quantidade'],prod['preco']))
    esc = input("Que produto deseja comprar?").upper()
    for prod in adm.produtos:
        if esc == prod['produto']:
            qntd = input("Qual a quantidade que deseja comprar? ")
            if functions.checagem_numero(qntd):
                qntd = float(qntd)
                if prod['quantidade'] >= qntd:
                    preco_compra = prod['preco'] * qntd
                    confirmar_compra = input("Deseja comprar {0:.0f} unidades do produto {1} por R$ {2:.2f}?".format(qntd, prod['produto'], preco_compra)).upper()
                    if confirmar_compra == 'SIM':
                            prod['quantidade'] -= qntd
                    elif confirmar_compra == 'NAO':
                        print("CANCELANDO SUA COMPRA...")
                    else:
                        print("ERRO, OPÇÃO INVÁLIDA.")
                else:
                    print("Não temos estoque suficiente para sua compra.")

def client_menu():
    client_screen()
    esc = input("DIGITE O QUE DESEJA FAZER: ")
    if functions.checagem_numero(esc):
        if esc == '1':
            mostrar_produtos()
        elif esc == '2':
            comprar_produto()
client_menu()