import random

def mutar_genes(poblacion: dict, prob_mutacion: float, archivo_log) -> None:
    if prob_mutacion >= random.random():
        first_half_array = (len(list(poblacion.values())[0]) / 2) - 1

        random_key = random.randint(0, first_half_array)

        for key, value in poblacion.items():
            if value[random_key] == 0: 
                value[random_key] = 1  
            else:
                value[random_key] = 0
        archivo_log.write(f"Mutación presente en columna {random_key} \n")
