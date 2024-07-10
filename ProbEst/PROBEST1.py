#                    Funções do curso PROBEST
# Cálculo de probabilidades para variáveis aleatórias e vetores aleatórios.

from sympy import Symbol,oo
import math
from math import e,sqrt,pi,erf
import statistics
import numpy as np
NM = statistics.NormalDist


# - - - - - - - - - - - - -  Aula 3 - - - - - - - - - - - - - - -# 

#1) Variável Aleatória Binomial

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
            soma_i = soma_i + probabilidade_i
            i+=1

        soma_j = 0
        j = x
        while j <= n:
            binomio = math.comb(n,j)
            probabilidade_j = binomio*(p**j)*(1-p)**(n-j)
            soma_j = soma_j + probabilidade_j
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





#2) Variável Aleatória Poisson

def prob_poisson(*args):
    '''Calcula a probabilidade de poisson de uma variável aleatória X -> x.
i) Imprime os valores das probabilidades de: X<x, X<=x, X=x, X>=x e X>x.
ii) Define variáveis globais [a,b,c,d,e1] para cada valor desses;
iii) Gera um dicionário com esses valores (índices a até e)
iv) Imprime os valores da esperança, variância e desvio padrão de X.

        *float , *int, *int --> *float
'''
    
    global a
    global b
    global c
    global d
    global e1
    global casos
    if len(args)== 2:
        lambd = args[0]
        x = int(args[1])
        px = e**(-lambd)*((lambd**x)/math.factorial(x))
        return px
    if len(args) == 3:
        lambd = args[0]       
        x = args[1]
        k = args[2]
        i = 0 if k == 0 else int(k)
        soma = 0
        while i <= x:
            soma = soma + prob_poisson(lambd,i)
            i+=1
        print('')
        print("(a) Caso X = x: ", prob_poisson(lambd,x))
        print("(a) Caso k <= X <= x: ", soma)
        print("(c) Caso X = k: ", prob_poisson(lambd,k))
        print("Para ver mais casos: usar função soma_prob_poi()")
        a = prob_poisson(lambd,x)
        b = soma
        c = prob_poisson(lambd,k)
        casos = {"a": prob_poisson(lambd,x), "b": soma, "c": prob_poisson(lambd,k)}
        print('')
        print("Dicionário: casos['letra']")
        return prob_poisson(lambd,x)

    else:
        print("X é poisson de parametro \u03bb > 0, se: ")
        print("X assume valores 0,1,2,... e segue a fórmula abaixo:")
        print("com probabilidade de sucesso p.  --->  X ~ poi(\u03bb)")
        print("Fórmula poisson == \u2211 e^(-\u03bb)*(\u03bb^x) / x! ")
        print("")
        print("")
        
        lambd = float(input("Insira lambda \u03bb (p * N) : "))
        print("")        
        y = input("Insira o caso P(x) o qual se deseja calcular a probabilidade                    OBS: Também serve para <, <=, >, >=  :   ")
        x = int(y)
        print("")
        k = input("Insira o número inferior do somátório (para 0, só deixar em branco): ")
        print("")
        print("---------------------------------------------------------------------")        
        if k == '':
            i = 0
            soma = 0
            while i <= x:
                soma = soma + prob_poisson(lambd,i)
                i+=1
            print("(a) Caso X = x: ", prob_poisson(lambd,x))
            print("(b) Caso X <= x: ", soma)
            print("(c) Caso X < x: ", soma - prob_poisson(lambd,x))
            print("(d) Caso X > x: ", 1-soma)
            print("(e1) Caso X >= x: ", 1 - (soma-prob_poisson(lambd,x)))
            a = prob_poisson(lambd,x)
            b = soma
            c = soma - prob_poisson(lambd,x)
            d = 1-soma
            e1 = 1 - (soma-prob_poisson(lambd,x))
            casos = {"a": prob_poisson(lambd,x), "b": soma, "c": soma - prob_poisson(lambd,x), "d": 1-soma, "e1": 1 - (soma-prob_poisson(lambd,x))}
            print('')        
            print("Dicionário: casos['letra']")
        else:
            i = int(k)
            soma = 0
            while i <= x:
                soma = soma + prob_poisson(lambd,i)
                i+=1
            print("(a) Caso X = x: ", prob_poisson(lambd,x))
            print("(a) Caso k <= X <= x: ", soma)
            print("(c) Caso X = k: ", prob_poisson(lambd,int(k)))
            print("Para ver mais casos: usar função soma_prob_poi()")
            a = prob_poisson(lambd,x)
            b = soma
            c = prob_poisson(lambd,int(k))            
            casos = {"a": prob_poisson(lambd,x), "b": soma, "c": prob_poisson(lambd,k)}
            print('')
            print("Dicionário: casos['letra']")
    print("---------------------------------------------------------------------") 
    print('')
    print("Valor esperado = Variância = \u03bb = ", lambd)
    print("Desvio Padrão = \u221a(\u03bb) = ", sqrt(lambd))
    print("---------------------------------------------------------------------") 
    print("")


