# Definimos una función llamada convertNumber
def convertirNumero (numero):
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
    return binario


# Definimos una función llamada operaciones
# Esta función realiza operaciones aritméticas con dos números enteros
def operaciones():
    # Solicitamos al usuario que ingrese dos números enteros
    numero1 = int(input("Ingrese el primer numero entero: "))
    numero2 = int(input("Ingrese el segundo numero entero: "))
    
    # Verificamos que los números ingresados sean mayores que 0
    # Si alguno de los números es menor o igual a 0, mostramos un mensaje de error y salimos de la función
    if(numero1 <= 0 or numero2 <= 0):
        print("Los numeros deben ser mayores a 0")
        return
    
    # Verificamos que el primer número sea mayor que el segundo para evitar errores en las operaciones
    if(numero1 < numero2):
        print("Error: El primer numero debe ser mayor que el segundo")
        return

    # Realizamos las operaciones aritméticas y guardamos los resultados
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 // numero2 
    
    # Mostramos los numeros ingresados y sus conversiones a binario
    print(f"El numero {numero1} en binario es {convertirNumero(numero1)}")
    print(f"El numero {numero2} en binario es {convertirNumero(numero2)}")
    
    # Mostramos los resultados de las operaciones
    print(f"La suma de {numero1} y {numero2} en binario es {convertirNumero(suma)}")
    print(f"La resta de {numero1} y {numero2} es {convertirNumero(resta)}")
    print(f"La multiplicacion de {numero1} y {numero2} es {convertirNumero(multiplicacion)}")
    print(f"La division de {numero1} y {numero2} es {convertirNumero(division)}")

# Llamamos a la función de operaciones
operaciones()