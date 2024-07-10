##
##             MÉTODOS NUMÉRICOS APLICADOS (EQE358)                   
##      Procedimentos gerais para todos os métodos numéricos
## 
##

from sympy import Symbol,diff,integrate,Number,log


def derivada(f,variable=Symbol('x'),n=1):
    ''' Calcula e retorna a enésima derivada de uma função qualquer f
    function, Symbol, int --> function '''
    
    for i in range(n):
        f = diff(f,variable)
    return f


def integral(f,var,definida=[]):
    ''' Calcula e retorna a integral de uma função f qualquer
    function, Symbol, list(float,float)'''
    
    if definida != []:
        I = integrate(f,(var,definida[0],definida[1]))
    else:
        I = integrate(f,var)
    return I


def arredondar_expr(eq, num_digitos):
    ''' Arredonda uma expressão do SymPy'''
    return eq.xreplace({n : round(n, num_digitos) for n in eq.atoms(Number)})


def avaliar(f,x0s,variables=Symbol('x'),casas_decimais=20):
    ''' Calcula e retorna o valor de uma função f avaliada em x0
    function,  list[float, float, ...],  list[Symbol, Symbol, ...],  float  -->  float'''
    
    if type(x0s)!= list:
        if type(x0s)!=tuple:
            x0s=[x0s]
    if type(variables)!=list:
        if type(variables)!=tuple:
            variables=[variables]
    if len(x0s)!= len(variables):
        raise Exception("O número de variáveis e valores deve ser igual.")
    
    return f.evalf(subs={var:float(x0) for x0,var in zip(x0s,variables)},n=casas_decimais)


def mudar_variavel(f,vars_antigas,vars_novas):
    ''' Realiza uma mudança de variáveis em uma função f 
    
    function,  list[Symbol, ...],  list[Symbol, ...]  -->  function'''

    if type(vars_antigas)!= list:
        if type(vars_antigas)!=tuple:
            vars_antigas=[vars_antigas]
    if type(vars_novas)!=list:
        if type(vars_novas)!=tuple:
            vars_novas=[vars_novas]
    if len(vars_antigas)!= len(vars_novas):
        raise Exception("O número de variáveis antigas e novas deve ser igual.")

    return f.subs({antiga:nova for antiga,nova in zip(vars_antigas,vars_novas)})


def prova_real(funcoes,variaveis,raizes,tolerancia):
    ''' Verifica se o método foi capaz de achar uma "raíz" coerente
    com a tolerância definida

    list[function,...], list[Symbol,...], list[float,...]
    --> bool'''
    
    lista_bool = []
    for f in funcoes:
        lista_bool.append(abs(avaliar(f,raizes,variaveis)) <= tolerancia)
    if all(lista_bool):
        return True
    return False



def casas_decimais_significativas(raizes,funcoes,variaveis,tolerancia):
    ''' list, list(Add), list, float --> int '''

    casas_decimais = 0
    while True:
        r = [round(raiz,casas_decimais) for raiz in raizes]
        if prova_real(funcoes,variaveis,r,tolerancia) == True:
            break
        casas_decimais+=1
    return casas_decimais


def mini_temporizador():
    for i in range(100000000):
        pass

def adicionar_a_lista(lista,quantidade,item=0):
    n = quantidade-len(lista) 
    for i in range(n):
        lista.append(item)





## Estatística

def media(amostra):
    ''' Retorna a média aritmética de uma amostra de dados
    list[float,float,...] --> float'''

    return sum(amostra)/len(amostra)

def variancia_amostral(amostra):
    ''' Retorna a variância corrigida de uma amostra de dados
    list[float,float,...] --> float'''
    
    med = media(amostra)
    n = len(amostra)
    soma = sum([(amostra[i]-med)**2 for i in range(n)])  
    return soma/(n-1)

def desvio_padrao_amostral(amostra):
    ''' Retorna o desvio padrão em torno da média de uma amostra de dados
    list[float,float,...] --> float'''
    
    return (desvio_padrao_amostral(amostra))**(1/2)





## Matrizes

def constroi_matriz(m,n):
    '''Constroi uma matriz com m linhas e n colunas, 
    com todos seus elementos sendo 0.
    int, int --> list'''

    Matriz = []
    for i in range(m):
        Matriz.append([])
        for j in range(n):
            Matriz[i].append(0)
    #for lista in Matriz: print(lista)
    return Matriz



def identidade(n=2):
    '''Retorna a matriz identidade com n linhas/colunas
    Valor padrão de n: 2
        int --> list(list,list,...)'''
    
    I = []
    for i in range(n):
        Im = []
        for j in range(n):
            Im = Im + ([1] if i==j else [0])
        I.append(Im)
    return I



def copia_matriz(A):
    '''Retorna uma cópia da matriz inserida'''  
    linhas = len(A)
    colunas = len(A[0])
    B = constroi_matriz(linhas, colunas)
 
    for i in range(linhas):
        for j in range(colunas):
            B[i][j] = A[i][j]

    return B
 