def soma_prob_poi(**soma_de_xi_ate_xm):
    '''Calcula a soma de probabilidades de uma variável poisson X; xi à xm.
Ou seja, calcula probabilide P(xi <= X <= xm) = P(X = xi) + ... + P(X = xm).
i) Imprime cada probabilidade xi individual
ii) Retorna a soma delas todas
'''
    lambd = float(input("Insira lambda (n*p): "))
    print('')
    print(" xi <= X <= xm ") 
    print('')
    i = int(input("Insira o valor xi : "))
    m = int(input("Insira o valor xm : "))
    print('')
    soma = 0
    def poisson(lambd,m,i):
        return e**(-lambd)*((lambd**i)/(math.factorial(i)))        
    while i <= m:
        soma = soma + poisson(lambd,m,i)
        print("Probabilidade para X = ", i, " : ", poisson(lambd,m,i))
        i+=1
    print("Soma das probabilidades acima: ", soma)
    return soma



# - - - - - - - - - - - - -  Aula 7 - - - - - - - - - - - - - - -#


#1) Variável Aleatória Exponencial - Cálculo f.d.p.

''' Uma v.a X é dita exponencial de parâmetro lambda se a sua
função densidade de probabilidade (fdp) é dada por:

        fX(x) = { lambda * e^(- lambda*x)), para x >= 0   } 
                { 0,                        para x < 0    }

    P ( a =< x =< b ) = integral(a->b)[  lambda * e^(-lambda*x)  ]                   
'''

def prob_exp():
    '''Calcula a função densidade de probabilidade de uma variável aleatória
exponencial X de parâmetro \u03bb.
Realiza o cálculo num intervalo de integração de a até b;
E retorna a probabilidade de que x esteja nesse intervalo.
   
        P ( a =< x =< b ) =  \u222b(a->b) (\u03bb*e^(-\u03bb*x))

        float, float, float --> float

'''    
    return fdp_exp()

def fdp_exp():
    '''Calcula a função densidade de probabilidade de uma variável aleatória
exponencial X de parâmetro \u03bb.
Realiza o cálculo num intervalo de integração de a até b;
E retorna a probabilidade de que x esteja nesse intervalo.
   
        P ( a =< x =< b ) =  \u222b(a->b) (\u03bb*e^(-\u03bb*x))

        float, float, float --> float

'''
    print("Uma v.a X é dita exponencial de parâmetro \u03bb se a sua ")
    print("função densidade de probabilidadae (fdp) é dada por:")
    print("")
    print("fX(x) = { \u03bb*e^(-\u03bb*x)), para x >= 0   }")
    print("        { 0,           para x < 0    }")
    print("")
    print("E a probabilidade de um x estar entre um intervalo (a,b) é:")
    print("")
    print("P ( a =< x =< b ) =  \u222b(a->b) (\u03bb*e^(-\u03bb*x))")
    print("")
    print("")

    lambd = float(input("Insira o parâmetro \u03bb = 1/media : "))
    print('')
    print('OBS.: Atenção nos intervalos de integração.')
    print('Se o objetivo for obter T > x, então o intervalo será (x -> infinito)')
    print('Se o objetivo for obter T < x, então o intervalo será (0 -> x)')
    print('Se o objetivo for obeter a <= T <= b, então o intervalo será (a -> b)')
    print('')
    a = float(input("Insira o valor inferior (a) do intervalo do cálculo: "))
    b1 = input("Insira o valor superior (b) do intervalo do cálculo: ")
    b = oo if b1=='infinito' else float(b1)
    
    fdp_integrada = lambd*((e**(-a*lambd))/lambd - (e**(-b*lambd))/lambd)

    print("")
    print("---------------------------------------------------------------------")        
    print("")
    print(" P ( a =< x =< b ) =  ", fdp_integrada)
    print("---------------------------------------------------------------------") 
    print("")
    print("Valor esperado = 1/\u03bb = ", 1/lambd)
    print("Variância = 1/\u03bb² = ", 1/(lambd**2))
    print("Desvio Padrão = \u221a(1/\u03bb²) = ", sqrt(1/(lambd**2)))
    print("---------------------------------------------------------------------") 
    print("")






# - - - - - - - - - - - - -  Aula 9 - - - - - - - - - - - - - - -# 



def prob_normal(*args):
    '''Calcula a probabilidade normal de uma variável aleatória X ~ N(Mi,Sigma2).
i) Imprime os valores das probabilidades de: X<=x, e X>=x.
ii) Define variáveis globais [a,b] para cada valor desses;
iii) Gera um dicionário com esses valores
iv) Imprime os valores da esperança, variância e desvio padrão de X.

        *float , *int, *int --> *float
'''


    if len(args) == 3:
        mi = args[0]        
        sigma = args[1]
        x = args[2]
        z = (x - mi)/sqrt(sigma)
        return phi_z(z)
    
    else:
        print("X v.a normal de parâmetros \u03bc e \u03c3²")
        print("    X ~ N(\u03bc,\u03c3²)")
        print("")
        print("Para calcular. Primeiro padronizamos X em Z:")
        print("      Z = ( X - \u03bc ) / \u03c3 ")
        print("")
        print("E então aproximamos a probabilidade de Z <= pela função \u03a6(z) ")
        print("")
        
        mi = float(input("Insira a média \u03bc: "))
        sigma2 = float(input("Insira a variância \u03c3²: "))
        print("")
        print(" *** Caso deseje calcular P ( a <= x <= b ), deixe em branco abaixo. ***")
        print("")
        y = input("Insira o caso P(x) o qual se deseja calcular a probabilidade                    OBS: Serve para <= e >=  :   ")
        x = float(y) if y != '' else ''
        print("")    

        if x == '':
            dif_normal(mi,sigma2)
        else:
            z = NM(mi,sqrt(sigma2)).cdf(x)

            print("---------------------------------------------------------------------") 
            global a
            a = z
            print("(a) Caso X <= x: ", z)
            global b
            b = 1-z
            print("(b) Caso X >= x: ", 1-z)

            global casos
            casos = {"a": a, "b": b}
            print('')        
            print("Dicionário: casos['letra']")
        print("---------------------------------------------------------------------") 
        print('')
        print("Valor esperado de X = \u03bc =  ", mi)
        print("Variância de X = \u03c3 = ", sigma2)
        print("Desvio Padrão de X = \u221a(var) = ", sqrt(sigma2))
        print("---------------------------------------------------------------------") 
        print('')



