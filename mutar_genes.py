import random

def mutar_genes(poblacion: dict, prob_mutacion: float) -> None:
    for key, value in poblacion.items():

        if prob_mutacion >= random.random():
            if value[2] == 0: 
                value[2] = 1  
            else:
                value[2] = 0
