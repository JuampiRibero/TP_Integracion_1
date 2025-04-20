# Definimos una función llamada convertNumber
def convertirNumero ():
    # Solicitamos al usuario que ingrese un número entero positivo
    numero = int(input("Ingrese un numero entero positivo: "))
    
    # Guardamos el número original para usarlo después en el mensaje
    numero_original = numero
    
    # Inicializamos una variable para guardar el número binario como cadena
    binario = ""
    
    # Verificamos que el número ingresado sea mayor que 0
    if numero <= 0:
        print("El numero debe ser mayor a 0")
        return # Salimos de la función si el número no es válido

    # Mientras el número sea mayor que 0
    while(numero > 0) :
        # Obtenemos el residuo de dividir el número por 2 (0 o 1) y lo añadimos al principio de la cadena binaria
        binario = str(numero % 2) + binario
        # Actualizamos el número dividiéndolo por 2 y descartando el decimal
        numero = numero // 2
    
    # Mostramos el mensaje con la conversión
    print(f"El número {numero_original} en base 10 es igual a {binario} en base 2")

# Llamamos a la función
convertirNumero()