##
##      MÉTODOS NUMÉRICOS APLICADOS (EQE358) - MÓDULO V                    
## Procedimentos gerais relacionados ao Módulo V da diciplina
## 
##                 Sistemas de equações lineares
##          Regra de Cramer, Eliminação de Gauss-Jordan
##

from sympy import Symbol


#### Número de variáveis ####

n_de_variaveis = 3
''' x1, x2, ... '''


#### Dados ####

# Equações, entre aspas, separadas por vírgula
equacoes = [    '3/10*x1+0.52*x2+x3=-0.01',
                '0.5*x1+x2+1.9*x3=0.67',
                '0.1*x1+0.3*x2+0.5*x3=-0.44'
]

# Erro aceitável  -- Limite de precisão (provisório) = 10^-10 (para 2 funções e 2 variáveis)
tolerancia = 10**(-2)                       

# True para usar o método de newton modificado (jacobiana única)
metodo_modificado = True





################## PROCEDIMENTOS ##################

## Procedimentos Gerais
from .procedimentos_gerais import (
    derivada,
    avaliar,
    prova_real,
    casas_decimais_significativas,
    copia_matriz,
    determinante,
    escalonamento_completo as escalonamento
)



def mostrar_matriz(matriz):
    ''' Imprime uma matriz linha por linha

    list[list,...] --> None'''
    
    for linha in matriz: print(linha)



def jacobiana(funcoes,variaveis,pontos_conhecidos):
    ''' Retorna a matriz jacobiana de um conjunto de funções e variáveis,
    calculada em pontos conhecidos.
    
    list[funtion,...], list[Symbol,...], list[float,...] --> Matriz'''
    
    
    Matriz = []
    for j in range(len(funcoes)):            
        linha = []
        for i in range(len(variaveis)):
            linha.append(avaliar(derivada(funcoes[j],variaveis[i],1),pontos_conhecidos,variaveis))
        Matriz.append(linha)
    return Matriz
    


def mescla_matriz_vetor(matriz,vetor,coluna):
    ''' Retorna a mescla de uma matriz com um vetor, em uma
    determinada coluna'''

    matriz = copia_matriz(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][coluna] = vetor[i][0]
    return matriz



def junta_matriz_vetor(matriz,vetor):
    ''' Retorna a junção de uma matriz com um vetor,
    (vetor será inserido à direita da matriz)'''

    matriz = copia_matriz(matriz)
    for linha in range(len(matriz)):
        matriz[linha].append(vetor[linha][0])
    return matriz


def extrai_coluna_matriz(matriz,coluna):
    ''' Extrai e retorna uma determinada coluna de uma matriz '''

    col = []
    for linha in matriz:
        col.append(linha[coluna])
    return col
    


def monta_vetor(lista):
    ''' Transforma uma lista em um vetor (list[list,...])'''
    
    return [[lista[i]] for i in range(len(lista))]



def vetor_resposta(equacoes):
    ''' Retorna o vetor de resposta de um sistema de equações'''
    
    vetor = []
    
    for equacao in equacoes:
        variaveis = list(equacao.atoms(Symbol))
        n_variaveis = len(variaveis)
        
        for i in range(n_variaveis):
            equacao = equacao.coeff(variaveis[i],0)
            
        vetor.append(-equacao)
        
    return monta_vetor(vetor)


def vetor_variaveis(variaveis):
    ''' Retorna o vetor de variáveis de um sistema de equações'''

    return monta_vetor(variaveis)


def matriz_de_coeficientes(equacoes,variaveis):
    ''' Retorna a matriz de coeficientes de um sistema de equações'''
    
    matriz = []
    n_de_variaveis = len(variaveis)
    
    for equacao in equacoes:
        linha = []
        
        for i in range(n_de_variaveis):
            linha.append(equacao.coeff(variaveis[i],1))
            
        matriz.append(linha)
        
    return matriz

#

## REGRA DE CRAMER

def cramer(equacoes,variaveis,tolerancia=tolerancia):
    ''' Aplica o a Regra de Cramer para resolver um sistema linear '''

    A = matriz_de_coeficientes(equacoes,variaveis)
    X = vetor_variaveis(variaveis)
    b = vetor_resposta(equacoes)

    det_A = determinante(A)
    if abs(det_A) <= tolerancia**2:
        return "Sistema mal-condicionado"

    raizes = []
    for i in range(len(variaveis)):
        Ab = mescla_matriz_vetor(A,b,i)
        det_Ab = determinante(Ab)
        
        v_i = det_Ab/det_A  
        raizes.append(v_i)

    if not prova_real(equacoes,variaveis,raizes,tolerancia):
        return raizes," Não foi possível achar uma solução "

    n = casas_decimais_significativas(raizes,equacoes,variaveis,tolerancia)
    raizes = [round(raiz,n) for raiz in raizes]
    
    return raizes,''

#

## ELIMINAÇÃO DE GAUSS JORDAN 


def eliminacao_gauss_jordan(equacoes,variaveis,tolerancia):

    A = matriz_de_coeficientes(equacoes,variaveis)
    b = vetor_resposta(equacoes)
    Ab = junta_matriz_vetor(A,b)
    matriz_escalonada = escalonamento(Ab)
    raizes = extrai_coluna_matriz(matriz_escalonada,-1)
    
    if not prova_real(equacoes,variaveis,raizes,tolerancia):
        return raizes," Não foi possível achar uma solução "

    n = casas_decimais_significativas(raizes,equacoes,variaveis,tolerancia)
    raizes = [round(raiz,n) for raiz in raizes]
    
    return raizes,''

#



#########################################################################


def main():

    ret = eliminacao_gauss_jordan(lista_fs,lista_variaveis,tolerancia)
    #ret = cramer(lista_fs,lista_variaveis,tolerancia)
    try:
        print('')
        print(' Sistema:  {','\n           { '.join(f"{str(f).replace('**','^')} = 0" for f in lista_fs),'\n')
        print(" Raízes:  ", '\n           '.join(f" {lista_variaveis[i]} = {ret[0][i]}" for i in range(len(ret[0]))))
        print('')
    except:
        print(" Não foi possível encontrar uma solução ")
    return ret
            
if __name__ == "__main__":
    
    #NÃO ALTERAR
    lista_variaveis = []
    for i in range(1,n_de_variaveis+1): 
        exec(f"x{i} = Symbol(f'x{i}')")
        exec(f"lista_variaveis.append(x{i})")
        
    lista_fs = []
    for i in range(len(equacoes)):
        if '=' in equacoes[i]: 
            k = equacoes[i].split('=')[1]
            exec(f"equacoes[i] = equacoes[i].split('=')[0]")
        exec(f"f{i+1} = {equacoes[i].replace('^','**')} - {k}")
        exec(f"lista_fs.append(f{i+1})")
        del(k)
    del(equacoes)

    ############
        
    ret = main()
    try:
        for i in range(len(ret[0])):
            exec(f"global X{i+1}")
            exec(f"X{i+1} = {ret[0][i]}")
    except:
        pass
    del(i)
    input()
