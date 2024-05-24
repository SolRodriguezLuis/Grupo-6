control = True

while control:
    numero = int(input("Ingrese un numero: "))

    if numero > 0:
        palabra_frase = input("Ingrese una palabra o frase: ")
    else:
        print("El número debe ser mayor que 0. El programa ha finalizado.")
        break
    
    num_caracteres = 0
    for _ in palabra_frase:
        num_caracteres += 1

    print(f"La palabra o frase tiene {num_caracteres} caracteres.")

    factorial = 1
    for i in range(1, num_caracteres + 1):
        factorial *= i

    print(f"El factorial del número de caracteres es: {factorial}")

    if factorial % 2 == 0:
        print("El resultado es par.")
    else:
        print("El resultado es impar.")
