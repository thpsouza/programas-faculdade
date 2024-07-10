##
##      MÉTODOS NUMÉRICOS APLICADOS (EQE358) - MÓDULO VI                     
## Procedimentos gerais relacionados ao Módulo VI da diciplina
## 
##                      Ajuste de curvas
##                Regressão:  Linear e Polinomial 
##                Interpolação: Newton e Lagrange
##

from time import time
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
plt.rcParams["font.size"] = 9
import math

## Dados
amostra_x = [-2, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]
amostra_y = [-5, -7.5, -5.2, -1.5, 1.1, 1.6, 1.0, 1.6, 7.2]

valor_para_estimar = None

visualizar_dados = False #(Pré ajuste)


## Precisão 
tolerancia = 1.0

casas_decimais = 10

''' OBS:
    Para a regressão, se tolerância for definida, os coeficientes serão arredondados automaticamente 
    até atingir tal valor.
    
    Se a tolerância tiver valor 'None', então os coeficientes serão arredondados para o número
    de casas definidas em 'casas_decimais' 
'''

## Opções
grau = len(amostra_x)-1
graus = [i for i in range(1,grau+1)]

plot = True     #(Após ajuste)
animado = True   #(Apenas interpolação)

# Definir qual(is) ajuste(s) realizar
ajuste_de_curva = {
    'regressao simples':                False,
    'regressao polinomial':             False,
    'regressao polinomial multipla':    False,
    'regressao exponencial':            False,
    'regressao logaritmica':            False, 
    'interpolacao newton':              True,
    'interpolacao lagrange':            False
}

# Variável da função
variavel = sp.Symbol('x')

# Retornar coeficientes em um dicionário
dic = True

# Nome dos eixos:
eixo_x = "Temperatura (°C)"
eixo_y = "Concentração (g/100g H2O)"
tamanho_eixos = 13

# Título gráfico:
titulo = "\n\nCurva de solubilidade KNO3"
tamanho_titulo = 18

################## PROCEDIMENTOS ##################

from procedimentos_gerais import avaliar,arredondar_expr



