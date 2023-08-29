import random
import producto
# definir los parámetros del algoritmo genético

tam_poblacion = 4

prob_mutacion = 0.1  #10% de probabilidad como prueba

generaciones = 50 #Número de generaciones a probar


# definir la capacidad de la mochila

lim_cal = 1200

lim_peso = 2


# definir la lista de pesos y calorías de los productos
productos = [
    producto.Producto("Coca Cola", 500, 0.7),
    producto.Producto("Pan", 300, 0.2),
    producto.Producto("Atún", 250, 0.8),
    producto.Producto("Agua", 20, 0.2),
    producto.Producto("Chocolate", 200, 0.6),
    producto.Producto("Papitas", 500, 0.9),
    producto.Producto("Fruta", 180, 0.6),
    producto.Producto("Palomitas", 400, 0.6)
]

#cal = [500, 300, 250, 20, 200, 500, 180, 400]

#peso = [0.7, 0.2, 0.8, 0.2, 0.6, 0.9, 0.6, 0.6]

#lista_prod = pd.DataFrame ({"Cal":cal, "Peso":peso},index=["Coca-cola", "Pan", "Atún", "Agua", 
# "Chocolate", "Papitas", "Fruta", "Palomitas"])


#Definir población inicial de conejitos

conejito1 = [1, 1, 1, 1, 1, 0, 1, 0]

conejito2 = [0, 1, 0, 0, 1, 1, 0, 1]

conejito3 = [1, 0, 0, 1, 0, 0, 0, 1]

conejito4 = [0, 1, 1, 0, 1, 1, 0, 1]


# crear una población inicial aleatoria

#poblacion = [random.choices([0, 1], k=len(peso)) for i in range(tam_poblacion)]

#poblacion fija para pruebas
poblacion = [conejito1, conejito2, conejito3, conejito4]

#array para comparar fitness
#la posicion de conejos va conectada con los indices del array 
fitness_calorias = []
fitness_peso = []

for conejo in poblacion:
    indice = 0
    calorias_total = 0
    peso_total = 0

    for producto in conejo:
        if producto:
            calorias_total += cal[indice]
            peso_total += peso[indice]
        indice += 1
    fitness_calorias.append(calorias_total)
    fitness_peso.append(peso_total)


fitness_peso.sort()
fitness_calorias.sort()
print(fitness_peso)
print(fitness_calorias)

#Pseudocodigo
# Obtener total de calorias y peso DONE
# Comparar total de cada conejo con los parametros establecidos DOING
# Catalogar los conejos segun el que se haya acercada mas a los parametros
# Hacer la seleccion fitness ej:
# 1 n n n n n n n n
# 2 n n n n n n n n
# -----------------
# 2 n n n n n n n n
# 3 n n n n n n n n
# Hacer el cruce a la seleccion
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