def dif_normal(mi,sigma2):
    
    print("P ( a <= X <= b ) = P(X <= b) - P(a <= X)")
    a = input("Insira o valor a o qual se quer calcular P(a <= X) : ")
    b = input("Insira o valor b o qual se quer calcular P(X <= b) : ")
    z1 = NM(mi,sqrt(sigma2)).cdf(float(b))
    z2 = NM(mi,sqrt(sigma2)).cdf(float(a))
    probabilidade = z1 - z2
    global p
    p = probabilidade
    print("")
    print('P ( a <= X <= b ) = ', probabilidade, ('  (p)'))


def inversa_normal():
    '''Essa função calcula os valores que originam uma probabilidade de uma
distribuição normal.
'''

    print("**ESSA FUNÇÃO ENCONTRA O INVERSO PARA UMA F.D.A NORMAL PHI(Z)**")
    print("")
    print("Qual caso deseja?")
    print("")
    print(" (0) Achar um valor de x tal que X<=x, dados média e variancia (\u03c3^2)")
    print(" (1) Achar um valor da Média (\u03bc), dados x e variancia (\u03c3^2)")
    print(" (2) Achar um valor de \u03c3, dados x e Média (\u03bc)")
    print(" (3) Achar os limites a = \u03bc - d e b = \u03bc + d, dados Média (\u03bc) e variancia (\u03c3^2)")
    print("                        P ( a < X < b )")
    escolha = input("")
    print("")

    if escolha == '':
        return 'Abortado.'
    
    elif escolha == '0':
        mi = float(input("Insira a média \u03bc: "))
        sigma2 = float(input("Insira a variancia (\u03c3^2): "))
        p = input("Insira a probabilidade (decimal): ")
        valor = NM(mi,sqrt(sigma2)).inv_cdf(float(p))
        print("**LEMBRANDO QUE O VALOR x ABAIXO É PARA X<=x**")
        print("")
        
    elif escolha == '1':
        x = float(input("Insira o valor de x: "))
        sigma2 = float(input("Insira a variancia (\u03c3^2): "))
        print("")
        print("OBS: A PROBABILIDADE p DE X <= x")
        print("Caso o valor que se tem seja para X>=x, basta por 1-p")
        p = input("Insira a probabilidade (decimal): ")
        n = input("Insira o número de casos (n): ")
        argumento = NM().inv_cdf(float(p))
        valor = (x - sqrt(sigma2)*argumento)/int(n)
        
    elif escolha == '2':
        x = float(input("Insira o valor de x: "))
        mi = float(input("Insira a média \u03bc: "))
        p = input("Insira a probabilidade (decimal): ")
        n = input("Insira o número de casos (n): ")
        argumento = NM().inv_cdf(float(p))
        valor = ((x-mi)/argumento)/int(n)
        
    elif escolha == '3':
        print("OBS: Se a ideia for os limites de uma média aritimética,")
        print("definir Mi e sigma2 = sigma2/n antes")
        print("")
        mi = float(input("Insira a média \u03bc: "))
        sigma2 = float(input("Insira a variancia (\u03c3^2): "))       
        p = input("Insira a probabilidade (decimal): ")
        d = NM().inv_cdf((float(p)+1)/2)*sqrt(sigma2)
        valor = (mi-d,mi+d)

    formatar = {'0': 'e x', '1': 'a média', '2': 'o desvio padrao', '3':'os limites inferior e superior'}
    print(f"Valor d{formatar[escolha]}: ", valor)

inversa_normal()



#1) Variável Aleatória normal - Cálculo f.d.p.
''' Uma v.a X é dita normal ou gaussiana de parâmetros mi e sigma2 se a sua
função densidade de probabilidade (fdp) é dada por:
'''

def fdp_normal(x,mi,sigma2,n=0):
    '''Calula a função densidade de probabilidade de uma v.a normal X
tal que X ~ N(mi,sigma2)
        float, float, float, int=0 --> float
        
'''
    p1 = 1/(sqrt(2*pi*sigma2))
    p2 = e**(((-1/2)*((x-mi)**2))/sigma2)
    fx = p1*p2
    if n == 0:
        return fx
    else:
        return round(fx, n)



