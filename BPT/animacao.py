import pygame
import pygame.freetype
import math
from random import randint
from sys import exit
from itertools import permutations

####### Configurações iniciais pygame #######
pygame.init()

## Tela
largura,altura = 1080,910
screen = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Smart Water')
cor_contorno = 'GREY'
cor_fundo = 'GREY'

## Framerate
relogio = pygame.time.Clock()
fps_maximo = 60


####### Configurações animação #######

## Texto
fonte = pygame.freetype.SysFont("Arial", 20, bold=True)

## Estados da animação
escolhendo_vertice_inicial = True
animacao_pausada = False
simulando = True

## Variáveis
# cor_solucao = 'GREEN'
# cor_arestas = 'RED'
# espessura_arestas = 5

# cor_vertices = 'BLACK'
# num_vertices = 7
# tamanho_vertices = 15

# cor_agua = 'LIGHTBLUE'
# tamanho_inicial_agua = tamanho_vertices+1
# velocidade_agua = 4

# CICLO_FECHADO = True

variaveis = {
    'cor_solucao':            'GREEN',
    'cor_arestas':            'RED',
    'espessura_arestas':      5,
    'cor_vertices':           'BLACK',
    'num_vertices':           7,
    'tamanho_vertices':       15,
    'cor_agua':               'LIGHTBLUE',
    'tamanho_inicial_agua':   16,
    'velocidade_agua':        4,
    'CICLO_FECHADO':          True
}

####### Funções ####### 
def forca_bruta(vertices,ida_igual_volta=True):
    ## Todos os caminhos possíveis
    permutacoes = list(permutations(vertices,len(vertices)))
    
    ## Filtrando caminhos iguais, mas em sentidos reversos (considera-se o custo da ida e volta igual)
    if ida_igual_volta:
        permutacoes = [p for p in permutacoes if p != p[::-1]]
    
    ## Caminho ótimo para comparação
    caminho_otimo = (None,float('inf'))
    
    ## Itera por todas as permutações para encontrar a de menor custo
    for permutacao in permutacoes: 
        custo_total = 0
        
        ## Adicionando o ponto de partida como o ponto final
        if configs.CICLO_FECHADO:
            permutacao += (permutacao[0],)
        
        ## Calculando a distância total no caminho
        for i in range(len(permutacao)-1):
            custo_total+= calcular_distancia(permutacao[i].pos,permutacao[i+1].pos)
        
        ## Se o custo da iteração atual for menor que o caminho ótimo atual, este é atualizado
        if custo_total<caminho_otimo[1]:
            caminho_otimo = permutacao,round(custo_total,4)
        
    ## Retorna o caminho ótimo (ordem+custo) encontrado   
    return caminho_otimo

def novo_grafo(num_vertices, inicial=True):
    '''
    Retorna uma lista com pontos aleatórios 
    '''
    if inicial:
        return [(randint(largura/10,9/10*largura),randint(altura*2/10,9/10*altura)) for i in range(num_vertices)]
    else:
        global vertices, caminho_solucao, custo_solucao, grafo, animacao_pausada, agua
        vertices = [Vertice(coordenada,configs.tamanho_vertices,configs.cor_vertices,k) for k,coordenada in enumerate(novo_grafo(num_vertices))]
        caminho_solucao, custo_solucao = forca_bruta(vertices)
        grafo = Grafo(screen, vertices, [Aresta(caminho_solucao[i],caminho_solucao[i+1],configs.cor_solucao,configs.espessura_arestas) for i in range(len(caminho_solucao)-1)])
        reset()
    
def pausar():
    global animacao_pausada
    animacao_pausada = not animacao_pausada

#pause_surf = pygame.image.load('Pause.png').convert_alpha()
#pause_rect = pause_surf.get_rect(center = (largura*23/25, altura/20))
def indicador_pause():
    pause_surf = fonte.render(f"PAUSADO",'WHITE')[0]
    pause_rect = pause_surf.get_rect(topleft= (largura*20/25,altura/20))
    screen.blit(pause_surf,pause_rect)

def reset():
    global escolhendo_vertice_inicial, animacao_pausada, simulando, agua
    grafo.arestas = []
    grafo.distancia = 0
    agua = None
    escolhendo_vertice_inicial = True
    animacao_pausada = False
    simulando = True
    
def calcular_distancia(ponto1, ponto2):
    dist = math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)
    return dist


####### Classes #######

## Vertice
class Vertice:
    def __init__(self, coordenadas, raio, cor, indice) -> None:
        self.cor = cor
        self.pos = coordenadas
        self.raio = raio
        self.id = indice+1

