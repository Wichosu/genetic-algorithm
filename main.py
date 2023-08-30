import random
import crusar_genes
import mutar_genes
import datetime
# definir los parámetros del algoritmo genético

tam_poblacion = 4

prob_mutacion = 0.1  #10% de probabilidad como prueba

generaciones = 50 #Número de generaciones a probar


# definir la capacidad de la mochila

lim_cal = 1200

lim_peso = 2


# definir la lista de pesos y calorías de los productos
cal = [500, 300, 250, 20, 200, 500, 180, 400]

peso = [0.7, 0.2, 0.8, 0.2, 0.6, 0.9, 0.6, 0.6]

#lista_prod = pd.DataFrame ({"Cal":cal, "Peso":peso},index=["Coca-cola", "Pan", "Atún", "Agua", 
# "Chocolate", "Papitas", "Fruta", "Palomitas"])


#Definir población inicial de conejitos

conejito1 = [1, 1, 1, 1, 1, 0, 1, 0]

conejito2 = [0, 1, 0, 0, 1, 1, 0, 1]

conejito3 = [1, 0, 0, 1, 0, 0, 0, 1]

conejito4 = [0, 1, 1, 0, 1, 1, 0, 1]

# crear una población inicial aleatoria

#poblacion = [random.choices([0, 1], k=len(peso)) for i in range(tam_poblacion)]
poblacion = {}

for i in range(1, tam_poblacion + 1):
    poblacion.update({ str(i): random.choices([0, 1], k=len(peso))})

#variables par debugear
mejor_de_la_generacion = {
    "key": 0,
    "value": []
} 

archivo = open(f"Generacion {datetime.datetime.now()}", "w")

#array para comparar fitness
#la posicion de conejos va conectada con los indices del array 
for generacion in range(0, generaciones):
    fitness_calorias = {} 
    fitness_peso = {}
    
    for conejo in poblacion.items():
        indice = 0
        calorias_total = 0
        peso_total = 0
    
        for producto in conejo[1]:
            if producto:
                calorias_total += cal[indice]
                peso_total += peso[indice]
            indice += 1
    
        fitness_calorias.update({conejo[0]: abs(calorias_total - lim_cal)})
        fitness_peso.update({conejo[0]: abs(lim_peso - peso_total)})
    
    #Ordenar conejor por mejor caloria y mejor peso
    sorted_fitness_calorias = dict(sorted(fitness_calorias.items(), key=lambda item: item[1]))
    sorted_fitness_peso = dict(sorted(fitness_peso.items(), key=lambda item: item[1]))

    #Pasar negativos a ultimo lugar
#    sorted_fitness_calorias = dict(sorted(sorted_fitness_calorias.items(), key=lambda item: item[1] < 0))
#    sorted_fitness_peso = dict(sorted(sorted_fitness_peso.items(), key=lambda item: item[1] < 0))


    promedios = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0
    }
    
    #Otorgar puntuaciones segun mejores calorias
    puntuacion = 1
    for conejo in sorted_fitness_calorias.items():
        promedios[conejo[0]] += puntuacion
        puntuacion /= 2
    
    #Otorgar puntuaciones segun mejores pesos
    puntuacion = 1
    for conejo in sorted_fitness_peso.items():
        promedios[conejo[0]] += puntuacion
        puntuacion /= 2
    
    #Mejores promedios iniciando con el mas alto
    sorted_promedios = dict(sorted(promedios.items(), key=lambda item : item[1], reverse=True))

    mejor_de_la_generacion["key"] = list(sorted_promedios.keys())[0]
    
    #alas de genes, la mejor el indice 0 y la peor indice 3
    alas = {
        "1": [],
        "2": [],
        "3": []
    } 
    
    key_alas = 1
    #Asignar a ramas o alas para hacer el cruce
    for mejor in sorted_promedios.items():
        if key_alas >= 4:
            break
    
        alas.update({str(key_alas): poblacion[mejor[0]]})
        key_alas += 1

    mejor_de_la_generacion["value"] = alas["1"]

    archivo.write(f"Datos de la generacion {generacion}:\n")
    print(f"Datos de la generacion {generacion}: ")

    archivo.write("{:<8} {:<25} {:<15} {:<10} \n".format('Conejo', 'Array', 'Calorias', 'Peso'))
    print("{:<8} {:<25} {:<15} {:<10}".format('Conejo', 'Array', 'Calorias', 'Peso'))

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
        print("{:<8} {:<25} {:<15} {:<10}".format(key, str(value), calorias_total, peso_total))

    archivo.write(f"Mejor de la generacion: {mejor_de_la_generacion} \n")
    print(f"Mejor de la generacion: {mejor_de_la_generacion}")

    #Cruce y mutacion para la nueva generacion
    poblacion = crusar_genes.crusar_genes(alas["1"], alas["2"], alas["3"])
    
    mutar_genes.mutar_genes(poblacion, prob_mutacion)
    
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
    #Hacer la mutacion aleatoria
    # La mutacion invierte el valor de una columna
    #Repetir el proceso
    # imprimir los arreglos de cada generacion para ver resultados
    #
    # for poblacion as conejo
    #      indice = 0
    #      for conejo as caloria
    #          if caloria = 1 
    #              
    #              agarrar valor de caloria y sumarlo