## ESTIMADORES INTERVALARES - ESTATÍSTICA
## Intervalos de confiança

from . import Student,Normal
from . import Medidas_Centralidade as mc, Medidas_Dispersao as md

def intervalo_confianca_media(*amostra,p,**distribuicao):
    ''' 
    Intervalo de valores que contem o verdadeiro parametro da media, com uma probabilidade p

    Parametros
    ----------

    amostra: list, opcional
        Dados amostrais
    
    p: float
        Nivel de confianca para o calculo

    distribuicao:
        n: int, opcional
            Tamanho da amostra
        media: float, opcional
            Media amostral
        sigma2: float,opcional
            Variancia amostral

    OBS: 
        Se a amostra for passada, n sera calculado a partir dela

        Se a amostra for passada, a media sera calculada a partir dela.
        
        Se a variancia não for passada, sera estimada a partir da amostra. 
               
    '''  
    
    ## Obtenção de n e da média amostral
    if amostra:
        amostra = amostra[0]
        media = mc.media(amostra)
        n = len(amostra)
    else:
        media = distribuicao['media']
        n = distribuicao['n']

    ## Se a variancia é conhecida: 
    ## Utiliza-se distribuição Normal
    if 'sigma2' in distribuicao:
        # Atribui o valor à variavel
        sigma2 = distribuicao['sigma2']      

    ## Se a variância é desconhecida: 
    else:
        # Verifica se a amostra não é vazia
        if not amostra: raise mc.AmostraVazia(" Se a variancia for desconhecida, é necessário fornecer uma amostra ")
        # Estima-se a variancia a partir da amostra
        sigma2 = md.variancia(amostra)
    
    # Utiliza-se distribuição t de Student para amostras com n<30
    if n<30:
        # Calcula o t de Student
        c = t = Student.inversa_t(1-(1-p)/2,n-1)
    # Utiliza-se distribuição Normal para amostras com n>=30 (TCL)
    else:
        c = z = Normal.inversa_normal(1-(1-p)/2)

    ## Cálculo limite inferior do intervalo
    inf = media-c*(sigma2/n)**(1/2)
    ## Cálculo limite superior do intervalo
    sup = media+c*(sigma2/n)**(1/2)

    intervalo = [inf,sup]
    return intervalo 


def intervalo_confianca_proporcao(proporcao,p,n,conservativo=False):
    ''' 
    Intervalo de valores que contem o verdadeiro parametro da proporção com uma probabilidade p

    Parametros
    ----------

    proporcao: float
        Proporcao amostral 
    
    p: float
        Nivel de confianca para o calculo

    n: int
        Tamanho da amostra

    conservativo: bool, opcional, padrao=False
        False   --> Calcula o intervalo nao conservativo
        True    --> Calcula o intervalo conservativo   
    '''
    
    ## Cálculo do z
    z = Normal.inversa_normal(1-(1-p)/2)

    ## Se deseja-se o intervalo conservativo:
    if conservativo:
        # Calcula a raiz como o valor máximo possível de proporcao(1-proporcao)
        # OBS: Isso faz com que os intervalos sejam maiores
        raiz = ((1/4)/n)**(1/2)

    ## Caso contrário:
    else:
        # Calcula a raiz estimando a proporcao populacional com a proporcao amostral
        raiz = (proporcao*(1-proporcao)/n)**(1/2)

    ## Cálculo limite inferior do intervalo
    inf = proporcao-z*raiz
    ## Cálculo limite superior do intervalo
    sup = proporcao+z*raiz

    intervalo = [inf,sup]
    return intervalo


def inversa_media(intervalo,n,confianca):
    '''
    '''
    ## Limite inferior do intervalo
    inf = intervalo[0]
    ## Limite superior do intervalo
    sup = intervalo[1]

    ## Significância 
    alpha = 1-confianca

    # Utiliza-se distribuição t de Student para amostras com n<30
    if n<30:
        c = t = Student.inversa_t(1-alpha/2,n-1)
    # Utiliza-se distribuição Normal para amostras com n>=30 (TCL)
    else:
        c = z = Normal.inversa_normal(1-alpha/2)

    media = (inf+sup)/2
    sigma = (sup-inf)/2 * n**(1/2) / c
    
    return media,sigma**2
