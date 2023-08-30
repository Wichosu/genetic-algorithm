import random
import crusar_genes
import mutar_genes
import datetime
import fitness
import promedio
import arn
import escribir_generacion

# definir los parámetros del algoritmo genético
tam_poblacion = 4

prob_mutacion = 0.1  #10% de probabilidad como prueba

generaciones = 5 #Número de generaciones a probar

# definir la capacidad de la mochila
lim_cal = 1200

lim_peso = 2

# definir la lista de pesos y calorías de los productos
cal = [500, 300, 250, 20, 200, 500, 180, 400]

peso = [0.7, 0.2, 0.8, 0.2, 0.6, 0.9, 0.6, 0.6]

# crear una población inicial aleatoria
poblacion = {}

for i in range(1, tam_poblacion + 1):
    poblacion.update({ str(i): random.choices([0, 1], k=len(peso))})

#archivo para logs
archivo = open(f"Generacion {datetime.datetime.now()}", "w")

for generacion in range(0, generaciones):

    #Obtener conejos con resultados mas cercanos a los parametros establecidos
    #Se encuentran ordenados del mas cercano al mas lejano
    resultado_calorias, resultado_peso = fitness.fitness(poblacion, cal, peso, lim_cal, lim_peso)

    #Asignar promedio para determinar el mejor conejo de la poblacion
    promedios = promedio.calificar_fitness(resultado_calorias, resultado_peso)

    #Obtener el array de los mejores conejos de la poblacion
    arn_resultante = arn.obtener_arn(poblacion, promedios)

    escribir_generacion.escribir_generacion(archivo, generacion, poblacion, cal, peso, promedios, arn_resultante)

    #Cruce y mutacion para la nueva generacion
    poblacion = crusar_genes.crusar_genes(arn_resultante["1"], arn_resultante["2"], arn_resultante["3"], archivo)

    #Mutar tercera columna de la poblacion segun la probabilidad de mutacion
    mutar_genes.mutar_genes(poblacion, prob_mutacion, archivo)
    
    #Pseudocodigo
    # Obtener total de calorias y peso DONE
    # Obtener promedio para saber cual conejo tiene mejor fitness usando diccionarios DONE
    # Comparar total de cada conejo con los parametros establecidos DONE
    # Catalogar los conejos segun el que se haya acercada mas a los parametros DONE
    # Hacer la seleccion fitness ej: DONE
    # 1 n n n n n n n n
    # 2 n n n n n n n n
    # -----------------
    # 2 n n n n n n n n
    # 3 n n n n n n n n
    # Hacer el cruce a la seleccion DONE
    # 1 n n n n 2n 2n 2n 2n
    # 2 n n n n 1n 1n 1n 1n
    # ----------------------
    # 2 n n n n 3n 3n 3n 3n
    # 3 n n n n 2n 2n 2n 2n
    #Hacer la mutacion aleatoria DONE
    # La mutacion invierte el valor de una columna
    #Repetir el proceso DONE
    # imprimir los arreglos de cada generacion para ver resultados
    #
    # for poblacion as conejo
    #      indice = 0
    #      for conejo as caloria
    #          if caloria = 1 
    #              
    #              agarrar valor de caloria y sumarlo