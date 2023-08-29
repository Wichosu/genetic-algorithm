def crusar_genes(ala1: list, ala2: list, ala3: list) -> dict:
    print(ala1)
    nuevo_conejo1 = ala1.copy() 
    nuevo_conejo2 = ala2.copy() 
    nuevo_conejo3 = ala2.copy()
    nuevo_conejo4 = ala3.copy()

    #Cruce del ala 1 con ala 2
    for i in range(int(len(ala2) / 2), len(ala2)):
        nuevo_conejo1[i] = ala2[i]
        nuevo_conejo2[i] = ala1[i]

    #Cruce del ala 2 con ala 3
    for i in range(int(len(ala2) / 2), len(ala2)):
        nuevo_conejo3[i] = ala3[i]
        nuevo_conejo4[i] = ala2[i]

    return {
        "1": nuevo_conejo1,
        "2": nuevo_conejo2,
        "3": nuevo_conejo3,
        "4": nuevo_conejo4
    }