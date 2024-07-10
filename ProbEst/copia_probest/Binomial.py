## DISTRIBUIÇÃO BINOMIAL - PROBABILIDADE
## Função de distribuição acumulada, Calculos de probabilidade

import math
from math import sqrt

def prob_binomial(*args):
    '''Calcula a probabilidade binomial de uma variável aleatória X -> x.
i) Imprime os valores das probabilidades de: X<x, X<=x, X=x, X>=x e X>x.
ii) Define variáveis globais [a,b,c,d,e1] para cada valor desses;
iii) Gera um dicionário com esses valores (índices a até e)
iv) Imprime os valores da esperança, variância e desvio padrão de X.

        *float , *int, *int --> *float
'''

    if len(args) == 3:
        p = args[0]        
        n = args[1]
        x = args[2]
        binomio = math.comb(n,int(x))
        probabilidade = binomio*(p**int(x))*(1-p)**(n-(int(x)))
        return probabilidade
    
    else:
        print("Se X é o número de sucessos em n ensaios de bernoulli,")
        print("com probabilidade de sucesso p.  --->  X ~ bin(n,p)")
        print("Fórmula binomial == \u2211 (n x)*(p^x)*(1-p)^(n-x)")
        print("")
        print("")
        
        p = float(input("Insira a chance p: "))
        n = int(input("Insira o número de casos: "))
        print("")
        y = input("Insira o caso P(x) o qual se deseja calcular a probabilidade                    OBS: Também serve para <, <=, >, >=  :   ")
        x = int(y)
        print("")    

        
        soma_i = 0
        i = 0      
        while i <= x: 
            binomio = math.comb(n,i)
            probabilidade_i = binomio*(p**i)*(1-p)**(n-i)
            soma_i += probabilidade_i
            i+=1

        soma_j = 0
        j = x
        while j <= n:
            binomio = math.comb(n,j)
            probabilidade_j = binomio*(p**j)*(1-p)**(n-j)
            soma_j += probabilidade_j
            j+=1

        print("---------------------------------------------------------------------") 
        global a
        a = prob_binomial(p,n,x)
        print("(a) Caso X = x: ", prob_binomial(p,n,x))
        global b
        b = soma_i
        print("(b) Caso X <= x: ", soma_i)
        global c
        c = soma_i - prob_binomial(p,n,x)
        print("(c) Caso X < x: ", soma_i - prob_binomial(p,n,x))
        global d
        d = soma_j
        print("(d) Caso X >= x: ", soma_j)
        global e1
        e1 = soma_j - prob_binomial(p,n,x)
        print("(e) Caso X > x:  ", soma_j - prob_binomial(p,n,x))
        print("")

        global casos
        casos = {"a": a, "b": b, "c": c, "d": d, "e1": e1}
        print('')        
        print("Dicionário: casos['letra']")
        print("---------------------------------------------------------------------") 
        print('')
        print("Valor esperado = n*p =  ", n*p)
        print("Variância = n*p*(1-p) = ", n*p*(1-p))
        print("Desvio Padrão = \u221a(var)", sqrt(n*p*(1-p)))
        print("---------------------------------------------------------------------") 
        print('')



def soma_prob_bin(**soma_de_xi_ate_xm):
    '''Calcula a soma de probabilidades de uma variável binomial X; xi à xm.
Ou seja, calcula probabilide P(xi <= X <= xm) = P(X = xi) + ... + P(X = xm).
i) Imprime cada probabilidade xi individual
ii) Retorna a soma delas todas
'''
    p = float(input("Insira a probabilidade p: "))
    n = int(input("Insira o número de ensaios n: "))
    print('')
    print(" xi <= X <= xm ") 
    print('')
    i = int(input("Insira o valor xi : "))
    m = int(input("Insira o valor xm : "))
    print('')
    soma = 0
    while i <= m:
        soma = soma + prob_binomial(p,n,i)
        print("Probabilidade para X = ", i, " : ", prob_binomial(p,n,i))
        i+=1
    print("Soma das probabilidades acima: ", soma)
    return soma