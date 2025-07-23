import random
from poblacion import generar_poblacion, guardar_poblacion, calcular_fitness
from seleccion import seleccion
from operadores import crossover, mutacion
import os

def leer_poblacion_archivo(archivo):
    poblacion = []
    with open(archivo, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                individuo, fitness = parts
                poblacion.append((individuo, int(fitness)))
            elif len(parts) == 1:
                individuo = parts[0]
                poblacion.append((individuo, calcular_fitness(individuo)))
    return poblacion

def guardar_poblacion_simple(poblacion, archivo):
    with open(archivo, 'w') as f:
        for individuo, _ in poblacion:
            f.write(f"{individuo}\n")

def porcentaje_unos_mejor_individuo(poblacion):
    mejor = max(poblacion, key=lambda x: x[1])
    return mejor[1] / len(mejor[0])

def algoritmo_genetico(
    num_individuos=100,
    num_genes=10,
    umbral=20,
    prob_mutacion=0.01,
    max_iter=300,
    porcentaje_objetivo=1.0
):
    poblacion = generar_poblacion(num_individuos, num_genes)
    guardar_poblacion(poblacion, archivo="poblacion_0.txt")
    iteracion = 0
    while iteracion < max_iter:
        # Selección
        seleccionados = seleccion(poblacion, umbral=umbral)
        if not seleccionados:
            seleccionados = poblacion  # Si nadie pasa el umbral, usar toda la población
        guardar_poblacion(seleccionados, archivo=f"seleccion_{iteracion+1}.txt")
        # Cruzamiento y mutación
        nueva_poblacion = []
        while len(nueva_poblacion) < num_individuos:
            padres = random.sample(seleccionados, 2)
            hijo = crossover(padres[0][0], padres[1][0])
            hijo = mutacion(hijo, prob_mutacion)
            fitness = calcular_fitness(hijo)
            nueva_poblacion.append((hijo, fitness))
        poblacion = nueva_poblacion
        guardar_poblacion(poblacion, archivo=f"poblacion_{iteracion+1}.txt")
        iteracion += 1
        if porcentaje_unos_mejor_individuo(poblacion) >= porcentaje_objetivo:
            print(f"Condición de paro alcanzada en la generación {iteracion}.")
            break
    print(f"Ejecución finalizada en {iteracion} generaciones.")
    print(f"Mejor individuo: {max(poblacion, key=lambda x: x[1])}")

if __name__ == "__main__":
    algoritmo_genetico()
