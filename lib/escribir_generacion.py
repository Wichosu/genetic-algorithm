def escribir_generacion(
    archivo,
    generacion: int,
    poblacion: dict,
    cal: list,
    peso: list, 
    promedios: dict,
    arn_resultante: dict
) -> None:
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

    #Encabezado de la generacion
    archivo.write(f"Datos de la generacion {generacion}:\n")
    archivo.write("{:<8} {:<25} {:<15} {:<10} \n".format('Conejo', 'Array', 'Calorias', 'Peso'))

    #Imprimir resultados de fitness de cada conejo
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

    #Obtener llave de conejo con mejor promedio
    mejor_de_la_generacion["key"] = list(promedios.keys())[0]
    segundo_mejor["key"] = list(promedios.keys())[1]
    tercer_mejor["key"] = list(promedios.keys())[2]

    #Obtener valor/lista de conejo con mejor promedio
    mejor_de_la_generacion["promedio"] = list(promedios.values())[0]
    segundo_mejor["promedio"] = list(promedios.values())[1]
    tercer_mejor["promedio"] = list(promedios.values())[2]

    mejor_de_la_generacion["value"] = arn_resultante["1"]
    segundo_mejor["value"] = arn_resultante["2"]
    tercer_mejor["value"] = arn_resultante["3"]

    archivo.write(f"Mejor de la generacion: {mejor_de_la_generacion} \n")
    archivo.write(f"Segundo de la generacion: {segundo_mejor} \n")
    archivo.write(f"Tercero de la generacion: {tercer_mejor} \n")
