##
##      MÉTODOS NUMÉRICOS APLICADOS (EQE358) - MÓDULO IX                     
## Procedimentos gerais relacionados ao Módulo IX da diciplina
## 
##               Equações diferenciais ordinárias
##                    Métodos de Runge-Kutta:
##      Método de Euler - Método de Heun - Método do ponto médio
##

import matplotlib.pyplot as plt
from sympy import Symbol, lambdify, exp
from numpy import linspace, poly1d
from time import time
from .ajustes_de_curvas import Interpolacao, Regressao


################## DADOS ##################

equacao = 'dy/dx = 4 - 0.3*y - 0.1*exp(-0.6 * x)*exp(1.4)'#'dy/dx = -0.5*y'

#'dy/dx = 4*exp(0.8*x) - 0.5*y' 
#'dx/dy = -2*x^3+12*x^2-20*x+8.5'

grau_equacao = None

condicao_inicial = x0,y0 = 0,6

intervalo = 0,2

passo = 0.5


# Opções

metodo = {
    'euler':True,
    'heun':False,
    'ponto medio': False
}

ajuste_de_curva = { ## Apenas para polinomios
    'interpolacao':False,
    'regressao polinomial':False,
    'regressao exponencial':True,
    'regressao logaritmica':False
}

plotar = True

tolerancia_refino_heun = 0.0001



################## PROCEDIMENTOS ##################

## Procedimentos gerais

from .procedimentos_gerais import avaliar,arredondar_expr




