from geral import *

def temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i, h_e, k, L):   
    C = L/(2*k) * h_i * (Ts_i - Tinf_i) + Ts_i
    Ts_e = (L/(2*k)*h_e*Tinf_e + C)/(1 + L*h_e/(2*k))
    return Ts_e

def main():
    ## Dados
    L = 8*10**-3 # m
    H = 0.5 # m 
    Ts_i = 15 + 273 # K
    Tinf_i = 10 + 273 # K 
    Tinf_e = -10 + 273 # K
    Var = 20 # m/s
    g = 9.81
    kvidro = 1.4
    
    ## Temperatura de filme interna:
    Tfilme_i = lambda Tinf_i: (Ts_i + Tinf_i) / 2

    ## Viscosidade cinemática, condutividade térmica e Pr interpolados em Tf = 285.5 
    ni_i = lambda Tinf_i: interpolacao_linear(Tfilme_i(Tinf_i),250,300,ar.ni250,ar.ni300)
    Pr_i = lambda Tinf_i: interpolacao_linear(Tfilme_i(Tinf_i),250,300,ar.Pr250,ar.Pr300)
    kar_i = lambda Tinf_i: interpolacao_linear(Tfilme_i(Tinf_i),250,300,ar.kar250,ar.kar300)
    
    ## Comprimento caracteristico: comprimento da placa
    Lc = H
    
    ## Coeficiente convectivo interno hi:
    beta = lambda Tinf_i: 1/Tfilme_i(Tinf_i)
    Gr = lambda Tinf_i: g * beta(Tinf_i) * (abs(Ts_i-Tinf_i)) * Lc**3 / ni_i(Tinf_i)**2
    Ra = lambda Tinf_i: Gr(Tinf_i)*Pr_i(Tinf_i)
    Nu_i = lambda Tinf_i: (0.825 + (0.387 * Ra(Tinf_i)**(1/6)) / ( 1 + (0.492/Pr_i(Tinf_i))**(9/16) )**(8/27) )**2
    h_i = lambda Tinf_i: Nu_i(Tinf_i) * kar_i(Tinf_i) / Lc
    print(f"Gr = {Gr(Tinf_i)}, Pr_i = {Pr_i(Tinf_i)}, Ra = {Ra(Tinf_i)}, Nu_i = {Nu_i(Tinf_i)}, hi = {h_i(Tinf_i)}\n")
    
    ## Chutando temperatura na superficie externa Ts_e = 10°C:  Tfilme = 0°C
    Ts_e = 10 + 273
    Tfilme_e = (Tinf_e + Ts_e)/2
    
    ## Propriedades em Tf = 273K
    kar_e = lambda Tfilme: interpolacao_linear(Tfilme,250,300,ar.kar250,ar.kar300)
    ni_e = lambda Tfilme: interpolacao_linear(Tfilme,250,300,ar.ni250,ar.ni300)
    Pr_e = lambda Tfilme: interpolacao_linear(Tfilme,250,300,ar.Pr250,ar.Pr300)
    
    ## Coeficiente convectivo externo:
    Re = lambda Tfilme, Var: Var * H / ni_e(Tfilme)    
    Nu_e = lambda Tfilme, Var: (0.037 * Re(Tfilme,Var)**(4/5) - 871) * Pr_e(Tfilme)**(1/3)
    h_e = lambda Tfilme, Var: Nu_e(Tfilme,Var) * kar_e(Tfilme) / H
    
    ## Recalculando Ts_e:
    Ts_e = temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i(Tinf_i), h_e(Tfilme_e,Var), kvidro, L)
    print(f"Re = {Re(Tfilme_e,Var)}, Nu = {Nu_e(Tfilme_e,Var)}, he = {h_e(Tfilme_e,Var)}, Ts_e = {Ts_e}\n")
    
    ## Recalculando iterativamente h_e e Ts_e:
    Ts_e_ = 285.39246996588776
    h_e_ = 41.37725019078463


    ############ a) Taxa volumétrica de aquecimento q ##############
    q = lambda Tinf_i, h_i, Tinf_e, h_e, Ts_e: (h_e*(Ts_e - Tinf_e) + h_i*(Ts_i - Tinf_i))/L
    print(f"a)\n Taxa volumétrica de aquecimento: q = {q(Tinf_i, h_i(Tinf_i), Tinf_e, h_e_, Ts_e_)}\n")
    

    ############ b) Plotando ###############

    ## Variação de q e Ts_e com a variação de Tinf_e no intervalo [-25°C, 5°C], em Var = 10,20,30 m/s, e Tinf_i = 10°C
    Tinf_i = 10 + 273
    # Intervalo de Tinf_e
    TINF_E = np.linspace(-25+273, 5+273, 100)
    # Listas para armazenar as temperaturas e taxas de geração de calor:
    TSE = []
    Q = []
    for Tinf_e in TINF_E:
        # Calculando a temperatura de filme, com Ts_e obtida em a)
        Tfilme_e = (Tinf_e + Ts_e)/2
        # Com a temperatura de filme, calculando Ts_e e q, com Var = 10m/s
        Ts_e1 = temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i(Tinf_i), h_e(Tfilme_e,Var=10), kvidro, L)
        q1 = q(Tinf_i, h_i(Tinf_i), Tinf_e, h_e(Tfilme_e,Var=10), Ts_e)
        # Com a temperatura de filme, calculando Ts_e e q, com Var = 20m/s
        Ts_e2 = temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i(Tinf_i), h_e(Tfilme_e,Var=20), kvidro, L)
        q2 = q(Tinf_i, h_i(Tinf_i), Tinf_e, h_e(Tfilme_e,Var=20), Ts_e)
        # Com a temperatura de filme, calculando Ts_e e q, com Var = 30m/s
        Ts_e3 = temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i(Tinf_i), h_e(Tfilme_e,Var=30), kvidro, L)
        q3 = q(Tinf_i, h_i(Tinf_i), Tinf_e, h_e(Tfilme_e,Var=30), Ts_e)
        # Guardando f1(x), f2(x) e f3(x) nas listas
        TSE.append((Ts_e1-273,Ts_e2-273,Ts_e3-273)) #Celsius
        Q.append((q1/1000,q2/1000,q3/1000)) # kW/m³
    TINF_E = [i - 273 for i in TINF_E] # Celsius
    
    plotar(
       X=TINF_E,
       Y=[TSE,Q],
       title1=r"Variação de $T_{S,e}$ com $T_{∞,e}$ ,  para diferentes $V_{ar}$ ,  $T_{∞,i}$ = 10°C",
       title2="Variação de q"+'\u0307'+r" com $T_{∞,e}$ ,  para diferentes $V_{ar}$ ,  $T_{∞,i}$ = 10°C",
       xlabel1="Temperatura do ar externo, em °C",
       ylabel1="Temperatura da superfície externa, em °C",
       xlabel2="Temperatura do ar externo, em °C",
       ylabel2=r"Taxa de aquecimento volumétrica, em kW/$m^3$",
       label1_1=r"$V_{ar}$ = 10m/s",
       label1_2=r"$V_{ar}$ = 20m/s",
       label1_3=r"$V_{ar}$ = 30m/s",
       label2_1=r"$V_{ar}$ = 10m/s",
       label2_2=r"$V_{ar}$ = 20m/s",
       label2_3=r"$V_{ar}$ = 30m/s"
       )


    
    ## Variação de q e Ts_e com a variação de Tinf_i no intervalo [5°C, 20°C], em Tinf_e = -25,-10,5 °C, e var = 30m/s

    # Listas para armazenar as temperaturas e taxas de geração de calor:
    TSE = []
    Q = [] 
    
    # Intervalo de Tinf_i
    TINF_I = np.linspace(5+273, 20+273, 100)    
    for Tinf_i in TINF_I:
        ## Calculando Ts_e e q com Tinf_e = -25°C
        ## Chutando Ts_e = 5°C
        Tfilme_e = (-25+273 + 5+273)/2
        Ts_e = temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i(Tinf_i), h_e(Tfilme_e,Var=30), kvidro, L)
        # Recalculando
        Tfilme_e = (-25+273 + Ts_e)/2
        Ts_e1 = temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i(Tinf_i), h_e(Tfilme_e,Var=30), kvidro, L)
        q1 = q(Tinf_i, h_i(Tinf_i), Tinf_e, h_e(Tfilme_e,Var=30), Ts_e1)
        
        ## Calculando Ts_e e q na com Tinf_e = -10°C
        # Chutando Ts_e = 10°C
        Tfilme_e = (-10+273 + 10+273)/2
        Ts_e = temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i(Tinf_i), h_e(Tfilme_e,Var=30), kvidro, L)
        # Recalculando
        Tfilme_e = (-10+273 + Ts_e)/2
        Ts_e2 = temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i(Tinf_i), h_e(Tfilme_e,Var=30), kvidro, L)
        q2 = q(Tinf_i, h_i(Tinf_i), Tinf_e, h_e(Tfilme_e,Var=30), Ts_e2)
        
        ## Calculando Ts_e e q na com Tinf_e = 5°C
        # Chutando Ts_e = 15°C
        Tfilme_e = (5+273 + 15+273)/2
        Ts_e = temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i(Tinf_i), h_e(Tfilme_e,Var=30), kvidro, L)
        # Recalculando
        Tfilme_e = (5+273 + Ts_e)/2
        Ts_e3 = temperatura_superficie_externa(Ts_i, Tinf_i, Tinf_e, h_i(Tinf_i), h_e(Tfilme_e,Var=30), kvidro, L)
        q3 = q(Tinf_i, h_i(Tinf_i), Tinf_e, h_e(Tfilme_e,Var=30), Ts_e3)
        
        # Guardando f1(x), f2(x) e f3(x) nas listas
        TSE.append((Ts_e1-273,Ts_e2-273,Ts_e3-273)) #Celsius
        Q.append((q1/1000,q2/1000,q3/1000)) # kW/m³
        
    TINF_I = [i - 273 for i in TINF_I] # Celsius


    plotar(
        X=TINF_I,
        Y=[TSE,Q],
        title1=r"Variação de $T_{S,e}$ com $T_{∞,i}$ ,  para diferentes $T_{∞,e}$ ,  $V_{ar}$ = 30m/s",
        title2="Variação de q"+'\u0307'+r" com $T_{∞,i}$ ,  para diferentes $T_{∞,e}$ ,  $V_{ar}$ = 30m/s",
        xlabel1="Temperatura do ar interno, em °C",
        ylabel1="Temperatura da superfície externa, em °C",
        xlabel2="Temperatura do ar interno, em °C",
        ylabel2=r"Taxa de aquecimento volumétrica, em kW/$m^3$",
        label1_1=r"$T_{∞,e}$ = -25°C",
        label1_2=r"$T_{∞,e}$ = -10°C",
        label1_3=r"$T_{∞,e}$ = 5°C",
        label2_1=r"$T_{∞,e}$ = -25°C",
        label2_2=r"$T_{∞,e}$ = -10°C",
        label2_3=r"$T_{∞,e}$ = 5°C"
        )
    
if __name__ == "__main__":
    main()