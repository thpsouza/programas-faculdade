##
##      MÉTODOS NUMÉRICOS APLICADOS (EQE358 - EQN) - GERAL                     
## Procedimentos gerais relacionados aos módulos da disciplina 
##

import math
import sympy as sp


################## MÓDULOS ##################
from .procedimentos_gerais import *
from .taylor import taylor,n_termos_para_erro
from .raizes_de_equacoes import metodo_bisseccao,metodo_falsa_posi,metodo_newton_raphson,metodo_secante
from .sistemas_nao_lineares import metodo_newton_sistemas
from .sistemas_lineares import cramer,eliminacao_gauss_jordan
from .ajustes_de_curvas import Regressao,Interpolacao
from .integracao_numerica import Newton_Cotes
from .integracao_de_equacoes import Quadratura

#############################################

x = Symbol('x')
ret = taylor('sin(x)',var='x',x=0.5,a=0)

print(ret)




    

    

############################

def main():
    return

if __name__ == "__main__":       
    main()
