import sympy as sp
import numpy as np
from Variaveis import *


class Pi():
    '''
    Classe customizada para criar grupos Pi.
    '''
    def __init__(self,n:int,expressao:str) -> None:
        self.n = n
        self.expressao = expressao
    def __repr__(self) -> str:
        PI = u'\u03A0'
        return f"{PI}{self.n} = {self.expressao}"


def achar_expoente(variavel:sp.Expr,dimensao:sp.Expr) -> int:
    '''
    Recebe uma variável em termo de dimensões primárias, e uma dimensão específica.
    Retorna o expoente da dimensão na variável.

    Ex: 
    >>> V = L/T
    >>> achar_expoente(V,L)
    1
    >>> achar_expoente(V,T)
    -1
    '''
    ## Contador para considerar erros desconhecidos
    # Caso o contador seja diferente de 1, a mesma dimensão foi considerada duas vezes
    # Provavelmente não será necessário.
    k = 0

    ## Abre a variável em seus argumentos
    argumentos = variavel.args

    ## Se não houverem argumentos, a variável tem expoente 1 em uma dimensão apenas.
    if len(argumentos) == 0:
        ## Achar dimensão e definir expoente:
        expoente = [int(variavel == dimensao)]
        k+=1

    ## Considerar possibilidade variavel [=] 1/dimensao**n:
    elif all([str(dimensao) in str(argumentos[0]),isinstance(argumentos[1],sp.core.numbers.Integer)]):
        expoente = [argumentos[1]]
        k+=1

    ## Se houverem argumentos (mais de uma dimensão):
    else:
        ## Itera pelos argumentos:
        for arg in argumentos:

            ## Se o argumento atual contiver a dimensão:
            if str(dimensao) in str(arg):

                ## Obtém a potência da dimensão -- Feito em lista para poder iterar numa linha apenas
                expoente = [j for j in arg.atoms() if j.is_number]           

                # Atualiza o contador
                k+=1

                # Casos em que a dimensão tem potência 1
                if not expoente:
                    expoente = [1]

    ## Caso o contador seja 0, essa variável não tem tal dimensão
    if not k:
        expoente = [0]

    ## Levanta erros caso o contador seja maior que 1 (sobrescreveu expoente), ou se houver mais de um expoente na lista (não deve ser possível)
    if len(expoente)>1:
        raise Exception("Algum erro desconhecido ocorreu. (Mais de um expoente)")
    elif k>1:
        raise Exception("Algum erro desconhecido ocorreu. (Expoente sobrescrito)")
    
    ## Retorna o primeiro item da lista (expoente)
    return expoente[0]


def teorema_pi(variaveis:list,MLT:bool=True,dimensoes_primarias:list=[]) -> list:
    '''
    Função para aplicar o Teorema Pi de Bunckingham

    Variáveis devem ser passadas com o auxílio da classe 'Variavel', em função das dimensões do problema, sejam elas 'MLT' ou não.
    # Observações: \n
    - O núcleo será escolhido a partir das 3 primeiras variáveis sempre.
    - A variável dependente das demais deve ser estar em último na lista.
    - Caso o parâmetro 'MLT' seja definido como False, devem ser passadas as dimensões primárias utilizadas, pelo parâmetro 'dimensoes_primarias'
    '''

    ## Definição das dimensões primárias
    if MLT:
        M,L,T = sp.symbols('M L T')
        dimensoes_primarias = M,L,T
    elif not dimensoes_primarias:
        raise Exception("Erro. As dimensões primárias não foram definidas.")
    else:
        dimensoes_primarias = dimensoes_primarias

    ## Matriz das variáveis em termos das dimensões primárias
    matriz = sp.Matrix([[achar_expoente(v.dimensoes,d) for v in variaveis] for d in dimensoes_primarias])

    for linha in np.array(matriz):
        print(linha)

    ## Núcleo da matriz
    nucleo = matriz.nullspace()

    ## Para fins de praticidade
    variaveis = np.array([v.simbolo for v in variaveis])

    ## Grupos Pi
    Pis = []
    for i,j in enumerate(nucleo):
        expr =  (variaveis**np.array([k for k in j])).prod()
        Pis.append(Pi(i+1,f"{expr}"))

    return Pis


def main():

    variaveis = [densidade,velocidade,diametro_maior,comprimento,rugosidade,viscosidade,gravidade,perda_de_carga]

    pis = teorema_pi(variaveis)
    if pis:
        for pi in pis: 
            print(pi)
            pass
    input("\n")
 


if __name__ == '__main__':
    main()