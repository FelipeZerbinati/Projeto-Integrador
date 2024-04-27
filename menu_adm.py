import functions
from conexao import db_produtos, db_usuario, fechar_conexao

conexao_produtos = db_produtos()
conexao_usuarios = db_usuario()


# TELA DE CADASTRO DE PRODUTOS
def tela_cadastro():
    '''Função para título do cadastro.'''
    print("**********************************")
    print("     | CADASTRO DE PRODUTOS |     ")
    print("**********************************")


# TELA DE REMOÇÃO DE PRODUTOS
def tela_remover():
    '''Função para título da remoção.'''
    print("**********************************")
    print("      | REMOÇÃO DE PRODUTOS |     ")
    print("**********************************")


# TELA DE VISUALIZAR ESTOQUE
def tela_estoque():
    '''Função para título de visualização dos produtos.'''
    print("**********************************")
    print("   | VISUALIZAÇÃO DO ESTOQUE |    ")
    print("**********************************")


# TELA DE ATUALIZAÇÃO DO PRODUTO
def tela_atualizar():
    '''Função para atualização dos produtos.'''
    print("**********************************")
    print("  | ATUALIZAÇÃO DOS PRODUTOS |    ")
    print("**********************************")


# TELA DO CÁLCULO DO PREÇO DO PRODUTO
def tela_calculo():
    '''Função para título do cálculo do preço de venda.'''

    print("**********************************")
    print("    | CÁLCULO PREÇO DE VENDA |    ")
    print("**********************************")


# CÁLCULO DO PREÇO PRODUTO E ATUALIZAÇÃO DIRETA
def calculo_pv(conexao):
    '''Esta função serve para realizar os cálculos do preço de venda do produto.'''
    try:
        produto = input("QUAL O PRODUTO QUE DESEJA CALCULAR O PREÇO? ")

        with conexao.cursor() as cursor:
            sql = "SELECT Custo, Custo_Fixo, Comissao, Impostos, Rentabilidade FROM Produto WHERE Nome = :1"
            cursor.execute(sql, (produto,))
            resultado = cursor.fetchone()

        if resultado:
            custo_produto, custo_fixo, comissao, imposto, lucro = resultado

            qntd = float(input("QUAL A QUANTIDADE DO PRODUTO? "))

            preco_venda = round((custo_produto*qntd) / (1 - (custo_fixo + comissao + imposto + lucro) ),2)
            custo_produto_total = custo_produto * qntd
            custo_fixo_total = custo_fixo * preco_venda
            comissao_total = comissao * preco_venda
            imposto_total = imposto * preco_venda
            lucro_total = custo_produto_total * (1 + lucro)

            preco_venda_unitario = preco_venda / qntd

            cursor = conexao.cursor()
            sql2 = "UPDATE Produto SET Preco_venda = :preco_venda_unitario WHERE Nome = :1"
            cursor.execute(sql2, (preco_venda_unitario, produto))
            conexao.commit()
            cursor.close()

            if lucro_total <= 0:
                nivel_lucro = "PREJUÍZO"
            elif lucro_total <= 10:
                nivel_lucro = "LUCRO BAIXO"
            elif lucro_total <= 20:
                nivel_lucro = "LUCRO MÉDIO"
            else:
                nivel_lucro = "LUCRO ALTO"

            print(f"O PREÇO DE VENDA DO PRODUTO '{produto}' FOI CALCULADO COM SUCESSO.")
            print(f"NOVO PREÇO POR UNIDADE: R$ {preco_venda_unitario:.2f}")
            print(f"NOVO PREÇO TOTAL: R$ {preco_venda:.2f}")
            print(f"CUSTO TOTAL DO PRODUTO: R$ {custo_produto_total:.2f}")
            print(f"CUSTO FIXO EM REAIS: R$ {custo_fixo_total:.2f}")
            print(f"COMISSÃO EM REAIS: R$ {comissao_total:.2f}")
            print(f"IMPOSTO EM REAIS: R$ {imposto_total:.2f}")
            print(f"LUCRO EM REAIS: R$ {lucro_total:.2f} - {nivel_lucro}")

        else:
            print(f"O PRODUTO '{produto}' NÃO FOI ENCONTRADO NO ESTOQUE.")
            #sleep()
    except Exception as e:
        print(f"ERRO AO CALCULAR O PREÇO DE VENDA: {str(e)}")

    return None


