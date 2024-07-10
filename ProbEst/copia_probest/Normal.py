## DISTRIBUIÇÃO NORMAL - PROBABILIDADE
## Função de distribuição acumulada, Calculos de probabilidade

from math import erf,sqrt
from statistics import NormalDist as ND


def fda_padrao(z):
    '''Calcula a função densidade acumulada de uma v.a normal padrão Z
    aplicada em z.
    '''
    return (erf(float(z)/2.0**(1/2))+1)/2

def fda(mu,sigma,x):
    ''' Função de distribuição acumulada de uma distribuição normal (não padronizada) 
    
    Padroniza e chama 'fda_padrao'
    '''
    return fda_padrao((x-mu)/sigma)

def probabilidade_normal(mu,sigma2,**x):
    ''' 
    Retorna as probabilidades P( X <= x ), P( X >= x )
        
    Se x1=...,x2=...: retorna P( x1 <= X <= x2 )
    '''      
    sigma = sigma2**(1/2)

    ## Calcula e retorna P(x1<=X<=x2):
    if len(x)>1:
        z1 = fda(mu,sigma,x['x1']) 
        z2 = fda(mu,sigma,x['x2'])
        z = z2-z1
        return z

    ## Calcula e retorna P(x<=X) e P(X>=x)
    elif len(x)==1:
        z = fda(mu,sigma,x['x1'])
        return z, 1-z

def inversa_normal(p,mu=0,sigma2=1,maior=False):
    ''' Retorna o valor de x tal que P(X <= x) = p, sendo X ~ N(mu,sigma2) 
    OBS:  maior = True para P(X >= x) = p'''
    if maior: p = 1-p
    x = ND(mu,sqrt(sigma2)).inv_cdf(p)
    return x

