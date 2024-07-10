from matrizes import Matriz
from vetores import Vetor
from math import sin,cos,pi

def rotacao2D(matriz:int, graus:float) -> Matriz:
    """Rotaciona em 2D uma matriz/vetor no sentido antihorário em theta graus.

    Args:
        matriz (int): _description_
        graus (float): _description_

    Returns:
        Matriz: _description_
    """
    ## Defesa
    if matriz.shape[0] != 2:
        raise("A matriz a ser rotacionada deve ter 2 linhas. \n")
    ## Grau para rad
    graus = pi*graus/180
    R = Matriz((cos(graus),-sin(graus),sin(graus),cos(graus)),2,2)
    return R*matriz
