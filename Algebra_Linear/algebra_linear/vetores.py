import numpy as np
from math import sqrt
from matrizes import Matriz

class Vetor(Matriz):
    def __init__(self,*valores) -> None:
        '''
        Define um vetor (COLUNA) de números reais a partir dos argumentos.
        
        >>> a = Vetor(1,2,3,4)
        >>> print(a)
        [1 2 3 4]
        
        Operações:
        - Adição '+'
        - Subtração '-'
        - Multiplicação '*'
        - Potenciação '**'
        - Igualdade '=='
        
        EXs:
        >>> print(a+1)
        [2 3 4 5]
        >>> print(a+1 == a)
        False
        
        Indexação por '[]'
        
        EX:
        >>> print(a[3])
        4
        >>> a[3] = 5
        >>> print(a[3])
        5
        '''
        if isinstance(valores[0], (tuple,list,np.ndarray)):
            self.elementos = list(valores[0])
        else:
            self.elementos = list(valores)
        self.len = len(self.elementos)
        self.shape = self.len,1
    
    ## Métodos especiais
    def __repr__(self) -> str:
        return "["+'\n '.join(str(i) for i in self.elementos)+"]"
       
    def __getitem__(self, indice:int) -> float:
        ''' 
        >>> v = Vetor(1,2,3)
        >>> print(v[2]) 
        3        
        '''
        if isinstance(indice, (tuple,list)):
            indice = indice[0]
        return self.elementos[indice]
       
    def __setitem__(self, indice:int, item:float) -> None:
        '''
        >>> v = Vetor(1,2,3)
        >>> v[2] = 10
        >>> print(v[2])
        10  
        '''  
        if not isinstance(item, (int,float)):
            raise TypeError("Todos os elementos do vetor devem ser numéricos. \n")
        if isinstance(indice, (tuple,list)):
            indice = indice[0]
        self.elementos[indice] = item
       
    #def __eq__(self, other) -> bool:
    #    ''' 
    #    Retorna True se todos os elementos do vetor forem iguais.
    #    Do contrário, retorna False
    #    '''
    #    if type(other) is Matriz:
    #        if other.matriz_linha:
    #            return all((i==j for i,j in zip(self.elementos,other.elementos)))
    #    return super().__eq__(other)
        
    def __add__(self, other):
        '''
        Soma dois vetores e retorna o vetor resultante
        '''
        if type(other) is Matriz:
            if other.matriz_linha:
                return Vetor([i+j for i,j in zip(self.elementos,other.elementos)])
        return Vetor(super().__add__(other).elementos)
    __radd__ = __add__
    
    def __sub__(self, other):
        '''
        Subtrai dois vetores e retorna o vetor resultante
        '''
        if type(other) is Matriz:
            if other.matriz_linha:
                return Vetor([i-j for i,j in zip(self.elementos,other.elementos)])
        return Vetor(super().__sub__(other).elementos)
    def __rsub__(self,other):
        '''
        Sentido contrário da operação de subtração
        '''
        if type(other) is Matriz:
            if other.matriz_linha:
                return Vetor([j-i for i,j in zip(self.elementos,other.elementos)])
        return Vetor(super().__rsub__(other).elementos)
    
    def __mul__(self, other):
        '''
        Define a multiplicação entre o Vetor e outro objeto.
        '''
        if isinstance(other, Vetor) or (isinstance(other, Matriz) and (self.shape[1] == other.shape[1] == 1)):
            return self.produto_interno(other)
        return super().__mul__(other)
    def __rmul__(self, other):
        '''
        Define a multiplicação no outro sentido. 
        Precisa ser explicitado para multiplicar vetores x matrizes coluna e produto matriz-vetor.
        '''
        if isinstance(other, Matriz):
            if (self.shape[1] == other.shape[1] == 1):
                return self.produto_interno(other)
            else:
                return other.__rmul__(self)
        return super().__rmul__(other)
       
    def __pow__(self, pot:float):
        '''
        Eleva todos os elementos do Vetor à 'pot'.
        '''
        return Vetor(super().__pow__(pot).elementos)

    ## Métodos gerais  
    def produto_por_escalar(self, escalar:float):
        '''
        Retorna o produto por escalar do Vetor com um número real.
        '''
        ## Defesa
        if not isinstance(escalar,(int,float)):
            raise TypeError("O valor passado deve ser um escalar. \n")
         
        ## Calculo
        return Vetor(super().produto_por_escalar(escalar).elementos)
    
    def produto_interno(self, other) -> float:
        '''
        Retorna o produto interno de dois vetores.
        '''
        return produto_interno(self,other)
    
    def produto_diadico(self, other) -> Matriz:
        '''
        Retorna o produto diádico (produto tensorial) entre dois vetores u(mx1) e v(nx1), tal que:
        
        u ⊗ v = uv^T = [u1v1...] (mxn)
        '''
        return produto_diadico(self,other)
    
    def produto_vetorial(self, other):
        '''
        Calcula o produto vetorial entre dois vetores.
        ''' 
        raise NotImplementedError()


def produto_interno(u:Vetor, v:Vetor) -> float:
    '''
    Retorna o produto interno de dois vetores.
    '''
    ## Defesa
    for i in (u,v):
        if not isinstance(i, Vetor):
            if not (isinstance(i, Matriz) and i.matriz_coluna):
                raise TypeError("Para calcular o produto interno, ambos os argumentos devem ser vetores. \n")
    
    ## Calculo
    return sum([i*j for i,j in zip(u.elementos,v.elementos)])

def produto_diadico(u:Vetor, v:Vetor) -> Matriz:
    '''
    Retorna o produto diádico (produto tensorial) entre dois vetores u(mx1) e v(nx1), tal que:
    
    u ⊗ v = uv^T = [u1v1...] (mxn)
    '''
    ## Defesa
    for i in (u,v):
        if not isinstance(i, Vetor):
            if not (isinstance(i, Matriz) and i.matriz_coluna):
                raise TypeError("Para calcular o produto diádico, ambos os argumentos devem ser vetores. \n")
    
    ## Calculo
    M = []
    for linha in range(u.len):
        for coluna in range(v.len):
            M.append(u[linha]*v[coluna])
    
    return Matriz(M,u.len,v.len)
   
def norma(vetor:Vetor, p:int=2):
    '''
    Retorna a norma-Lp de um dado Vetor, de forma que, se:
    - p == 1     --> Retorna a norma-1 de um Vetor.
    - p == 2     --> Retorna a norma-2 (induzida por produto interno com ele mesmo) do Vetor.
    - ...
    - p == 'inf' --> Retorna a norma-inf de um Vetor.
    '''   
    ## Casos especiais (mais comuns)
    match str(p):
        case '1':
            return sum(abs(i) for i in vetor.elementos)
        case '2':
            return sqrt(vetor.produto_interno(vetor))
        case 'inf':
            return max(vetor.elementos)    
    
    ## Defesa para evitar overflow:
    if p<1 or p>100:
        raise ValueError("O valor de 'p' deve estar no intervalo [1,100]. \n")
    
    ## Caso geral da norma p
    return sum(abs(i)**p for i in vetor.elementos)**(1/p)

    
def main():
    a = Vetor(1,2,3,4)
    b = Vetor(1,2,3)
    print(a.produto_diadico(b))

if __name__ == "__main__":
    main()