## Ajuste de Curvas
class Regressao:
    ''' Regressão linear/polinomial/logaritmica/exponencial para uma dada amostra x,y 
    
        OBS:
        Se tolerância for definida, os coeficientes serão arredondados automaticamente 
        até atingir tal valor.

        No entanto, se a tolerância tiver valor 'None', então os coeficientes serão arredondados 
        com o número de casas definidas em 'casas_decimais' 
'''
    def __init__(self,x,y):
        self.X = np.array(x,dtype='float')
        self.y = np.array(y,dtype='float')
        self.n = len(self.X)

    
    def plot(self,coeficientes,tipo_de_regressao,string_polinomio='',titulo='',multi=False, nomes_eixos=['X','Y']):
        ''' Plota o gráfico da reta de regressão de uma dada amostra 
        '''
        ## Inicia a figura/subplot e define as margens
        self.fig,self.ax = plt.subplots()
        self.ax.margins(0.1)
        self.ax.grid()

        ## Plota os dados amostrais
        self.ax.plot(self.X,self.y,'o',color='red')

        ## Mostra as coordenadas nos pontos (se menos que 20)
        if len(self.X)<=20:
            for i,j in zip(self.X,self.y):
                self.ax.annotate(f'({i} , {round(j,3)})',xy=(i,j), fontsize=tamanho_eixos)

        ## Espaço linear para suavizar o plot
        pontos_x = np.linspace(min(self.X),max(self.X))

        ## Plota a(s) curva(s) ajustada(s) no espaço linear definido
        # Multi curvas
        if multi == True:
            for coefs,string in zip(coeficientes,string_polinomio):
                funcao = self.montar_funcao(coefs.flatten(),tipo_de_regressao)
                pontos_y = [funcao(l) for l in pontos_x]
                self.ax.plot(pontos_x,pontos_y,label=string)
        # Curva única
        else:  
            if type(coeficientes) == np.ndarray: coeficientes = coeficientes.flatten()
            funcao = self.montar_funcao(coeficientes,tipo_de_regressao)
            pontos_y = [funcao(l) for l in pontos_x] 
            self.ax.plot(pontos_x,pontos_y,color='blue',label=string_polinomio)

        ## Adiciona a legenda e titulo da figura
        self.ax.legend(loc='upper left', fontsize=tamanho_eixos)
        self.fig.suptitle(titulo, fontsize=tamanho_titulo)
        
        ## Nomeia os eixos
        plt.xlabel(nomes_eixos[0],fontsize = tamanho_eixos)
        plt.ylabel(nomes_eixos[1],fontsize = tamanho_eixos)

        ## Deixa o gráfico na tela
        plt.show()


    def montar_funcao(self,coeficientes,tipo_de_regressao):
        ''' Retorna a função da regressão (callable) dados coeficientes e tipo de regressão '''
        # Dicionário com as funções das regressões possíveis
        tipos_de_regressao = {
            'polinomial':np.poly1d(coeficientes),
            'exponencial':lambda x : np.exp(coeficientes[0]*x) * np.exp(coeficientes[1]),
            'logaritmica':lambda x : coeficientes[0]*np.log(x) + coeficientes[1]
        }
        # Define a função a partir do dicionário
        funcao = tipos_de_regressao[tipo_de_regressao]
        # Retorna a função
        return funcao


    def avaliar_r2(self,tipo_de_regressao):
        ''' Avalia o coeficiente R2 da regressão'''
        # Define a função a partir dos coeficientes, de acordo com o tipo de regressão
        funcao = self.montar_funcao(self.coefs,tipo_de_regressao)
        # Avalia a função em todos os pontos x da amostra
        avalia_funcao = np.array([funcao(i) for i in self.X])
        # Calcula R2
        SSR = ((self.y-avalia_funcao)**2).sum()
        SST = ((self.y - self.y.mean())**2).sum()
        R2 = 1 - SSR/SST
        # Arredonda R2 se for 1 (retira os 0 excessivos)
        if R2 == 1:
            R2 = 1.0
        # Retorna o valor
        return R2
    

    def arredonda_coeficientes(self,coeficientes,tipo_de_regressao,tolerancia,casas_decimais):
        ''' Arredonda os coeficientes obtidos na regressão '''
        ## Arredonda automaticamente com o menor número de casas decimais necessárias para atingir a tolerancia definida
        if isinstance(tolerancia,float):
            k = 0
            novo_R2 = 0
            while True:
                # Arredonda os coeficientes com k casas decimais
                self.coefs = np.array([round(i,k) for i in coeficientes])
                # Calcula o R2 para tais coeficientes
                self.R2 = self.avaliar_r2(tipo_de_regressao)
                # Para o laço se o R2 for maior que a tolerancia
                if tolerancia <= abs(self.R2) <= 1:
                    break
                # Para o laço se não for possível atingir uma maior precisão
                if (self.R2-novo_R2) == 0:
                    self.coefs = np.array([round(i,k) for i in coeficientes])
                    break
                # Atualiza e aumenta o contador
                novo_R2 = self.R2
                k+=1

        ## Arredondamento manual caso um número específico de casas decimais seja requisitado
        else:
            self.coefs = np.array([round(i,casas_decimais) for i in coeficientes])
            self.R2 = self.avaliar_r2(tipo_de_regressao)


    def regressao_linear_simples(self,x0=None,plot=False,tolerancia=tolerancia,casas_decimais=10,dic=False,nomes_eixos=['X','Y'],titulo=''):
        ''' Calcula a reta de regressão linear de uma dada amostra 
        '''
        X2 = [float(self.X[i])**2 for i in range(self.n)]
        Y2 = [float(self.y[i])**2 for i in range(self.n)]
        XY = [float(self.X[i])*float(self.y[i]) for i in range(self.n)]
        
        sumX = sum(self.X)
        sumY = sum(self.y)
        sumX2 = sum(X2)
        sumY2 = sum(Y2)
        sumXY = sum(XY)

        a1 = (self.n*sumXY-sumX*sumY)/(self.n*sumX2-(sumX)**2)
        a0 = (sumY - a1*sumX)/self.n
        R = (self.n*sumXY-sumX*sumY)/((self.n*sumX2-(sumX)**2)**(1/2)*(self.n*sumY2-(sumY)**2)**(1/2))
        R2 = R**2
        
        self.coefs = [a1,a0]
        self.R2 = R2
        self.arredonda_coeficientes(self.coefs,'polinomial',tolerancia,casas_decimais)
        a1,a0 = self.coefs
        R2 = self.R2

        if a0 >= 0:
            string = f'f(x)  =  {round(a1,casas_decimais)} * x  +  {round(a0,casas_decimais)} \n' + f'R² =  {round(R2,casas_decimais)}'
        elif a0 <0:
            string = f'f(x)  =  {round(a1,casas_decimais)} * x  -  {round(abs(a0),casas_decimais)} \n' + f'R² =  {round(R2,casas_decimais)}'
        retorno = [self.coefs,self.R2,string]

        if plot == True:
            if not titulo:
                titulo = "REGRESSÃO LINEAR\n"
            self.plot([a1,a0],'polinomial',string,titulo=titulo,nomes_eixos=nomes_eixos)
     
        if x0 != None:
            f_x0 = a1*x0+a0
            retorno.append(f_x0)
           
        if dic == True: 
            self.dict = {'a0':round(a0,casas_decimais),'a1':round(a1,casas_decimais),'R2':round(R2,casas_decimais)}
            try:
                self.dict['f_x0'] = f_x0
            except UnboundLocalError:
                pass
            return self.dict
        
        return retorno


    def regressao_polinomial(self,grau,x0=None,plot=False,tolerancia=0.99,casas_decimais=10,dic=False,nomes_eixos=['X','Y'],titulo=''):
        ''' Calcula a curva de regressão de uma amostra pelo método 
        matricial
        '''
        if grau >= self.n: raise ValueError(" O grau do polinomio tem que ser menor do que o número de pontos conhecidos ")
    
        if grau == 1:
            return self.regressao_linear_simples(x0,plot,tolerancia,casas_decimais,dic)

        ## Regressao polinomial
        self.fit = np.polyfit(self.X,self.y,grau)

        ## Arredonda os coeficientes
        self.arredonda_coeficientes(self.fit,'polinomial',tolerancia,casas_decimais)
        
        ## Retira os termos de ordens superiores se foram arredondados para 0
        while True:
            if self.coefs[0] == 0:
                self.coefs = np.delete(self.coefs,0)
            else:
                break

        ## Redefine o grau da regressão
        grau = len(self.coefs)-1

        ## Monta a string do polinomio regredido
        string_poly = ' f(x)  =  ' + ' '.join((" + " if self.coefs[i]>=0 else " - ") + f'{abs(self.coefs[i])}*x^{abs(grau-i)}' for i in range(len(self.coefs)))
        string_poly = string_poly + f'\n R²  =  {self.R2}'

        ## Lista de retorno
        retorno = [self.coefs,self.R2,string_poly]
    
        ## Plota
        if plot == True:
            if not titulo:
                titulo = f'REGRESSÃO POLINOMIAL DE GRAU {grau}\n'
            self.plot(self.coefs,'polinomial',string_poly,titulo=titulo,nomes_eixos=nomes_eixos) 

        ## Avalia no ponto x0 (se desejado)
        if x0 is not None:
            f_x0 = np.poly1d(self.coefs)(x0)
            retorno.append(f_x0)

        ## Retorna os coeficientes em forma de um dicionário
        if dic == True:
            self.dict = {f'a{i}':self.coefs[-1-i] for i in range(len(self.coefs))}   
            try:
                self.dict['f_x0'] = f_x0
            except UnboundLocalError:
                pass
            return self.dict,string_poly             
        
        return retorno 


    def regressao_polinomial_multipla(self,graus,plot=False,tolerancia=0.99,casas_decimais=10,nomes_eixos=['X','Y'],titulo=''):
        ''' Encontra multiplas curvas de regressão dada amostra 
        '''
        coeficientes = []
        strings_polinomios = []

        for grau in graus:
            ret = self.regressao_polinomial(grau,plot=False,tolerancia=tolerancia,casas_decimais=casas_decimais,dic=False)
            coeficientes.append(ret[0])
            strings_polinomios.append(ret[2])
        
        if plot == True:
            if not titulo:
                titulo = f'REGRESSÃO POLINOMIAL DE GRAU {graus[-1]}\n'
            self.plot(coeficientes,'polinomial',strings_polinomios,titulo=titulo,multi=True,nomes_eixos=nomes_eixos) 
    
        coeficientes = [coef.tolist() for coef in coeficientes]

        return coeficientes,strings_polinomios


    def regressao_exponencial(self,x0=None,plot=False,tolerancia=0.99,casas_decimais=10,dic=False,nomes_eixos=['X','Y'],titulo=''):
        ''' Calcula a curva de regressão exponencial de uma amostra 
            y = e^Ax * e^B  '''
        ## Regressao
        self.fit = np.polyfit(self.X,np.log(self.y),1)

        ## Arredonda os coeficientes
        self.arredonda_coeficientes(self.fit,'exponencial',tolerancia,casas_decimais)

        ## Monta a string para a exponencial regredida
        string_poly = f' f(x)  =  exp({self.coefs[0]} * x) * exp({self.coefs[1]})' 
        string_poly = string_poly + f'\n R²  =  {self.R2}'

        ## Lista de retorno
        retorno = [self.coefs,self.R2,string_poly]
    
        ## Plota
        if plot == True:
            if not titulo:
                titulo = f'REGRESSÃO EXPONENCIAL \n'
            self.plot(self.coefs,'exponencial',string_poly,titulo=titulo,nomes_eixos=nomes_eixos)

        ## Avalia no ponto x0 (se desejado)
        if x0 is not None:
            f_x0 = np.exp(self.coefs)(x0)
            retorno.append(f_x0)

        ## Retorna os coeficientes em forma de um dicionário
        if dic == True:
            self.dict = {'A':self.coefs[0],'B':self.coefs[1],'R2':self.R2}   
            try:
                self.dict['f_x0'] = f_x0
            except UnboundLocalError:
                pass
            return self.dict,string_poly             
        
        return retorno       


    def regressao_logaritmica(self,x0=None,plot=False,tolerancia=0.99,casas_decimais=10,dic=False,nomes_eixos=['X','Y'],titulo=''):
        ''' Calcula a curva de regressão logaritmica de uma amostra 
            y = A * ln(x) + B '''
        ## Regressao
        self.fit = np.polyfit(np.log(self.X),self.y,1)

        ## Arredonda os coeficientes
        self.arredonda_coeficientes(self.fit,'logaritmica',tolerancia,casas_decimais)

        ## Monta a string para o log regredido
        string_poly = f' f(x)  =  {self.coefs[0]} * ln(x) + {self.coefs[1]}'
        string_poly = string_poly + f'\n R²  =  {self.R2}'

        ## Lista de retorno
        retorno = [self.coefs,self.R2,string_poly]
    
        ## Plota
        if plot == True:
            if not titulo:
                titulo = f'REGRESSÃO LOGARITMICA \n'
            self.plot(self.coefs,'logaritmica',string_poly,titulo=titulo,nomes_eixos=nomes_eixos)

        ## Avalia no ponto x0 (se desejado)
        if x0 is not None:
            f_x0 = np.poly1d(self.coefs)(x0)
            retorno.append(f_x0)

        ## Retorna os coeficientes em forma de um dicionário
        if dic == True:
            self.dict = {'A':self.coefs[0],'B':self.coefs[1],'R2':self.R2}   
            try:
                self.dict['f_x0'] = f_x0
            except UnboundLocalError:
                pass
            return self.dict,string_poly      

        return retorno



