def obtener_arn(poblacion: dict, promedios: dict) -> dict:
    #arn de genes, la mejor el indice 0 y la peor indice 3
    arn = {
        "1": [],
        "2": [],
        "3": []
    } 
    
    key_arn = 1
    #Asignar a ramas o arn para hacer el cruce
    for mejor in promedios.items():
        if key_arn >= 4:
            break
    
        arn.update({str(key_arn): poblacion[mejor[0]]})
        key_arn += 1

    return arn
