##
##      MÉTODOS NUMÉRICOS APLICADOS (EQE358) - MÓDULO IV                    
## Procedimentos gerais relacionados ao Módulo IV da diciplina
## 
##               Sistemas de equações não-lineares
##                      Método de Newton
##

from sympy import Symbol, symbols


################## DADOS ##################

''' -- Exemplo: --
equacoes = "x1^2+x2^2=1", "x1^2-x2^2=-1/2"
chutes_iniciais = 1.5,3.2
'''

# Equações homogêneas, entre aspas, separadas por vírgula


equacoes = (
    "x5*x1^2 + x1  - 5  = 0",
    "x5*x2^2 + x2  - x1 = 0",
    "x5*x3^2 + x3  - x2 = 0",
    "x5*x4^2 + x4  - x3 = 0",
    "0.25*x5 + 0.5 - x4 = 0")


chutes_iniciais = 2,1.1,0.8,0.7,0.6


# Necessário para definição automatica das variaveis usadas
n_de_variaveis = 5


# Erro aceitável  -- Limite de precisão (provisório) = 10^-10 (para 2 funções e 2 variáveis)
tolerancia = 10**(-5)                       


# True para usar o método de newton modificado (jacobiana única)
metodo_modificado = True


# Selecionar quais critérios de parada se deseja usar
# (o primeiro a ser atingido irá parar o método)

criterios_de_parada = {
    "Erros absolutos das funções": True,  # Critério escolhido
    "Erros absoluto das raízes": False,
    "Erros relativos das raízes": False
}



################## PROCEDIMENTOS ##################

## Procedimentos Gerais
from procedimentos_gerais import (
    derivada,
    avaliar,
    prova_real,
    casas_decimais_significativas,
    soma_matrizes,
    multiplicacao_matrizes,
    determinante,
    inversa
)



def jacobiana(funcoes,variaveis,pontos_conhecidos):
    ''' Retorna a matriz jacobiana de um conjunto de funções e variáveis,
    calculada em pontos conhecidos.
    
    list[funtion,...], list[Symbol,...], list[float,...] --> Matriz'''
    
    
    Matriz = []
    for j in range(len(funcoes)):            
        linha = []
        for i in range(len(variaveis)):
            linha.append(avaliar(derivada(funcoes[j],variaveis[i],1),pontos_conhecidos,variaveis))
        Matriz.append(linha)
    return Matriz
    

def mostrar_matriz(matriz):
    ''' Imprime uma matriz linha por linha

    list[list,...] --> None'''
    
    for linha in matriz: print(linha)

#

## Método de Newton para sistemas

def iteracao_newton(funcoes,variaveis,chutes_iniciais,modificado=False):
    ''' Aplica uma iteracao do método de newton para sistemas não lineares

    list[expr,...], list[Symbol,...], list[float,...]
    --> list[list[float,...],...]'''    

    if modificado==False:
        #avalia jacobiana e inverte
        J = jacobiana(funcoes,variaveis,chutes_iniciais)
        if determinante(J) == 0:
            raise ValueError(" O determinante da jacobiana = 0, defina outros chutes iniciais ")
    else:
        J = modificado
        #mostrar_matriz(J)
        #print('')
    
    JI = inversa(J)
    
    #avalia valores das funcoes nos chutes iniciais
    F = []
    for f in funcoes:
        F.append([-avaliar(f,chutes_iniciais,variaveis)])
        
    #multiplica inverso pelos valores das funcoes    
    JI_F = multiplicacao_matrizes(JI,F)

    #estabelece vetor dos chutes iniciais
    V = []
    for c in chutes_iniciais:
        V.append([-c])
        
    #subtrai a matriz resultante da multiplicacao com o vetor   
    ret = soma_matrizes(JI_F,V,'-')

    # Retorno
    return ret

    

