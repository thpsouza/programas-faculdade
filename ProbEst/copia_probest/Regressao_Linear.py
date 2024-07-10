## RETA DE REGRESSÃO - ESTATÍSTICA
## Regressão Linear

from . import Medidas_Centralidade, Medidas_Dispersao
import matplotlib.pyplot as plt
import numpy as np

def regressao_linear(X,Y,plot=False):
    ''' Retorna os coeficientes da regressão linear Y = aX+b, e o coeficiente R²
    Dada uma amostra X,Y
    
    list, list -->  dict[str,float]
                        ['a' , ...]
                        ['b' , ...]
                        ['R2', ...]
    '''
    a = Medidas_Dispersao.covariancia_amostral(X,Y)/Medidas_Dispersao.variancia(X)
    b = Medidas_Centralidade.media(Y) - a * Medidas_Centralidade.media(X)
    R2 = Medidas_Dispersao.correlacao_amostral(X,Y)
    if plot:
        x = np.linspace(min(X),max(X))
        y = [a*i+b for i in x]
        plt.plot(X,Y,'o',label=' amostra ')
        plt.plot(x,y,label=f" y  =  {round(a,4)} x  +  {round(b,4)}")
        plt.legend()
        plt.show()
    return {'a' : a, 'b' : b, 'R2':R2}
