import random

def crossover(padre1, padre2):
    punto = random.randint(1, len(padre1) - 1)
    hijo = padre1[:punto] + padre2[punto:]
    return hijo

def mutacion(individuo, prob_mutacion=0.01):
    nuevo = ''
    for gen in individuo:
        if random.random() < prob_mutacion:
            nuevo += '1' if gen == '0' else '0'
        else:
            nuevo += gen
    return nuevo