# ADICIONAR PRODUTO NA BASE
def adicionar_produto(conexao):
    '''Esta função serve para adicionar um novo produto na base de dados, recebendo os valores
    do preço de venda, nome do produto e a quantidade em estoque.'''
    functions.limpar_tela()
    tela_cadastro()
    try:
        addproduto = input("DIGITE O NOME DO PRODUTO A SER CADASTRADO: ")
        qnt_estoque = int(input("QUAL A QUANTIDADE DO ESTOQUE? "))
        preco_venda = float(input("QUAL O PREÇO DO PRODUTO POR UNIDADE? "))
        descricao = input("DE UMA BREVE DESCRIÇÃO DO PRODUTO: ")
        codigo = input("DIGITE O CODIGO DO PRODUTO: ")

        with conexao.cursor() as cursor:
            sql = "INSERT INTO Produto (Codigo, Nome, Quantidade, Preco_venda, Descricao) VALUES (:1, :2, :3, :4, :5)"
            cursor.execute(sql, (codigo, addproduto, qnt_estoque, preco_venda, descricao))
            conexao.commit()

        print(f"O PRODUTO '{addproduto}' FOI ADICIONADO COM SUCESSO!")
    except Exception as e:
        print(f"Erro ao adicionar o produto: {str(e)}")

    functions.visualizar_tela()


# REMOVER PRODUTO NA BASE
def remover_produto(conexao):
    '''Esta função serve para realizar a remoção do produto da base de dados e pedir uma confirmação ao usuário.'''
    try:
        print("**********************************")
        print("|      REMOÇÃO DE PRODUTOS      |")
        print("**********************************")

        print("PRODUTOS DISPONÍVEIS: ")
        with conexao.cursor() as cursor:
            cursor.execute("SELECT Nome FROM Produto")
            produtos = cursor.fetchall()
            for produto in produtos:
                print(produto[0])

        remproduto = input("DIGITE O PRODUTO A SER REMOVIDO: ")

        confirmacao = input(f"DESEJA MESMO REMOVER O PRODUTO '{remproduto}'? (S/N)").upper()

        if confirmacao == 'S':
            with conexao.cursor() as cursor:
                cursor.execute("DELETE FROM Produto WHERE Nome = :1", (remproduto,))
                conexao.commit()
                print(f"O PRODUTO '{remproduto}' FOI REMOVIDO COM SUCESSO!")

        elif confirmacao == 'N':
            print(f"CANCELANDO A REMOÇÃO DO PRODUTO '{remproduto}'!")

        else:
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE!")

    except Exception as e:
        print(f"ERRO AO REMOVER O PRODUTO: {str(e)}")
    functions.visualizar_tela()


# MOSTRAR PRODUTOS DA BASE
def mostrar_estoque(conexao):
    '''Esta função serve para mostrar todas as informações dos produtos disponíveis no estoque.'''
    try:
        print("**********************************")
        print("|   VISUALIZAÇÃO DO ESTOQUE      |")
        print("**********************************")

        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM Produto")
            produtos = cursor.fetchall()

        if produtos:
            for produto in produtos:
                codigo, nome, descricao, custo, custo_fixo, comissao, impostos, rentabilidade, preco_venda, desc_cripto, quantidade = produto
                print("CÓDIGO:", codigo)
                print("NOME:", nome)
                print("DESCRIÇÃO:", descricao)
                print("CUSTO:", custo)
                print("CUSTO FIXO:", custo_fixo)
                print("COMISSÃO:", comissao)
                print("IMPOSTOS:", impostos)
                print("RENTABILIDADE:", rentabilidade)
                print("PREÇO DE VENDA:", preco_venda)
                print("DESCRIÇÃO CRIPTOGRAFADA:", desc_cripto)
                print("QUANTIDADE NO ESTOQUE:", quantidade)
                print("----------------------------------")
        else:
            print("NENHUM PRODUTO ENCONTRADO NO ESTOQUE.")

    except Exception as e:
        print(f"ERRO AO MOSTRAR O ESTOQUE: {str(e)}")

def tornar_administrador(conexao):
    '''Esta função serve para transformar um usuário em administrador na base de dados.'''
    try:
        print("**********************************")
        print("|   TORNAR USUÁRIO ADMINISTRADOR |")
        print("**********************************")

        with conexao.cursor() as cursor:
            cursor.execute("SELECT nome_usuario FROM cadastro")
            usuarios = cursor.fetchall()

        if usuarios:
            print("USUÁRIOS DISPONÍVEIS:")
            for usuario in usuarios:
                print(usuario[0])

            nome_usuario = input("QUAL USUÁRIO DESEJA TORNAR ADMINISTRADOR? ")

            confirmacao = input(f"DESEJA TORNAR O USUÁRIO '{nome_usuario}' ADMINISTRADOR? (S/N)").upper()

            if confirmacao == 'S':
                with conexao.cursor() as cursor:
                    cursor.execute("UPDATE cadastro SET administrador = 'SIM' WHERE nome_usuario = :1", (nome_usuario,))
                    conexao.commit()
                print(f"O USUÁRIO '{nome_usuario}' FOI TORNADO ADMINISTRADOR COM SUCESSO!")
            elif confirmacao == 'N':
                print(f"OPERAÇÃO CANCELADA. O USUÁRIO '{nome_usuario}' NÃO FOI TORNADO ADMINISTRADOR.")
            else:
                print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")

        else:
            print("NÃO HÁ USUÁRIOS NA BASE DE DADOS.")

    except Exception as e:
        print(f"ERRO AO TORNAR USUÁRIO ADMINISTRADOR: {str(e)}")



