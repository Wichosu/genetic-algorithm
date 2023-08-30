def fitness(poblacion: dict, cal: list, peso: list, lim_cal: int, lim_peso: int) -> dict:
    fitness_calorias = {} 
    fitness_peso = {}
    
    for key, value in poblacion.items():
        indice = 0
        calorias_total = 0
        peso_total = 0
    
        for producto in value:
            if producto:
                calorias_total += cal[indice]
                peso_total += peso[indice]
            indice += 1
    
        fitness_calorias.update({key: abs(calorias_total - lim_cal)})
        fitness_peso.update({key: abs(lim_peso - peso_total)})

    #Ordenar conejor por mejor caloria y mejor peso
    sorted_fitness_calorias = dict(sorted(fitness_calorias.items(), key=lambda item: item[1]))
    sorted_fitness_peso = dict(sorted(fitness_peso.items(), key=lambda item: item[1]))

    return sorted_fitness_calorias, sorted_fitness_peso

    #Pasar negativos a ultimo lugar
#    sorted_fitness_calorias = dict(sorted(sorted_fitness_calorias.items(), key=lambda item: item[1] < 0))
#    sorted_fitness_peso = dict(sorted(sorted_fitness_peso.items(), key=lambda item: item[1] < 0))