#2) Variável Aleatória padrão:

    #Cálculo f.d.p

''' Uma v.a Z tem distribuição normal padrão se Z ~ N(0,1).
Denotamos por phi minuscula e phi maiuscula suas fdp e fda, respectivamente:
'''

def fdp_padrao(z,n=0):
    '''Calcula a função densidade de probabilidade de uma v.a normal padrão Z
aplicada em z.
        float, int = 0 --> float
    
'''
    p1 = 1/(sqrt(2*pi))
    p2 = e**((-1/2)*z**2)
    phix = p1*p2
    if n == 0:
        return phix
    else:
        return round(phix, n)

def fda_padrao(z):
    '''Calcula a função densidade acumulada de uma v.a normal padrão Z
aplicada em z.
        
'''
    p1 = erf(float(z)/sqrt(2))+1
    return p1/2

def phi_z(z):
    return fda_padrao(z)




# Variável aleatória com função qualqer:


x = Symbol('x')
c = Symbol('c')

f = 2/35*x


def Esp_var_2(funcao,limites,var=Symbol('x')):

    l0 = limites[0]
    l1 = limites[1]
    
    if limites[0] in ['inf','infinite','-inf','-infinite']:
        if limites[0] in ['inf','infinite']:
            l0 = oo
        else:
            l0 = -oo
    if limites[1] in ['inf','infinite','-inf','-infinite']:
        if limites[1] in ['inf','infinite']:
            l1 = oo
        else:
            l1 = -oo

    f = ((var**2)*funcao).integrate((var,l0,l1))            
    
    return f


    
def Esp(funcao,limites,var=Symbol('x')):

    l0 = limites[0]
    l1 = limites[1]
    
    if limites[0] in ['inf','infinite','-inf','-infinite']:
        if limites[0] in ['inf','infinite']:
            l0 = oo
        else:
            l0 = -oo
    if limites[1] in ['inf','infinite','-inf','-infinite']:
        if limites[1] in ['inf','infinite']:
            l1 = oo
        else:
            l1 = -oo
            
    f = (var*funcao).integrate((var,l0,l1))
    
    return f


    

def f_densidade(funcoes,limites,var=Symbol('x')):

    try:
        funcoes = list(funcoes)
        limites = list(limites)
        E_var_2 = 0 
        E_2 = 0
        for i in range(len(funcoes)):
            E_var_2 += Esp_var_2(funcoes[i],limites[i],var)
            E_2 += Esp(funcoes[i],limites[i],var)**2         
            
    except:
        E_var_2 = Esp_var_2(funcoes,limites,var)
        E_2 = Esp(funcoes,limites,var)**2

    VAR = E_var_2-E_2
    #DP = sqrt(E_var_2-E_2)

    #print("\n Desvio Padrão: ") 
    return VAR











############################ PARTE 2 - ESTATÍSTICA #############################


