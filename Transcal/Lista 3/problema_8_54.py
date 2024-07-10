from geral import *

def temperatura_saida(Tinf,Tentrada,h_i,h_e,L,D,m,cp_i):
    '''
    Calcula e retorna a temperatura de saída do gás
    
    PARÂMETROS:
    - Tinf: Temperatura do ar externo
    - Tentrada: Temperatura do gás na entrada da chaminé
    - h_i: Coeficiente convectivo interno
    - h_e: Coeficiente convectivo externo
    - L: Comprimento da chaminé
    - D: Diâmetro interno
    - m: Vazão mássica
    - cp_i: Calor específico a pressão constante
    '''
    ## Cálculo do coeficiente convectivo global
    U = 1/(1/h_i + 1/h_e)
    ## Cálculo da temperatura de saída
    return Tinf - exp(-pi*D*L*U/(m*cp_i))*(Tinf - Tentrada)
    
def temperatura_superficie(Tinf,Tentrada,h_i,h_e,L,D,m,cp_i):
    '''
    Calcula e retorna a temperatura de superfície da chaminé no local de saída do gás
    
    PARÂMETROS:
    - Tinf: Temperatura do ar externo
    - Tentrada: Temperatura do gás na entrada da chaminé
    - h_i: Coeficiente convectivo interno
    - h_e: Coeficiente convectivo externo
    - L: Comprimento da chaminé
    - D: Diâmetro interno
    - m: Vazão mássica
    - cp_i: Calor específico a pressão constante
    '''
    ## Obtenção da temperatura de saída
    Tsaida = temperatura_saida(Tinf,Tentrada,h_i,h_e,L,D,m,cp_i)
    ## Cálculo da temperatura de superfície na saída
    return (Tinf + Tsaida*h_i/h_e)/(1+h_i/h_e) 
     
