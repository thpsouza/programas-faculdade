from geral import *

def main():
    ## Dados
    L = 2.5*10**-3
    Kc = 135
    Tsat = 57+273
    q0 = 5*10**4
    g = 9.81

    ## Propriedades
    Cp_l = 1100
    hfg = 84400
    pv = 13.4
    pl = 1619.2
    sigma = 8.1*10**-3
    mu = 440*10**-6
    Pr = 9.01
    Csf = 0.005
    n = 1.7

    ## Calculando as temperaturas superior e inferior:
    A = lambda q: (q/(mu*hfg))**(1/3)
    B = (sigma/(g*(pl-pv)))**(1/6)
    C = Csf*hfg*Pr**n/Cp_l
    Ts = lambda q: Tsat + A(q)*B*C
    T0 = lambda q: Ts(q) + q*L/Kc

    ## a) Temperaturas do chip
    print("a)")
    ## Calculando a temperatura da superfície
    print(f" q\" = {q0} --> Ts = {Ts(q0)}, T0 = {T0(q0)}")
    ## Se q = 0.9qmax
    qmax = 0.149*hfg*pv*(sigma*g*(pl-pv)/pv**2)**(1/4)
    q = 0.9*qmax
    print(f" q\" = {q} --> Ts = {Ts(q)}, T0 = {T0(q)}")


    ## b) Plotando T = f(q)
    X = np.linspace(0.2,0.9,100)
    T_S = [Ts(x*qmax) - 273 for x in X]
    T_0 = [T0(x*qmax) - 273 for x in X]
    Y = list(zip(T_S,T_0))
    plotar(
        X=X,
        Y=Y,
        label1_1=r"Temperatura da superfície superior, $T_S$",
        label1_2=r"Temperatura da superfície inferior, $T_0$",
        xlabel1=r"Porcentagem de $q_{max}$",
        ylabel1=r"Temperatura de superfície, em °C",
        title1="Variação das temperaturas de superfície com o fluxo de calor."
        )
    print(f"q0,max = {qmax*0.7327}")
    
    
if __name__ == "__main__":
    main()