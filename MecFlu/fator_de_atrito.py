import sympy as sp
import sys
from metodos_numericos.raizes_de_equacoes import metodo_newton_raphson
from adimensionais import reynolds

#### DADOS ####

## Reynolds (Re)
Re = reynolds(999,8.488,0.05,1.002*10**-3)

## Rugosidade Relativa (E/D)
E_D = 0

## Chute inicial para o fator de atrito
chute_inicial = 0.02




#### EQUAÇÃO ####


def colebrook_white(Re, E_D, chute_inicial=0.02, imprimir=False):
    '''
    Resolve a equação de colebrook_white para dados Número de Reynolds e Rugosidade Relativa.

    Utiliza o método iterativo de newton-raphson 

    float, float, float --> float
    '''
    Fd = sp.Symbol('Fd')
    f = 1/sp.sqrt(Fd) + 2*sp.log(E_D/3.7 + 2.51/(Re*sp.sqrt(Fd)),10)
    Fd = metodo_newton_raphson(f,chute_inicial,var=Fd,tolerancia=10**(-4))[0]
    if imprimir:
        print(Fd)
    return Fd



def main():
    fator_de_atrito = colebrook_white(Re,E_D,chute_inicial=chute_inicial)
    print(fator_de_atrito) 

if __name__ == "__main__":
    main()
    input()