def soma_matrizes(A,B,operador):
    '''Calcula e retorna a soma (+ ou -) de duas matrizes, A e B
        C = A +/- B
        list[list,list,...] , list(list,list,...) --> list(list,list,...)'''

    C = []#= A+-B
    i = 0
    for linha in A:
        Cm = []
        j = 0
        for Aij in linha:
            soma = eval(f"Aij {operador} B[i][j]")
            Cm.append(soma)
            j+=1
        C.append(Cm)
        i+=1
    return C



def adicao_matrizes(A,B):
    '''Calcula e retorna a adição de duas matrizes, A e B
        C = A+B
        list[list,list,...] , list(list,list,...) --> list(list,list,...)'''
    
    return soma_matrizes(A,B,'+')



def subtracao_matrizes(A,B):
    '''Calcula e retorna a subtração de duas matrizes, A e B
        C = A-B
        list[list,list,...] , list(list,list,...) --> list(list,list,...)'''
    
    return soma_matrizes(A,B,'-')



def transposta(A):
    '''Calcula e retorna a matriz transposta de A'''
    
    A1 = A if type(A[0]) == list else [A]
    
    return [[A1[j][i] for j in range(len(A1))] for i in range(len(A1[0]))]


def multiplicacao_escalar(A,k,casas_decimais=0):
    '''Calcula e retorna a multiplicação de uma matriz Amxn por um real k
    list(list,list,...), float --> list(list,list,...)'''

    B = []
    for linha in A:
        Bm = []
        for Aij in linha:
            if casas_decimais != 0:
                Bm.append(round(Aij*k,casas_decimais))
            else:
                Bm.append(Aij*k)
        B.append(Bm)
    return B          


def multiplicacao_matrizes(A,B):
    '''Calcula e retorna a multiplicação de matrizes Amxn e Bkxm'''
    aprox = 10 # casa decimais para aproximar

    if len(A[0]) != len(B):
        raise ArithmeticError(
            "O número de colunas da matriz A deve ser igual ao número de linhas da matriz B")

    C = []
    for linha_A in A:
        Cm = []
        for linha_B in transposta(B):  #= B
            Cij = 0
            for i in range(len(linha_A)):
                    Cij += linha_A[i]*linha_B[i]
            Cm.append(round(Cij,aprox))
        C.append(Cm)
    return C


def multiplica_matrizes(*Matrizes):
    '''Retorna o produto da multiplicação de n matrizes
    list[list,...], list[list,...], ... --> list[list,...]'''

    multiplicacao = Matrizes[0]
    for matriz in Matrizes[1:]:
        multiplicacao = multiplicacao_matrizes(multiplicacao,matriz)
    return multiplicacao


def escalonamento_parcial(A):
    '''Escalona a matriz A até sua forma diagonal superior
    list[list,list,...] --> list[list,list,...]'''
    B = copia_matriz(A)
    n = len(B)
    for d in range(n): 
        for i in range(d+1,n): # B) Só são alteradas as linhas abaixo da linha de 'd'
            if B[d][d] == 0: # C) Se d é zero  ...
                B[d][d] == 1.0e-18 # Mudemos para ~zero
            escala = B[i][d] / B[d][d] 
            for j in range(n): 
                B[i][j] = B[i][j] - escala * B[d][j]
    return B

    
def escalonamento_completo(A):
    '''Escalona completamente a matriz A'''
    B = copia_matriz(A)

    def eliminar(linha1, linha2, coluna, alvo=0):
        '''Função auxiliar para o escalonamento'''
        fac = (linha2[coluna]-alvo) / linha1[coluna]
        for i in range(len(linha2)):
            linha2[i] -= fac * linha1[i]

    for i in range(len(B)):
        if B[i][i] == 0:
            for j in range(i+1, len(B)):
                if B[i][j] != 0:
                    B[i], B[j] = B[j], B[i]
                    break
        for j in range(i+1, len(B)):
            eliminar(B[i], B[j], i)
    for i in range(len(B)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminar(B[i], B[j], i)
    for i in range(len(B)):
        eliminar(B[i], B[i], i, alvo=1)
    return B



def menor_complementar(A,i,j):
    '''Função auxiliar para o calculo do determinante e da inversa
    list[list,list,...], int, int --> list[list, list,...]'''
    return [linha[:j] + linha[j+1:] for linha in (A[:i]+A[i+1:])]


def determinante(A):
    '''Retorna o determinante de uma matriz A
    list(list,list,list,...) --> float'''
    if len(A) == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    det = 0
    for c in range(len(A)):
        det += ((-1)**c)*A[0][c]*determinante(menor_complementar(A,0,c))
    return det


def inversa(A):
    '''Retorna a matriz inversa de A
    list[list,list,...] --> list[list,list,...]''',
    
    det = determinante(A)
    
    #Para uma matriz 2x2:
    if len(A) == 2:
        return [[A[1][1]/det, -1*A[0][1]/det],
                [-1*A[1][0]/det, A[0][0]/det]]

    cofatores = []
    for linha in range(len(A)):
        cofator_linha = []
        for coluna in range(len(A)):
            menor = menor_complementar(A,linha,coluna)
            cofator_linha.append(((-1)**(linha+coluna)) * determinante(menor))
        cofatores.append(cofator_linha)
        
    cofatores = transposta(cofatores)
    for linha in range(len(cofatores)):
        for coluna in range(len(cofatores)):
            cofatores[linha][coluna] = cofatores[linha][coluna]/det
    return cofatores


