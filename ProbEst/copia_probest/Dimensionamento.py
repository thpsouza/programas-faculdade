## DIMENSIONAMENTO DA AMOSTRA - ESTATÍSTICA
## Para média (variancia conhecida), para proporção

from . import Normal


def media(d,alpha,sigma=1,inteiro=True):
    ''' Retorna o tamanho da amostra (n) mínimo necessário para que
    P(|X-mu| <= d) = 1-alpha
    '''
    n = (Normal.inversa_normal(1-alpha/2)*sigma/d)**2
    if not inteiro: 
        return n
    return int(n)+1


def proporcao(d,alpha,p=0.5,relativo=False,inteiro=True):
    ''' Retorna o tamanho da amostra (n) mínimo necessário para que
    P(|_p_-p| <= d) = 1-alpha
    '''
    if relativo:
        n = (Normal.inversa_normal(1-alpha/2)/d)**2*(1-p)/p
    else:
        n = (Normal.inversa_normal(1-alpha/2)/d)**2*p*(1-p)
    if not inteiro: 
        return n
    return int(n)+1


def intervalo(amplitude,confianca,sigma2,inteiro=True):
    ''' Retorna o tamanho da amostra (n) mínimo necessário para que
    um intervalo de confianca tenha a mesma amplitude com outro nível de confianca
    '''
    n = ( 2 * Normal.inversa_normal(1-(1-confianca)/2) * sigma2**(1/2) / amplitude)**2
    if not inteiro: 
        return n
    return int(n)+1