def main():
    ## Dados problema
    L = 6
    D = 0.5
    m = 0.5
    Tentrada = 600 + 273
    Tinf = 4 + 273
    v_e = 5
    
    ## Chutando temperatura de saida em 300°C, e computando Tmedia (450°C)
    Tsaida = 300 + 273
    Tmedia = (Tentrada+Tsaida)/2
    
    ## Chutando temperatura de superfície em 200°C, e computando Tfilme (102°C)
    Tsuperficie = 200 + 273
    Tfilme = (Tsuperficie+Tinf)/2
    

    ## Dados da tabela interpolados para ar atm na temperatura média
    p1 = interpolacao_linear(Tmedia,700,750,ar.p700,ar.p750)
    cp1 = interpolacao_linear(Tmedia,700,750,ar.cp700,ar.cp750)
    ni1 = interpolacao_linear(Tmedia,700,750,ar.ni700,ar.ni750)
    kar1 = interpolacao_linear(Tmedia,700,750,ar.kar700,ar.kar750)
    Pr1 = interpolacao_linear(Tmedia,700,750,ar.Pr700,ar.Pr750)
    
    ## Dados da tabela interpolados para ar atm na temperatura de filme
    ni2 = interpolacao_linear(Tfilme,350,400,ar.ni350,ar.ni400)
    kar2 = interpolacao_linear(Tfilme,350,400,ar.kar350,ar.kar400)
    Pr2 = interpolacao_linear(Tfilme,350,400,ar.Pr350,ar.Pr400)
    
    print(ni2,kar2,Pr2)

    ## Coeficiente convectivo do escoamento interno
    A = pi*D**2/4
    v_i = lambda p: m/(A*p)
    Re_i = lambda p,ni: v_i(p)*D/ni
    Nu_i = lambda p,ni,Pr: 0.023*Re_i(p,ni)**(4/5)*Pr**0.3
    h_i = lambda p,ni,Pr,kar: Nu_i(p,ni,Pr)*kar/D
    
    ## Coeficiente convectivo do escoamento externo
    Re_e = lambda v_e,ni: v_e*D/ni
    Nu_e = lambda v_e,ni,Pr: 0.3 + ((0.62*Re_e(v_e,ni)**(1/2)*Pr**(1/3))/(1+(0.4/Pr)**(2/3))**(1/4)) * (1+(Re_e(v_e,ni)/282000)**(5/8))**(4/5)
    h_e = lambda v_e,ni,Pr,kar: Nu_e(v_e,ni,Pr)*kar/D
    
    
    ## a) Calculando Tsaida e Tsuperficie baseado nos chutes:
    Tsaida = temperatura_saida(Tinf, Tentrada, h_i(p1,ni1,Pr1,kar1), h_e(v_e,ni2,Pr2,kar2), L, D, m, cp1)
    Tsuperficie = temperatura_superficie(Tinf, Tentrada, h_i(p1,ni1,Pr1,kar1), h_e(v_e,ni2,Pr2,kar2), L, D, m, cp1)
    print(f"a)\n Tsaida = {Tsaida}\n Tsuperficie = {Tsuperficie}\n") 
    
    ####### RECALCULANDO ITERATIVAMENTE (Tmedia = 844K, Tfilme = 388K) #######
    # Interpolando as propriedades novamente
    Tmedia = (Tsaida+Tentrada)/2
    Tfilme = (Tsuperficie+Tinf)/2
    # Gás (interno)
    p1 = interpolacao_linear(Tmedia,800,850,ar.p800,ar.p850)
    cp1 = interpolacao_linear(Tmedia,800,850,ar.cp800,ar.cp850)
    ni1 = interpolacao_linear(Tmedia,800,850,ar.ni800,ar.ni850)
    kar1 = interpolacao_linear(Tmedia,800,850,ar.kar800,ar.kar850)
    Pr1 = interpolacao_linear(Tmedia,800,850,ar.Pr800,ar.Pr850)
    # Ar atm (externo)
    ni2 = interpolacao_linear(Tfilme,350,400,ar.ni350,ar.ni400)
    kar2 = interpolacao_linear(Tfilme,350,400,ar.kar350,ar.kar400)
    Pr2 = interpolacao_linear(Tfilme,350,400,ar.Pr350,ar.Pr400)
    # Recalculando Tsaida e Ts
    Tsaida = temperatura_saida(Tinf, Tentrada, h_i(p1,ni1,Pr1,kar1), h_e(v_e,ni2,Pr2,kar2), L, D, m, cp1)
    Tsuperficie = temperatura_superficie(Tinf, Tentrada, h_i(p1,ni1,Pr1,kar1), h_e(v_e,ni2,Pr2,kar2), L, D, m, cp1)
    print(f"RECALCULANDO \n Tsaida = {Tsaida}\n Tsuperficie = {Tsuperficie}\n") 
    
    
    ## b) Variação de temperatura de saída do gás em diferentes Tinf e v_e (Tsuperficie fixada em 505K)
    # Interpolando as propriedades do escoamento interno novamente
    Tmedia = (Tsaida+Tentrada)/2
    p1 = interpolacao_linear(Tmedia,800,850,ar.p800,ar.p850)
    cp1 = interpolacao_linear(Tmedia,800,850,ar.cp800,ar.cp850)
    ni1 = interpolacao_linear(Tmedia,800,850,ar.ni800,ar.ni850)
    kar1 = interpolacao_linear(Tmedia,800,850,ar.kar800,ar.kar850)
    Pr1 = interpolacao_linear(Tmedia,800,850,ar.Pr800,ar.Pr850)
    # Coeficiente convectivo interno (fixo já que só variam as propriedades do escoamento externo)
    h_i = h_i(p1,ni1,Pr1,kar1)

    # Plotando Tsaida para os diferentes intervalos de v_e:
    X = np.linspace(2,10,100)  
        
    ## 1) Tinf = -25°C
    # Temperatura de filme
    Tfilme = (-25 + 273 + 505)/2
    # Propriedades escoamento externo em Tfilme = 376.5
    ni2 = interpolacao_linear(Tfilme,350,400,ar.ni350,ar.ni400)
    kar2 = interpolacao_linear(Tfilme,350,400,ar.kar350,ar.kar400)
    Pr2 = interpolacao_linear(Tfilme,350,400,ar.Pr350,ar.Pr400)
    # Calculando (EM CELSIUS) os valores de Tsaida para as diferentes v_e
    Y1 = [temperatura_saida(Tinf, Tentrada, h_i, h_e(x,ni2,Pr2,kar2), L, D, m, cp1) - 273 for x in X] 
    
    ## 2) Tinf = 5°C
    # Temperatura de filme
    Tfilme = (5 + 273 + 505)/2
    # Propriedades escoamento externo em Tfilme = 391.5
    ni2 = interpolacao_linear(Tfilme,350,400,ar.ni350,ar.ni400)
    kar2 = interpolacao_linear(Tfilme,350,400,ar.kar350,ar.kar400)
    Pr2 = interpolacao_linear(Tfilme,350,400,ar.Pr350,ar.Pr400)
    # Calculando (EM CELSIUS) os valores de Tsaida para as diferentes v_e
    Y2 = [temperatura_saida(Tinf, Tentrada, h_i, h_e(x,ni2,Pr2,kar2), L, D, m, cp1) - 273 for x in X] 
    
    ## 3) Tinf = 35°C
    # Temperatura de filme
    Tfilme = (35 + 273 + 505)/2
    # Propriedades escoamento externo em Tfilme = 406.5
    ni2 = interpolacao_linear(Tfilme,400,450,ar.ni400,ar.ni450)
    kar2 = interpolacao_linear(Tfilme,400,450,ar.kar400,ar.kar450)
    Pr2 = interpolacao_linear(Tfilme,400,450,ar.Pr400,ar.Pr450)
    # Calculando (EM CELSIUS) os valores de Tsaida para as diferentes v_e
    Y3 = [temperatura_saida(Tinf, Tentrada, h_i, h_e(x,ni2,Pr2,kar2), L, D, m, cp1) - 273 for x in X] 
    
    ## Jutando Y1,Y2,Y3:
    Y = list(zip(Y1,Y2,Y3))
    
    plotar(
        X=X,
        Y=Y,
        label1_1="T∞ = -25°C",
        label1_2="T∞ = 5°C",
        label1_3="T∞ = 35°C",
        title1="Temperatura de saída do gás x velocidade do ar externo, em diferentes temperaturas",
        xlabel1="Velocidade do ar externo, em m/s",
        ylabel1="Temperatura de saída do gás interno, em °C",
        size=(10,6)
    )

    
if __name__ == "__main__":
    main()