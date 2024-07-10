#                        Funções álgebra Linear II


#DADOS:
a = [
	[1,4,5],
	[2,7,6],
	[3,7,8]
]

b = [
	[1,2,3],
	[4,7,7],
	[5,6,8]
]

c = [
        [3,5,2],
        [5,7,-1],
        [9,1,0]
]


#FUNÇÕES

import math
sqrt = math.sqrt

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
    from Algebra_Linear_II import constroi_matriz
    
    linhas = len(A)
    colunas = len(A[0])
    B = constroi_matriz(linhas, colunas)
 
    for i in range(linhas):
        for j in range(colunas):
            B[i][j] = A[i][j]

    return B
 


def soma_matrizes(A,B):
    '''Calcula e retorna a adição de duas matrizes, A e B
        C = A+B
        list[list,list,...] , list(list,list,...) --> list(list,list,...)'''
    
    C = []#= A+B
    i = 0
    for linha in A:
        Cm = []
        j = 0
        for Aij in linha:
            soma = Aij + B[i][j]
            Cm.append(soma)
            j+=1
        C.append(Cm)
        i+=1
    return C


def subtracao_matrizes(A,B):
    '''Calcula e retorna a subtração de duas matrizes, A e B
        C = A-B
        list[list,list,...] , list(list,list,...) --> list(list,list,...)'''
    
    C = []#= A-B
    i = 0
    for linha in A:
        Cm = []
        j = 0
        for Aij in linha:
            soma = Aij - B[i][j]
            Cm.append(soma)
            j+=1
        C.append(Cm)
        i+=1
    return C



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
    from Algebra_Linear_II import transposta

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
    '''Retorna o produto da multiplicação de n matrizes'''

    multiplicacao = Matrizes[0]
    for matriz in Matrizes[1:]:
        multiplicacao = multiplicacao_matrizes(multiplicacao,matriz)
    return multiplicacao


def escalonamento(A):
    '''Escalona a matriz A até sua forma diagonal superior'''
    from Algebra_Linear_II import copia_matriz
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
    from Algebra_Linear_II import copia_matriz
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



def menor_matriz(A,i,j):
    '''Função auxiliar para o calculo do determinante'''
    return [linha[:j] + linha[j+1:] for linha in (A[:i]+A[i+1:])]


def determinante(A):
    '''Retorna o determinante de uma matriz A
    list(list,list,list,...) --> float'''
    from Algebra_Linear_II import menor_matriz
    if len(A) == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    det = 0
    for c in range(len(A)):
        det += ((-1)**c)*A[0][c]*determinante(menor_matriz(A,0,c))
    return det


def inversa(A):
    '''Retorna a matriz inversa de A'''
    from Algebra_Linear_II import menor_matriz
    from Algebra_Linear_II import determinante
    det = determinante(A)
    #Caso especial para matriz 2x2:
    if len(A) == 2:
        return [[A[1][1]/det, -1*A[0][1]/det],
                [-1*A[1][0]/det, A[0][0]/det]]

    cofatores = []
    for linha in range(len(A)):
        cofator_linha = []
        for coluna in range(len(A)):
            menor = menor_matriz(A,linha,coluna)
            cofator_linha.append(((-1)**(linha+coluna)) * determinante(menor))
        cofatores.append(cofator_linha)
    cofatores = transposta(cofatores)
    for linha in range(len(cofatores)):
        for coluna in range(len(cofatores)):
            cofatores[linha][coluna] = cofatores[linha][coluna]/det
    return cofatores










    

## Vetores

def vetor_matriz(v):
    '''Retorna a matriz associada ao vetor v
    list --> list(list)'''
    u = []
    for vi in v:
        u.append([vi])
    return u


def produto_interno(u,v):
    '''Calcula e retorna o produto interno de dois vetores u e v de mesma dimensão
        list , list --> int'''

    u = [u[i][0] for i in range(len(u))] if type(u[0]) == list else u
    v = [v[i][0] for i in range(len(v))] if type(v[0]) == list else v

    
    PI = 0 # = A × B
    if len(u) == len(v):
        for i in range(len(u)):
            PI += u[i]*v[i]
        return PI
    else:
        print("Os vetores devem ter a mesma dimensão")



def norma2(v):
    '''Calcula e retorna a norma ao quadrado de um vetor v
    list --> int'''
    from Algebra_Linear_II import produto_interno

    u = v[0] if type(v[0]) == list and len(v) == 1 else v
    
    return produto_interno(u,u)



def norma(v):
    '''Calcula e retorna a norma (comprimento) de um vetor v
    list --> int'''
    from Algebra_Linear_II import norma2
    
    return sqrt(norma2(v))



def normalizar_vetor(v):
    '''Retorna o vetor unitário correspondente à v'''
    if len(v) > 1 and len(v[0]) > 1:
        raise ArithmeticError(
            'O vetor deve estar descrito como vetor-linha ou vetor-coluna')
    linhas = len(v); colunas = len(v[0])
    norma = 0
    for linha in v:
        for valor in linha:
            norma += valor**2
    norma = sqrt(norma)
    vetor_normal = copia_matriz(v)
    for i in range(linhas):
        for j in range(colunas):
            vetor_normal[i][j] = vetor_normal[i][j]/norma
    return vetor_normal





def reflexaor3(a,b,c,d=0,v=[],casas_decimais=4):
    '''Retorna a matriz de reflexão pelo plano ax+by+zc=d
    bem como a reflexão de v nesse plano.'''

    a = round(a,casas_decimais)
    b = round(b,casas_decimais)
    c = round(c,casas_decimais)
    if v == []:
        v = [[a],[b],[c]]
    if type(v) != list:
        v = list(v)
    if type(v[0]) != list:
        v = vetor_matriz(v)
    
    d1 = 1/(a**2+b**2+c**2)
    Rb = [
        [ -(a**2)+(b**2)+(c**2),             -2*(a*b),  -2*(a*c) ],
        [              -2*(a*b), (a**2)-(b**2)+(c**2),   -2*(b*c)],
        [              -2*(a*c),             -2*(b*c), (a**2)+(b**2)-(c**2)]
    ]

    R = multiplicacao_escalar(Rb,d1,casas_decimais)
    v_linha = multiplicacao_matrizes(R,v)
    
    plano = " ({}x) + ({}y) + ({}c) = {}".format(a,b,c,d)
    print(" O vetor v' (Reflexão de v no plano",plano,"  é: ")
    print( v_linha)
    print('')
    print(" A matriz correspondente à reflexão (R) é: ")
    return R



def projecao_ortogonal(w,H):
    '''Calcula e retorna a projeção ortogonal de w em H
    list, list --> dict'''

    projecoes = {}
    Ph = matriz_projecao_reta(H)
    Pht = subtracao_matrizes(identidade(len(Ph)),Ph)


    
    return projecoes

# NAO TA FUNCIONANDO DIREITO    
H = [[1], [2], [-1], [0], [2]]
def matriz_projecao_reta(H):
    '''Retorna as matrizes de projeção ortogonal nas retas H e H⊥
    onde v é um vetor de H
    list --> dict'''

    v = H[0] if type(H[0]) == list and len(H[0]) != 1 else ([H] if type(H[0]) != list else H)       
    
    numerador = multiplicacao_matrizes(v,transposta(v))
    Ph = multiplicacao_escalar(numerador,1/(norma2(v)))

    return Ph








