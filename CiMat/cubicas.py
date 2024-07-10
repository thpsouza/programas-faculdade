def volumeCCC(raio: float) -> float :
    return 64*raio**3*3**(1/2)/9

def volumeCFC(raio: float) -> float :
    return 16*raio**3*2**(1/2)

VCCC = lambda r: volumeCCC(r)
VCFC = lambda r: volumeCFC(r)

def deltaV(raio1:float, raio2: float, ccc_to_cfc:bool=True) -> float:
    '''
    Retorna a diferença relativa entre os volumes de células CFC e CCC (dados os raios).
    '''
    if ccc_to_cfc: return (1/2*VCFC(raio2) - VCCC(raio1))/VCCC(raio1)
    return (VCCC(raio2) - 1/2*VCFC(raio1))/(1/2*VCFC(raio1))