class Interpolacao:
    ''' Interpolação de Newton/Lagrange de grau n para uma dada amostra x,y '''
    def __init__(self,x,y,grau,var=sp.Symbol('x')):
        self.var = var
        self.x = np.array(x)
        self.y = np.array(y)
        if grau >= len(self.x):
            raise ValueError(" O polinômio interpolador deve ter um grau menor do que a quantidade de pontos conhecidos. ")
        self.n = grau 

    def plot_auxiliar(self,string='',metodo='',nomes_eixos=['X','Y'],time=False):
        self.ax.clear()
        self.ax.margins(0.1)
        if time == True: plt.pause(0.75)
        plt.grid()
        plt.xlabel(nomes_eixos[0],fontsize = 'large')
        plt.ylabel(nomes_eixos[1],fontsize = 'large')
        if time == True: plt.pause(0.75)
        if metodo:
            plt.title(f" {metodo} \n\n {string}")
        elif string:
            plt.title(string)


    def plot(self,functions,erros,r2s,metodo,animado=False,casas_decimais=4,nomes_eixos=['X','Y'],titulo=''):
        self.fig,self.ax = plt.subplots()

        string = ''
        pontos_x = np.linspace(min(self.x),max(self.x))
        
        if casas_decimais is None: casas_decimais=4

        ## Se for desejado o plot animado:
        if animado == True:
            
            self.plot_auxiliar(metodo=metodo,nomes_eixos=nomes_eixos,time=True)

            for self.i,self.j in zip(self.x,self.y):
                self.ax.plot(self.i,self.j,'o',color='red')
                self.ax.annotate(f'({self.i} , {round(self.j,3)})',xy=(self.i,self.j))
                plt.pause(0.75)

            for k in range(len(functions)):
                if k > 0 and self.x0 != None: 
                    string = f' f{k}({self.x0}) = {avaliar(functions[k],self.x0,self.var)} \n Erro(f{k}({self.x0})) = {erros[k]} '

                self.plot_auxiliar(string,metodo=metodo)
                self.ax.plot(self.x,self.y,'o',color='red')
                if len(self.x)<=20:
                    for self.i,self.j in zip(self.x,self.y): self.ax.annotate(f'({self.i} , {round(self.j,3)})',xy=(self.i,self.j))
                F = [functions[k].evalf(subs={self.var:x}) for x in pontos_x]
                str_f = str(arredondar_expr(functions[k],casas_decimais))+f'\nR² = {round(r2s[k],4)}'
                self.ax.plot(pontos_x,F,label=str_f)
                plt.legend(loc = 'upper left')
                plt.pause(1)

        ## Caso contrário  
        else:
            self.plot_auxiliar(metodo=metodo,nomes_eixos=nomes_eixos,time=False)
            if self.x0 != None:
                string = f' fn({self.x0}) = {avaliar(functions[-1],self.x0,self.var)} \n Erro(fn({self.x0})) = {erros[-1]} '
                plt.title(f" {metodo} \n\n {string}")

            ## Plota os pontos de dados
            self.ax.plot(self.x,self.y,'o',color='red')

            ## Anota as coordenadas dos pontos
            for self.i,self.j in zip(self.x,self.y): self.ax.annotate(f'({self.i} , {round(self.j,3)})',xy=(self.i,self.j))
            
            ## Monta a função (a partir dos pontos) e sua string (para legenda)
            f = functions[-1]
            F = [f.evalf(subs={self.var:x}) for x in pontos_x]
            str_f = str(arredondar_expr(f,casas_decimais))+f'\nR² = {round(r2s[-1],4)}'

            ## Plota a função
            self.ax.plot(pontos_x,F,label=str_f)
            
            ## Ativa a legenda 
            plt.legend(loc = 'upper left')


        ## Nomeia os eixos
        plt.xlabel(nomes_eixos[0],fontsize = 'large')
        plt.ylabel(nomes_eixos[1],fontsize = 'large')


        plt.show()


    def avaliar_r2(self,funcao):
        ''' Avalia o coeficiente R2 da interpolação'''
        # Avalia a função em todos os pontos x da amostra
        avalia_funcao = np.array([avaliar(funcao,i,self.var) for i in self.x])
        # Calcula R2
        SSR = ((self.y-avalia_funcao)**2).sum()
        SST = ((self.y - self.y.mean())**2).sum()
        R2 = 1 - SSR/SST
        # Arredonda R2 se for 1 (retira os 0 excessivos)
        if R2 == 1:
            R2 = 1.0
        # Retorna o valor
        return R2


    def erro_absoluto_aproximado(self,funcao,x0,var=sp.Symbol('x')):
        self.valor = avaliar(funcao,x0,var)
        erro = abs(self.valor-self.valor_antigo)
        self.valor_antigo = self.valor
        return erro

        
    def coeficientes_newton(self,i):
        ''' Calcula e retorna o coeficiente de Newton de ordem i '''
        
        ## Indices auxiliares para o cálculo
        indices = [j for j in range(i+1)]
        
        ## Procedimentos de ordens 0 e 1 definidos manualmente 
        def ordem_0(p):
            return self.y[0]
        def ordem_1(p):
            return (self.y[p[1:][0]]-self.y[p[:-1][0]])/(self.x[p[-1]]-self.x[p[0]])

        ## Lista com os procedimentos
        ordem = [ordem_0,ordem_1]

        ## Define os procedimentos de ordens superiores automaticamente 
        for j in range(2,i+1):
            # String definindo o procedimento
            procedimento = f'def ordem_{j}(p): return (ordem_{j-1}(p[1:])-ordem_{j-1}(p[:-1]))/(self.x[p[-1]]-self.x[p[0]])'
            # Executa a string no escopo local, definindo o procedimento
            exec(procedimento,locals())
            # Executa a string no escopo local, guardando o procedimento criado na lista de procedimentos
            exec(f"ordem.append(ordem_{j})",locals())

        ## Calcula o coeficiente chamando o procedimento de ordem i, com os índices criados como argumento
        coef = ordem[i](indices)

        ## Retorna o coeficiente
        return coef


    def produtorio_newton(self,i,var=sp.Symbol('x')):
        ''' Produtório para aplicação da Interpolação de Newton'''
        k = 0
        prod = 1
        for k in range(i):
            prod*= (var-self.x[k])
        return prod

    def newton(self,x0=None,plot=False,animado=False,casas_decimais=20,nomes_eixos=['X','Y'],titulo=''):
        '''Retorna o polinomio interpolador de Newton '''
        lista_pol = []
        lista_erros = []
        lista_r2s = []
        self.f = 0
        self.erro = 0
        self.valor_antigo = 0
        for i in range(self.n+1):
            self.f+=sp.expand(self.produtorio_newton(i,self.var)*self.coeficientes_newton(i))
            lista_pol.append(self.f)
            lista_r2s.append(self.avaliar_r2(self.f))
            if isinstance(x0, (int, float)):
                self.erro = self.erro_absoluto_aproximado(self.f,x0)
                lista_erros.append(self.erro)
        self.x0 = x0
        if plot == True: self.plot(lista_pol,lista_erros,lista_r2s,'Interpolação de Newton',animado=animado,casas_decimais=casas_decimais,nomes_eixos=nomes_eixos,titulo=titulo)
        return lista_pol[-1]


    def polinomio_base_lagrange(self,n,i,var=sp.Symbol('x')):
        self.Pol = 1
        for j in range(n+1):
            if j == i:
                continue
            self.Pol *= (var-self.x[j])/(self.x[i]-self.x[j])
        return self.Pol

    def lagrange(self,x0=None,plot=False,animado=False,casas_decimais=20,nomes_eixos=['X','Y'],titulo=''):
        '''Retorna o polinomio interpolador de lagrange '''
        lista_pol = []
        lista_erros = []
        lista_r2s = []
        self.f = 0
        self.erro = 0
        self.valor_antigo = 0 
        for i in range(self.n+1):
            self.f+=sp.expand(self.polinomio_base_lagrange(self.n,i,self.var)*self.y[i])
            lista_pol.append(self.f)
            lista_r2s.append(self.avaliar_r2(self.f))
            if isinstance(x0, (int, float)):
                self.erro = self.erro_absoluto_aproximado(self.f,x0)
                lista_erros.append(self.erro)
        self.x0 = x0
        if plot == True: self.plot(lista_pol,lista_erros,lista_r2s,'Interpolação de Lagrange',animado=animado,casas_decimais=casas_decimais,nomes_eixos=nomes_eixos,titulo=titulo)
        return lista_pol[-1]



