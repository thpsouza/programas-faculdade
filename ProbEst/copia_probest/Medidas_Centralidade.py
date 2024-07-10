## MEDIDAS DE CENTRALIDADE - ESTATÍSTICA
## Média aritimética, Mediana e Moda

def media(amostra):
    ''' Retorna a média aritimética de uma amostra (lista de floats) '''
    if len(amostra)==0:
        raise AmostraVazia( " Amostra vazia. ")
    media = sum(amostra)/len(amostra)
    return media


def mediana(amostra):
    ''' Retorna a mediana de uma amostra (lista de floats) '''
    if len(amostra)==0:
        raise AmostraVazia( " Amostra vazia. ")
    amostra = list(amostra)
    amostra.sort()
    n = len(amostra)
    if (n%2 != 0):
        Q2 = amostra[(((n+1)//2)-1)]
    elif (n%2 == 0):
        Q2 = ( amostra[(n//2)-1]+amostra[((n//2)+1)-1] )/2
    return Q2


def moda(amostra): #PRECISA DE REVISÃO
    ''' Retorna a moda de uma amostra (lista de floats)'''
    if len(amostra)==0:
        raise AmostraVazia( " Amostra vazia. ")    
    ocorrencias = {i:amostra.count(i) for i in amostra}
    moda = max(ocorrencias, key=lambda key: ocorrencias[key])
    return moda


class AmostraVazia(Exception):
    pass