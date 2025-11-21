def agregar_producto(inventario): # Función para agregar un producto al inventario
    inv = {"nombre": "", "cantidad": 0, "precio": 0.0}
    inv["nombre"] = input("Ingrese el nombre del producto: ")
    while True:#este bucle valida que la cantidad sea un entero
        try:
            inv["cantidad"] = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad.")
    while True:#esre otro bucle valida que el precio sea un decimal
        try:
            inv["precio"] = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un precio válido.")
    inventario.append(inv)#esto es para agregar el diccionario inv a la lista inventario (inv es abreviatura de inventario)
    print(f"Producto {inv['nombre']} agregado al inventario.")

def mostrar_inventario(inventario):#esta función muestra el inventario
    if len (inventario) == 0:#esto es un condicional que verifica si el inventario está vacío
        print("El inventario está vacío.")
    if len (inventario) > 0:
        print("Inventario de productos:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']:.2f}")#estra linea imprime el nombre, cantidad y precio de cada producto en el inventario
    input("Presiona Enter para volver al menú principal...")

def calcular_estadisticas(inventario): #esta función calcula estadísticas del inventario
    if len (inventario) == 0:
        print("El inventario está vacío. No se pueden calcular estadísticas.")
        return
    precio = sum(producto['precio'] * producto['cantidad'] for producto in inventario) #opera el precio por la cantidad de cada producto y lo suma
    cantidad = sum(producto['cantidad'] for producto in inventario) #opramos la cantidad de cada producto y lo sumamos
    valor_total_inventario = precio#aqui se asigna el valor total del inventario
    print(f"Cantidad total de productos en inventario: {cantidad}")#deja ver la cantidad total de productos
    print(f"Valor total del inventario: ${valor_total_inventario:.2f}")#deja ver el valor total del inventario
    input("Presiona Enter para volver al menú principal...")

def buscador_producto(inventario):
    if len (inventario) == 0:
        print("El inventario está vacío. No se pueden buscar productos.")
        return
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").lower()
    encontrados = [producto for producto in inventario if producto['nombre'].lower() == nombre_buscar]
    if encontrados:
        for producto in encontrados:
            print(f"Producto encontrado: Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']:.2f}")
            return producto
    else:
        print("Producto no encontrado en el inventario.")
    input("Presiona Enter para volver al menú principal...")

def actualizar_producto(inventario):
    producto = buscador_producto(inventario)
    if producto:
        while True:
            try:
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {producto['nombre']}: "))
                producto['cantidad'] = nueva_cantidad
                print(f"Cantidad actualizada para {producto['nombre']}.")
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido para la cantidad.")
    while True:
        try:
            nuevo_precio = float(input(f"Ingrese el nuevo precio para {producto['nombre']}: "))
            producto['precio'] = nuevo_precio
            print(f"Precio actualizado para {producto['nombre']}.")
            break
        except ValueError:
            print("Por favor, ingrese un precio válido.")
    input("Presiona Enter para volver al menú principal...")

def eliminar_producto(inventario):
    producto = buscador_producto(inventario)
    while True:
        try:
            inventario.remove(producto)
            print(f"Producto {producto['nombre']} eliminado del inventario.")
            break
        except ValueError:
            print("Producto no encontrado en el inventario.")
    input("Presiona Enter para volver al menú principal...")