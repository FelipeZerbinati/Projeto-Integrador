import oracledb
import sympy
import numpy as np
import functions
connection = oracledb.connect(user="BD150224532", password="Zthrh10", host="172.16.12.14", port=1521)
cursor=connection.cursor()
for row in cursor.execute("select descricao from produto"):
    print(row)
connection.commit()
matriz_cod=np.array([[2,1],
                    [-1,4]])
a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
j=10
k=11
l=12
m=13
n=14
o=15
p=16
q=17
r=18
s=19
t=20
u=21
v=22
w=23
x=24
y=25
z=0
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
descn[1]=np.array([[13,1,19,19,1,4,15,16,1,15],
                 [20,9,16,15,2,21,18,7,5,18]])
descn[2]=np.array([16,1,5,19,6,18],
                   [1,14,3,5,19,0])
descn[3]=np.array([[3,1,16,21,3,3,9],
                    14,15,5,13,16,15])
descn[4]=np.array([[3,8,15,3,15,12,1],
                   [20,5,2,1,18,18,1]])
descn[5]=np.array([[16,1,15,6,5,9,20,15,3,15,13,17,21,5,9,10,15],
                   [15,22,15,16,15,18,3,1,15,3,15,13,16,1,5,19,0]])
descn[6]=np.array([16,1,15,5,13,6,15,18,13,1,20,15,17],
                  [21,1,4])
descn[7]=np.array([],
                  [])
descn[8]=np.array([],
                  [])
descn[9]=np.array([],
                  [])
descn[10]=np.array([],
                   [])

for i in range(1,11):
    descm[i]=np.array(matriz_cod@descn[i])

connection.close()