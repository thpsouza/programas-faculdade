from geral import *

def main():
    ## Dados problema
    L = 1 # m
    D = 0.01 # m
    m = 18 / 3600 # Kg/s
    Tentra = 85 + 273 # K
    Tsai = 78 + 273 # K
    Tinf = 25 + 273 # K
    
    ## Propriedades fluido interno
    p = 1079 # Kg/m³
    cp = 2637 # J/(Kg*K)
    mi = 0.0034 # N*s/m²
    k = 0.261 # W/(m*K)
    ni = mi/p # m²/s

    ## Coeficiente convectivo global
    U = - log((Tinf - Tsai)/(Tinf - Tentra)) * m*cp/(pi*D*L)

    ## Reynolds
    Q = m/p
    A = pi*D**2/4
    Re = Q*D/(A*ni)
    print(f"Re = {Re}")
    
    ## L/D
    print(f"L/D = {L/D}")
    
    ## Prandtl
    Pr = cp*mi/k
    print(f"Pr = {Pr}")

    ## NuD cte --> hi cte --> U cte
    
    ## Temperatura de saída só depende de m:
    Tsaida = Tinf - exp(-pi*D*L*U/(2*m*cp))*(Tinf - Tentra)
    print(f"Tsaida ~ {round(Tsaida - 273,2)}°C")


if __name__ == "__main__":
    main()