class RungeKutta():
    def __init__(self,equacao,intervalo,passo,grau,var=Symbol('x')):
        
        for v in var:
            exec(f"{v} = Symbol('{v}')")

        self.eq = equacao
        if isinstance(self.eq,str):
            if '=' in self.eq:
                self.eq = self.eq.split('=')[1]
            self.eq = eval(self.eq.replace('^','**'))

        self.eq_implicita = False
        if str(equacao).split('=')[0].split('/')[0].split('d')[1] in str(self.eq):
            self.eq_implicita = True

        self.a,self.b = intervalo
        self.h = passo

        if isinstance(grau,int):
            self.grau = grau
        else:
            self.grau = int((self.b-self.a)/self.h)
 
        if self.eq_implicita:
            self.var = var[0]
            self.vars = var
            if len(self.eq.atoms(Symbol))==1:
                self.vars = ['',self.var]
        else:
            self.var = var
    

    def plot(self,derivada,funcoes,pontos,temporizador=False):
        ''' Esboça o gráfico'''
        # Inicia o temporizador
        if temporizador:
            start = time()

        # Define a figura e eixo de plot
        self.fig = plt.figure(figsize=(12,6))
        self.ax = self.fig.subplots()

        # Plota os pontos
        self.ax.plot(*pontos,'o',label=' Pontos obtidos pelo método',color='red')
        # Anota se há igual ou menos de 16 pontos:
        if len(pontos[0])<=16:
            for i,j in zip(*pontos): 
                self.ax.annotate(str(' ({:.3f}'.format(round(i,3)) + ', {:.3f})'.format(round(j,3))),xy=(i,j))

        # Define as coordenadas x
        coordenadas_x = linspace(self.a,self.b)

        # Plota a derivada (se for em função de apenas uma variável)
        if not self.eq_implicita:
            self.ax.plot(coordenadas_x,lambdify(self.var,derivada,modules=['numpy'])(coordenadas_x),label=f" f'({self.var}) = "+str(arredondar_expr(derivada,10)).replace('**','^'))

        for funcao,tipo,string in funcoes:
            # Plota a(s) função(ões) obtida(s)
            if tipo == 'interpolacao':
                # Define as coordenadas y para plotar a(s) função(ões)
                coordenadas_y = lambdify(self.var,funcao,modules=['numpy'])(coordenadas_x)
                self.ax.plot(coordenadas_x,coordenadas_y,label=' F'+string[2::]+'\n (Interpolação)')
            if tipo.split(' ')[0] == 'regressao':
                # Define as coordenadas y para plotar a(s) função(ões)
                coordenadas_y = [funcao(px) for px in coordenadas_x]
                self.ax.plot(coordenadas_x,coordenadas_y,label=' F'+string[2::]+'    (Regressão)',linestyle='dashed')
     
        # Legenda
        self.ax.legend(loc='upper left')

        if temporizador:
            tempo_plot = time()-start
            plt.show()
            return tempo_plot

        plt.show()



    def geral(self,condicao_inicial,metodo='euler',ajuste_curva=None,plotar=False):    
        ''' 
        Parâmetros:
        condicao_inicial    ==>     [float,float,...]; 
        metodo:             ==>     str;
        ajuste_curva        ==>     dict(str:bool);
        plotar              ==>     bool;
            
        Retorno:
        pontos              ==>     list(zip(list,list)); 
        funcoes             ==>     list(sympy function/ lambda function);
        tempo               ==>     float;
        tempo_grafico       ==>     float;
        '''
                
        ## Inicia o cronometro
        start = time()

        ## Erros
        erros = []

        ## Primeiros x e y
        atual_x, atual_y = condicao_inicial
        
        ## Calcula a quantidade de iterações necessárias
        iteracoes = int((self.b-self.a)/self.h)

        ## Pontos iniciais xn,yn
        pontos_x = [atual_x]
        pontos_y = [atual_y]

        ## Para cada ponto de x no intervalo (atualiza o xn a cada iteração)
        for i in range(iteracoes):
            # Calcula o xn+1
            prox_x = atual_x + self.h

            if metodo != 'ponto medio':
                # Calcula o yn+1 com o método de euler
                if self.eq_implicita:
                    prox_y = atual_y + self.h * avaliar(self.eq,[atual_x,atual_y],self.vars)
                else:
                    prox_y = atual_y + self.h * avaliar(self.eq,atual_x,self.var)

                # Corrige o yn+1 com o método de heun
                if metodo == 'heun':
                    if self.eq_implicita:     
                        # Refina o yn+1 a partir do y predito até onde não for possível mais alterar seu valor           
                        while True:
                            y_predito = prox_y
                            prox_y = atual_y + self.h * (avaliar(self.eq,[atual_x,atual_y],self.vars) + avaliar(self.eq,[prox_x,y_predito],self.vars))/2
                            if abs(y_predito-prox_y)<=self.tolerancia_refino: break  # Para quando forem iguais
                    # Se a equação não for função da variável dependente, calcula apenas com o valor anterior de x
                    else:
                        prox_y = atual_y + self.h * (avaliar(self.eq,atual_x,self.var) + avaliar(self.eq,prox_x,self.var))/2

            # Calcula o yn+1 com o método do ponto medio
            elif metodo == 'ponto medio':
                if self.eq_implicita:
                    prox_y = atual_y + self.h * avaliar(self.eq, [atual_x+self.h/2, atual_y+avaliar(self.eq,[atual_x,atual_y],self.vars)*self.h/2], self.vars)
                else:
                    prox_y = atual_y + self.h * avaliar(self.eq, atual_x+self.h/2, self.var)

            # Guarda xn+1 e yn+1
            pontos_y.append(prox_y)
            pontos_x.append(prox_x)
            # Atualiza xn e yn
            atual_x = prox_x
            atual_y = prox_y

        funcoes = []
        tempo_na_tela_do_grafico = 0
        if any(ajuste_curva.values()):
        ## Interpola/Regride os pontos obtidos para obter a função
            interp = Interpolacao(pontos_x,pontos_y,grau=self.grau,var=self.var)
            reg = Regressao(pontos_x,pontos_y)

            if ajuste_curva['interpolacao']:
                funcao = interp.newton()
                tipo = 'interpolacao'
                string = 'f(x) = ' + str(arredondar_expr(funcao,10)).replace('**','^')
                funcoes.append([funcao,tipo,string])

            if ajuste_curva['regressao polinomial']:  
                funcao,r2,string = reg.regressao_polinomial(grau=self.grau)
                funcao = reg.montar_funcao(funcao,'polinomial')
                tipo = 'regressao polinomial'
                funcoes.append([funcao,tipo,string])

            if ajuste_curva['regressao exponencial']:
                funcao,r2,string = reg.regressao_exponencial()
                funcao = reg.montar_funcao(funcao,'exponencial')
                tipo = 'regressao exponencial'
                funcoes.append([funcao,tipo,string])
                
            if ajuste_curva['regressao logaritmica']:
                funcao,r2,string = reg.regressao_logaritmica()
                funcao = reg.montar_funcao(funcao,'logaritmica')
                tipo = 'regressao logaritmica'
                funcoes.append([funcao,tipo,string])

        tempo_na_tela_do_grafico = 0
        ## Plota o gráfico se True e se a função não for em termos da variável dependente
        if plotar:
            start2 = time()
            tempo_plot = self.plot(self.eq,funcoes,[pontos_x,pontos_y],True)
            tempo_na_tela_do_grafico = time()-start2-tempo_plot

        ## Para o cronometro
        tempo = time()-start-tempo_na_tela_do_grafico

        return list(zip(pontos_x,pontos_y)),funcoes,tempo,tempo_na_tela_do_grafico


    def euler(self,condicao_inicial,ajuste_curva=None,plotar=False):
        ''' Aplica o método de euler para a resolução de equações diferenciais ordinárias de primeira ordem'''
        return self.geral(condicao_inicial,'euler',ajuste_curva,plotar)


    def heun(self,condicao_inicial,ajuste_curva=None,plotar=False,tolerancia_refino=10**(-4)):
        ''' Aplica o método de heun para a resolução de equações diferenciais de primeira ordem'''
        self.tolerancia_refino = tolerancia_refino
        return self.geral(condicao_inicial,'heun',ajuste_curva,plotar)


    def ponto_medio(self,condicao_inicial,ajuste_curva=None,plotar=False):
        ''' Aplica o método do ponto medio para a resolução de equações diferenciais de primeira ordem'''
        return self.geral(condicao_inicial,'ponto medio',ajuste_curva,plotar)





