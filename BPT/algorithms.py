import math
import pandas as pd
from random import randint
from time import perf_counter
from algebra_linear.matrizes import *
from itertools import permutations
from math import factorial

class Node:
    def __init__(self, x, y) -> None:
        '''
        Node of a graph, with x,y coordinates.
        '''
        self.x = x
        self.y = y
        self.coordinates = x,y
        self.id = None
        
    def distance(self, other) -> float:
        '''
        Returns the distance to another Node.
        '''
        return calculate_distance(self.coordinates, other.coordinates)

class Graph:
    def __init__(self, nodes:list, decimal_places=4) -> None:
        '''
        Graph with nodes, cujas distancias
        '''
        # Inputs
        self.nodes = nodes
        self.decimal_places = decimal_places
        self.n = len(nodes)
        
        # Egdes matrix, representing the distances between two nodes
        self.edges = zeros(self.n, self.n)
        for i in range(self.n):
            for j in range(self.n):
                self.edges[i,j] = 0 if i == j else self.nodes[i].dist(self.nodes[j])           
    
        # Atribuir ID aos vértices
        for k,v in enumerate(self.nodes):
            v.id = k
    
    def __repr__(self):
        return self.edges.__repr__(self.decimal_places)
    
    def custo_sequencia(self, sequencia:list):
        '''
        Retorna o custo total de uma dada sequencia do grafo
        '''
        custo = 0
        for i in range(len(sequencia)-1):
            custo += self.edges[sequencia[i],sequencia[i+1]]
        return custo        

def generate_nodes(n:int, dx, dy) -> list:
    '''
    Creates a n-sized list of randomly distributed nodes in the rectangle [0,x] [0,y].
    '''
    return [Node(randint(0,dx),randint(0,dy)) for k in range(n)]

def calculate_distance(point1:tuple, point2:tuple) -> float:
    '''
    Calculates the distance bewtween two points (x,y)
    '''
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def algoritmo_agua(grafo:Graph, posicao_inicial:int):
    '''
    Resolve pelo algoritmo da água (vizinho mais próximo)
    '''
    ## Definindo a posição inicial
    vertice_atual = posicao_inicial
    ## Copiando a matriz de conexões
    conexoes = grafo.edges.copy()
    ## Inicializando sequencia e custo
    sequencia = [vertice_atual]
    custo_total = 0
    
    ## Algoritmo com n iterações
    for k in range(grafo.n-1):
        ##
        ## 'Removendo' da matriz a coluna correspondente ao vértice atual
        conexoes[:,vertice_atual] = float('inf')
        ## Obtendo, da matriz, as distâncias até o vizinho mais próximo
        distancias = conexoes[vertice_atual,:]
        ## Encontra o vertice mais proximo   
        vizinho_mais_proximo = distancias.index(min(distancias))               
        ## Atualiza custo e sequencia 
        sequencia.append(vizinho_mais_proximo)
        custo_total+=grafo.edges[vertice_atual,vizinho_mais_proximo]
        ## Atualiza o vértice atual
        vertice_atual = vizinho_mais_proximo
        
    ## Adiciona o inicial no final da sequência
    sequencia.append(sequencia[0])
    custo_total += grafo.edges[vertice_atual,sequencia[0]]
        
    ## Retorna os valores encontrados
    return sequencia,custo_total
  
def forca_bruta(grafo:Graph) -> list:
    '''
    Resolve o problema do caixeiro viajante por força bruta.
    Retorna uma lista com a ordem dos vértices
    '''
    ## Lista de vertices:
    lista = [i.id for i in grafo.nodes]
    
    ## Matriz de distancias
    distancias = grafo.edges
    
    ## Caminho ótimo para comparação
    caminho_otimo, custo_otimo = None,float('inf')

    ## Itera por todas as permutações para encontrar a de menor custo
    for permutacao in permutations(lista): 

        ## Filtrando caminhos iguais, mas em sentidos ou ordens diferentes (considera-se o custo da ida e volta igual)
        if permutacao[0] != 0:
            continue
        
        ## Adicionando o ponto de partida como o ponto final
        permutacao += (permutacao[0],)
        
        ## Calculando a distância total no caminho
        custo_total = 0
        for i in range(len(permutacao)-1):
            custo_total += distancias[permutacao[i],permutacao[i+1]]

            ## Se o caminho atual ultrapassar o caminho ótimo, pula para a próxima permutação
            if custo_total >= custo_otimo:
                break
    
        ## Se o laço completou, o custo da iteração atual é menor que o caminho ótimo prévio. Logo, este deve ser atualizado
        else:
            caminho_otimo = list(permutacao)
            custo_otimo = custo_total
        
    ## Retorna o caminho ótimo (ordem+custo) encontrado   
    return caminho_otimo, custo_otimo

