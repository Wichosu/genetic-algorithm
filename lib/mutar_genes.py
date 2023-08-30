import random

def mutar_genes(poblacion: dict, prob_mutacion: float, archivo_log) -> None:
    if prob_mutacion >= random.random():
        for key, value in poblacion.items():
            if value[2] == 0: 
                value[2] = 1  
            else:
                value[2] = 0
        archivo_log.write("Mutación presente \n")
