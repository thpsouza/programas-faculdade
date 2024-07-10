##
##      MÉTODOS NUMÉRICOS APLICADOS (EQE358) - MÓDULO II                    
## Procedimentos gerais relacionados ao Módulo II da diciplina
## 
##                 Aproximação por série de Taylor
##

from sympy import Symbol,factorial,nsimplify,sin
import time
import animation
    
################## DADOS ##################

f = "(x/13.5)**(2/3)" #exp(-x)-1 #função f(x)

var = "x"
# variaveis da função f definida

X = 3
# valor desconhecido

a = 13.5
# valor conhecido

erro = 10**(-2)
# valor de erro aceitável

erro_relativo = False
# False --> erro absoluto ;  True --> erro relativo

symbolic = True
# False --> valores;   True --> expressões

imprimir = True
# True --> imprime interface; False --> retorna valor na variável t

imprimir_erro = False
# True --> imprime o valor dos erros

tempo_limite = 30
# Tempo máximo aproximado que o programa pode demorar

imprimir_tempo = False
# True --> programa imprime o tempo total aproximado

n = 5
# Número de termos para calcular para taylor multivariavel
# (caso o erro esperado não possa ser seja atingido)




################## PROCEDIMENTOS ##################

# Procedimentos Gerais
from procedimentos_gerais import (
    derivada,
    avaliar,
    adicionar_a_lista
)
#

#def termo_a0(f,var,x,a):
#    ''' Calculo e retorna o termo_a0 da série de taylor, 
#    com x,a definidos.
#    expr,Symbol,float,float --> float'''
#
#    try:
#        i = iter(var)
#        if len(var)!=len(a) or len(var)!=len(x):
#            raise TypeError(" O número de variáveis deve ser igual ao número de valores ")
#        ret = f
#        for j in range(len(var)):
#            ret = termo_an(ret,var[j],x[j],a[j],0)
#        return avaliar(ret,a,var)
#    
#    except TypeError:
#        pass
#    
#    return avaliar(f,a,var)


def termo_an(f,var,x,a,n,symbolic=False,eval=False):
    ''' Calcula e retorna o termo_an da série de taylor,
    com x,a e n definidos.
    expr,Symbol,float,float,int --> float
    eval: list[list[variables],list[values]]'''

    numerador = derivada(f,var,n)
    numerador2 = ((x-a)**n)
    denominador = factorial(n)
    numerador = numerador*numerador2#
    if symbolic == True:
        return str(nsimplify(numerador))+'*'+str(denominador),str(numerador)+'/'+str(denominador),numerador/denominador
    if eval!=False:
        return avaliar(numerador,eval[1],variables=eval[0])/denominador
    return numerador/denominador


def erro_taylor(f,var,x,valor_taylor,rel=False):
    ''' Calcula e retorna o erro de uma aproximação por série de taylor
    expr, float, float, float --> float '''

    valor_real = avaliar(f,x,variables=var,casas_decimais=20)
    erro = abs(valor_real - valor_taylor)
    if rel == True:
        erro = erro/valor_real
    return erro


def erro_estimado(f,var,x,a,valor_taylor):
    ''' Calcula e retorna o erro estimado de uma f(x) aproximada por série de taylor
    expr,float,float,float --> float'''
    
    valor_real = avaliar(f,x,variables=var,casas_decimais=20)
    passo = x-a
    derivada_primeira = abs(avaliar(derivada(f,variable=var,n=1),a,variables=var,casas_decimais=20))
    erro = derivada_primeira*passo
    return erro



