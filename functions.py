import os


def checagem_numero(valor):
    try:
        float(valor)
    except ValueError:
        return False
    return True


def limpar_tela():
    os.system('cls')


def visualizar_tela():
    input("APERTE ENTER PARA CONTINUAR.")
    limpar_tela()


def pular_linha():
    print("\n")
