##
##      MÉTODOS NUMÉRICOS APLICADOS (EQE358) - MÓDULO VII                     
## Procedimentos gerais relacionados ao Módulo VII da diciplina
## 
##                   Integração numérica
##          Método de Newton-Cotes: Regra do trapézio
##                                  Regra de 1/3 de Simpson
##
##


import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines,patches
from numpy import array
from time import time
from raizes_de_equacoes import metodo_bisseccao,metodo_falsa_posi,metodo_newton_raphson,metodo_secante
from ajustes_de_curvas import Interpolacao



################## DADOS ##################

#x = sp.Symbol('x')
#funcao = '0.2 + 25*x - 200*x^2 + 675*x^3 - 900*x^4 + 400*x^5'
#intervalo = 0,math.pi
 
#funcao = 'sin(y)'
#intervalo = 0,math.pi

# Problema avaliação 6
funcao = amostra = ([0,10,20,30,35,40,45,50],[10,35,55,52,40,37,32,34])
constante = Q = 4
unidade = 'mg/min'
intervalo = 0,50

## A partir da tolerância, o número de retangulos/polinomios será automaticamente definido
tolerancia = 10**(-4)

## Caso desejado definir manualmente a quantidade de retangulos/polinomios, basta atribuir valor à n 
n = 16

## Regra(s) a se utilizar
regra = {
    'Regra do Trapézio':True,
    'Regra de 1/3 de Simpson':False
}

## Define se vai plotar o gráfico
plotar = True
plot_animado = True

## Define se vai imprimir o texto formatado
formatar = True






################## PROCEDIMENTOS ##################

## Procedimentos gerais

from procedimentos_gerais import avaliar,derivada



## Integração numérica

