from sympy import Symbol,sympify

class Variavel():
    '''
    Classe customizada para variáveis na análise dimensional
    '''
    def __init__(self, simbolo:str, dimensoes:str) -> None:
        self.simbolo = Symbol(simbolo)
        self.dimensoes = sympify(dimensoes)
    def __mul__(self,other):
        if isinstance(other,Variavel):
            return self.simbolo*other.simbolo
        else:
            return self.simbolo*other
    __rmul__ = __mul__ 
    def __repr__(self) -> str:
        return f"{self.simbolo} [=] {self.dimensoes}"


#### "Dicionário" de variáveis

## Propriedades fluido
densidade = Variavel('p','M/L**3')
viscosidade = Variavel('mu','M/L/T')
tensao_superficial = Variavel('σ','M/T**2')
viscosidade_cinematica = Variavel('Ni','L**2/T')

## Propriedades de comprimento
comprimento = Variavel('x','L')
altura = Variavel('h','L')
raio = Variavel('r','L')
diametro_maior = Variavel('D','L')
diametro_menor = Variavel('d','L')
comprimento_de_onda = Variavel('λ','L')
rugosidade = Variavel('E','L')
perda_de_carga = Variavel('h_L','L')

## Tempo
tempo = Variavel('t','T')

## Velocidades
velocidade = Variavel('v','L/T')
velocidade_som = Variavel('c','L/T')
velocidade_angular = Variavel('w','1/T')

## Demais
gravidade = Variavel('g','L/T**2')
potencia = Variavel('Pot','M*L**2/T**3')
pressao = Variavel('P','M/L/T**2')




