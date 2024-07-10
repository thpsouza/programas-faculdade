## MEDIDAS DE DISCREPÂNCIA - ESTATÍSTICA
## Cerca superior, Cerca inferior, Valores discrepantes

from . import Quartis


def cerca_inferior(amostra):
    ''' Retorna a cerca inferior de discrepância de uma amostra (lista de floats) '''
    Q1,_,_,diq = Quartis.quartis(amostra)
    ci = Q1 - ((3/2) * diq)
    return ci    
    

def cerca_superior(amostra):
    ''' Retorna a cerca superior de discrepância de uma amostra (lista de floats) '''
    _,_,Q3,diq = Quartis.quartis(amostra)
    cs = Q3 + ((3/2) * diq)
    return cs  
    

def valores_discrepantes(amostra):
    ''' Retorna uma lista com os valores discrepantes de uma amostra (lista de floats) '''
    discrepantes = []
    ci,cs = cerca_inferior(amostra),cerca_superior(amostra)
    for x in amostra:
        if x < ci or x > cs:
            discrepantes.append(x) 
    return discrepantes

