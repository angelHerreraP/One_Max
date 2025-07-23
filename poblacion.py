import random
from seleccion import seleccion
from operadores import generar_nueva_poblacion 


#Funcion para generar a un individuo en un array #
def generar_individuo(num_genes=10):
    return ''.join(random.choice(['0','1']) for _ in range (num_genes))
#Funcion para contar su fitness, segun GPT, los unos que tiene#
def calcular_fitness(individuo):
    return individuo.count('1')


# Funcion para generar una poblacion de individuos
def generar_poblacion(num_individuos=100, num_genes=10):
    poblacion = []
    for _ in range(num_individuos):
        individuo = generar_individuo(num_genes)
        fitness = calcular_fitness(individuo)
        poblacion.append((individuo, fitness))
    return poblacion 


#Funcion para guardar en un archivo, porque me gusto la idea
def guardar_poblacion(poblacion, archivo="poblacion.txt"):
    with open(archivo, 'w') as f:
        for individuo, fitness in poblacion:
            f.write(f"{individuo} {fitness}\n")

