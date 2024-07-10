##
##      MÉTODOS NUMÉRICOS APLICADOS (EQE358) - MÓDULO VIII                     
## Procedimentos gerais relacionados ao Módulo VIII da diciplina
## 
##                     Integração de equações
##

import matplotlib.pyplot as plt
from matplotlib import lines,patches
from sympy import Symbol,lambdify
from numpy import polynomial,linspace
from ajustes_de_curvas import Interpolacao


################## DADOS ##################

# Variável x
x = Symbol('x')

from sympy import log
funcao = 'log(x)' #'0.2 + 25*x - 200*x^2 + 675*x^3 - 900*x^4 + 400*x^5'

intervalo = 2,3

tolerancia = 10**(-4)

grau = 3


################## PROCEDIMENTOS ##################

## Procedimentos gerais

from procedimentos_gerais import avaliar, derivada, mudar_variavel



## Integração de equações

class Quadratura:
    def __init__(self,funcao,var=Symbol('x'),a=intervalo[0],b=intervalo[1]):
        ''' Inicia a função (expr) e a variável (Symbol) '''
        self.f = funcao
        self.var = var
        self.a,self.b = a,b

        ## Se a função for uma amostra
        if isinstance(self.f,list) or isinstance(self.f,tuple):
            if len(self.f) != 2: raise IndexError(" A função deve ser uma expressão sympy, ou duas listas, uma com os pontos x e outra com os pontos y ")
            ## Separa os pontos da amostra
            self.pontos_x = self.f[0]
            self.pontos_y = self.f[1]
            ## Define a função a partir da interpolação de newton dos pontos
            self.f = Interpolacao(self.pontos_x,self.pontos_y,len(self.pontos_x)-1,self.var).newton()

        ## Se a função não for uma amostra, separá-la em pontos
        else:
            self.pontos_x = linspace(self.a,self.b)
            self.pontos_y = lambdify(self.var,self.f,modules = ['numpy'])(self.pontos_x)


    def iniciar_plot(self,f,var,n):
        ''' Função auxiliar '''
        ## Inicia a figura e mostra as grades 
        self.fig = plt.figure(figsize=(12,6))
        self.axs = self.fig.subplots(2)
        self.axs[0].grid()   
        self.axs[1].grid()  

        ## Define o título da figura
        titulo = f'Quadratura de Newton-Legendre \n grau {n} \n'
        self.fig.suptitle(titulo)
        
        ## Plota a função, define sua legenda e pinta a área abaixo da curva
        self.axs[0].plot(self.pontos_x,self.pontos_y,color='Black',label=f'f(x) = {self.f}   [{self.a},{self.b}]'.replace('**','^'))
        self.axs[0].fill_between(self.pontos_x,self.pontos_y,color='Black',alpha=0.2)
        self.axs[0].legend(loc='upper left')
        self.axs[0].margins(0.1)

        ## Plota a função com intervalo alterado e define sua legenda
        self.pontos_x2 = linspace(-1,1)
        self.pontos_y2 = lambdify(var,f,modules = ['numpy'])(self.pontos_x2)
        self.axs[1].plot(self.pontos_x2,self.pontos_y2,color='Black')
        # Pinta a área abaixo da curva em transparete apenas para definir a margem automaticamente
        self.axs[1].fill_between(self.pontos_x2,self.pontos_y2,color='Black',alpha=0.0)
        self.axs[1].margins(0.1)
        # Legenda
        self.labels = [f'f({var}) = {f}   [-1, 1]'.replace('**','^'),'']
        self.axs[1].legend(labels=self.labels, loc='upper left')  

        ## Pausa o código por 1sec, para fins de visualização
        plt.pause(2)


    def plot(self,pontos,area):
        ''' Função auxiliar '''

        ## Desenha os retangulos
        self.axs[1].add_patch(patches.Polygon(xy=pontos, fill=True,color='orange',alpha=0.4))

        ## Atualiza a legenda
        patchs = lines.Line2D([],[],color='Black'), patches.Patch(color='orange', alpha=0.2)
        self.labels[1] = f' Área ≈ {area}'    
        self.axs[1].legend(handles=patchs, labels=self.labels, loc='upper left')   

        ## Pausa o código por 0.5sec, para fins de visualização
        plt.pause(0.75)


    def mudanca_intervalo(self,f,var,a,b):
        ''' Função auxiliar para a aplicação da Quadratura de Gauss-Legendre.
        Muda o intervalo de uma função(var) de [a,b] para [-1,1] 

        expr,Symbol,float,float --> expr,Symbol'''

        ## Define a nova variável
        xd = Symbol('xd')

        ## Estabelece a mudança de variável para alterar o intervalo
        x = (b+a)/2 + (b-a)*xd/2

        ## Estabelece a mudança do dx da variável
        dx = derivada(x,xd,n=1)

        ## Aplica a mudança na função e multiplica pelo dx
        f = mudar_variavel(f,var,x)*dx

        ## Retorna a função e a nova variável (Symbol)
        return f,xd
    

    def gauss_legendre(self,n):
        ''' Aplica a Quadratura de Guass-Legendre para uma função no intervalo [a,b], com grau n.

        float,float,int --> float'''
        
        ## Chama a função auxiliar para a mudança de intervalo
        funcao,variavel = self.mudanca_intervalo(self.f,self.var,self.a,self.b)

        ## Decide se haverá plot
        plot = False
        if n <= 20:
            plot = True
            self.iniciar_plot(funcao,variavel,n)
            soma_pesos = -1

        ## Obtém os pontos e pesos tabelados para a quadratura de grau n
        pontos,pesos = polynomial.legendre.leggauss(n)

        ## Realiza a integração numérica
        I = 0
        for ponto,peso in zip(pontos,pesos):
            I += avaliar(funcao,ponto,variavel)*peso
            ## Se 'plot' for True, define os retangulos e esboça o gráfico
            if plot:
                soma_pesos_antigo = soma_pesos
                soma_pesos += peso
                pontos_plot = [(soma_pesos_antigo,0), (soma_pesos_antigo,avaliar(funcao,ponto,variavel)), (soma_pesos,avaliar(funcao,ponto,variavel)), (soma_pesos,0)]
                self.plot(pontos_plot,round(I,4))

        if plot: plt.show()
            
        ## Retorna o valor
        return I




#########################################################################

def main():
    a = Quadratura(funcao,x,intervalo[0],intervalo[1]).gauss_legendre(grau)
    print(a)


if __name__ == "__main__":
    if isinstance(funcao,str):
        funcao = eval(funcao.replace('^','**'))
    main()