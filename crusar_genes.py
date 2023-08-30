def crusar_genes(ala1: list, ala2: list, ala3: list, archivo_log) -> dict:
    nuevo_conejo1 = ala1.copy() 
    nuevo_conejo2 = ala2.copy() 
    nuevo_conejo3 = ala2.copy()
    nuevo_conejo4 = ala3.copy()

    archivo_log.write("-----------VISUALIZAR CRUCE--------------\n")
    archivo_log.write("Generación Padre:\n")
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo1)))
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo2)))
    archivo_log.write("---------------------------------------------\n")
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo3)))
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo4)))

    #Cruce del ala 1 con ala 2
    for i in range(int(len(ala2) / 2), len(ala2)):
        nuevo_conejo1[i] = ala2[i]
        nuevo_conejo2[i] = ala1[i]

    #Cruce del ala 2 con ala 3
    for i in range(int(len(ala2) / 2), len(ala2)):
        nuevo_conejo3[i] = ala3[i]
        nuevo_conejo4[i] = ala2[i]

    archivo_log.write("Generación Hijo:\n")
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo1)))
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo2)))
    archivo_log.write("---------------------------------------------\n")
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo3)))
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo4)))

    return {
        "1": nuevo_conejo1,
        "2": nuevo_conejo2,
        "3": nuevo_conejo3,
        "4": nuevo_conejo4
    }