## Aresta
class Aresta:
    def __init__(self, vertice1, vertice2, cor, espessura) -> None:
        self.v1 = vertice1
        self.v2 = vertice2
        self.espessura = espessura
        self.cor = cor
        self.distancia = calcular_distancia(self.v1.pos,self.v2.pos)

## Grafo
class Grafo:
    def __init__(self, screen, vertices, solucao=None) -> None:
        self.screen = screen
        self.vertices = vertices
        self.solucao = solucao
        self.arestas = []
        self.distancia = 0
   
    def desenhar_solucao(self):
        for s in self.solucao:
            pygame.draw.line(self.screen, s.cor, s.v1.pos, s.v2.pos, s.espessura)
    
    def desenhar_vertices(self):
        for i,v in enumerate(self.vertices):
            pygame.draw.circle(self.screen, v.cor, v.pos, v.raio)
            texto = fonte.render(str(i+1), 'WHITE')[0]
            retangulo = texto.get_rect(center=v.pos)
            self.screen.blit(texto, retangulo)

    def desenhar_arestas(self):
        for a in self.arestas:
            pygame.draw.line(self.screen, a.cor, a.v1.pos, a.v2.pos, a.espessura)
        self.distancia = round(sum(a.distancia for a in self.arestas),4)
    
    def update(self):
        self.desenhar_solucao()
        self.desenhar_arestas()
        self.desenhar_vertices()
        
## Água
class Agua:
    def __init__(self, screen, vertice_inicial, lista_vertices, raio_inicial, cor) -> None:
        self.screen = screen
        self.raio_inicial = raio_inicial
        self.raio_atual = self.raio_inicial
        self.cor = cor
        ## Vértice em que a simulação começará
        self.vertice_inicial = vertice_inicial
        self.vertice_atual = vertice_inicial
        ## Cria uma cópia, sem o vértice inicial
        self.lista_vertices = lista_vertices.copy()
        self.lista_vertices.remove(vertice_inicial)
        ## Lista para adicionar os vértices na ordem da solução
        self.solucao = [self.vertice_inicial]
        ## Variável para controlar o retorno ao ponto de origem
        self.fim = True
        
    def crescer(self):
        ## Cresce o círculo de água
        self.raio_atual+=configs.velocidade_agua
        
    def desenhar_agua(self):
        ## Desenha o circulo de água
        pygame.draw.circle(self.screen, self.cor, self.vertice_atual.pos, self.raio_atual, width=3)
                
    def colisao(self):
        ## Itera sobre todos os vértices,
        for v in self.lista_vertices:
            ## Calcula qual vértice 'colidirá' primeiro com a água
            if calcular_distancia(self.vertice_atual.pos,v.pos) <= v.raio + self.raio_atual:
                ## Cria a nova aresta no grafo
                grafo.arestas.append(Aresta(self.vertice_atual,v, configs.cor_arestas, configs.espessura_arestas))
                ## Remove o vértice atual da lista e continua a simuação a partir dele
                self.raio_atual = self.raio_inicial
                self.lista_vertices.remove(v)
                self.vertice_atual = v
                self.solucao.append(v)
        
    def update(self):
        if self.lista_vertices:
            self.crescer()
            self.desenhar_agua()
            self.colisao()
        ## Quando a lista terminar, volta pro vértice de origem
        elif self.fim:
            self.fim = False
            if configs.CICLO_FECHADO:
                self.lista_vertices.append(self.vertice_inicial)
        ## Final da simulação
        else:
            global simulando
            simulando = False
                   