def taylor(f,var,x,a,n=100,casas_decimais=10,imprimir=False,return_error=False,error_type=erro_relativo,symbolic=False,mv=False):
    ''' Calcula e mostra o valor de uma função f avaliada em x, partindo de
    f(a) conhecida; através da série de taylor, com uma ordem de grandeza n
    expr,float,float,int --> Symbolic|float '''
        
    if symbolic == True:
        valor_simplified = []
        valor_decimal = []
        valor_numerico = []
        for i in range(n+1):
            termo = termo_an(f,var,x,a,i,symbolic)
            valor_simplified.append(termo[0])#nsimplify(termo[0]))
            valor_decimal.append(termo[1])
            valor_numerico.append(termo[2])
        return valor_simplified,valor_decimal,valor_numerico


    # Termo de ordem 0
    #a0 = termo_a0(f,var,x,a)
    #if n == 0:
    #    return a0

    # Ordens superiores
    valor = 0
    for i in range(n+1):
        valor += termo_an(f,var,x,a,i,eval=[var,a])

    # Multivariável --> retorna função simbolica
    if mv == True:
        return valor

    # Avalia função
    valor = avaliar(valor,a,var)#+a0
    
    valor = valor
     
    erro = erro_taylor(f,var,x,valor,error_type)
    if imprimir == False:
        if return_error == True:
            return erro
        return valor
    
    valor_real = 0 if round(avaliar(f,a,variables=var),120) == 0 else avaliar(f,a,variables=var)
    string1 = str(f)[0:len(str(f))-3] if str(f)[-3] == '(' else str(f)+' '
    string2 = "({}) = {}, temos:" if str(f)[-3] == '(' else "( x = {} )  = {}, temos:"
    string3 = "({}) = ".format(x) if str(f)[-3] == '(' else "( x = {} )  = ".format(x)

    print( "\n Pela série de Taylor, partindo de", 
    string1,string2.format(a,round(valor_real,4)))
    print('\n      ',string1,string3,valor)
    print('\n ( números de termos calculados (n) = {} )'.format(n))   
    print('\n\n ERRO REAL = ', erro)
    print('\n ERRO ESTIMADO = ', erro_estimado(f,var,x,a,valor))
    print('')


def n_termos_para_erro(f,var,x,a,erro_procurado=erro,casas_decimais=20,imprimir_erro=False,imprimir_tempo=False,symbolic=False):
    lista_erros = [float('inf'),float('inf')]
    n = 0
    erro_t = taylor(f,var,x,a,n,casas_decimais=casas_decimais,imprimir=False,return_error=True)
    t0 = cronometro(lst=True) #lista dos tempos
    m = 0
    t1 = [0,0]
    #print('n  --  \u0394t   --  Total')  #nome das colunas
    if imprimir_erro == True:
        print('n - erro')
    while erro_t-erro_procurado > 0:
        t0 = cronometro(imprimir=False)  #começa o cronometro
        if imprimir_tempo == True:
            print(t1[1])
        if t1[1] > tempo_limite:
            print("\n\n # Erro muito pequeno ou valor 'a' muito distante ") 
            break
        if imprimir_erro == True:
            print(n,'-','{0:.80f}'.format(erro_t))
        lista_erros.append(erro_t)
        n+=1
        erro_t = taylor(f,var,x,a,n,casas_decimais=casas_decimais,imprimir=False,return_error=True)   
        t1 = cronometro(end=True,contador=n,imprimir=False) #para o cronometro
    return n


def cronometro(end=False,lst=False,contador='',imprimir=True):
    ''' Cronometro para medir tempo de processamento de um procedimento'''
    global start
    global lista_tempo
    if end == True:
        try:
            tempo = (time.process_time() - start)
        except:
            tempo = 'error'
            pass
        try:
            lista_tempo.append(tempo)
            soma = sum(lista_tempo)
        except:
            soma = ''
            pass
        if imprimir==True:
            print(contador,' -- ', tempo, ' -- ', soma)
        elif imprimir==False:
            start = time.process_time()
            return tempo,soma
    elif lst == True:
        lista_tempo = []
    start = time.process_time()
   
    
    
def expressoes(variables):
    global t
    global a
    global f
    if symbolic == True:
        lengths = [len(i) for i in t[1]]
        k = max(lengths)+1
        string1 = ''
        string2 = ''
        for i in range(len(t[0])):
            s1 = ' '+str(t[1][i]) if str(t[1][i])[0]!='-' else str(t[1][i])
            s2 = ' '+str(t[0][i]) if str(t[0][i])[0]!='-' else str(t[0][i])
            string1 +='\n termo (n={}):  '.format(i)+' '*(3-len(str(i)))+s1+' '*(k-len(s1))+' =  '+str(t[2][i])
            string2 +='\n termo (n={}):  '.format(i)+' '*(3-len(str(i)))+s2#+')'
        t = t[2]
        print("\n\nExpressão: \n\n",string1[2:])
        print(" ------------- \n    Total:    ",sum(t))
        print("\n\n\nExpressão simplificada: \n\n",string2[2:])
        print(" ------------- \n    Total:    ",nsimplify(sum(t)))
        print("\n\n\nValor:  ( f(x) = {} )\n\n \u27f9 f({}) = {}".format(f,X,avaliar(sum(t),a,variables=variables)))
        print('')



