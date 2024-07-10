from geral import *

def main():
    ## Dados problema
    Ts = 100+273
    Tinf = 27+273
    V = 15
    D = 30*10**-3
    L = 1
    SL = ST = 60*10**-3
    NT = 7
    NL = 10
    
    ## Dados da tabela interpolados para temperatura de filme
    ni = interpolacao_linear(Tinf,300,350,ar.ni300,ar.ni350)
    kar = interpolacao_linear(Tinf,300,350,ar.kar300,ar.kar350)
    Pr = interpolacao_linear(Tinf,300,350,ar.Pr300,ar.Pr350)
    Prs = interpolacao_linear(Ts,350,400,ar.Pr350,ar.Pr400)
    
    ## Reynolds
    Re = V*D/ar.ni300
    V_max = ST/(ST-D)*V 
    Re_max = V_max * D/ni
    
    ## Tabelas 7.7 e 7.8
    C = 0.27
    m = 0.63
    C2 = 0.97
    
    ## Número de Nusselt
    Nu = C * C2 * Re_max**m * Pr**0.36 * (Pr/Prs)**(1/4)
    
    ## Coeficiente convectivo
    h = Nu*kar/D
    
    ## a) Temperatura de saída do ar
    Tsai = Ts - exp(-pi*D*NT*NL*h / (ar.p300*V*NT*ST*ar.cp300)) * (Ts - Tinf)
    print(f"a)\n Temperatura de saída: Tsai = {Tsai}") 
    
    ## Recalculando 
    T_ = (Tinf + Tsai)/2
    p = interpolacao_linear(T_,300,350,ar.p300,ar.p350)
    cp = interpolacao_linear(T_,300,350,ar.cp300,ar.cp350)
    ni = interpolacao_linear(T_,300,350,ar.ni300,ar.ni350)
    kar = interpolacao_linear(T_,300,350,ar.kar300,ar.kar350)
    Pr = interpolacao_linear(T_,300,350,ar.Pr300,ar.Pr350)
    Re_max = V_max * D/ni
    Nu = C * C2 * Re_max**m * Pr**0.36 * (Pr/Prs)**(1/4) 
    h = Nu*kar/D
    Tsai = Ts - exp(-pi*D*NT*NL*h / (p*V*NT*ST*cp)) * (Ts - Tinf)
    print(f" Recalculando iterativamente: Tsai = {Tsai}\n") 

    ## b) Queda de potencia
    x = 1
    f = 0.20
    print(V_max)
    delta_P = NL * x * (p * V_max ** 2 / 2) * f
    print(delta_P)
    
if __name__ == "__main__":
    main()
