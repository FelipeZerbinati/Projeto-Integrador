import functions

# UTILIZANDO LISTA E DICIONÁRIOS ENQUANTO NÃO CONSEGUIMOS INTEGRAR O BANCO DE DADOS

produtos = [{'produto': 'PAO BURGUER', 'quantidade': 24, 'preco': 6.4},
            {'produto': 'PAO FRANCES', 'quantidade': 20, 'preco': 0.2},
            {'produto': 'CAPUCCINO', 'quantidade': 20, 'preco': 10.53}]


# TELA DE CADASTRO DE PRODUTOS
def tela_cadastro():
    print("**************************************************************************************************")
    print("\t\t\t\t\tCADASTRO DE PRODUTOS")
    print("**************************************************************************************************")


# TELA DE REMOÇÃO DE PRODUTOS
def tela_remover():
    print("**************************************************************************************************")
    print("\t\t\t\t\t      REMOVER")
    print("**************************************************************************************************")


# TELA DE VISUALIZAR ESTOQUE
def tela_estoque():
    print("**************************************************************************************************")
    print("\t\t\t\t\t     ESTOQUE")
    print("**************************************************************************************************")


# TELA DE ATUALIZAÇÃO DO PRODUTO
def tela_atualizar():
    print("**************************************************************************************************")
    print("\t\t\t\t\t      ATUALIZAR")
    print("**************************************************************************************************")


# TELA DO CÁLCULO DO PREÇO DO PRODUTO
def tela_calculo():
    print("**************************************************************************************************")
    print("\t\t\t\t       CALCULO PREÇO DE VENDA")
    print("**************************************************************************************************")


# CÁLCULO DO PREÇO PRODUTO E ATUALIZAÇÃO DIRETA
def calculo_pv():
    functions.limpar_tela()
    tela_calculo()
    prod = input("QUAL O PRODUTO QUE DESEJA CALCULAR O PREÇO? ").upper()
    for produto in produtos:
        if produto['produto'] == prod:
            custo_produto = float(input('QUAL O CUSTO DE PRODUÇÃO? '))
            if functions.checagem_numero(custo_produto):
                custo_fixo = float(input('Qual O CUSTO FIXO? '))
                if functions.checagem_numero(custo_fixo):
                    comissao_vendas = float(input('QUAL A COMISSAO DE VENDAS? '))
                    if functions.checagem_numero(comissao_vendas):
                        imposto = float(input('QUAL O IMPOSTO? '))
                        if functions.checagem_numero(imposto):
                            lucro = float(input('QUAL A PORCENTAGEM DE LUCRO QUE VOCÊ QUER? '))
                            if functions.checagem_numero(lucro):
                                valor_venda = custo_produto / (
                                        1 - ((custo_fixo + comissao_vendas + imposto + lucro) / 100))

                                qntd = input("QUAL A QUANTIDADE DO PRODUTO? ")
                                if functions.checagem_numero(qntd):
                                    qntd = float(qntd)  # Convertendo para float
                                    produto['quantidade'] = int(qntd)
                                    valor_venda_unitaria = valor_venda / qntd
                                    produto['preco'] = valor_venda_unitaria
                                    print(f"O preço de venda do produto '{prod}' foi calculado com sucesso.")
                                    print(f"Novo preço de venda: R$ {valor_venda_unitaria:.2f}")
                                    return valor_venda_unitaria
                                else:
                                    print("A QUANTIDADE DO PRODUTO DEVE SER UM NÚMERO.")
                                    return None
                            else:
                                print("A PORCENTAGEM DE LUCRO DEVE SER UM NÚMERO.")
                                return None
                        else:
                            print("O IMPOSTO DEVE SER UM NÚMERO.")
                            return None
                    else:
                        print("A COMISSÃO DE VENDAS DEVE SER UM NÚMERO.")
                        return None
                else:
                    print("O CUSTO FIXO DEVE SER UM NÚMERO.")
                    return None
            else:
                print("O CUSTO DE PRODUÇÃO DEVE SER UM NÚMERO.")
                return None
    print(f"O produto '{prod}' não foi encontrado no estoque.")
    return None


