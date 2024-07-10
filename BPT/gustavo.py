import itertools
import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import random
from time import perf_counter

def generate_rounded_coordinates(n, x_min, x_max, y_min, y_max):
    coordinates = []
    for _ in range(n):
        x = round(random.uniform(x_min, x_max), 1)  # Gere um número aleatório para x e arredonde para uma casa decimal
        y = round(random.uniform(y_min, y_max), 1)  # Gere um número aleatório para y e arredonde para uma casa decimal
        coordinates.append((x, y))  # Adicione o par de coordenadas à lista
    return coordinates


# Function to calculate the total lenght of a tour
def calculate_tour_length(city_coordinates, tour):
    tour_length = 0
    for i in range(len(tour) - 1):
        city1 = city_coordinates[tour[i]]
        city2 = city_coordinates[tour[i + 1]]
        distance = ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) * 0.5
        tour_length += distance
    return tour_length

# Function to plot the optimized tour on a 2D plane
def plot_tour(tour, city_coordinates, color='b'):
    x = [city_coordinates[i][0] for i in tour]
    y = [city_coordinates[i][1] for i in tour]

    plt.plot(x, y, marker='o', linestyle='-', markersize=8, color=color)
    plt.title('Optimized TSP Tour')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)

# Função para encontrar o tour mais curto usando busca exaustiva
def exhaustive_tsp(city_coordinates):
    num_cities = len(city_coordinates)

    #City coordinates é gerado com tuples e permutations também, então indicamos permut como uma lista
    permut = list(itertools.permutations(range(len(city_coordinates))))

    #Agora indicamos cada item como uma list também
    for i in range(len(permut)):
      permut[i]=list(permut[i])

    #Removemos as replicas de caminhos que começam em pontos diferentes do círculo
    for tour in permut:
      replicas=[]
      for i in range(len(tour)):
        replica= tour[i:]+tour[:i]
        replicas.append(replica)
      replicas.remove(replicas[0])
      for i in replicas:
        if i in permut:
          permut.remove(i)

    #Adicionamos a cidade inicial ao fim do caminho
    all_tours = []
    for tour in permut:
        tour.append(tour[0])
        all_tours.append(tour)

    #Elimina caminhos no sentido contrário
    visited_tours = []
    for tour in all_tours:
        reversed_tour = list(reversed(tour))
        if tour in visited_tours or reversed_tour in visited_tours:
            continue

        visited_tours.append(reversed_tour)

    for duplicated in visited_tours:
      all_tours.remove(duplicated)

    #Loop pelos caminhos restantes para achar o mais curto
    best_tour = None
    best_tour_length = float('inf')
    all_tour_lenghts = []

    for tour in all_tours:
      tour_length = calculate_tour_length(city_coordinates, tour)
      all_tour_lenghts.append(tour_length)
      if tour_length < best_tour_length:
        best_tour = tour
        best_tour_length = tour_length

    return best_tour, all_tours, all_tour_lenghts

random.seed(2)

# Exemplo de uso:
city_coordinates = generate_rounded_coordinates(8, 0, 10, 0, 10)
start = perf_counter()
best_tour, all_tours, all_tour_lenghts = exhaustive_tsp(city_coordinates)
stop = perf_counter() - start
print(f"Tempo de execução: {stop}")
#print(city_coordinates)
#print(all_tour_lenghts)
#print("Tour exaustivo:", best_tour)
#
#plot_tour(best_tour,city_coordinates)