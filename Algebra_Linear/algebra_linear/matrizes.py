import numpy as np
from math import sqrt

class Matriz():
    def __init__(self, valores:list, m:int=0, n:int=0) -> None:
        '''
        Define uma matriz mxn de números reais.
        
        CASO não sejam passados valores suficientes, o restante da matriz é preenchida automaicamente com zeros.
        
        >>> a = Matriz((1,2,3,4),2,2)
        >>> print(a)
        [[1 2 
          3 4]]
        
        Operações:
        - Adição '+'
        - Subtração '-'
        - Multiplicação '*'
        - Potenciação '**'
        - Igualdade '=='
        
        EXs:
        >>> print(a+1)
        [[2 3 
          4 5]]
        >>> print(a+1 == a)
        False
        
        Indexação por '[,]'
        
        EX:
        >>> print(a[1,1])
        4
        >>> a[1,1] = 5
        >>> print(a[1,1])
        5
        '''   
        if (m == 0 or n == 0):
            if isinstance(valores,Matriz):
                m,n = valores.shape
            else:
                raise ValueError("As dimensões da matriz (mxn) não foram passadas.\n")
        self.matriz_linha = m == 1
        self.matriz_coluna = n == 1
        self.shape = (m,n)
        self.elementos = list(valores)  
        self.len = len(self.elementos)
        ## Preenche o restante com zeros caso não sejam passados argumentos suficientes
        if self.len != self.shape[0]*self.shape[1]:
            for i in range(self.len,self.shape[0]*self.shape[1]):
                self.elementos.append(0)
                
    ## Métodos especiais
    def __repr__(self) -> str:
        '''
        Representação da Matriz em formato de string (pretty print).
        '''
        return "["+ "\n ".join(f"[{' '.join(str(self.elementos[i*self.shape[1]+j]) for j in range(self.shape[1]))}]" for i in range(self.shape[0])) +"]"
    
    def __iter__(self) -> list:
        return iter(self.elementos)
    
    def __len__(self) -> int:
        '''
        Retorna o tamanho do Vetor que representa a Matriz achatada.
        '''
        return self.len
    
    def __getitem__(self, ij:tuple) -> float:
        ''' 
        EX1:
        >>> m = Matriz((1,2,3,4),2,2)
        >>> print(m[1,1]) 
        4        
        
        EX2 (Matriz 1D):
        >>> m = Matriz((1,2,3,4),4,1)
        >>> print(m[2,0])
        3
        >>> print(m[2])
        3
        '''
        ## Caso 1D
        if isinstance(ij, int):
            if bool(self.matriz_coluna) ^ bool(self.matriz_linha):   
                ## Defesa valor                
                if ij<0 or ij>self.shape[0]-1+self.shape[1]-1:
                    raise IndexError(f"Inválido. Os índices da matriz devem ser: i∈[0,{self.shape[0]-1}] e j∈[0,{self.shape[1]-1}]. \n")
                return self.elementos[ij]
        ## Descompatando os índices
        i,j = ij
        ## Defesa de índices
        if any([i<0,i>=self.shape[0],j<0,j>=self.shape[1]]): 
            raise IndexError(f"Inválido. Os índices da matriz devem ser: i∈[0,{self.shape[0]-1}] e j∈[0,{self.shape[1]-1}]. \n")
        ## Retornando o elemento correspodnente aos índices
        return self.elementos[i*self.shape[1] + j]
       
    def __setitem__(self, ij:int, item:float) -> None:
        '''
        EX:
        >>> m = Matriz((1,2,3,4,5,6),3,2)
        >>> print(v[2,1])
        6
        >>> m[2,1] = 10
        >>> print(m)
        [[1  2
          3  4 
          5 10]]  
        '''  
        ## Defesa de valor
        if not isinstance(item, (int,float)):
            raise TypeError("Todos os elementos da matriz devem ser numéricos. \n")
        ## Caso 1D
        if isinstance(ij, int):
            if bool(self.matriz_coluna) ^ bool(self.matriz_linha):   
                ## Defesa valor                
                if ij<0 or ij>self.shape[0]-1+self.shape[1]-1:
                    raise IndexError(f"Inválido. Os índices da matriz devem ser: i∈[0,{self.shape[0]-1}] e j∈[0,{self.shape[1]-1}]. \n")
                self.elementos[ij] = item
        ## Caso geral
        else:
            ## Descompactando
            i,j = ij
            ## Defesa de índices
            if any([i<0,i>=self.shape[0],j<0,j>=self.shape[1]]): 
                raise IndexError(f"Inválido. Os índices da matriz devem ser: i∈[0,{self.shape[0]-1}] e j∈[0,{self.shape[1]-1}]. \n")
            ## Atribuindo o elemento à posição
            self.elementos[i*self.shape[1] + j] = item
       
    def __eq__(self, other) -> bool:
        ''' 
        Retorna True se todos os elementos da matriz forem iguais.
        Do contrário, retorna False
        '''
        if not isinstance(other, Matriz):
            return False
        if self.shape != other.shape:
            return False
        return all((i==j for i,j in zip(self.elementos,other.elementos)))
    
    def __add__(self, other):
        '''
        Soma duas matrizes e retorna a matriz resultante
        '''
        if isinstance(other, Matriz):
            return Matriz([i+j for i,j in zip(self.elementos,other.elementos)], *self.shape)
        if isinstance(other, (float, int)):
            return Matriz([i+other for i in self.elementos], *self.shape)
        else:
            raise TypeError(f"Não é possível somar um(a) {type(self)} com um {type(other)}. \n")
    __radd__ = __add__
    
    def __sub__(self, other):
        '''
        Subtrai duas matrizes e retorna a matriz resultante
        '''
        if isinstance(other, Matriz):
            return Matriz([i-j for i,j in zip(self.elementos,other.elementos)], *self.shape)
        if isinstance(other, (float, int)):
            return Matriz([i-other for i in self.elementos], *self.shape)
        else:
            raise TypeError(f"Não é possível subtrair um {type(other)} de um(a) {type(self)}. \n")
    def __rsub__(self,other):
        '''
        Sentido contrário da operação de subtração
        '''
        if isinstance(other, Matriz):
            return Matriz([j-i for i,j in zip(self.elementos,other.elementos)], *self.shape)
        if isinstance(other, (float, int)):
            return Matriz([other-i for i in self.elementos], *self.shape)
        else:
            raise TypeError(f"Não é possível subtrair um(a) {type(self)} de um {type(other)} \n")
    
    def __mul__(self, other):
        '''
        Define a multiplicação entre a Matriz e outro objeto.
        '''
        if isinstance(other, (int, float)):
            return self.produto_por_escalar(other)
        if isinstance(other, Matriz):
            return self.produto_de_matrizes(other)
        else:
            raise TypeError(f"Não é possível multiplicar um(a) {type(self)} e um {type(other)}. \n")
    __rmul__ = __mul__
    #def __rmul__(self, other):
    #    '''
    #    Multiplicação no outro sentido
    #    '''
    #    if isinstance(other, (int, float)):
    #        return self.produto_por_escalar(other)
    #    if isinstance(other, Matriz):
    #        return self.produto_de_matrizes(other)
    #    else:
    #        raise TypeError(f"Não é possível multiplicar um(a) {type(self)} e um {type(other)}. \n")
       
    def __pow__(self, pot:float):
        '''
        Eleva todos os elementos da Matriz à 'pot'.
        '''
        return Matriz([i**pot for i in self.elementos], *self.shape)

    ## Métodos gerais
    def produto_por_escalar(self, escalar:float):
        '''
        Retorna o produto por escalar do Vetor com um número real.
        '''
        return Matriz([i*escalar for i in self.elementos], *self.shape)  
    
    def produto_de_matrizes(self, other):
        '''
        Multiplica duas matrizes (ou uma matriz e um vetor)
        '''
        # Defesa    
        if (self.shape[1] != other.shape[0]):
            raise ValueError("Erro. O número de colunas da primeira Matriz tem que ser igual ao número de linhas da segunda Matriz. \n")
        ## Algoritmo
        M = zeros(self.shape[0], other.shape[1])
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                for k in range(self.shape[1]):
                    M[i,j] += self[i,k]*other[k,j]      
        ## Escalar
        if M.shape == (1,1):
            return M[0,0]
        return M
    
    
    def resize(self, m, n):
        '''
        Modifica o formato (shape) da matriz
        '''
        if m*n == self.len:
            self.shape = (m,n)
        else:
            raise ValueError(f"Formato inválido. Os índices devem multiplicar para {self.len}")


    def transposta(self):
        '''
        Transpõe a matriz
        '''
        return transposta(self)



def shape(matriz:Matriz) -> tuple:
    '''
    Retorna o formato de uma dada matriz.
    '''
    return matriz.shape

def identidade(n:int) -> Matriz:
    '''
    Retorna a matriz identidade nxn.
    '''
    return Matriz((int(i==j) for j in range(n) for i in range(n)),n,n)

def zeros(m:int,n:int) -> Matriz:
    '''
    Retorna uma matriz mxn composta de zeros.
    '''
    return Matriz((),m,n)

def transposta(matriz:Matriz) -> Matriz:
    '''
    Retorna a transposta nxm de uma dada matriz mxn
    '''
    M = zeros(matriz.shape[1],matriz.shape[0])
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            M[i,j] = matriz[j,i] 
    return M


def SVD(matriz:Matriz) -> Matriz:
    '''
    Calcula a decomposição em valores singulares de uma dada matriz.
    '''
    #AAT = matriz*transposta(matriz)
    return np.linalg.svd(matriz)