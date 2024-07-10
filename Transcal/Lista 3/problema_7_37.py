from metodos_numericos.integracao_de_equacoes import Quadratura
from geral import *

def letra_a(V_ar,L,H,ni,k,Ts,Tinf,Pr):
    ## Área de superfície
    A = H*L
    ## Número de Reynolds
    Re = V_ar*L/ni
    ## Número de Nusselt (Churchill e Chu):
    Nu = 0.664*Re**(1/2)*Pr**(1/3)
    ## Coeficiente convectivo h:
    h = Nu * k/L
    ## Taxa de perda de calor:
    qconv = h*A*(Ts - Tinf)
    q = qconv
    ## Output
    print("a)")
    print(f"q = {q}, h = {h}, Nu = {Nu}, Re = {Re}, ni = {ni}, k = {k}, Pr = {Pr}\n")

def letra_b(V_ar,L,H,ni,k,Ts,Tinf,Pr):
    ## Recalculando Reynolds médio
    Re = V_ar*(2+L)/ni
    # ## Número de Reynolds local
    # Rex = lambda x: V_ar*x/ni
    # ## Número de nusselt local
    # Nu = lambda x: 0.332*Rex(x)**(1/2)*Pr**(1/3) / (1-(2/x)**(3/4))**(1/3)
    # ## Coeficiente convectivo local
    # h = lambda x: Nu(x) * k/x
    ## Integral em x
    funcao = '1/(x**(1/2)*(1-(2/x)**(3/4))**(1/3))'
    integral_em_x = Quadratura(funcao,2,2+L).gauss_legendre(500)
    ## Taxa
    q_conv = 0.332*(V_ar/ni)**(1/2)*Pr**(1/3) * k * (Ts-Tinf) * H * integral_em_x
    ## Output
    print("b)")
    print(f"q = {q_conv}, Re = {Re}, integral em x = {integral_em_x} \n")

def main():
    ## Dados problema
    Ts = 273 + 15
    Tinf = 273 + 10
    H = 2
    L = 1
    V_ar = 2 
       
    ## Temperatura de filme
    Tf = (Ts+Tinf)/2
    
    ## Dados da tabela interpolados para temperatura de filme
    ni = interpolacao_linear(Tf,250,300,ar.ni250,ar.ni300)
    k = interpolacao_linear(Tf,250,300,ar.k250,ar.k300)
    Pr = interpolacao_linear(Tf,250,300,ar.Pr250,ar.Pr300)

    letra_a(V_ar,L,H,ni,k,Ts,Tinf,Pr)
    letra_b(V_ar,L,H,ni,k,Ts,Tinf,Pr)

if __name__ == "__main__":
    main()
