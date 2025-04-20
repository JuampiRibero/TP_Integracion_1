def convertNumber ():
    numero = int(input("Ingrese un numero entero positivo: "))
    binario = ""
    
    if numero <= 0:
        print("El numero debe ser mayor a 0")
        return

    while(numero > 0) :
        binario = str(numero % 2) + binario
        numero = numero // 2
    
    return binario

print(convertNumber())