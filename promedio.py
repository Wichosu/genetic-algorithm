def calificar_fitness(resultado_calorias: dict, resultado_peso: dict) -> dict:
    promedios = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0
    }

    #Otorgar puntuaciones segun mejores calorias
    puntuacion = 1
    for key, value in resultado_calorias.items():
        promedios[key] += puntuacion
        puntuacion /= 2

    #Otorgar puntuaciones segun mejores pesos
    puntuacion = 1
    for key, value in resultado_peso.items():
        promedios[key] += puntuacion
        puntuacion /= 2

    #Mejores promedios iniciando con el mas alto
    sorted_promedios = dict(sorted(promedios.items(), key=lambda item : item[1], reverse=True))

    return sorted_promedios