def metodo_newton_sistemas(funcoes,variaveis,chutes_iniciais,tolerancia=tolerancia,criterios_parada=criterios_de_parada,modificado=False):
    ''' Aplica o método de newton para sistemas não lineares

    list[expr,...], list[Symbol,...], list[float,...], float
    --> tuple(list[float,...],int)'''

    iteracoes = 0
    valores = chutes_iniciais
    
    if modificado==True:
        #avalia jacobiana
        J0 = jacobiana(funcoes,variaveis,chutes_iniciais)
        if determinante(J0) == 0:
            raise ValueError(" O determinante da jacobiana = 0, defina outros chutes iniciais ")
        modificado = J0
    
    while True:

        if criterios_parada["Erros absolutos das funções"] == True:
            #checa se o critério de parada (erro absoluto da função) foi atingido
            erros = criterio_parada_erros_abs_funcoes(funcoes,variaveis,valores,tolerancia)
            if all(erros):
                raizes = valores
                criterio="Erros absolutos das funções"
                break

        if criterios_parada["Erros absoluto das raízes"] == True and iteracoes>=1:
            #checa se o critério de parada (erro absoluto das raizes) foi atingido
            erros2 = criterio_parada_erros_abs_raizes(funcoes,valores,valores_antigos,tolerancia)
            if all(erros2):
                raizes = valores
                criterio="Erros absoluto das raízes"
                break

        if criterios_parada["Erros relativos das raízes"] == True and iteracoes>=1:
            #checa se o critério de parada (erro absoluto das raizes) foi atingido
            erros3 = criterio_parada_erros_rel_raizes(funcoes,valores,valores_antigos,tolerancia)
            if all(erros3):
                raizes = valores
                criterio="Erros relativos das raízes"
                break
        
        #define os novos valores para as raizes
        valores_antigos = valores
        valores = iteracao_newton(funcoes,variaveis,valores,modificado=modificado)
        valores = [valores[i][0] for i in range(len(valores))] #extrai do formato matricial
    
        #aumenta contador de iteracoes
        iteracoes+=1
      
    if not prova_real(funcoes,variaveis,raizes,tolerancia):
        return "Método não convergiu",iteracoes,criterio
           
    n = casas_decimais_significativas(raizes,funcoes,variaveis,tolerancia)
    raizes = [round(raiz,n) for raiz in raizes]
        
    return raizes,iteracoes,criterio

##


## Critérios de parada

def criterio_parada_erros_abs_funcoes(funcoes,variaveis,valores,tolerancia=tolerancia):
    ''' Avalia os erros absoluto das funções no método de newton para sistemas não lineares

    list[expr,...], list[Symbol,...], list[float,...], float
    --> list[bool,...]'''

    F = [avaliar(funcoes[i],valores,variaveis) for i in range(len(funcoes))]
    erros = [abs(F[i]) <= tolerancia for i in range(len(funcoes))]

    #F = [round(F[i],7) for i in range(len(F))]   <-- Apenas para imprimir
    #print(F)
    
    return erros


def criterio_parada_erros_abs_raizes(funcoes,valores_novos,valores_antigos,tolerancia=tolerancia):
    ''' Avalia os erros absoluto das raízes no método de newton para sistemas não lineares

    list[expr,...], list[float,...], list[float,...], float
    --> list[bool,...]'''
    
    erros = [abs(valores_novos[i] - valores_antigos[i]) <= tolerancia for i in range(len(valores_novos))]

    return erros


def criterio_parada_erros_rel_raizes(funcoes,valores_novos,valores_antigos,tolerancia=tolerancia):
    ''' Avalia os erros relativos das raízes no método de newton para sistemas não lineares

    list[expr,...], list[float,...], list[float,...], float
    --> list[bool,...]'''
    
    erros = [abs((valores_novos[i] - valores_antigos[i])/valores_novos[i]) <= tolerancia for i in range(len(valores_novos))]

    return erros

##



#########################################################################

def main():
    if metodo_modificado == False:
        ret = metodo_newton_sistemas(lista_fs,lista_variaveis,chutes_iniciais,tolerancia,criterios_de_parada)
    else:
        ret = metodo_newton_sistemas(lista_fs,lista_variaveis,chutes_iniciais,tolerancia,criterios_de_parada,modificado=True)
    try:
        print('\n\n Método de Newton','modificado' if metodo_modificado == True else '','\n')
        print('')
        print(' Sistema:  {','\n           { '.join(f"{str(f).replace('**','^')} = 0" for f in lista_fs),'\n')
        print(" Raízes:  ", '\n           '.join(f" {lista_variaveis[i]} = {ret[0][i]}" for i in range(len(ret[0]))))
        print('\n')
        print(f" Número de iterações totais = {ret[1]} \n\n")
        print(f" Critério de parada:  {ret[2]} \n")
    except:
        print(" Não foi possível encontrar uma solução ")
        try:
            print('')
            print(f" Número de iterações totais = {ret[1]} \n")
            print(f" Critério de parada:  {ret[2]} \n")
        except:            
            pass
    return ret

            
if __name__ == "__main__":

    #NÃO ALTERAR
    
    equacoes = list(equacoes)
    lista_variaveis = []
    for i in range(1,n_de_variaveis+1): 
        exec(f"x{i} = Symbol(f'x{i}')")
        exec(f"lista_variaveis.append(x{i})")
        
    lista_fs = []
    for i in range(len(equacoes)):
        k = 0
        if '=' in equacoes[i]: 
            k = equacoes[i].split('=')[1]
            exec(f"equacoes[i] = equacoes[i].split('=')[0]")
        exec(f"f{i+1} = {equacoes[i].replace('^','**')} - {k}")
        exec(f"lista_fs.append(f{i+1})")
        del(k)
        
    ############
        
    ret = main()
    try:
        for i in range(len(ret[0])):
            exec(f"X{i+1} = {ret[0][i]}")
    except:
        pass
    del(i)
    input()