def atualizar_produto(conexao):
    '''Esta função serve para atualizar as informações de um produto na base de dados.'''
    try:
        print("**********************************")
        print("|   ATUALIZAÇÃO DE PRODUTO      |")
        print("**********************************")

        nome_produto = input("QUAL O NOME DO PRODUTO QUE DESEJA ATUALIZAR? ")

        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM Produto WHERE Nome = :1", (nome_produto,))
            produto = cursor.fetchone()

        if produto:
            print("INFORMAÇÕES ATUAIS DO PRODUTO:")
            print("CÓDIGO:", produto[0])
            print("NOME:", produto[1])
            print("DESCRIÇÃO:", produto[2])
            print("CUSTO:", produto[3])
            print("CUSTO FIXO:", produto[4])
            print("COMISSÃO:", produto[5])
            print("IMPOSTOS:", produto[6])
            print("RENTABILIDADE:", produto[7])
            print("PREÇO DE VENDA:", produto[8])
            print("DESCRIÇÃO CRIPTOGRAFADA:", produto[9])
            print("QUANTIDADE NO ESTOQUE:", produto[10])

            opcao = input("QUAL INFORMAÇÃO DESEJA ATUALIZAR (CODIGO/NOME/DESCRICAO/CUSTO/CUSTO_FIXO/COMISSAO/IMPOSTOS/RENTABILIDADE/PRECO_VENDA/DESC_CRIPTO/QUANTIDADE)? ").upper()

            if opcao == 'NOME':
                novo_valor = input("NOVO NOME DO PRODUTO: ")
            elif opcao == 'DESCRICAO':
                novo_valor = input("NOVA DESCRIÇÃO DO PRODUTO: ")
            elif opcao == 'CODIGO':
                novo_valor = input("NOVO CÓDIGO DO PRODUTO: ")
            elif opcao == 'PREÇO DE VENDA':
                novo_valor = input("NOVO PREÇO DE VENDA: ")
            elif opcao == 'DESCRIÇÃO CRIPTOGRAFADA':
                novo_valor = input("NOVA DESC. CRIPTOGRAFADA: ")
            elif opcao == 'QUANTIDADE':
                novo_valor = input("NOVA QUANTIDADE: ")
            elif opcao == 'CUSTO' or opcao == 'CUSTO FIXO' or opcao == 'COMISSÃO' or opcao == 'IMPOSTOS' or opcao == 'RENTABILIDADE':
                novo_valor = float(input(f"NOVO VALOR DE {opcao}: "))
            else:
                print("OPÇÃO INVÁLIDA!")
                return

            with conexao.cursor() as cursor:
                cursor.execute(f"UPDATE Produto SET {opcao} = :1 WHERE Nome = :2", (novo_valor, nome_produto))
                conexao.commit()

            print(f"A INFORMAÇÃO '{opcao}' DO PRODUTO '{nome_produto}' FOI ATUALIZADA COM SUCESSO.")

        else:
            print(f"O PRODUTO '{nome_produto}' NÃO FOI ENCONTRADO NO ESTOQUE.")

    except Exception as e:
        print(f"ERRO AO ATUALIZAR O PRODUTO: {str(e)}")

# MENU PRINCIPAL
def main_menu():
    functions.limpar_tela()
    while True:
        print("**********************************")
        print("             | MENU |             ")
        print("**********************************")
        print("| 1. ADICIONAR PRODUTOS ")
        print("| 2. REMOVER PRODUTOS")
        print("| 3. MOSTRAR PRODUTOS")
        print("| 4. ATUALIZAR PRODUTOS")
        print("| 5. CÁLCULO DO PREÇO DE VENDA")
        print("| 6. ADICIONAR USUÁRIO COMO ADMINISTRADOR")
        print("| 7. LOGOUT\n")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case '1':
                adicionar_produto(conexao_produtos)
                functions.limpar_tela()
            case '2':
                remover_produto(conexao_produtos)
            case '3':
                mostrar_estoque(conexao_produtos)
            case '4':
                atualizar_produto(conexao_produtos)
            case '5':
                valor_venda = calculo_pv(conexao_produtos)
                if valor_venda is not None:
                    print(f"O VALOR DE VENDA DO PRODUTO É: R$ {valor_venda:.2f}")
            case '6':
                tornar_administrador(conexao_usuarios)
                functions.visualizar_tela()
            case '7':
                functions.limpar_tela()
                print("FINALIZANDO SESSÃO...")
                fechar_conexao(conexao_produtos)
                fechar_conexao(conexao_usuarios)
                functions.visualizar_tela()
                break
            case _:
                print("ERROR!! OPÇÃO INVÁLIDA!")
                print("TENTE NOVAMENTE!")
                functions.visualizar_tela()
