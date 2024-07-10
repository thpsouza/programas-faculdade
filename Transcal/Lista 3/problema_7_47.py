from geral import *

def plotar(X1,Y1,X2,Y2):
    ## Inicia a figura e mostra as grades 
    fig = plt.figure(figsize=(9,8))
    axs = fig.subplots(2)
    plt.subplots_adjust(hspace=0.5)
    axs[0].grid()   
    axs[1].grid()  
    
    ## Plota a primeira função
    axs[0].plot(X1,Y1,color='Black')
    axs[0].set_title("Perda total de calor do chip por diâmetro do pino (V_ar = 10m/s)")
    axs[0].set_xlabel("Diâmetro do pino, em m")
    axs[0].set_ylabel("Perda de calor total, em W")

    ## Plota a segunda função
    axs[1].plot(X2,Y2,color='Black')
    axs[1].set_title("Perda total de calor do chip por diâmetro do pino (D = 2mm)")
    axs[1].set_xlabel("Velocidade do ar, em m/s")
    axs[1].set_ylabel("Perda de calor total, em W")
    
    plt.show()


def main():
    ## Dados problema
    Tb = 350
    Tinf = 300
    L = 12*10**-3
    W = 4*10**-3
    D = 2*10**-3
    V_ar = 10
    kcobre = 401
       
    ## Temperatura de filme
    Tf = (Tb+Tinf)/2
    
    ## Dados da tabela interpolados para temperatura de filme
    ni = interpolacao_linear(Tf,300,350,ar.ni300,ar.ni350)
    kar = interpolacao_linear(Tf,300,350,ar.kar300,ar.kar350)
    Pr = interpolacao_linear(Tf,300,350,ar.Pr300,ar.Pr350)
    
    ## Número de Reynolds do escoamento
    Re = lambda V,D : V * D / ni
    
    ## Número de Nusselt médio
    Nu = lambda V,D: 0.3 + (0.62*Re(V,D)**(1/2)*Pr**(1/3)/(1+(0.4/Pr)**(2/3))**(1/4)) * (1+(Re(V,D)/282000)**(5/8))**(4/5)

    ## a) Coeficiente convectivo médio
    h = lambda V,D: kar/D * Nu(V,D)
    print(f"a)\n h = {h(V_ar,D)}\n")
    
    ## b) Taxa de transferência de calor do pino de cobre
    Lc = lambda D: L + D/4
    theta_b = Tb - Tinf
    P = lambda D: pi*D
    Ac = lambda D: pi*D**2/4
    M = lambda V,D: ( h(V,D) * P(D) * kcobre * Ac(D) )**(1/2) * theta_b
    m = lambda V,D: ( h(V,D) * P(D) / (kcobre * Ac(D) ))**(1/2)
    q_pino =  lambda V,D: M(V,D) * tanh( m(V,D) * Lc(D) )
    print(f"b)\n q = {q_pino(V_ar,D)}\n")
    
    ## c) Perda total de calor do chip
    A_base = lambda D: W**2 - pi*D**2/4
    q_base = lambda V,D: h(V,D) * A_base(D) * (Tb-Tinf)
    q_total = lambda V,D: q_base(V,D) + q_pino(V,D)
    print(f"c)\n qtotal = {q_total(V_ar,D)}\n")
    
    ## d)
    ## Variação do diâmetro do pino
    X1 = np.linspace(2*10**-3,4*10**-3,100)
    Y1 = [q_total(10,x) for x in X1]
    ## Variação da velocidade do ar
    X2 = np.linspace(10,40,100)
    Y2 = [q_total(x,2*10**-3) for x in X2]
    plotar(X1,Y1,X2,Y2)
    print(f"D)\n qtotal = {q_total(40,4*10**-3)}\n")
    
if __name__ == "__main__":
    main()
