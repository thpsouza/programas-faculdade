from geral import *

def main():
    ## Dados problema
    L = 5
    D = 25.4*10**-3
    Ts = 350
    Tinf = 290
    v = 1
    A = pi*D**2/4
    
    ## Vazão mássica
    m = lambda p: p*A*v
    ## Reynolds
    Re = lambda p,mu: p*v*D/mu
    ## Nusselt
    Nu = lambda p,mu,Pr: 0.023*Re(p,mu)**(4/5)*Pr**0.4
    ## Coeficiente convectivo h
    h = lambda p,mu,Pr,k: Nu(p,mu,Pr)*k/D
    ## Temperatura de saída
    Tsaida = lambda p,mu,Pr,k,cp,L: Ts - exp(-pi*D*L*h(p,mu,Pr,k)/(m(p)*cp))*(Ts-Tinf)        
        
    ## a) Temperatura de saída para Tm = 300K
    print(f"a)\n Tsaida = {Tsaida(agua.p300, agua.mu300, agua.Pr300, agua.k300, agua.cp300, L)}\n")
    
    ## b) Recalculando para Tm = (Tinf+Tsaida)/2 ~ 305K
    ## Propriedades a 305K
    p = agua.p305
    mu = agua.mu305
    k = agua.Pr305
    Pr = agua.k305
    cp = agua.cp305
    ## Recalculando
    print(f"b)\n Tsaida = {Tsaida(p,mu,Pr,k,cp,L)}\n")
    
    ## c) Gráfico de velocidade média
    ## Fixando Tsaida e h como os obtidos em b)
    Tsaida = Tsaida(p,mu,Pr,k,cp,L)
    h = h(p,mu,Pr,k)
    ## Expressando velocidade em termos de L
    v = lambda L: (-4*L*h/(p*D*cp))/log((Ts-Tsaida)/(Ts-Tinf))
    ## Plotando
    X = np.linspace(4,7,100)     
    Y = [v(L) for L in X]  
    plt.plot(X,Y)
    plt.grid()
    plt.title("Variação da velocidade média da água para tubos entre 4m e 7m de comprimento.")
    plt.xlabel("Comprimento do tubo, em m")
    plt.ylabel("Velocidade média da água, em K")
    plt.show()
        
if __name__ == "__main__":
    main()
