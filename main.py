import random
import crusar_genes
import mutar_genes
import datetime
import fitness
import promedio
import arn
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

#lista_prod = pd.DataFrame ({"Cal":cal, "Peso":peso},index=["Coca-cola", "Pan", "Atún", "Agua", 
# "Chocolate", "Papitas", "Fruta", "Palomitas"])


#Definir población inicial de conejitos

#conejito1 = [1, 1, 1, 1, 1, 0, 1, 0]

#conejito2 = [0, 1, 0, 0, 1, 1, 0, 1]

#conejito3 = [1, 0, 0, 1, 0, 0, 0, 1]

#conejito4 = [0, 1, 1, 0, 1, 1, 0, 1]

# crear una población inicial aleatoria

#poblacion = [random.choices([0, 1], k=len(peso)) for i in range(tam_poblacion)]
poblacion = {}

for i in range(1, tam_poblacion + 1):
    poblacion.update({ str(i): random.choices([0, 1], k=len(peso))})

#variables par debugear
mejor_de_la_generacion = {
    "key": 0,
    "value": [],
    "promedio": 0
} 
segundo_mejor = {
    "key": 0,
    "value": [],
    "promedio": 0
}

tercer_mejor = {
    "key": 0,
    "value": [],
    "promedio": 0
}

#archivo para logs
archivo = open(f"Generacion {datetime.datetime.now()}", "w")

#array para comparar fitness
#la posicion de conejos va conectada con los indices del array 
for generacion in range(0, generaciones):

    #Obtener conejos con resultados mas cercanos a los parametros establecidos
    #Se encuentran ordenados del mas cercano al mas lejano
    resultado_calorias, resultado_peso = fitness.fitness(poblacion, cal, peso, lim_cal, lim_peso)

    #Asignar promedio para determinar el mejor conejo de la poblacion
    promedios = promedio.calificar_fitness(resultado_calorias, resultado_peso)

    mejor_de_la_generacion["key"] = list(promedios.keys())[0]
    segundo_mejor["key"] = list(promedios.keys())[1]
    tercer_mejor["key"] = list(promedios.keys())[2]
    
    mejor_de_la_generacion["promedio"] = list(promedios.values())[0]
    segundo_mejor["promedio"] = list(promedios.values())[1]
    tercer_mejor["promedio"] = list(promedios.values())[2]

    #Obtener el array de los mejores conejos de la poblacion
    arn_resultante = arn.obtener_arn(poblacion, promedios)

    mejor_de_la_generacion["value"] = arn_resultante["1"]
    segundo_mejor["value"] = arn_resultante["2"]
    tercer_mejor["value"] = arn_resultante["3"]

    archivo.write(f"Datos de la generacion {generacion}:\n")
#    print(f"Datos de la generacion {generacion}: ")

    archivo.write("{:<8} {:<25} {:<15} {:<10} \n".format('Conejo', 'Array', 'Calorias', 'Peso'))
#    print("{:<8} {:<25} {:<15} {:<10}".format('Conejo', 'Array', 'Calorias', 'Peso'))

    for key, value in poblacion.items():
        indice = 0
        calorias_total = 0
        peso_total = 0
    
        for producto in value:
            if producto:
                calorias_total += cal[indice]
                peso_total += peso[indice]
            indice += 1

        archivo.write("{:<8} {:<25} {:<15} {:<10} \n".format(key, str(value), calorias_total, peso_total))
#        print("{:<8} {:<25} {:<15} {:<10}".format(key, str(value), calorias_total, peso_total))

    archivo.write(f"Mejor de la generacion: {mejor_de_la_generacion} \n")
    archivo.write(f"Segundo de la generacion: {segundo_mejor} \n")
    archivo.write(f"Tercero de la generacion: {tercer_mejor} \n")
#    print(f"Mejor de la generacion: {mejor_de_la_generacion}")

    #Cruce y mutacion para la nueva generacion
    poblacion = crusar_genes.crusar_genes(arn_resultante["1"], arn_resultante["2"], arn_resultante["3"], archivo)
    
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