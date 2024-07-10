from math import sqrt, exp, log, pi
from ..geral import Funcao, isalambda, isafunction, isamethod


BRADLEY = 'Bradley'
RIETEMA = 'Rietema'
CBV_DEMCO = 'CBV-Demco'


def eficiencia_granulometrica_reduzida(d:float|Funcao, d50:float, n=3) -> float:
    ## Defesa contra função lambda de entrada, para funcionar acoplado com outras funções    
    if isalambda(d) or isafunction(d) or isamethod(d):
        G = lambda x: 1 - exp(-0.693*(d(x)/d50)**n)
    else:
        G = 1 - exp(-0.693*(d/d50)**n)
    return G


def reynolds(Q,Dc,p,mu):
    return 4*p*Q/(pi*mu*Dc)


def Eu(ciclone, Re, Cv):
    k2, n3, n4 = {
        RIETEMA:(371.5, 0.12, -2.12),
        BRADLEY:(258, 0.37, -0),
        CBV_DEMCO:(3300, 0, 0)
    }[ciclone]
    return k2*Re**n3*exp(n4*Cv)


def razao_de_fluido(ciclone, Du, Dc, Eu):
    k3, n5, n6 = {
        RIETEMA:(1218, 4.75, -0.3),
        BRADLEY:(1.21e6, 2.63, -1.12),
        CBV_DEMCO:(0.127, 0.78, 0)
    }[ciclone]
    return k3*(Du/Dc)**n5 * Eu**n6


def Stk50Eu(ciclone,Rf,Cv):
    k1, n1, n2 = {
        RIETEMA:(0.0474, 0.74, 9),
        BRADLEY:(0.0550, 0.66, 12),
        CBV_DEMCO:(0.0088, 2.31, 15.5)
    }[ciclone]
    return k1*log(1/Rf)**n1*exp(n2*Cv)


def calcular_d50(Stk50_Eu:float, Dc:float, Q:float, dP:float, 
                 ps:float, p:float, mu:float) -> float:
    return sqrt(Stk50_Eu * 36 * mu * p * Q / (pi * (ps-p) * dP * Dc))


def calcular_vazao(ciclone, dP, Dc, p, mu, Cv=None):
    if ciclone is BRADLEY:
        Q = (Dc * dP**0.23 * mu**0.085 / (3.5 * p**0.31))**(1/0.54)
    elif ciclone is RIETEMA:
        if not Cv:
            raise ValueError("Para o ciclone Rietema, deve-se informar Cv. \n")
        Q = (Dc * dP**0.24 * mu**0.028 / (4 * p**0.27 * exp(-0.52 * Cv)))**(1/0.51)
    elif ciclone is CBV_DEMCO:
        raise NotImplementedError()
    else:
        raise NotImplementedError()
    return Q


def calcular_Cv_underflow(Et, Rf, Cv):
    return Et*Cv/(Rf*(1-Cv) + Et*Cv)