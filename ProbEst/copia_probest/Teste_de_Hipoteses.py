## TESTE DE HIPÓTESES - ESTATÍSTICA
## Teste para média e para proporção

from . import Normal, Student
from . import Medidas_Centralidade, Medidas_Dispersao


## EM DESENVOLVIMENTO
def erro_tipo_2_media(*amostra,mu,intervalo_aceitacao,**distribuicao):
    '''
    Calculo do erro tipo II para um teste de hipótese de média
    '''
    ## Define os dados
    # Calcula da amostra se não foram passados
    if amostra:
        n = len(amostra)
        sigma2 = Medidas_Dispersao.variancia(amostra)
    # Obtém da distribuição, se foram passados
    else:
        n = distribuicao['n']
        sigma2 = distribuicao['sigma2']
    
    ## Probabilidade de H0 ser falsa e não a rejeitarmos
    P = Normal.probabilidade_normal(mu,sigma2/n,x1=intervalo_aceitacao[0],x2=intervalo_aceitacao[1])

    return P



def teste_media_igual(*amostra,significancia,mu0=None,maior=False,**distribuicao):
    
    
    
    return 



def teste_media(*amostra,significancia,mu0=None,maior=False,**distribuicao):
    '''
    Teste de Hipóteses para média

    H0: mu <= mu0
    H1: mu > mu0
    
    Se maior = True:
    H0: mu >= mu0
    H1: mu < mu0

    Parametros:
    ----------

    distribuicao: 
        n:  int
        media: float
        sigma2: float, opcional
    '''

    ## Obtenção de n e da média amostral
    if amostra:
        amostra = amostra[0]
        n = len(amostra)
        media = Medidas_Centralidade.media(amostra)
    else:
        n = distribuicao['n']
        media = distribuicao['media']

    ## Se a variancia é conhecida: 
    if 'sigma2' in distribuicao:
        # Atribui o valor à variavel
        sigma2 = distribuicao['sigma2']    
        # Calcula C com a distribuição normal
        C = Normal.inversa_normal(1-significancia)*(sigma2/n)**(1/2)
    
    ## Se a variancia é desconhecida:
    else:
        # Estima a variancia a partir da amostra
        sigma2 = Medidas_Dispersao.variancia(amostra)
        # Calcula C com a distribuição t de Student
        C = Student.inversa_t(1-sigma2,n-1)*(sigma2/n)**(1/2)          
   

    if maior:
        ## Hipótese H0
        H0 = media < (mu0-C)       

        ## Erro tipo II
        P = 0
        if H0:
            pass

    else:
        ## Hipótese H0
        H0 = media > (mu0+C)

        ## Erro tipo II
        P = 0
        if H0:
            pass
      
    return {'H0':H0,'Erro II':P}



def teste_proporcao(*amostra,significancia,menor=False,**distribuicao):
    '''
    Teste de Hipóteses para média
    '''

    C = None

    if amostra:
        pass
    else:
        media = distribuicao['media']
        sigma2 = distribuicao['sigma2']
    
    H0 = 0
    H1 = 1

    return



