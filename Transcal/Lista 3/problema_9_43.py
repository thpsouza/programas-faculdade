import sympy as sp
from geral import *


def temperatura_superficie_externa(chute_inicial,propriedades_iniciais,Tinf,Tviz,Ts_i,A,P,resistencia,emissividade,tolerancia=10e-4):
    ## Constantes
    g = 9.81
    sigma = 5.6697*10**-8
    
    ## Comprimento característico
    Lc = A/P
    
    ## Chute, temperatura de filme e propriedades iniciais:
    Ts_e = chute_inicial
    Tfilme = (Ts_e + Tinf)/2
    k,ni,Pr =  propriedades_iniciais

    ## Solução numérica
    Tse = sp.Symbol('Ts,e')
    antigo = Ts_e
    while True:
        ## Número de Rayleigh:
        beta = 1/Tfilme
        Gr =  g * beta * (Ts_e - Tinf) * Lc**3 / ni**2 
        Ra = Gr * Pr

        ## Número de Nusselt
        Nu = 0.15 * Ra**(1/3)

        ## Coeficiente convectivo
        h =  Nu * k / Lc

        #print(f"Tf = {Tfilme}", f"ni = {ni}", f"Gr = {Gr}", f"Pr_i = {Pr}", f"Ra = {Ra}", f"Nu = {Nu}", f"h = {h}", sep='\n')

        ## Recalculando Ts_e:
        f = emissividade*sigma*Tse**4 + (h + 1/resistencia)*Tse - (Ts_i/resistencia + emissividade*sigma*Tviz**4 + h*Tinf)
        Ts_e = sp.solve(f,Tse)[1]
        
        ## Para o laço se atingiu a tolerância
        if abs(Ts_e - antigo) <= tolerancia:
            break

        ## Continuando...
        antigo = Ts_e
        Tfilme = (Ts_e + Tinf)/2
        
        ## Determinando os intervalos de interpolação
        LI = int((Tfilme//100 + 0.5*((Tfilme%100)//50))* 100)
        LE = int(LI + 50)
        
        ## Interpolando para obter as novas propriedades do ar
        k = eval(f"interpolacao_linear(Tfilme,LI,LE,ar.kar{LI},ar.kar{LE})")
        ni = eval(f"interpolacao_linear(Tfilme,LI,LE,ar.ni{LI},ar.ni{LE})")
        Pr = eval(f"interpolacao_linear(Tfilme,LI,LE,ar.Pr{LI},ar.Pr{LE})")
        
    return Ts_e,h


def main():
    ## Dados
    Ts_i = 1700
    Tinf = Tviz = 25+273
    e = 0.3
    H1 = 5*10**-3
    H2 = 0.08
    H3 = 20*10**-3
    L = 4
    A = L**2
    P = 4*L
    
    ## Chutando Ts,e = 600K (chute inicial)
    Ts_e = 600
    ## Temperatura de filme = 449K, e propriedades a 450K:
    Tfilme = (Ts_e + Tinf)/2
    k =  ar.kar450
    ni = ar.ni450
    Pr = ar.Pr450
    ## Coeficientes de condutividade 
    Ktijolo = Tijolos_refratarios().k1478
    Kaco = interpolacao_linear(700,600,800,Aco1010().k600,Aco1010().k800)
    #print(f"k = {k}, ni = {ni}, Pr = {Pr}, Ktijolo = {Ktijolo}, Kaço = {Kaco}")

    ## a) Perda de calor pro ambiente
    # Resistencia por unidade de área
    R = H2/Ktijolo + H1/Kaco
    # Temperatura e coeficiente convectivo
    Ts_e,h = temperatura_superficie_externa(Ts_e,(k,ni,Pr),Tinf,Tviz,Ts_i,A,P,R,e)
    # Taxa
    q = A*(Ts_i - Ts_e)/R
    print("a)")
    print(f"Ts,e = {Ts_e}, h = {h}, q = {q}\n")
    
    ## b) Perda de calor se houver isolante de 20mm entre tijolos e aço:
    Kisolante = 0.125
    # Resistencia por unidade de área
    R = H2/Ktijolo + H1/Kaco + H3/Kisolante
    # Temperatura e coeficiente convectivo
    Ts_e,h = temperatura_superficie_externa(Ts_e,(k,ni,Pr),Tinf,Tviz,Ts_i,A,P,R,e)
    # Taxa
    q = A*(Ts_i - Ts_e)/R
    # Temperatura interna do isolante
    Tiso_i = Ts_i - q/A* (H2/Ktijolo)
    print("b)")
    print(f"Ts,e = {Ts_e}, h = {h}, q = {q}, Tiso,i = {Tiso_i}\n")


    ## c) Encontrar H2 tal que Tiso_i = 1350K:
    X = np.linspace(H2,10*H2,50)
    Y = []
    for x in X:
        # Resistencia por unidade de área
        R = x/Ktijolo + H1/Kaco + H3/Kisolante
        # Temperatura e coeficiente convectivo
        Ts_e,h = temperatura_superficie_externa(Ts_e,(k,ni,Pr),Tinf,Tviz,Ts_i,A,P,R,e,tolerancia=10e-2)
        # Taxa
        q = A*(Ts_i - Ts_e)/R
        # Temperatura interna do isolante
        Tiso_i = Ts_i - q/A* (x/Ktijolo)
        Y.append(Tiso_i)
    
    # Regressão linear
    from metodos_numericos.ajustes_de_curvas import Regressao
    coefs,R2,string,y0 = Regressao(X,Y).regressao_polinomial(2,0.132)
    print(y0)
    # Plot
    plt.plot(X,Y,label=r"$T_{iso,i}$($H_2$)")
    plt.plot(X,[coefs[0]*x**2 + coefs[1]*x + coefs[2] for x in X],label=string)
    plt.title(r"Variação de $T_{iso,i}$ com $H_2$", fontsize=14)
    plt.xlabel("Espessura da camada de tijolos, em m", fontsize=12)
    plt.ylabel("Temperatura da superfície interna do isolante, em K", fontsize=12)
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()