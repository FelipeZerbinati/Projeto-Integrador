import os
import functions



def tela_cadastro():

    print("**************************************************************************************************")
    print("\t\t\t\t\t     CADASTRO")
    print("**************************************************************************************************")

def tela_remover():
    print("**************************************************************************************************")
    print("\t\t\t\t\t      REMOVER")
    print("**************************************************************************************************")

def tela_estoque():
    print("**************************************************************************************************")
    print("\t\t\t\t\t      ESTOQUE")
    print("**************************************************************************************************")

def tela_atualizar():
    print("**************************************************************************************************")
    print("\t\t\t\t\t     ATUALIZAR")
    print("**************************************************************************************************")



def adicionar_produto():
    functions.limpar_tela()
    tela_cadastro()
    
    addproduto=input("DIGITE O NOME DO PRODUTO A SER CADASTRADO: ").upper()
    if(addproduto not in produtos):
        if(functions.checagem_numero(addproduto) == False):    
            qnt_estoque = input("QUAL A QUANTIDADE DO ESTOQUE? ")
            if(functions.checagem_numero(qnt_estoque)):
                produtos.append(addproduto)
                estoque.append(qnt_estoque)
                print(f"O PRODUTO '{addproduto}' FOI ADICIONADO COM SUCESSO!")
            else:
                print(f"ERROR! QUANTIDADE DO PRODUTO '{addproduto}' NÃO É INTEIRO!")    
        else:
            print(f"ERROR! O NOME DO PRODUTO NÃO PODE SER EM NÚMEROS!")
    else:
        print(f"O ITEM '{addproduto}' JÁ SE ENCONTRA NA LISTA DE PRODUTOS.")
    functions.visualizar_tela()   

def remover_produto():
    functions.limpar_tela()
    tela_remover()
    functions.pular_linha()
    print("PRODUTOS DISPONÍVEIS: ")
    for prod in produtos:
        print(prod)
    functions.pular_linha()
    
    remproduto=input("DIGITE O PRODUTO A SER REMOVIDO: ").upper()
    if(remproduto in produtos):
        index = produtos.index(remproduto)
        produtos.remove(remproduto)
        estoque.pop(index)
        print(f"O ITEM '{remproduto}' FOI REMOVIDO COM SUCESSO!")
    else:
        print(f"O ITEM '{remproduto}' NÃO SE ENCONTRA NA LISTA DE PRODUTOS.")
    functions.visualizar_tela() 

def mostrar_estoque():
    functions.limpar_tela()
    tela_estoque()
    
    for prod,qtd in zip(produtos, estoque):
        print("PRODUTO: {0}, QUANTIDADE: {1}".format(prod,qtd))
    functions.pular_linha()
    functions.visualizar_tela()    

def atualizar_estoque():
    functions.limpar_tela()
    tela_atualizar()
    
    for prod,qtd in zip(produtos, estoque):
        print("PRODUTO: {0}, QUANTIDADE: {1}".format(prod,qtd))
   
    att_produto = input("QUAL O PRODUTO QUE DESEJA ATUALIZAR A QUANTIDADE DO ESTOQUE? ").upper()
    if(att_produto in produtos):
        index = produtos.index(att_produto)
        att_estoque = input("QUAL A QUANTIDADE NOVA DO ESTOQUE? ")
        if(functions.checagem_numero(att_estoque)):
            estoque[index] = att_estoque
        else:
            print("ERROR!")
    else:
        functions.pular_linha()
        print(f"ERROR! PRODUTO {att_produto} NÃO ESTÁ NO ESTOQUE!")
    functions.visualizar_tela() 

def main_menu():
    functions.limpar_tela()
    funcionar=True
    while funcionar:
        print("**************************************************************************************************")
        print("\t\t\t\t\t        MENU")
        print("**************************************************************************************************")
        print("1.CADASTRAR PRODUTO | 2.REMOVER PRODUTO | 3.VISUALIZAR NO ESTOQUE | 4.ATUALIZAR ESTOQUE | 5.SAIR |")
        print("**************************************************************************************************")
        opcao=input("Escolha uma opção: ")
        if(functions.checagem_numero(opcao)):
            if opcao=='1':
                adicionar_produto()
            elif opcao=='2':
                remover_produto()
            elif opcao=='3':
                mostrar_estoque()
            elif opcao =='4':
                atualizar_estoque()
            elif opcao=='5':
                functions.limpar_tela()
                print("FINALIZANDO PROGRAMA...")
                input()
                break
            else:
                print("ERROR! OPÇÃO INVÁLIDA!")
                functions.visualizar_tela()
                functions.limpar_tela()
                
              
        else:
            print("ERROR! OPÇÃO INVÁLIDA!")
            functions.visualizar_tela()
            functions.limpar_tela()
    

produtos = ['BANANA', 'OVO']
estoque = ['26', '12']

main_menu()
