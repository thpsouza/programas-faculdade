from math import pi,sqrt
from eficiencia import eficiencia_aleta_anular

def main():
    ## Dados
    N = 5
    L = 20*10**-3
    r1 = 25*10**-3
    r2 = 45*10**-3
    t = 6*10**-3
    h = 50
    H = 0.15
    Tb = 500
    Tinf = 300
    theta = Tb-Tinf

    ## Coeficiente de condução metal
    k = 151

    ## m
    m = sqrt((2*h)/(k*t))

    ## Área base sem aletas
    A = 2*pi*r1*H

    ## Taxa sem aletas
    qs = theta*h*A

    ## Raio corrigido
    r2c = r2 + t/2
    Lc = L + t/2

    ## Área aleta
    Aa = 2*pi*(r2c**2 + r1**2)
    ## Área total (aletas + base)
    AT = N*Aa + A - 2*pi*r1*t*N

    ## Eficiência de cada aleta (gráfico)
    na = eficiencia_aleta_anular(r1,r2c,m)

    ## Eficiência global
    n0 = lambda na: 1 - N*Aa/AT*(1-na)

    ## Taxa com aletas
    qt = lambda n0: n0*h*AT*theta
    
    ## Output
    print(f"Eficiência global: {n0(na)}")
    print(f"Taxa sem aletas: {qs}")
    print(f"Taxa com aletas: {qt(n0(na))}")
    print(f"Diferença entre taxas: {qt(n0(na)) - qs}")

if __name__ == "__main__":
    main()