def analise_geral(*Amostra):
    '''Imprime todos valores para análise de uma amostra:
        (1)- Medidas de centralidade: Média, Mediana (2º quartil)  e Moda
        (2)- Medidas de dispersao: Variância, Desvio Padrão, Coeficiente de variação
        (3)- Quartis: 1º Quartil, 3º Quartil e Distância Interquartis
        (4)- Discrepancia: Cerca inferior, Cerca Superior, valores discrepantes
        (5)- Maior valor e menor valor
        
        Monta também o Boxplot, se desejado (basta indicar nos argumentos)'''
    
    
    if len(Amostra) == 0:
        print("Insira a amostra de Xi's (separados por vírgula, sem colchetes e sem espaço): ")
        xis = input()
        lista_xis = [int(i) for i in xis.split(',')]
    else:
        lista_xis = Amostra[0]
    lista_xis.sort()
    n = len(lista_xis)    

    m = Amostra[1] if len(Amostra) == 2 else 4 #CASAS DECIMAIS

    med = round((sum(lista_xis))/n,m) #media aritimetica
    #2º Quartil - Mediana
    if (n%2 != 0):
        Q2 = round(lista_xis[(((n+1)//2)-1)],m)
    elif (n%2 == 0):
        Q2 = round((lista_xis[(n//2)-1]+lista_xis[((n//2)+1)-1])/2,m)
    ocorrencias = {i:lista_xis.count(i) for i in lista_xis}
    moda = max(ocorrencias, key=lambda key: ocorrencias[key]) #moda

    xi_med_2 = [(i - med)**2 for i in lista_xis] 
    var_A = round(sum(xi_med_2)/(n-1),m) #variancia
    DP = round(sqrt(var_A),m) #desvio padrao
    cv = round(DP/med,m) #coeficiente de variacao

    #1º Quartil
    q1 = (n+3)/4
    if q1 == int(q1):
        Q1 = round(lista_xis[int(q1)-1],m) 
    else:
        viz_sup = int((n+3)/4) + 1
        peso_superior = q1 - int(q1)
        viz_inf = int((n+3)/4)
        peso_inferior = 1 - peso_superior
        Q1 = round(peso_inferior*lista_xis[viz_inf-1]+peso_superior*lista_xis[(viz_sup)-1],m)       
    #3º Quartil
    q3 = (3*n+1)/4
    if q3 == int(q3):
        Q3 = round(lista_xis[int(q3)-1],m)
    else:
        viz_sup = int((3*n+1)/4) + 1
        peso_superior = q3 - int(q3)
        viz_inf = int((3*n+1)/4)
        peso_inferior = 1 - peso_superior
        Q3 = round(peso_inferior*lista_xis[viz_inf-1]+peso_superior*lista_xis[(viz_sup)-1],m) 
    #DIQ (Distância interquartil)
    DIQ = round((Q3 - Q1),m)

    #Discrepancia
    CI = round(Q1 - ((3/2) * DIQ),m) #cerca inferior
    CS = round(Q3 + ((3/2) * DIQ),m) #cerca superior 
    discrepantes = []
    for x in lista_xis:
        if x < CI or x > CS:
            discrepantes.append(x) 

    x_max = round(max(lista_xis),m) #maior valor
    x_min = round(min(lista_xis),m) #menor valor

    
    if len(Amostra) == 2:
        return {
            'media':med,'mediana':Q2,'moda':moda,
            'variancia':var_A,'DP':DP,'cv':cv,
            'Q1':Q1,'Q3':Q3,'DIQ':DIQ,
            'CI':CI,'CS':CS,'discrepantes':discrepantes,
            'maximo':x_max,'minimo':x_min
        }
    else:
        informacoes = {
            '(1) MEDIDAS DE CENTRALIDADE': '',
            '   Média Aritimética (x\u0304)  = ' : med,
            '   Mediana (Q2)  = ' : Q2,
            '   Moda = ': moda,
            '':'',
            '(2) MEDIDAS DE DISPERSÃO': '',
            '   Variância (s²)  = ' : var_A,
            '   Desvio Padrão (s)  = ' : DP,
            '   Coeficiente de variacao (c\u03c5)  = ' : cv,
            ' ':' ',
            '(3) QUARTIS': '',   
            '   1º Quartil (Q1)  = ' : Q1,
            '   3º Quartil (Q3)  = ' : Q3,
            '   Distância interquartil (DIQ)  = ': DIQ,
            '  ':'  ',
            '(4) DISCREPÂNCIA': '', 
            '   Cerca inferior (CI)  = ' : CI,
            '   Cerca superior (CS)  = ' : CS,
            '   Valores discrepantes = ' : discrepantes,
            '   ':'   ',
            '(5) MAX E MIN': '',
            '   Valor max.  = ': x_max,
            '   Valor min.  = ': x_min
        }
        print('')
        for i in informacoes:
            print(i,informacoes[i])
            print('')

        plotar = input("Caso queira o BoxPlot, digite qualquer coisa")
        if plotar != '':
            boxplot(lista_xis)



#- - - - - - - - - - - - - - - - - AULA 13 - - - - - - - - - - - - - - - - - -#

exemplo_7_aula13 = ex713 = [83,96,73,102,93,94,99,85,91,118,
                            93,103,87,95,102,84,100,95,90,81,
                            102,98,94,89,91,78,85,83,105,96
]
# medidas_centralidade(exemplo_7_aula13)

def medidas_centralidade(*Amostra):
    '''Essa função calcula e imprime as medidas de centralidade de uma amostra
            *list --> null'''
    
    if len(Amostra) == 0:
        print("Insira a amostra de Xi's (separados por vírgula, sem colchetes e sem espaço): ")
        xis = input()
        lista_xis = [int(i) for i in xis.split(',')]
    else:
        lista_xis = Amostra[0] 
    lista_xis.sort()
    n = len(lista_xis)
    print('')
    print("  Amostra (ordenada):")
    print(lista_xis)
    print('')
    print("  n = ", n)
    print('')
    print('')
    print("Abaixo os valores referentes as medidas de centralidade da amostra fornecida:")
    print('')
    casas_decimais = 4 #NÚMERO DE CASAS DECIMAIS NAS RESPOSTAS
    
    #Media
    med = analise_geral(lista_xis,casas_decimais)['media']
    print("  Média aritimética = ", med)
    print('')
    #Mediana
    Q2 = analise_geral(lista_xis,casas_decimais)['mediana']
    print("  Mediana = ", Q2)
    print('')
    #Moda
    ocorrencias = {i:lista_xis.count(i) for i in lista_xis}
    moda = max(ocorrencias, key=lambda key: ocorrencias[key])
    print("  Moda = ", moda ," ,  com {} ocorrências".format(ocorrencias[moda]))
    print('  OBS: Pode ser que além de {}, haja outro(s) valor(es) com {} ocorrências'.format(moda,ocorrencias[moda]))
    print('')
    global amostra
    amostra = lista_xis
    print('Para reaproveitar a lista em outra função, basta usar a variável "amostra" como argumento')
    print('')
    print('')



def medidas_dispersao(*Amostra):
    '''Essa função calcula e imprime as medidas de dispersão de uma amostra
        *list --> null'''
    
    if len(Amostra) == 0:
        print("Insira a amostra de Xi's (separados por vírgula, sem colchetes e sem espaço): ")
        xis = input()
        lista_xis = [int(i) for i in xis.split(',')]
    else:
        lista_xis = Amostra[0] 
    lista_xis.sort()
    n = len(lista_xis)
    print('')
    print("  Amostra (ordenada):")
    print(lista_xis)
    print('')
    print("  n = ", n)
    print('')
    print('')
    print("Abaixo os valores referentes as medidas de dispersão da amostra fornecida:")
    print('')
    casas_decimais = 4 #NÚMERO DE CASAS DECIMAIS NAS RESPOSTAS

    #Variância amostral 
    var_A = analise_geral(lista_xis,casas_decimais)['variancia']
    print("  Variância amostral = ", var_A)
    print('')
    #Desvio Padrão Amostral
    DP_A = analise_geral(lista_xis,casas_decimais)['DP']
    print("  Desvio Padrão amostral = ", DP_A)
    print('')
    #Coeficiente de variação amostral 
    cv = analise_geral(lista_xis,casas_decimais)['cv']
    print("  Coeficiente de variação amostral = ", cv, " = {}%".format(round(cv*100,2)))
    print('')
    print('')
    global amostra
    amostra = lista_xis
    print('Para reaproveitar a lista em outra função, basta usar a variável "amostra" como argumento')
    print('')
    print('')


#- - - - - - - - - - - - - - - - - AULA 14 - - - - - - - - - - - - - - - - - -#


def quartis(*Amostra):
    '''Essa função calcula e retorna os quartis e a distância interquartil de uma amostra
            *list --> list'''

    if len(Amostra) == 0:
        print("Insira a amostra de Xi's (separados por vírgula, sem colchetes e sem espaço): ")
        xis = input()
        lista_xis = [int(i) for i in xis.split(',')]
    else:
        lista_xis = Amostra[0]
    lista_xis.sort()
    n = len(lista_xis)

    casas_decimais = Amostra[1] if len(Amostra) == 2 else 4 #NÚMERO DE CASAS DECIMAIS NAS RESPOSTAS

    #1º Quartil
    Q1 = analise_geral(lista_xis,casas_decimais)['Q1']
     
    #2º Quartil - Mediana
    Q2 = analise_geral(lista_xis,casas_decimais)['mediana']
    
    #3º Quartil
    Q3 = analise_geral(lista_xis,casas_decimais)['Q3']
    
    #DIQ (Distância interquartil)
    DIQ = analise_geral(lista_xis,casas_decimais)['DIQ']

    if len(Amostra) == 2:
        return [Q1,Q2,Q3,DIQ]

    #Explicação sobre definição dos quartis
    print('')
    print(" Não há unanimidade no cálculo dos quartis, então os valores podem variar, ")
    print("a depender da definição matemática utilizada.")
    print('')
    print(" Aqui serão usadas as definições abaixo: ")
    print('')
    print(" Q1:  | Se (n+3)/4 for inteiro,   Q1 = x na posição (n+3)/4")
    print('      |')
    print("      | Caso contrário,           Q1 é uma interpolação entre os valores nas")
    print("      |                           posições vizinhas a (n+3)/4") 
    print('')
    print('')
    print(" Q2:  | Q2 = Mediana")
    print('')
    print('')
    print(" Q3:  | Se (3n+1)/4 for inteiro,  Q3 = x na posição (3n+1)/4")
    print('      |')
    print("      | Caso contrário,           Q3 é uma interpolação entre os valores nas")
    print("      |                           posições vizinhas a (3n+1)/4") 
    print('')
    #Valores
    print('')
    print(" ###### Quartis: ######")
    print('')
    print("  1º Quartil: Q1 = ", round(Q1,casas_decimais))
    print('')  
    print("  2º Quartil (Mediana): Q2 = ", round(Q2,casas_decimais))
    print('')
    print("  3º Quartil: Q3 = ", round(Q3,casas_decimais))
    print('')
    print("  Distância Interquartil: DIQ = ", round(DIQ,casas_decimais))
    print('')

    
exemplo_2_aula14 = ex214 = [1.68, 1.8, 1.63, 1.76, 1.75, 1.5, 1.79, 1.73, 1.94, 1.72]


def discrepantes(*Amostra):
    '''Essa função calcula e retorna os valores discrepantes de uma amostra
            *list --> list'''

    if len(Amostra) == 0:
        print("Insira a amostra de Xi's (separados por vírgula, sem colchetes e sem espaço): ")
        xis = input()
        lista_xis = [int(i) for i in xis.split(',')]
        print('')
        print('')
        d = analise_geral(lista_xis,4)
        print("Intervalo [CI;CS] = [{};{}]".format(d['CI'],d['CS']))
        print('')
        print("Valores Discrepantes: ")        
    else:
        lista_xis = Amostra[0]

    m = 4 #casas decimais
    discrepantes = analise_geral(lista_xis,m)['discrepantes']
    return discrepantes
        

def boxplot(*Amostra):
    '''Imprime o boxplot de uma amostra (FUNCIONA ATÉ 6 DIGITOS)'''


    m = 2  #CASAS DECIMAIS PARA ARREDONDAR

    if len(Amostra) == 0:
        print("Insira a amostra de Xi's (separados por vírgula, sem colchetes e sem espaço): ")
        xis = input()
        lista_xis = [int(i) for i in xis.split(',')]
    else:
        lista_xis = Amostra[0]
    lista_xis.sort()
    n = len(lista_xis)
    
    med = round((sum(lista_xis))/n,m) #media aritimetica
    Q2 = round(quartis(lista_xis,1)[1],m) #2º quartil - mediana

    xi_med_2 = [(i - med)**2 for i in lista_xis] 
    var_A = sum(xi_med_2)/(n-1) #variancia
    DP = round(sqrt(var_A),m) #desvio padrao

    Q1 = round(quartis(lista_xis,1)[0],m) #1º quartil
    Q3 = round(quartis(lista_xis,1)[2],m) #3º quartil
    DIQ = round(quartis(lista_xis,1)[3],m) #distancia interquartil
    
    CI = round(Q1 - ((3/2) * DIQ),m) #cerca inferior
    CS = round(Q3 + ((3/2) * DIQ),m) #cerca superior 
    x_max = round(max(lista_xis),m) if max(lista_xis) > CS else ''#maior valor
    x_min = round(min(lista_xis),m) if min(lista_xis) < CI else ''#menor valor

    
    def string_6(valor):
        '''Formata uma string com len = 6'''
        string = str(valor)
        new_string = string[::-1]
        while len(new_string) < 6:
            new_string = new_string + ' '
        return new_string[::-1]

    s1 = string_6(x_max)
    s2 = string_6(round((x_max+CS)/2,m)) if x_max != '' else string_6(round(CS+DP,m))
    s3 = string_6(CS)
    s4 = string_6(float(Q3))
    s5 = string_6(Q2)
    s6 = string_6(float(Q1))
    s7 = string_6(CI)
    s8 = string_6(round((CI+x_min)/2,m)) if x_min != '' else string_6(round(CI-DP,m))
    s9 = string_6(x_min)
        

    print(                                  '          _____________________________________________________')
    print(                                  '         |                                                     |')
    print(                                  '         |                      \u00d7{}'.format(s1),'                       |')
    print(                                  '         |                                                     |')
    print(' ',s2,                           '|_                                                    |')
    print(                                  '         |                                                     |')
    print(                                  '         |           ___________________________  {}'.format(s3),'      |', ' --> CS')
    print(                                  '         |                        |                            |')
    print(' ',s4,                           '|_       ________________|_________________           |', ' --> Q3')
    print(                                  '         |       |                                  |          |')
    print(                                  '         |       |                                  |          |')
    print(                                  '         |       |----------------------------------| \u2022{}  |'.format(s5), ' --> Q2')
    print(                                  '         |       |                                  |          |')
    print(' ',s6,                           '|_      |__________________________________|          |', ' --> Q1')
    print(                                  '         |                        |                            |')
    print(                                  '         |           _____________|______________ {}'.format(s7),'      |', ' --> CI')
    print(                                  '         |                                                     |')
    print(' ',s8,                           '|_                                                    |')
    print(                                  '         |                                                     |')
    print(                                  '         |                      \u00d7{}'.format(s9),'                       |')
    print(                                  '         |_____________________________________________________|')
               




def covariancia_amostral(*Amostra):
    '''Calcula e retorna a covariância amostral de duas amostras x e y
        *list,*list --> float'''
    
    if len(Amostra) == 0:
        print('')
        print(" # É IMPORTANTE destacar que a covariância amostral é uma relação entre ")
        print("   duas variáveis x e y; e portanto devem ser inseridas duas listas;")
        print("   de maneira que a ordem dessa lista não é necessariamente sempre crescente")
        print('')
        print("Insira a amostra de Xi's (separados por vírgula, sem colchetes e sem espaço): ")
        xis = input()
        lista_xis = [int(i) for i in xis.split(',')]
        print("Insira a amostra de yi's (separados por vírgula, sem colchetes e sem espaço): ")
        yis = input()
        lista_yis = [int(i) for i in yis.split(',')]
        print('')
        print("A covariância amostral é: ")
        
    elif len(Amostra) > 1:
        lista_xis = Amostra[0]
        lista_yis = Amostra[1]   

    n = len(lista_xis)
    
    m = Amostra[2] if len(Amostra) == 3 else 4  #CASAS DECIMAIS PARA ARREDONDAR
    
    med_x = sum(lista_xis)/n #media aritimetica
    med_y = sum(lista_yis)/n #media aritimetica
    soma = 0
    
    for i in range(1,n+1):
        soma = soma + ((lista_xis[i-1] - med_x)*(lista_yis[i-1]-med_y))

    cov_a = soma/(n-1)

    return round(cov_a,m)



def correlacao_amostral(*Amostra):
    '''Calcula e retorna o coeficiente de correlação amostral de duas amostras x e y
        *list,*list --> float'''
    
    if len(Amostra) == 0:
        print('')
        print(" # É IMPORTANTE destacar que a correlação amostral é uma relação entre ")
        print("   duas variáveis x e y; e portanto devem ser inseridas duas listas;")
        print("   de maneira que a ordem dessa lista não é necessariamente sempre crescente")
        print('')
        print("Insira a amostra de Xi's (separados por vírgula, sem colchetes e sem espaço): ")
        xis = input()
        lista_xis = [int(i) for i in xis.split(',')]
        print("Insira a amostra de yi's (separados por vírgula, sem colchetes e sem espaço): ")
        yis = input()
        lista_yis = [int(i) for i in yis.split(',')]
        print('')
        print("O coeficiente de correlação amostral é: ")
        
    elif len(Amostra) > 1:
        lista_xis = Amostra[0]
        lista_yis = Amostra[1]   

    n = len(lista_xis)
     
    m = Amostra[2] if len(Amostra) == 3 else 4  #CASAS DECIMAIS PARA ARREDONDAR
    
    r_xy = covariancia_amostral(lista_xis,lista_yis,m)/(analise_geral(lista_xis,m)['DP']*analise_geral(lista_yis,m)['DP'])

    return round(r_xy,m)



def reta_regressao(*Amostras):
    '''Calcula e retorna a reta de regressão linear de duas amostras x e y
        *list,*list --> float'''
    
    if len(Amostras) == 0:
        print('')
        print(" # É IMPORTANTE destacar que para calcular a reta de regressão entre ")
        print("   duas variáveis x e y, é necessário que sejam inseridas duas listas;")
        print("   de maneira que a ordem dessa lista não é necessariamente sempre crescente")
        print('')
        print("Insira a amostra de Xi's (separados por vírgula, sem colchetes e sem espaço): ")
        xis = input()
        lista_xis = [int(i) for i in xis.split(',')]
        print("Insira a amostra de yi's (separados por vírgula, sem colchetes e sem espaço): ")
        yis = input()
        lista_yis = [int(i) for i in yis.split(',')]
        print('')
        print("A reta de regreessão linear é: ")
        
    elif len(Amostras) > 1:
        lista_xis = Amostras[0]
        lista_yis = Amostras[1]

    n = len(lista_xis)    
    m = Amostras[2] if len(Amostras) == 3 else 4  #CASAS DECIMAIS PARA ARREDONDAR

    beta = covariancia_amostral(lista_xis,lista_yis,m)/(analise_geral(lista_xis,m)['variancia'])
    alfa = analise_geral(lista_yis,m)['media'] - beta * analise_geral(lista_xis,m)['media']
    coeficientes = {'a' : alfa, 'b' : beta}

    if len(Amostras) == 3:
        return coeficientes
    else:
        print('')
        print("  Y =  b X + a  ")
        print('')
        print("  Y = {}X + {}  ".format(round(beta,m),round(alfa,m)))


def analise_geral2(*Amostras):
    '''Imprime todos valores para análise de duas amostras X e Y:
        (1)- Covariância amostral
        (2)- Coeficiente de correlação amostral 
        (3)- Reta de regressão - Método dos mínimos quadrados
        '''
    
    if len(Amostras) == 0:
        print('')
        print(" # É IMPORTANTE destacar que para calcular a reta de regressão entre ")
        print("   duas variáveis x e y, é necessário que sejam inseridas duas listas;")
        print("   de maneira que a ordem dessa lista não é necessariamente sempre crescente")
        print('')
        print("Insira a amostra de Xi's (separados por vírgula, sem colchetes e sem espaço): ")
        xis = input()
        lista_xis = [int(i) for i in xis.split(',')]
        print("Insira a amostra de yi's (separados por vírgula, sem colchetes e sem espaço): ")
        yis = input()
        lista_yis = [int(i) for i in yis.split(',')]
        print('')
        
    elif len(Amostras) > 1:
        lista_xis = Amostras[0]
        lista_yis = Amostras[1]

    return


    if len(Amostras) == 3:
        return {
            'media':med,'mediana':Q2,'moda':moda,
            'variancia':var_A,'DP':DP,'cv':cv,
            'Q1':Q1,'Q3':Q3,'DIQ':DIQ,
            'CI':CI,'CS':CS,'discrepantes':discrepantes,
            'maximo':x_max,'minimo':x_min
        }
    else:
        informacoes = {
            '(1) MEDIDAS DE CENTRALIDADE': '',
            '   Média Aritimética (x\u0304)  = ' : med,
            '   Mediana (Q2)  = ' : Q2,
            '   Moda = ': moda,
            '':'',
            '(2) MEDIDAS DE DISPERSÃO': '',
            '   Variância (s²)  = ' : var_A,
            '   Desvio Padrão (s)  = ' : DP,
            '   Coeficiente de variacao (c\u03c5)  = ' : cv,
            ' ':' ',
            '(3) QUARTIS': '',   
            '   1º Quartil (Q1)  = ' : Q1,
            '   3º Quartil (Q3)  = ' : Q3,
            '   Distância interquartil (DIQ)  = ': DIQ,
            '  ':'  ',
            '(4) DISCREPÂNCIA': '', 
            '   Cerca inferior (CI)  = ' : CI,
            '   Cerca superior (CS)  = ' : CS,
            '   Valores discrepantes = ' : discrepantes,
            '   ':'   ',
            '(5) MAX E MIN': '',
            '   Valor max.  = ': x_max,
            '   Valor min.  = ': x_min
        }
        print('')
        for i in informacoes:
            print(i,informacoes[i])
            print('')
    




#- - - - - - - - - - - - - - - - - AULA 15 - - - - - - - - - - - - - - - - - -#