# ADICIONAR PRODUTO NA BASE
def adicionar_produto():
    functions.limpar_tela()
    tela_cadastro()

    addproduto = input("DIGITE O NOME DO PRODUTO A SER CADASTRADO: ").upper()
    for prod in produtos:
        if prod['produto'] == addproduto:
            print(f"O PRODUTO '{addproduto}' JÁ FOI CADASTRADO ANTERIORMENTE!")
            return

    qnt_estoque = input("QUAL A QUANTIDADE DO ESTOQUE? ")
    if functions.checagem_numero(qnt_estoque):
        preco = input("QUAL O PREÇO DO PRODUTO POR UNIDADE? ")
        if functions.checagem_numero(preco):
            produtos.append({'produto': addproduto, 'quantidade': qnt_estoque, 'preco': preco})
            print(f"O PRODUTO '{addproduto}' FOI ADICIONADO COM SUCESSO!")
            return


# REMOVER PRODUTO NA BASE
def remover_produto():
    functions.limpar_tela()
    tela_remover()
    print("PRODUTOS DISPONÍVEIS: ")
    for prod in produtos:
        print(prod['produto'])

    remproduto = input("DIGITE O PRODUTO A SER REMOVIDO: ").upper()
    for prod in produtos:
        if prod['produto'] == remproduto:
            produtos.remove(prod)
            print(f"O ITEM '{remproduto}' FOI REMOVIDO COM SUCESSO!")
            print(produtos)
            return

    print(f"O ITEM '{remproduto}' NÃO SE ENCONTRA NA LISTA DE PRODUTOS.")


# MOSTRAR PRODUTOS NA BASE
def mostrar_estoque():
    functions.limpar_tela()
    tela_estoque()

    for prod in produtos:
        print("PRODUTO: {0}, QUANTIDADE: {1}, PREÇO: R$ {2:.2f}".format(prod['produto'], prod['quantidade'],
                                                                        prod['preco']))


# ATUALIZAR O ESTOQUE NA BASE
def atualizar_estoque():
    functions.limpar_tela()
    tela_atualizar()

    for prod in produtos:
        print("PRODUTO: {0}, QUANTIDADE: {1}".format(prod['produto'], prod['quantidade'], prod['preco']))

    att_produto = input("QUAL O PRODUTO QUE DESEJA ATUALIZAR? ").upper()
    for prod in produtos:
        if prod['produto'] == att_produto:
            esc = input("O QUE DESEJA ATUALIZAR? ").upper()
            if esc == 'ESTOQUE':
                att_estoque = input("QUAL A QUANTIDADE NOVA DO ESTOQUE? ")
                if functions.checagem_numero(att_estoque):
                    prod['quantidade'] = att_estoque
                else:
                    print("A NOVA QUANTIDADE DO PRODUTO TEM QUE SER INTEIRO.")
            elif esc == 'PRECO':
                att_preco = input("QUAL O NOVO PREÇO DO PRODUTO? ")
                if functions.checagem_numero(att_preco):
                    prod['preco'] = att_preco
                else:
                    print("VALOR DO PRODUTO TEM QUE SER EM VALOR MONETÁRIO.")
                print(f"A QUANTIDADE DO PRODUTO '{att_produto}' FOI ATUALIZADA COM SUCESSO!")
                return
            else:
                print(f"O PRODUTO '{att_produto}' NÃO ESTÁ NO ESTOQUE.")


# MENU PRINCIPAL
def main_menu():
    functions.limpar_tela()
    while True:
        print("*********************************************************************")
        print("                              | MENU |                             ")
        print("*********************************************************************")
        print("| 1. CADASTRAR PRODUTO | 2. REMOVER PRODUTO | 3. VISUALIZAR ESTOQUE |")
        print("| 4. ATUALIZAR ESTOQUE | 5. CALCULAR PREÇO | 6. LOGOUT |")
        print("*********************************************************************")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            remover_produto()
        elif opcao == '3':
            mostrar_estoque()
        elif opcao == '4':
            atualizar_estoque()
        elif opcao == '5':
            valor_venda = calculo_pv()
            if valor_venda is not None:
                print(f"O VALOR DE VENDA DO PRODUTO É: R$ {valor_venda:.2f}")
        elif opcao == '6':
            functions.limpar_tela()
            print("FINALIZANDO SESSÃO...")
            break
        else:
            print("ERROR! OPÇÃO INVÁLIDA!")
