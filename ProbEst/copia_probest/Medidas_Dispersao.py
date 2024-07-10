## MEDIDAS DE DISPERSÃO - ESTATÍSTICA
## Variância, Desvio padrão e Coeficiente de variação

from . import Medidas_Centralidade


def variancia(amostra):
    ''' Retorna a variância amostral de uma amostra (lista de floats) '''
    med = Medidas_Centralidade.media(amostra)
    n = len(amostra)
    variancia_amostral = sum([(i - med)**2 for i in amostra]) / (n-1)
    return variancia_amostral


def desvio_padrao(amostra):
    ''' Retorna o desvio padrão de uma amostra (lista de floats) '''
    dp = (variancia(amostra))**(1/2)
    return dp


def coeficiente_variacao(amostra):
    ''' Retorna o coeficiente de variacao de uma amostra (lista de floats) '''
    cv = desvio_padrao(amostra)/Medidas_Centralidade.media(amostra)
    return cv


def covariancia_amostral(X,Y):
    ''' Retorna a covariância amostral entre duas amostras X,Y
    (listas de floats)'''
    n = len(X)
    if n!=len(Y):
        raise ValueError(" O tamanho das amostras deve ser igual ")
    
    media_x = Medidas_Centralidade.media(X)
    media_y = Medidas_Centralidade.media(Y)
    soma = 0
    for i in range(n):
        soma += ((X[i] - media_x)*(Y[i]-media_y))
 
    cov_a = soma/(n-1)
    return cov_a


def correlacao_amostral(X,Y):
    '''Retorna o coeficiente de correlação amostral (r) de duas amostras X e Y
    (listas de floats)'''
    try:
        R = covariancia_amostral(X,Y)/(desvio_padrao(X)*desvio_padrao(Y))
    except ZeroDivisionError:
        R = 0
    return R