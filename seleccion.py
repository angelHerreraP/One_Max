def seleccion(poblacion, porcentaje=None, umbral=None):
    if umbral is not None:
        return [ind for ind in poblacion if ind[1] >= umbral]
    elif porcentaje is not None:
        poblacion_ordenada = sorted(poblacion, key=lambda x: x[1], reverse=True)
        num_seleccionados = int(len(poblacion) * porcentaje)
        return poblacion_ordenada[:num_seleccionados]
    else:
        raise ValueError("Debes pasar porcentaje o umbral")
