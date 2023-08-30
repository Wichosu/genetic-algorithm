def crusar_genes(arn1: list, arn2: list, arn3: list, archivo_log) -> dict:
    nuevo_conejo1 = arn1.copy() 
    nuevo_conejo2 = arn2.copy() 
    nuevo_conejo3 = arn2.copy()
    nuevo_conejo4 = arn3.copy()

    archivo_log.write("-----------VISUALIZAR CRUCE--------------\n")
    archivo_log.write("Generación Padre:\n")
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo1)))
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo2)))
    archivo_log.write("---------------------------------------------\n")
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo3)))
    archivo_log.write("{:<25} \n".format(str(nuevo_conejo4)))

    #Cruce del arn 1 con arn 2
    for i in range(int(len(arn2) / 2), len(arn2)):
        nuevo_conejo1[i] = arn2[i]
        nuevo_conejo2[i] = arn1[i]

    #Cruce del arn 2 con arn 3
    for i in range(int(len(arn2) / 2), len(arn2)):
        nuevo_conejo3[i] = arn3[i]
        nuevo_conejo4[i] = arn2[i]

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