##
##      MÉTODOS NUMÉRICOS APLICADOS (EQE358) - MÓDULO IX                     
## Procedimentos gerais relacionados ao Módulo IX da diciplina
## 
##            Sistemas de equações diferenciais ordinárias
##                        Método de Euler
##

from .resolucao_de_edos import RungeKutta
from sympy import Symbol, exp

################## DADOS ##################

y1 = Symbol('y1')
y2 = Symbol('y2')
x = Symbol('x')

equacoes = [    
    'dy1/dx = -0.5*y1',
    'dy2/dx = 4 - 0.3*y2 - 0.1*y1'
]

grau_equacao = None

condicoes_iniciais = x0,y1_0,y2_0 = 0,4,6

intervalo = 0,2

passo = 0.5


# Opções

ajuste_de_curva = { ## Apenas para polinomios
    'interpolacao':False,
    'regressao polinomial':False,
    'regressao exponencial':True,
    'regressao logaritmica':False
}

plotar = True




############################################################################################

def interface(solucao):
    print(' Solução: \n')
    for k,sol in enumerate(solucao):
        print(f' y{k+1}{sol} \n')

def main():
    solucao = []
    for k,equacao in enumerate(equacoes):

        ## Se houver uma variável independente de uma equação anterior, substitui pela função
        ## obtida como solução na iteração anterior
        if f'y{k}' in str(equacao):
            equacao = str(equacao).replace(f'y{k}',str(funcoes[0][2]).split('=')[1].split('\n')[0])

        ## Define a condição inicial da equação
        condicao_inicial = condicoes_iniciais[0],condicoes_iniciais[k+1]

        ## Define as variáveis usadas 
        if isinstance(equacao,str):
            if '=' in equacao:
                eq = equacao.split('=')[1]
            eq = eval(eq.replace('^','**'))
        variaveis = list(eq.atoms(Symbol))
        variaveis.sort(key=str)

        ## Aplicação do método de euler
        metodos = RungeKutta(equacao,intervalo,passo,grau_equacao,var=variaveis)
        pontos,funcoes,tempo,tempo_tela_grafco = metodos.euler(condicao_inicial,ajuste_curva=ajuste_de_curva,plotar=plotar)
        
        ## Guarda a solução (string da função ajustada)
        solucao.append(funcoes[0][2].split('f(x)')[1])

    interface(solucao)


if __name__ == "__main__":
    main()