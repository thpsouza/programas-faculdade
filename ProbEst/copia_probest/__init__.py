'''
Parte de Probabilidade:
 -  Bernoulli
 -  Binomial
 -  Poisson
 -  Normal
 -  Exponencial
 -  Student

Parte de Estatistica:
 -  Medidas_Dispersao
 -  Medidas_Centralidade
 -  Quartis
 -  Discrepancia
 -  Boxplot
 -  Regressao_Linear
 -  Estimadores 
 -  Dimensionamento
 -  Teste_de_Hipoteses
'''

## Estatística
from . import (
    Medidas_Dispersao,
    Medidas_Centralidade,
    Quartis,
    Discrepancia,
    Boxplot,
    Regressao_Linear,
    Estimadores,
    Dimensionamento,
    Teste_de_Hipoteses
)

## Probabilidade
from . import (
    Bernoulli,
    Binomial,
    Poisson,
    Normal,
    Exponencial,
    Student
)


def analise_geral(*amostras):
    pass