## Fundo
class Fundo:
    def __init__(self, screen, cor) -> None:
        self.screen = screen
        self.cor = cor
        
        ## Espessura contorno
        k = 1/10
        ## Superior
        self.parede_superior_surf = pygame.Surface((largura,altura*1.5*k))
        self.parede_superior_rect = self.parede_superior_surf.get_rect(topleft = (0,0))
        self.parede_superior_surf.fill(color=self.cor)
        ## Direita
        self.parede_direita_surf = pygame.Surface((largura*k,altura))
        self.parede_direita_rect = self.parede_direita_surf.get_rect(bottomright = (largura,altura))
        self.parede_direita_surf.fill(color=self.cor)
        ## Esquerda
        self.parede_esquerda_surf = pygame.Surface((largura*k,altura))
        self.parede_esquerda_rect = self.parede_esquerda_surf.get_rect(topleft = (0,0))
        self.parede_esquerda_surf.fill(color=self.cor)
        ## Inferior
        self.parede_inferior_surf = pygame.Surface((largura,altura*k))
        self.parede_inferior_rect = self.parede_inferior_surf.get_rect(bottomleft = (0,altura))
        self.parede_inferior_surf.fill(color=self.cor)

    def contorno(self):
        self.screen.blit(self.parede_inferior_surf,self.parede_inferior_rect)
        self.screen.blit(self.parede_esquerda_surf,self.parede_esquerda_rect)
        self.screen.blit(self.parede_direita_surf,self.parede_direita_rect)
        self.screen.blit(self.parede_superior_surf,self.parede_superior_rect)

    def texto(self):        
        ## Solução por força bruta
        self.solucao_surf = fonte.render(f"Solução por força bruta: {[i.id for i in caminho_solucao]} ;  Distância: {custo_solucao}.",'DARKGREEN')[0]
        self.solucao_rect = self.solucao_surf.get_rect(topleft= (largura*1/50,altura/50))
        self.screen.blit(self.solucao_surf,self.solucao_rect)
        if agua:
            ## Água
            self.simulacao_surf = fonte.render(f"Solução por simulação:  {[i.id for i in agua.solucao]} ;  Distância: {grafo.distancia}.", 'RED')[0]
            self.simulacao_rect = self.simulacao_surf.get_rect(topleft = (largura*1/50,altura*3/50))
            self.screen.blit(self.simulacao_surf,self.simulacao_rect)
            if not simulando:
                ## Erro percentual
                self.erro_surf = fonte.render(f"Diferença percentual entre os caminhos: {round((grafo.distancia-custo_solucao)/custo_solucao*100,2)}%")[0]
                self.erro_rect = self.erro_surf.get_rect(topleft = (largura*1/50,altura*5/50))
                self.screen.blit(self.erro_surf,self.erro_rect)
        ## 
                 
                
    def update(self):
        self.contorno()
        self.texto()

## Classe para editar as configurações
class Configuracoes:
    def __init__(self, **kwargs) -> None:
        ## Arestas
        self.cor_solucao = kwargs['cor_solucao']
        self.cor_arestas = kwargs['cor_arestas']
        self.espessura_arestas = kwargs['espessura_arestas']
        ## Vértices
        self.cor_vertices = kwargs['cor_vertices']
        self.num_vertices = kwargs['num_vertices']
        self.tamanho_vertices = kwargs['tamanho_vertices']
        ## Água
        self.cor_agua = kwargs['cor_agua']
        self.tamanho_inicial_agua = kwargs['tamanho_inicial_agua']
        self.velocidade_agua = kwargs['velocidade_agua']
        ## Topologia
        self.CICLO_FECHADO = kwargs['CICLO_FECHADO']
    
    def modificar(self):
        ...
    
    
    
###########################################
fundo = Fundo(screen, cor_contorno)
configs = Configuracoes(**variaveis)
vertices = [Vertice(coordenada,configs.tamanho_vertices,configs.cor_vertices,k) for k,coordenada in enumerate(novo_grafo(configs.num_vertices))]
caminho_solucao, custo_solucao = forca_bruta(vertices)
grafo = Grafo(screen, vertices, [Aresta(caminho_solucao[i],caminho_solucao[i+1],configs.cor_solucao,configs.espessura_arestas) for i in range(len(caminho_solucao)-1)])
agua = None

####### Laço #######
while True:
    
    ## Fecha o jogo
    for evento in pygame.event.get():
        ## Quit
        if evento.type == pygame.QUIT:
            ## Fecha o jogo
            pygame.quit()
            exit()
        
        ## Pause, reset e novo grafo
        if evento.type == pygame.KEYDOWN:
            if evento.key == 110:
                novo_grafo(configs.num_vertices,False)
            if evento.key == 112:
                pausar()
            if evento.key == 114 and agua:
                reset()  
        
        ## Posição mouse
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            print(pygame.mouse.get_pos())
            
            ## Escolha do vértice inicial
            if escolhendo_vertice_inicial:
                distancias = [calcular_distancia(pygame.mouse.get_pos(),v.pos) for v in vertices]
                vertice_inicial = vertices[distancias.index(min(distancias))]
                agua = Agua(screen, vertice_inicial, vertices, configs.tamanho_inicial_agua, configs.cor_agua)
                escolhendo_vertice_inicial = False

    ## Animação rolando...
    if not animacao_pausada:
        
        ## Limpar tela
        screen.fill(cor_fundo)

        ## Atualiza a 'água'
        if not escolhendo_vertice_inicial:
            agua.update()

        ## Atualiza o fundo
        fundo.update()

        ## Desenha e atualiza o grafo
        grafo.update()
        
    else:
        ## Indicador de pause
        indicador_pause()


    pygame.display.update()
    relogio.tick(fps_maximo)