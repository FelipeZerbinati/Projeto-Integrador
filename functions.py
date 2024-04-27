import os
import re
from unidecode import unidecode


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
'''
import re
from unidecode import unidecode

def remover_caractere(string:str):
    string=string.lower()
    # Remove caracteres especiais e acentos da string
    string_sem_acentos = unidecode(string)
    # Remove caracteres não alfanuméricos da string resultante
    desc = re.sub('[^A-Za-z]+', '', string_sem_acentos)
    return desc

print(remover_caractere('Coxinha-1-de frângo'))
texto = remover_caractere('Coxinha-1-de frângo')
tam = len(texto)
seq = ' '
for i in range(tam):
    seq = seq + str(ord(texto[i])-96)
if tam%2 != 0:
    s = slice(1,tam+1)
    linha1= string(s)
    #linha1= seq(slice(1,int(tam/2)+1))
    #linha2= seq(slice(int(tam/2)+1))
print(linha1)
#print(linha2)
#print(result)
print(seq)
'''
