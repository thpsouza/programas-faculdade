## ESTIMADORES PONTUAIS - ESTATÍSTICA
## Média amostral, proporção amostral, erros absolutos

from . import Normal
from . import Medidas_Centralidade, Medidas_Dispersao

## EM REVISÃO
def analise_amostra(*amostra,a=None,b=None,**distribuicao):
    ''' Faz a analise de uma determinada amostra

    amostra         -->     lista com os dados;

    a               -->     a para calcular P(a<=X) e P(a>=X)
    b               -->     a e b para calcular P(a<=X<=b)

    distribuicao    -->     n (tamanho da amostra)
                            mu (media),
                            sigma2 (variancia),
    '''
    ## Se for passada a amostra, calcula os dados
    if amostra != ():
        n = len(amostra)
        mu = Medidas_Centralidade.media(amostra)
        sigma2 = Medidas_Dispersao.variancia(amostra)
    ## Se for passada a distribuicao, guarda os dados
    elif distribuicao != {}:
        try:
            n = distribuicao['n']
            mu = distribuicao['mu']
            sigma2 = distribuicao['sigma2']
        # Se a o tamanho da amostra, a média e a variancia não forem passados, lança um erro
        except KeyError:
            raise TypeError(" Distribuicao requer os seguintes argumentos: n, mu, sigma2 ")
            
    ## Se não for passado nenhum argumento, lança um erro
    else:
        raise TypeError("analise_amostra() precisa de ao menos 1 argumento. Nenhum foi passado")

    ## Análise
    sigma2 = sigma2/n
    if a:
        z,z_1 = Normal.probabilidade_normal(mu,sigma2,x1=a)
##

def prob_erro_absoluto_media(sigma,n,d,maior=False):
    ''' Retorna a probabilidade P(|X-mu|<=d)
        OBS:  maior = True para P(|X-mu|>=d)'''
    P = 2*Normal.fda_padrao(d/(sigma/n**(1/2)))-1
    return abs(maior-P) 


def prob_erro_absoluto_proporcao(n,d,maior=False):
    ''' Retorna a probabilidade P(|_p_-p|<=d)
        OBS:  maior = True para P(|_p_-p|>=d)'''
    P = 2*Normal.fda_padrao(2*d*n**(1/2))-1
    return abs(maior-P)


def inversa_media_amostral(p,maior=False):
    ''' Retorna δ tal que P(|X|<=δ) = p
        OBS:  maior = True para P(|X|>=δ) = p'''
    if maior: p = 1-p
    delta = 2*Normal.inversa_normal(1-(1-p)/2)
    return delta
    

construcao = [

#def inversa_proporcao_amostral(p,maior=False):
#    ''' Retorna δ tal que P(|X|<=δ) = p
#    OBS:  maior = True para P(|X|>=δ) = p'''
#    if maior: p = 1-p
#    delta = 2*Normal.inversa_normal(1-(1-p)/2)
#    return delta
#
#
#def vies_estimador(estimador,parametro):
#    ''' Retorna o vies de um estimador '''
#    return estimador-parametro
#
#
#def variancia_estimador(estimador,parametro,media): #EM CONSTRUÇÃO
#    ''' Retorna a variancia de um estimador
#
#        estimador   --> sympy expression
#        parametro   --> sympy symbol(cls=Function)
#        media       --> sympy symbol
#    '''
#    from sympy import summation, symbols
#    i, n = symbols("mu i n")
#    return summation((parametro(i)-media)**2,(i,1,n))/(n-1)
#
#
#def erro_quadratico_medio(estimador): #EM CONSTRUÇÃO
#    ''' Retorna o erro quadrático médio de um estimador '''
#    return 
]

