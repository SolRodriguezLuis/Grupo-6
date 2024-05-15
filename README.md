# Grupo-6
Clase Practica I (Clase 8) Python Inicial 


# sol_rodriguezluis@hotmail.com - Sol Rodriguez Luis 	
# - Florencia Zeoli	
# - Mailen Filippone	
# - Karen Andrea Basualdo	
# - Marielis Bozo	

import random
numero_secreto =random.randint(1,50)
intentos = 0

print("Bienvenido al juego de adivinanzas. Adivina el numero que estoy pensando entre 1 y 50, tenes 5 intentos")

n = int(input("Adivine el numero entre 1 y 50 " ))

while n!= numero_secreto and intentos <= 5:
    n = int(input("Adivine el numero entre 1 y 50 " ))
    intentos+=1
    if n == numero_secreto:
        print("Adivinaste! Ganaste el juego")
    elif n > numero_secreto:
        print("El numero secreto es mas chico")    
    else:
        print("El numero secreto es mas grande") 
print(f"Perdiste! El numero secreto era {numero_secreto}")
input()
