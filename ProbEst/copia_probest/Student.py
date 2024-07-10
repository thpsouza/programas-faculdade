## DISTRIBUIÇÃO NORMAL - PROBABILIDADE
## Função de distribuição acumulada, Calculos de probabilidade

from scipy.stats import t


def inversa_t(p,graus_de_liberdade,maior=False):
    ''' 
    Retorna o valor de t tal que P(X <= t) = p, com n-1 graus de liberdade,
    sendo X ~ T(n-1).

    OBS:  maior = True para P(X >= x) = p
    '''
    if maior: p = 1-p
    return t.ppf(p,graus_de_liberdade)