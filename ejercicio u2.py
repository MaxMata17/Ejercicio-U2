class InventarioTienda:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0:
            print("El precio debe ser positivo.")
            return

        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:

            if producto["nombre"].lower() == nombre.lower():

                if cantidad <= 0:
                    print("La cantidad debe ser positiva.")
                    return

                if cantidad > producto["cantidad"]:
                    print("No hay suficiente stock.")
                    return

                producto["cantidad"] -= cantidad
                print("Venta realizada correctamente.")
                return

        print("El producto no existe.")

    def mostrar_inventario(self):
        print("\n INVENTARIO")

        if len(self.productos) == 0:
            print("El inventario está vacío.")
            return

        for producto in self.productos:
            print("Nombre:", producto["nombre"])
            print("Precio:", producto["precio"])
            print("Cantidad:", producto["cantidad"])


    def producto_mas_caro(self):
        if len(self.productos) == 0:
            print("El inventario está vacío.")
            return

        producto_caro = self.productos[0]

        for producto in self.productos:
            if producto["precio"] > producto_caro["precio"]:
                producto_caro = producto

        return producto_caro["nombre"], producto_caro["precio"]


tienda = InventarioTienda("Mi Tienda")

opcion = 0

while opcion != 5:

    print("\n MENU")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Ver inventario")
    print("4. Consultar producto mas caro")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:

        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        tienda.agregar_producto(nombre, precio, cantidad)

    elif opcion == 2:

        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad a vender: "))

        tienda.vender_producto(nombre, cantidad)

    elif opcion == 3:

        tienda.mostrar_inventario()

    elif opcion == 4:

        resultado = tienda.producto_mas_caro()

        if resultado:
            nombre, precio = resultado
            print("Producto más caro:", nombre)
            print("Precio:", precio)

    elif opcion == 5:

        print("bye.")

    else:
        print("Opción invalida.")