def previsao_forca_bruta(n,k,recalcular=False):
    '''
    Imprime o tempo previsto para a execução do algoritmo de força bruta para k grafos aleatórios com n vértices.
    
    Usa como base para o cálculo o tempo médio para um grafo de 9 vértices, previamente obtido:\n
    --> 0.0.6023539035999995 s  (média de 1000 execuções com 1000 grafos aleatórios distintos)
    
    Se 'recalcular' == True, recalcula esse tempo médio na hora, com 100 execuções.
    '''
    t = 0.6023539035999995
    if recalcular:
        t = sum(benchmark_forca_bruta(9,100,imprimir=False))/100
        print(f"Tempo 9 vértices: {t}\n\n")
    previsao_tempo = lambda n: factorial(n)/factorial(9) * t
    
    ## Previsão tempos:
    print(f"\nTEMPO DE EXECUÇÃO PREVISTO (n = {n}, k = {k}): \n" + "-"*43)
    if n >= 13:
        string1 = f"{round(previsao_tempo(n)/3600,4)} horas"
        string2 = f"{round(previsao_tempo(n)*k/3600,4)} horas"
    elif n >= 10:
        string1 = f"{round(previsao_tempo(n)/60,4)} minutos"
        string2 = f"{round(previsao_tempo(n)*k/60,4)} minutos"
    else: 
        string1 = f"{round(previsao_tempo(n),4)} segundos"
        string2 = f"{round(previsao_tempo(n)*k,4)} segundos"
    print("Previsão de tempo médio: " + string1)
    if k>1:
        print(f"Previsão de tempo total necessário: " + string2) 
    print('\n')
    
def benchmark_forca_bruta(n,k,imprimir=True,tempo_previsto=True):
    '''
    Função para calcular o tempo médio de execução do algoritmo de força bruta, 
    para k grafos aleatórios com n vértices cada. 
    '''
    ## Imprimir tempo previsto
    if imprimir and tempo_previsto:
        previsao_forca_bruta(n,k)
    
    ## Benchmark
    tempo_total = perf_counter()
    tempos = []
    for i in range(k):
        # Gerar gráfico aleatório
        grafo = Graph(generate_nodes(n,100,100),4)
        # Começar cronometro
        start = perf_counter()
        # Força bruta
        forca_bruta(grafo)
        # Adiciona a lista
        tempos.append(perf_counter() - start)
    tempo_total = perf_counter() - tempo_total
    
    ## Resultados
    if imprimir:
        print(f"TEMPO DE EXECUÇÃO DECORRIDO (n = {n}, k = {k}): \n")
        if n >= 13:
            # Imprimindo o tempo médio
            print(f"Tempo médio para grafos com {n} vértices: {round(sum(tempos)/k/3600,4)} horas  --- (Amostra com {k} grafos aleatórios)")
            # Imprimindo o tempo total
            print(f"Tempo total para {k} grafos com {n} vértices: {round(sum(tempos)/3600,4)} horas\n")   
        elif n >= 10:
            # Imprimindo o tempo médio
            print(f"Tempo médio para grafos com {n} vértices: {round(sum(tempos)/k/60,4)} minutos  --- (Amostra com {k} grafos aleatórios)")
            # Imprimindo o tempo total
            print(f"Tempo total para {k} grafos com {n} vértices: {round(sum(tempos)/60,4)} minutos\n")        
        else:
            # Imprimindo o tempo médio
            print(f"Tempo médio para grafos com {n} vértices: {round(sum(tempos)/k,4)} segundos  --- (Amostra com {k} grafos aleatórios)")
            # Imprimindo o tempo total
            print(f"Tempo total para {k} grafos com {n} vértices: {round(sum(tempos),4)} segundos\n")   

    return tempos
    
def main():
    
    imprimir = True
    escrever_txt = False
    
    # String para o .txt
    string = ''
    # Lista tempos
    # Lista soluções
    
    # Algoritmo análise:
    for n in range(2,13):
        print(f"Processando n = {n}...\n")
        
        ## 1) Gerar/Receber Grafo de tamanho n
        start = perf_counter()
        grafo = Graph(generate_nodes(n,10,10),4)
        print(f"Gerar grafo: {perf_counter()-start}")
        
        ## 2) Escolher posição inicial (para algoritmo da água)
        posicao_inicial = randint(0,n-1)
        
        ## 3) Força bruta
        start = perf_counter()
        solucao_forca_bruta, custo_forca_bruta = forca_bruta(grafo)
        tempo_forca_bruta = perf_counter() - start
        
        ## 4) Nearest neighbour       
        start = perf_counter()
        solucao_agua, custo_agua = algoritmo_agua(grafo,posicao_inicial)
        tempo_agua = perf_counter() - start
        
        ## 5) Comparar e analisar dados
        #diferenca_custo = (custo_agua - custo_forca_bruta)/custo_forca_bruta
        #diferenca_tempo = (tempo_agua - tempo_forca_bruta)/tempo_forca_bruta
        
        ## 6) Armazenar dados
        #string += f"GRAFO COM {n} VÉRTICES {tuple(range(0,n))}:"
        #string += f"\nSolução Força Bruta: {[i for i in solucao_forca_bruta]}\n"
        string += f"Tempo Força Bruta: {round(tempo_forca_bruta,4)}\n"
        string += f"Custo Força Bruta: {round(custo_forca_bruta,4)}\n"
        #string += f"\nSolução Algoritmo Água: {solucao_agua}\n"
        string += f"Tempo Algoritmo Água: {round(tempo_agua,4)} s\n"
        string += f"Custo Algoritmo Água: {round(custo_agua,4)} s\n\n"
        #string += "\n Comparação dos algoritmos:"
        #string += f"Diferenca de tempo: {round(diferenca_tempo,4)} s\n"
        #string += f"Diferença de custo: {round(diferenca_custo,4)} s\n"
        string += "\n\n"
        
        
    # Printar dados
    if imprimir:
        print(string)
    
    # Escrever os dados
    if escrever_txt:
        with open("dados.txt", 'w+', encoding='utf-8') as f:
            f.write(string)
            
    
if __name__ == "__main__":
    main()