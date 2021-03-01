import math
def decomposition (nombre):

    
    tableau = []

    
    while nombre % 2 == 0:

        
        tableau.append(2)
        
        nombre = nombre / 2
    

    for i in range(3, int(math.sqrt(nombre)) + 1, 2):
        
        while nombre % i == 0:
            tableau.append(int(i))
            nombre = nombre / i


    
    if nombre > 2:
        tableau.append(int(nombre))

    return tableau


print(decomposition(int(input("Veuillez saisir un nombre: "))))
