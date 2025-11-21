inventario = [] 

from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscador_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas
)

from archivos import guardar_csv, cargar_csv

def mostrar_menu(inventario):#por ultimo, esta función muestra el menú principal
    while True:
        print ("==================================")
        print ("= Bienvenido a inventarios Branner =")
        print ("==================================")
        print ("Selecciona una opción:")
        opcion = (input("1. Agregar Producto\n2. Mostrar Inventario\n3. Buscar\n4. Actualizar\n5. Eliminar\n6. Calcular Estadisticas\n7. Guardar CSV\n8. Cargar CSV\n9. Salir\n"))
        if opcion == "1":  
            print("Redirigiendo al control de productos...")
            agregar_producto(inventario)#llama a la función para agregar 
        elif opcion == "2":
            print("Redirigiendo al inventario...")
            mostrar_inventario(inventario)#llama a la función que deja ver el inventario
        elif opcion == "3":
            print("Abriendo Buscador...")
            buscador_producto(inventario)#llama a la función que busca productos
        elif opcion == "4":
            print("Actualizar Inventario Listo...")
            actualizar_producto(inventario)
        elif opcion == "5":
            print("Administrador activado...")
            eliminar_producto(inventario)
        elif opcion == "6":
            print("Abriendo Estadisticas...")
            calcular_estadisticas(inventario)#llama a la función que hace las estadísticas
        elif opcion == "7":
            print("Guarda tu CSV...")
            guardar_csv(inventario, 'inventario.csv')
        elif opcion == "8":
            print("Carga tu CSV...")
        elif opcion == "9":
            cargar_csv(inventario, 'inventario.csv')
            print("Saliendo del menú...")
            exit()
        else:
            print ("Opción inválida. Por favor ingresa una opción válida: ") 

mostrar_menu(inventario) #el menu lo puse abajo para que agarre todas las funciones :)