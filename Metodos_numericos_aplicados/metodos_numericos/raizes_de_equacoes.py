##
##      MÉTODOS NUMÉRICOS APLICADOS (EQE358) - MÓDULO III                    
## Procedimentos gerais relacionados ao Módulo III da diciplina
## 
##                      Raízes de equações
##          Métodos Intervalares: Bissecção e Falsa-posição
##          Métodos abertos: Newton-Raphson e Secante
##

from sympy import Symbol
import math



################## DADOS ##################

#erro aceitável
tolerancia = 10**(-4)                      

# Função
x = Symbol('x')
e = 0.9
s = 5.67*10**-8
Tviz = Tinf = 293.15
r = 3*10**-3
c = 1.25
f = e*s*(x**4-Tviz**4) + c*((x-Tinf)/(2*r))**(1/4)*(x-Tinf) - 4/(math.pi*2*r)



#Definir True para os métodos com quais se deseja calcular (e False para os que não se deseja)
tipo_metodos = {'intervalares':False,        
                'abertos':True,               
}

#chutes iniciais interevalares
x1 = 294.15
x2 = 1000

#chutes iniciais abertos
xi = 294.15
xi_1 = 295.15




################## PROCEDIMENTOS ##################

### Procedimentos Gerais ###
from procedimentos_gerais import derivada,avaliar



### MÉTODOS INTERVALARES ###

# MÉTODO DA BISSECÇÃO

def metodo_bisseccao(f,x1,x2,tolerancia=tolerancia,xr=False,casas_decimais=20):
    if xr == True:
        return (x1+x2)/2
    return intervalares_geral(f,x1,x2,metodo=metodo_bisseccao,casas_decimais=casas_decimais)
    
# método da bisseccao outra versão --> em desenvolvimento

def metodo_bisseccao_2(f,x1,x2,tolerancia=tolerancia,casas_decimais=20):
    n = n_iteracoes(x2,x1,tolerancia)
    f_x1 = round(avaliar(f,x1,casas_decimais=casas_decimais),120)
    f_x2 = round(avaliar(f,x2,casas_decimais=casas_decimais),120)
    xr = (x1+x2)/2
    f_xr = round(avaliar(f,xr,casas_decimais=casas_decimais),120)
    for i in range(1,n+1):
            if f_x1*f_xr < 0:
                x2 = xr
                xr_a = xr
            elif f_x1*f_xr>0:
                x1 = xr
                xr_a = xr
            xr = (x1+x2)/2
            f_x1 = round(avaliar(f,x1,casas_decimais=casas_decimais),120)
            f_x2 = round(avaliar(f,x2,casas_decimais=casas_decimais),120)
            f_xr = round(avaliar(f,xr,casas_decimais=casas_decimais),120)
    return xr,n


# MÉTODO DA FALSA POSIÇÃO OU Regula Falsi

def metodo_falsa_posi(f,x1,x2,tolerancia=tolerancia,xr=False,casas_decimais=20):
    if xr == True:
        f_x1 = avaliar(f,x1,casas_decimais=casas_decimais)
        f_x2 = avaliar(f,x2,casas_decimais=casas_decimais)
        return x2-f_x2*(x1-x2)/(f_x1-f_x2)
    return intervalares_geral(f,x1,x2,metodo=metodo_falsa_posi,tolerancia=tolerancia)
    

# MÉTODOS INTERVALARES PROCEDIMENTOS GERAIS

def n_iteracoes(x2,x1,tolerancia):
    return int(math.log((x2-x1)/tolerancia,2))

def intervalares_geral(f,x1,x2,metodo,tolerancia=tolerancia,casas_decimais=20):
    '''expr,float,float,str,float --> float|tuple(float,float)'''
    L = [float('inf'),float('inf')]
    f_x1 = avaliar(f,x1,casas_decimais=casas_decimais)
    f_x2 = avaliar(f,x2,casas_decimais=casas_decimais)
    if f_x1 == 0 and f_x2 == 0:
        return x1,x2
    elif f_x1 == 0:
        return x1,0
    elif f_x2 == 0:
        return x2,0
    if not(f_x1*f_x2 < 0):
        return "O intervalo [x1,x2] contém 2 raízes, ou nenhuma raiz"
    n=1
    xr = metodo(f,x1,x2,tolerancia,xr=True)
    f_xr = avaliar(f,xr,casas_decimais=casas_decimais)
    L.append(f_xr)
    xr_a = float('inf')
    erro_a = float('inf')
    while abs(f_xr-0)>tolerancia:
        if (erro_a <= tolerancia and abs(f_xr-0)< tolerancia) or abs(f_xr-0)< tolerancia or L[-1]==L[-2]==L[-3]:
            return xr,n      
        if f_x1*f_xr < 0:
            x2 = xr
        elif f_x1*f_xr>0:
            x1 = xr
        if n>1000:
            return "Intervalo muito grande"
        xr_a = xr
        xr = metodo(f,x1,x2,tolerancia,xr=True)
        f_x1 = avaliar(f,x1,casas_decimais=casas_decimais)
        f_x2 = avaliar(f,x2,casas_decimais=casas_decimais)
        f_xr = avaliar(f,xr,casas_decimais=casas_decimais)
        L.append(f_xr)
        erro_a = abs(xr - xr_a)/xr*100
        n+=1
    if abs(xr-0)<tolerancia:
        xr = 0.0
    return xr,n


