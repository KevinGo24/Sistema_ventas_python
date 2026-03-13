# Crear un Diccionario vacio para almacenar datos  ( Productos )
productos = {}
total_general = 0


def ventas():
    global total_general
    continuar = "si"
    while continuar == "si":
        print("-"*50)
        print("Bienvenido a Nuestro sistema de Ventas")
        print("-"*50)
        Nombre_producto = str(input('Ingresar nombre de producto:  '))
        # condicional para saber si el usuario ingresa un numero y en caso que si mandar mensaje 
        if Nombre_producto.isnumeric():
            print('Ingresa un nombre de producto valido')
            continue
        # Condiconal para que el usario no ingrese un numero menor a 0 o igual ( PRECIO )
        Precio = float(input('Ingrese el precio del producto: '))
        if Precio <= 0:
            print('El Precio debe ser mayor a 0')
            continue
        # Condiconal para que el usario no ingrese un numero menor a 0 o igual ( CANTIDAD )
        Cantidad = int(input('Cuanto desea llevarse:  '))
        if Cantidad <= 0:
            print('La Cantidad debe ser mayor a 0 ')
            continue
        costo_total = Precio * Cantidad 
        productos[Nombre_producto] = {
            "cantidad": Cantidad, 
            "total": costo_total
        }
        print("-"*50)
        continuar = input('Desea seguir con la compra y/n: ')
        print("-"*50)

        print("\n--- RESUMEN DE VENTAS DEL DÍA ----")

        for producto, datos in productos.items():
            print("-"*50)
            print("Producto:", producto)
            print("Total por producto:", datos["total"])
            print("Cantidad total vendida:", datos["cantidad"])
            print("-"*50)
        print("-"*50)
        print("TOTAL GENERAL RECAUDADO:", costo_total)
        print("-"*50)