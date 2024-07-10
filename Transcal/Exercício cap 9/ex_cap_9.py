def interpolacao_linear(x, x1, x2, y1, y2):
    return y1 + (x-x1)/(x2-x1)*(y2 - y1)


def main():
    ## Dados problema
    Ts = 273 - 6
    Tinf = Tsup = 273 + 18
    e = 0.95
    W = 1.5
    L = 1
    g = 9.8
    sigma = 5.6697*10**-8
    taxa_kWH = 0.5*10**-3
    
    ## Área de superfície
    A = W*L
    
    ## Temperatura de filme
    Tf = (Ts+Tinf)/2
    beta = 1/Tf
    
    ## Dados da tabela
    v250 = 11.44*10**-6
    k250 = 22.3*10**-3
    a250 = 15.9*10**-6
    v300 = 15.89*10**-6
    k300 = 26.3*10**-3
    a300 = 22.5*10**-6
    Pr300 = 0.707
    Pr250 = 0.720
    
    ## Dados da tabela interpolados para temperatura de filme
    ni = interpolacao_linear(Tf,250,300,v250,v300)
    k = interpolacao_linear(Tf,250,300,k250,k300)
    alpha = interpolacao_linear(Tf,250,300,a250,a300)
    Pr = interpolacao_linear(Tf,250,300,Pr250,Pr300)

    ## Número de Rayleigh:
    Ra = g*beta*(Tinf-Ts)*L**3 / (ni*alpha)

    ## Número de Nusselt (Churchill e Chu):
    Nu = ( 0.825 + (0.387*Ra**(1/6)) / ((1+(0.492/Pr)**(9/16))**(8/27)) )**2
    
    ## Coeficiente convectivo h:
    h = Nu * k/L

    ## Taxa de perda de calor:
    qrad = e*sigma*A*(Tsup**4 - Ts**4)
    qconv = h*A*(Tinf - Ts)
    q = qrad + qconv
    
    ## Custo diário
    C = q*24*taxa_kWH
    
    print(q,C,sep='\n')


if __name__ == "__main__":
    main()