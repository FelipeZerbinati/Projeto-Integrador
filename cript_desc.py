import oracledb
import sympy
import numpy as np
connection = oracledb.connect(user="BD150224532", password="Zthrh10", host="172.16.12.14", port=1521)
cursor=connection.cursor()
for row in cursor.execute("select descricao from produto"):
    print(row)
connection.commit()
matriz_cod= [[2,1],
             [-1,4]]
A=1
B=2
C=3
D=4
E=5
F=6
G=7
H=8
I=9
J=10
K=11
L=12
M=13
N=14
O=15
P=16
Q=17
R=18
S=19
T=20
U=21
V=22
W=23
X=24
Y=25
Z=0
desc1='Massa do Pão tipo Burger 12 unidades'
desc2='20 pães francês'
desc3='Capuccino em pó'
desc4='Chocolate em barra 125g'
desc5='Pão feito com queijo e ovo porção com 4 pães'
desc6='Pão em formato quadrado 1 pacote'
desc7='Doce feito com milho 1 unidade'
desc8='Rosca doce 1 unidade'
desc9='Bolo simples 1 fatia'
desc10='Salgado empanado e frito com frango 1 unidade'
descn1=
descn2=
descn3=
descn4=
descn5=
descn6=
descn7=
descn8=
descn9=
descn10=

connection.close()