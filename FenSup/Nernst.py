import math
import constantes_quimicas


def equacao_nernst(K,Q,n,T=298.15):
    '''
    Calcula a equação de Nernst na forma:

        ΔE = RT/nF * ln{K/Q}

    Ex:
    >>> equacao_nernst()

    '''
    F = constantes_quimicas.F()
    R = constantes_quimicas.R()

    return 