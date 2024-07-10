## QUARTIS - ESTATÍSTICA
## 1º, 2º (mediana), 3º e Distância Interquartil 

from . import Medidas_Centralidade


def primeiro_quartil(amostra,ordenada=False):
    ''' Retorna o primeiro quartil de uma amostra (lista de floats) '''

    if not ordenada:
        amostra = list(amostra)
        amostra.sort()

    n = len(amostra)

    q1 = (n+3)/4
    if q1 == int(q1):
        Q1 = amostra[int(q1)-1]
    else:
        viz_sup = int((n+3)/4) + 1
        peso_superior = q1 - int(q1)
        viz_inf = int((n+3)/4)
        peso_inferior = 1 - peso_superior
        Q1 = peso_inferior*amostra[viz_inf-1]+peso_superior*amostra[(viz_sup)-1]    
    return Q1


def terceiro_quartil(amostra,ordenada=False):
    ''' Retorna o terceiro quartil de uma amostra (lista de floats) '''

    if not ordenada:
        amostra = list(amostra)
        amostra.sort()

    n = len(amostra)

    q3 = (3*n+1)/4
    if q3 == int(q3):
        Q3 = amostra[int(q3)-1]
    else:
        viz_sup = int(q3) + 1
        peso_superior = q3 - int(q3)
        viz_inf = int(q3)
        peso_inferior = 1 - peso_superior
        Q3 = peso_inferior*amostra[viz_inf-1]+peso_superior*amostra[(viz_sup)-1]   
    return Q3    


def quartis(amostra,ordenada=False):
    ''' Retorna os quartis, e distância interquartil de uma amostra (lista de floats) '''

    if not ordenada:
        amostra = list(amostra)
        amostra.sort()
        
    #1º Quartil
    Q1 = primeiro_quartil(amostra,True)

    #2º Quartil
    Q2 = Medidas_Centralidade.mediana(amostra)    

    #3º Quartil
    Q3 = terceiro_quartil(amostra,True)

    #DIQ (Distância interquartil)
    diq = (Q3 - Q1)

    return Q1,Q2,Q3,diq