def erro_absoluto_aproximacao(valor_obtido,f,variaveis,pontos_desconhecidos,casas_decimais=20):
    valor_real = avaliar(f,pontos_desconhecidos,variaveis,casas_decimais)
    return abs(valor_real - valor_obtido)


thrd = False
intervalo_tempo = 0.25
tempo_animacao = 0.0001

def taylor_mv(f,variaveis,pontos_desconhecidos,pontos_conhecidos,error=False,n_de_termos=n,casas_decimais=20):
    global thrd
    k=0
    funcao = f
    t0 = cronometro(lst=True)
    while True:
        t0 = cronometro(imprimir=False)
        
        for i in range(n_de_variaveis):
            f = taylor(f,variaveis[i],pontos_desconhecidos[i],pontos_conhecidos[i],k,imprimir=False,mv=True)
        f = avaliar(f,pontos_conhecidos,variaveis)

        ''' 
        l = list(f.atoms(Symbol))
        #print(l)
        if len(l)>0:
            print('\n ',f"A função {f} não é suportada nativamente...",'\n')
            mini_temporizador()
            print('\n  Utilizando códigos built-in ... \n')
            mini_temporizador()
            ret = f
            for j in range(n_de_variaveis):
                ret = ret.series(var[0],a[0],n_de_termos).removeO()
            return avaliar(ret,a,var),n_de_termos
        '''


        k+=1
        
        if error==False:
            if k>n_de_termos:
                break
        try:
            erro_abs = erro_absoluto_aproximacao(f,funcao,variaveis,pontos_desconhecidos,casas_decimais)
            if  erro_abs <= erro:
                break
        except:
            if k>n_de_termos:
                break
            
        f = funcao

        t1 = cronometro(end=True,imprimir=False)
        
        if t1[0] > tempo_animacao:
            #print(f"        Nº de termos: {k}       Erro: {erro_abs} ")
            animation.text(f"        Nº de termos: {k}       Erro: {erro_abs}     Tempo total aproximado: {round(t1[1],2)}s")            
            if  thrd == False:
                thrd = True
                try:
                    animation.start(intervalo_tempo)
                except NameError:
                    pass
    try:
        animation.stop()
        print('')
        print(' - - - -'*13)
    except NameError:
        pass
        
    return f,k,erro_abs
        


if __name__ == "__main__":
    
    for i in var.split(','):
        exec("{} = Symbol('{}')".format(i,i))
    del(i)
    exec("var = {}".format(var))
    exec("f = {}".format(f))
    
    
    if type(var)==tuple or type(var)==list:
        n_de_variaveis = len(var)

        if type(X)==tuple:
            X = list(X)
            adicionar_a_lista(X,n_de_variaveis)
        if type(X)!=tuple and type(X)!=list:
            X = [X]
            adicionar_a_lista(X,n_de_variaveis)

        if type(a)==tuple:
            a = list(a)
            adicionar_a_lista(a,n_de_variaveis)
        if type(a)!=tuple and type(a)!=list:
            a = [a]
            adicionar_a_lista(a,n_de_variaveis)
                
        t = taylor_mv(f,var,X,a,error=erro,casas_decimais=20)
        if type(t)!= tuple:
            print('\n',t)
        else:
            F = t[0]
            print('')
            print("\n Função = {}  \n\n f{} = {} \n\n Número de termos calculados = {}".format(f,X,t[0],t[1]))
            print("\n Erro absoluto  = {} < {}".format(t[2],erro))

    
    else:
        n2 = n_termos_para_erro(f,var,X,a,erro_procurado=erro,symbolic=symbolic,imprimir_erro=imprimir_erro,imprimir_tempo=imprimir_tempo)
        t = taylor(f,var,X,a,n2,symbolic=symbolic,imprimir=imprimir)
        expressoes(var)


    input()
