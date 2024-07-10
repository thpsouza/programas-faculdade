
####### CALCULADORA SÉRIE DE TAYLOR PARA MAIS DE UMA VARIÁVEL ########

from sympy import *
import numpy as np
import math
import time
from taylor import termo_an,avaliar,taylor

######## DADOS ########

# SELECIONAR NUMERO DE VARIAVEIS
n_de_variaveis = 2

# DESCREVER A FUNÇÃO (x1,x2,x3,...,xn)
function = ' sin(x1*x2) '       
function1 = 'x1*x2*x3'

# LISTAR OS ARGUMENTOS TAIS QUE F É DESCONHECIDA
xis = [5,3]

# LISTAR OS ARGUMENTOS TAIS QUE F É CONHECIDA
ais = [1,1]

# valor de erro aceitável
erro = 0.00001          


#### PROCEDIMENTOS ####

lista_variaveis = []
for i in range(1,n_de_variaveis+1): #NÃO ALTERAR
    exec(f"x{i} = Symbol(f'x{i}')")
    exec(f"lista_variaveis.append(x{i})")
exec('function = {}'.format(function))

def erro_absoluto_aproximacao(valor_obtido,f,variaveis,pontos_desconhecidos,casas_decimais=20):
    valor_real = evaluation(f,pontos_desconhecidos,variaveis,casas_decimais)
    return abs(valor_real - valor_obtido)
    

def taylor_mv(f,variaveis,pontos_desconhecidos,pontos_conhecidos,error,casas_decimais=20):
    soma = 0
    k=0
    function = f
    while True:
        for i in range(n_de_variaveis):
            f = taylor(f,variaveis[i],pontos_desconhecidos[i],pontos_conhecidos[i],k,imprimir=False)
        if erro_absoluto_aproximacao(f,function,variaveis,pontos_desconhecidos,casas_decimais) <= erro:
            return f,k
        f = function
        k+=1


if __name__ == "__main__":
    f = function
    ret = taylor_mv(function,lista_variaveis,xis,ais,error=erro)
    print("\n Valor = {} \n Número de termos calculados = {}".format(ret[0],ret[1]))
    input()