def interface_intervalares():
    print(' - - - - - - - Métodos Intervalares - - - - - - - ')
    print('\n Intervalos -->   x1 = {}, x2 = {}'.format(x1,x2))
    print('\n Cálculo: \n')
    print(' Método ',' '*16,' (   Raiz     ,      n  )')
    print(' -'*25)
    metodos_intervalares()
    print('')

def metodos_intervalares():
    print(' Método bissecção:  ','      ', metodo_bisseccao(f,x1,x2,tolerancia))
    #print(' Método bissecção 2:  ','  ', metodo_bisseccao_2(f,x1,x2,tolerancia))
    print(' Método da falsa posição:  ', metodo_falsa_posi(f,x1,x2,tolerancia))



### MÉTODOS ABERTOS ###
    
# MÉTODO DE NEWTON-RAPHSON

def metodo_newton_raphson(f,xi,xi_1='',var=Symbol('x'),tolerancia=tolerancia,xr=False,casas_decimais=20):
    '''
    - f:                expr        (função)
    - xi:               float       (chute inicial)
    - xi_1:             float       (proximo chute)
    - var:              Symbol      (variável a se trabalhar)
    - tolerancia:       float       (critério de parada)
    - xr:               bool        (#### NÃO LEMBRO ####)
    - casas_decimais:   int         (para aproximar)
    - return:           float,int   (valor,número de iterações)
    '''

    if xr == True:
        f_xi = avaliar(f,xi,variables=var,casas_decimais=casas_decimais)
        ddx_f_xi = avaliar(derivada(f,var,1),xi,variables=var,casas_decimais=casas_decimais)
        if ddx_f_xi == 0:
            return "ddx 0"
        div = f_xi/ddx_f_xi
        xii = xi - div
        return xii,ddx_f_xi
    return abertos_geral(f,xi,xi_1,var=var,metodo=metodo_newton_raphson,tolerancia=tolerancia)


# MÉTODO DA SECANTE

def metodo_secante(f,xi,x0,var=Symbol('x'),tolerancia=tolerancia,xr=False,casas_decimais=20):
    '''
    f: expr
    xi: float
    x0: float
    return: float,int'''
    if xr == True:
        f_xi = avaliar(f,xi,variables=var,casas_decimais=casas_decimais)
        f_x0 = avaliar(f,x0,variables=var,casas_decimais=casas_decimais)
        div = (f_xi*(x0 - xi))/(f_x0-f_xi)
        xii = xi - div
        return xii
    return abertos_geral(f,xi,x0,metodo=metodo_secante,tolerancia=tolerancia)


# MÉTODOS ABERTOS PROCEDIMENTOs GERAIS

def abertos_geral(f,xi,x0,metodo,var=Symbol('x'),tolerancia=tolerancia,casas_decimais=20):
    n=0
    l_ddx = [float('inf'),float('inf')]
    l_fxr = [float('inf'),float('inf')]
    l_xi = [x0,xi]
    if metodo==metodo_secante and xi==x0:
        return "Chutes inicias iguais"
    while True:
        n+=1
        ret = metodo(f,xi,x0,var=var,tolerancia=tolerancia,xr=True)
        if ret == 'ddx 0':
            return "Derivada  0 (denominador)"
        xr = ret[0] if type(ret) == tuple else ret
        ddx_f_xi = ret[1] if type(ret) == tuple else 1

        f_xr = avaliar(f,xr,variables=var,casas_decimais=casas_decimais)

        l_ddx.append(ddx_f_xi)
        l_fxr.append(f_xr)
        l_xi.append(xr)
        
        if abs(xr-0)<tolerancia:
            xr = 0.0

        if abs(abs(l_fxr[-1])-abs(l_fxr[-2]))<tolerancia:
            break
        if abs(f_xr-0)<=tolerancia:
            break
            
        if metodo == metodo_secante:
            if l_xi[-1] == l_xi[-2]:
                return "Chutes iniciais ruins \n                            (tente um xi_1 mais próximo de xi)"
            k = abs(l_fxr[-1])/abs(l_fxr[-2])
            #if k<tolerancia or k>(1/(tolerancia)):
             #   #print(l_fxr[-1],l_fxr[-2])
              #  maior_menor = "maiores" if l_fxr[-1] < 0 else "menores"
               # return "Chutes inicais ruins \n                            (tente valores {})".format(maior_menor)
            
        if metodo == metodo_newton_raphson:
            if abs(l_ddx[-2])/abs(l_ddx[-1])<tolerancia:
                string = "Chute inicial (xi) ruim --> f'(xi) ~ 0 \n                            (tente um xi {})"
                maior_menor = 'maior' if l_ddx[-1] > 0 else 'menor'
                return string.format(maior_menor)
        if n>1000:
            return "Chutes inicias ruins"
        
        x0 = xi
        xi = xr

    return xr,n


def interface_abertos():
    print(' - - - - - - - - Métodos Abertos - - - - - - - - ')
    print('\n Cálculo: \n')
    print(' Método ',' '*16,' (   Raiz     ,      n  )')
    print(' -'*25)
    metodos_abertos()
    print('')
    
def metodos_abertos():
    print(' Método Newton-Raphson:  ',' ', metodo_newton_raphson(f,xi,tolerancia))
    print(' Método da Secante:  ','     ', metodo_secante(f,xi,xi_1,tolerancia))
    


    
############################

def main():
    print('\n Função: \n')
    print(f' f(x) = {f} \n')
    print(f' Tolerância = {tolerancia} \n\n')
    for key in tipo_metodos:
        string = 'interface_'+key+'()'
        if tipo_metodos[key]:
            exec(string)
            print('\n')


if __name__ == "__main__":    
    main()
    input()
