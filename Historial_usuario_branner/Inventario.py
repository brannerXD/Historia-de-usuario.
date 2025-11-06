#Task2 Entrada de datos (variables en Python)

nombre = input("Ingrese el nombre del producto: ") #aqui se ingresa el nombre del producto

while True: #el while True crea un ciclo infinito hasta que se ingrese un valor valido
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break #el break evita que el ciclo continue si la entrada es valida
    except ValueError: #el except captura el error si la entrada no es un entero
        print("Por favor, ingrese un número entero válido para la cantidad.")

while True: #lo mismo que el anterior pero para el precio jejeje
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido para el precio.")
        
nombre = (nombre, precio, cantidad) #combina las variables para imprimirlas
print(nombre)

#Task3 Operación matemática (costo total):

Costo_total = cantidad * precio #multiplicación sencilla
print("El costo total del inventario es:", Costo_total) #imprime el costo total

#Task4 Mostrar resultados en consola:
print("Resumen del inventario:")
print("Nombre del producto:", nombre) #el 0 muestra la primera letra del nombre
print("Cantidad del producto:", nombre) 
print("Precio del producto:", nombre)
print("Costo total del inventario:", Costo_total) #aqui se imprime con la variable de la task4, para sumar y mostrar todo 


#Task5 Comentarios en el código:
#Los comentarios ya estan incluidos en cada linea del codigo para explicar su funcion, sin embargo, aqui hay un resumen general:

#El usuario puede manejar un inventario basico ingresando el nombre, cantidad y precio de un producto.
#El programa valida que la cantidad sea un entero y el precio un numero decimal.
#Luego calcula el costo total del inventario multiplicando la cantidad por el precio. 
#Finalmente, muestra un resumen del inventario con todos los detalles ingresados y el costo total calculado.
#si en el proceso de ingreso de datos se ingresa un valor invalido, el programa solicita nuevamente la entrada hasta que sea correcta.