class Newton_Cotes:
    ''' Substitui funções complicadas ou dados tabulados por funções
    aproximadas simples e fáceis de integrar. '''
    def __init__(self,funcao,a,b,var=sp.Symbol('x'),constante=1,unidade=''):       
        self.f = funcao
        self.var = var
        self.a,self.b = a,b
        self.C = constante
        self.unidade = unidade

        ## Se a função for uma string:
        if isinstance(self.f,str):
            self.f = sp.sympify(self.f.replace('^','**'))
            self.var = list(self.f.free_symbols)[0]


        ## Se a função for uma amostra
        if isinstance(self.f,list) or isinstance(self.f,tuple):
            if len(self.f) != 2: raise IndexError(" A função deve ser uma expressão sympy, ou duas listas, uma com os pontos x e outra com os pontos y ")
            ## Separa os pontos da amostra
            self.pontos_x = self.f[0]
            self.pontos_y = self.f[1]
            ## Define a função a partir da interpolação de lagrange dos pontos
            grau = len(self.pontos_x)-1     #maior possível
            self.f = Interpolacao(self.pontos_x,self.pontos_y,grau,self.var).newton()

        ## (Re)Define os pontos a partir da função  (para o plot)
        self.pontos_x = np.linspace(self.a, self.b, num=100)
        self.pontos_y = sp.lambdify(self.var,self.f,modules = ['numpy'])(self.pontos_x)


    def iniciar_plot(self,regra,n,animado=True):
        ''' Função auxiliar '''
        ## Inicia a figura e define uma margem de 10%
        self.fig = plt.figure(figsize=(16,8))
        self.ax = self.fig.add_subplot()
        self.ax.margins(0.1)

        ## Define o título da figura
        titulos = {self.calculo_regra_simpson:f'Regra 1/3 de Simpson \n {n} Polinômios \n',self.calculo_regra_trapezio:f'Regra do trapézio \n {n} Trapézios \n'}
        titulo = titulos[regra]
        plt.title(titulo)

        ## Pausa o código por 1sec, para fins de visualização
        if animado:
            plt.pause(1)

        ## Configura a figura
        plt.grid()
        plt.xlabel(f'{str(self.var).upper()}',fontsize = 'large')
        plt.ylabel(f'F({str(self.var).upper()})',fontsize = 'large')

        ## Pausa o código por 1sec, para fins de visualização
        if animado:
            plt.pause(1)

        ## Plota a função, pinta a área abaixo da curva e define a legenda
        self.ax.plot(self.pontos_x,self.pontos_y,color='Black')
        plt.fill_between(self.pontos_x,self.pontos_y,color='Black',alpha=0.2)
        self.labels = [f' f({self.var}) = {self.f*self.C}   [{self.a},{self.b}]'.replace('**','^'),' Integral','']
        self.ax.legend(labels=self.labels, loc='upper left') 

        ## Pausa o código por 1.25sec, para fins de visualização
        if animado:
            plt.pause(1.25)


    def plot(self,pontos,regra,area,erro,animado=True):
        ''' Função auxiliar '''

        ## Plota de acordo com a regra utilizada
        if regra == self.calculo_regra_trapezio:    # Desenha trapézios (com área preenchida)
            self.ax.add_patch(patches.Polygon(xy=pontos, fill=True,color='orange',alpha=0.2))
        
        elif regra == self.calculo_regra_simpson:   # Desenha polinômios (com área abaixo preenchida)
            self.ax.plot(pontos[0],pontos[1])
            self.ax.fill_between(array(pontos[0], dtype=float),array(pontos[1], dtype=float),alpha=0.2)
       
        ## Atualiza a legenda
        patchs = lines.Line2D([],[],color='Black'), patches.Patch(color='Black', alpha=0.2), lines.Line2D([], [], color='red', marker='x',markersize=5, linestyle='None')
        self.labels[1] = f' Integral ≈ {area*self.C} {self.unidade}'    
        self.labels[2] = f' Erro = {erro}%'  
        self.ax.legend(handles=patchs, labels=self.labels, loc='upper left')   
        
        ## Pausa o código por 0.25sec, para fins de visualização
        if animado:
            plt.pause(0.25)


    def regras_geral(self,regra,calculo_erro,a,b,tolerancia=10e-2,n=None,plotar=False,plot_animado=False,formatar=True):
        '''Procedimento geral para aplicação tanto da Regra de 1/3 de Simpson quanto da Regra do Trapézio.
       
        regra -->  Procedimento de calculo referente à regra escolhida
        
        calculo_erro -->  Lista contendo:  divisor do cálculo do erro (12 ou 2880), a derivada (segunda/quarta) e o expoente da raiz (quadrada ou quarta)
        
        a,b -->  Intervalo total para aplicação da regra
        
        tolerancia -->  Valor máximo do erro

        n --> Número de trapezios/polinomios (Definido apenas se não for desejado que o procedimento calcule-o automaticamente)

        Retorna o resultado da integração numérica, n, e o tempo levado para o cálculo.
        float,int,lista'''

        ## Erros aproximados
        lista_erros = []

        ## Temporizador
        lista_tempos = []

        denominador,derivada,expoente = calculo_erro

        ## Definição automática do n   (a partir da relação com a segunda/quarta derivada)
        if not n:  
            # Cálculo do valor máximo da segunda/quarta derivada
            valor_de_maximo = max([sp.maximum(derivada,self.var,sp.Interval(a,b)).evalf(),sp.minimum(derivada,self.var,sp.Interval(a,b)).evalf()],key=abs)
            
            # Cálculo do x0 correspondente ao ponto de máximo (homogeinizar e resolver)
            metodos = [metodo_newton_raphson,metodo_secante,metodo_falsa_posi,metodo_bisseccao]
            for metodo in metodos:
                ponto_de_maximo = metodo(derivada-valor_de_maximo,a,b)[0]
                # Se algum método for capaz de resolver, não há necessidade de verificar os demais
                if isinstance(ponto_de_maximo,float): break               
  
            # Caso nenhum método do Modulo_3 seja capaz de resolver, utilizará-se o método built-in do sympy
            if not isinstance(ponto_de_maximo,float): 
                ponto_de_maximo = sp.nsolve((derivada-valor_de_maximo),(b+a)/2)
        
            # Estimativa do passo e do número de polinomios necessários
            h = (abs((denominador*tolerancia)/((b-a)*avaliar(derivada,ponto_de_maximo,self.var))))**(expoente)
            n = (b-a)/h

            # Transformar n em inteiro
            n = int(n)+1 #Soma-se um para considerar arredondamentos para cima sempre

        # Redefinir passo
        h = (b-a)/n

        ## Pontos
        xi = [a+h*k for k in range(n+1)]
        atual = xi[0]

        ## Avalia se haverá plot
        if plotar and plot_animado:
            self.iniciar_plot(regra,n)
            
        todos_pontos = []
        ## Integração numérica pela Regra do Trapézio ou pela Regra de 1/3 de Simpson
        I = 0
        for i in range(1,n+1):
            start = time()  # Temporizador

            # Define o próximo ponto
            prox = xi[i]

            # Define o antigo valor da integração (para cálculo do erro) 
            I_antigo = I            
            
            # Obtém-se o valor da iteração atual e pontos (para plotagem) de acordo com cada regra
            valor,pontos_plot = regra(atual,prox,plotar)  
            todos_pontos.append(pontos_plot)
            
            # Adiciona-se o valor atual ao total
            I += valor

            # Avalia o erro de cada iteração e adiciona à lista
            lista_erros.append(round(abs((I-I_antigo)/I*100),4))

            # Traça o gráfico, caso plot == True
            if plotar and plot_animado: 
                self.plot(pontos_plot,regra,round(I,4),lista_erros[-1]) 

            # Atualiza o ponto atual
            atual = prox
            lista_tempos.append(time()-start)  # Temporizador

        ## Troca o valor do primeiro erro para None
        lista_erros[0] = None

        ## Mantém o gráfico aberto, se houver
        if plotar: 
            if not plot_animado:
                self.iniciar_plot(regra,n,False)
                for ponto in todos_pontos:
                    self.plot(ponto,regra,round(I,4),lista_erros[-1],animado=False)
            plt.show()

        ## Retorna/imprime a integração, o número de subintervalos, o tempo levado e os erros
        if formatar:
            return self.formata(regra,I,n,lista_tempos,lista_erros)
        else:
            return I,n,lista_tempos,lista_erros



    def calculo_regra_trapezio(self,a,b,plot):
        ''' Função auxiliar para a aplicação da regra do trapézio'''
        ## f(a) e f(b)
        f_a = avaliar(self.f,a,self.var)
        f_b = avaliar(self.f,b,self.var)
        ## Integral
        I = (b-a)*(f_a+f_b)/2
        ## Pontos para plot
        pontos = None
        if plot:
            pontos = [(a,0),(a,f_a),(b,f_b),(b,0)]  
        return I,pontos


    def regra_trapezio(self,tolerancia=tolerancia,n=None,plotar=False,plot_animado=False,formatar=True):
        ''' Aplica a regra do trapézio para a integração numérica de uma função no intervalo [a,b].
        Encontra o valor de trapézios necessários baseado na tolerancia definida para o erro
        
        Retorna o resultado da integração numérica, o número de trapézios, e o tempo levado para o cálculo.
       
        float,float,*float,*float --> float,int,lista'''

        return self.regras_geral(self.calculo_regra_trapezio,[12,derivada(self.f,self.var,n=2),1/2],self.a,self.b,tolerancia,n,plotar,plot_animado)



    def calculo_regra_simpson(self,a,b,plot):
        ''' Função auxiliar para a aplicação da regra de 1/3 de Simpson.'''
        ## Cálculo h
        h = (b-a)/2
        ## Cálculo do ponto médio
        ponto_medio = (a+b)/2
        ## Avaliação da função nos pontos
        f_x0 = avaliar(self.f,a,self.var)
        f_x1 = avaliar(self.f,ponto_medio,self.var)
        f_x2 = avaliar(self.f,b,self.var)
        ## Integração numérica pela regra de 1/3 de Simpson
        I = h/3 * (f_x0+4*f_x1+f_x2)
        
        pontos_plot = None
        if plot:
            ## Interpola o polinomio de lagrange
            pontos_x = [a,ponto_medio,b]
            pontos_y = [f_x0,f_x1,f_x2]
            pol = Interpolacao(pontos_x,pontos_y,2,self.var).newton()
            ## Define os pontos para plotar o gráfico
            pontos_x = np.linspace(a,b,num=4)
            pontos_y = [avaliar(pol,px,self.var) for px in pontos_x]
            pontos_plot = pontos_x,pontos_y

        return I,pontos_plot


    def regra_simpson(self,tolerancia=tolerancia,n=None,plotar=False,plot_animado=False,formatar=True):
        ''' Aplica a regra de 1/3 de Simpson para a integração numérica de uma funcao no intervalo [a,b].
        Encontra o valor de polinômios necessários baseado na tolerancia definida para o erro
        
        Retorna o resultado da integração numérica, o número de polinômios, e o tempo levado para o cálculo.
       
        float,float,*float,*float --> float,int,lista'''
        
        return self.regras_geral(self.calculo_regra_simpson,[2880,derivada(self.f,self.var,n=4),1/4],self.a,self.b,tolerancia,n,plotar,plot_animado)


    def formata(self,regra,*retorno):
        ''' Imprime na tela o retorno formatado. '''
        if regra == self.calculo_regra_trapezio: regra = "trapézios" 
        if regra == self.calculo_regra_simpson: regra = "polinômios" 
        strs = [
            f"\nValor aproximado:     {retorno[0]} " + (f"* {self.C} (constante)   [{metodo.unidade}]" if self.C!=1 else ''),
            f"\n\nTolerância:     {tolerancia} ",
            f"  \n\nNúmero de {regra}:  {retorno[1]} ",
            f"\nOBS: Caso o número de {regra} tenha sido definido automaticamente, provavelmente um número menor já seria suficiente para a tolerância estabelecida ",
            f'\n\nErros aproximados relativos:   {retorno[-1]}',
            f"\n\nTempo total decorrido (s):  {round(sum(retorno[2]),4)} ",
            '\n'
        ]
        print(''.join(strs))
        return retorno






#########################################################################


def main():

    try:
        argumentos = [funcao,intervalo[0],intervalo[1],x,constante,unidade]
        constant = True
    except NameError:
        argumentos = [funcao,intervalo[0],intervalo[1]]
        constant = False

    metodo = Newton_Cotes(*argumentos)


    if regra['Regra de 1/3 de Simpson']:
        print(metodo.regra_simpson(tolerancia=tolerancia,n=n,plotar=plotar,plot_animado=plot_animado,formatar=formatar))

    if regra['Regra do Trapézio']:
        print(metodo.regra_trapezio(tolerancia=tolerancia,n=n,plotar=plotar,plot_animado=plot_animado,formatar=formatar))


if __name__ == "__main__":
    main()