def interface(pontos,funcoes,tempos):        
    print(f'\n Pontos: \n{pontos}')
    for funcao in funcoes:
        print(f'\n  {funcao[1]}: \n ',str(funcao[2]).replace('**','^'))
    print(f'\n Tempo cálculo:  {tempos[0]}')
    #print(f'\n Tempo na tela do gráfico:  {round(tempos[1],2)} \n')



def main():

    if isinstance(equacao,str):
        if '=' in equacao:
            eq = equacao.split('=')[1]
        eq = eval(eq.replace('^','**'))
    variaveis = list(eq.atoms(Symbol))
    variaveis.sort(key=str)
    metodos = RungeKutta(equacao,intervalo,passo,grau_equacao,var=variaveis)

    if metodo['euler']:
        pontos,funcoes,tempo,tempo_tela_grafco = metodos.euler(condicao_inicial,ajuste_curva=ajuste_de_curva,plotar=plotar)
        interface(pontos,funcoes,[tempo,tempo_tela_grafco])

    if metodo['heun']:
        pontos,funcoes,tempo,tempo_tela_grafco = metodos.heun(condicao_inicial,ajuste_curva=ajuste_de_curva,plotar=plotar,tolerancia_refino=tolerancia_refino_heun)
        interface(pontos,funcoes,[tempo,tempo_tela_grafco])

    if metodo['ponto medio']:
        pontos,funcoes,tempo,tempo_tela_grafco = metodos.ponto_medio(condicao_inicial,ajuste_curva=ajuste_de_curva,plotar=plotar)
        interface(pontos,funcoes,[tempo,tempo_tela_grafco])







if __name__ == "__main__":
    x = Symbol('x')
    y = Symbol('y')
    main()