#########################################################################


def main():
    regressao = Regressao(amostra_x,amostra_y)
    interpolacao = Interpolacao(amostra_x,amostra_y,grau=grau,var=variavel) 

    if visualizar_dados:
        plt.scatter(amostra_x,amostra_y)
        plt.show()

    if ajuste_de_curva['regressao simples']:
        a = regressao.regressao_linear_simples(x0=valor_para_estimar,plot=plot,casas_decimais=casas_decimais,dic=dic,nomes_eixos=[eixo_x,eixo_y],titulo=titulo)
        print(a)

    if ajuste_de_curva['regressao polinomial']:
        b = regressao.regressao_polinomial(grau=grau,x0=valor_para_estimar,plot=plot,tolerancia=tolerancia,casas_decimais=casas_decimais,dic=dic,nomes_eixos=[eixo_x,eixo_y],titulo=titulo)
        for i in b: print(f'{i}\n')

    if ajuste_de_curva['regressao polinomial multipla']:
        c = regressao.regressao_polinomial_multipla(graus=graus,plot=plot,tolerancia=tolerancia,casas_decimais=casas_decimais,nomes_eixos=[eixo_x,eixo_y],titulo=titulo)
        for i in range(len(c[0])): print('\n',c[0][i],'\n',c[1][i],'\n')
    
    if ajuste_de_curva['regressao exponencial']:
        d = regressao.regressao_exponencial(x0=valor_para_estimar,plot=plot,tolerancia=tolerancia,casas_decimais=casas_decimais,dic=dic,nomes_eixos=[eixo_x,eixo_y],titulo=titulo)
        for i in d: print(f'{i}\n')

    if ajuste_de_curva['regressao logaritmica']:
        e = regressao.regressao_logaritmica(x0=valor_para_estimar,plot=plot,tolerancia=tolerancia,casas_decimais=casas_decimais,dic=dic,nomes_eixos=[eixo_x,eixo_y],titulo=titulo)
        for i in e: print(f'{i}\n')

    if ajuste_de_curva['interpolacao newton']:
        start = time()
        f = interpolacao.newton(x0=valor_para_estimar,plot=plot,animado=animado,casas_decimais=casas_decimais,nomes_eixos=[eixo_x,eixo_y],titulo=titulo)
        end = time() - start
        print(f"\n Interpolação de Newton:\n f({interpolacao.var}) = {str(f).replace('**','^')} \n\n Tempo total decorrido: {end}\n")

    if ajuste_de_curva['interpolacao lagrange']:
        start = time()
        f = interpolacao.lagrange(x0=valor_para_estimar,plot=plot,animado=animado,casas_decimais=casas_decimais,nomes_eixos=[eixo_x,eixo_y],titulo=titulo)
        end = time() - start
        print(f"\n Interpolação de Lagrange:\n f({interpolacao.var}) = {str(f).replace('**','^')} \n\n Tempo total decorrido: {end}\n")



if __name__ == "__main__":
    main()
    
