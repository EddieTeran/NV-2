import os  # importamos el inventario desde el archivo txt

class Caprichos:   #Definimos la clase
    def __init__(self, sap, nombre, cantidad, precio): # Constructor que inicia los atributos
        self.sap = sap
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

#Metodos getter para obtener atributos
    def get_sap(self):
        return self.sap

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

#Definimos clase inventario
class Inventario:
    def __init__(self):
        self.productos = []
                             # DEFINIMOS LOS METODOS
    def agregar_producto(self, sap, nombre, cantidad, precio): #Metodo agregar
        self.productos.append(Caprichos(sap, nombre, cantidad, precio))

    def eliminar_producto(self, sap): # Metodo eliminar
        for producto in self.productos:
            if producto.get_sap() == sap:
                self.productos.remove(producto)
                print("Producto eliminado con éxito.")
                return
        print("No se encontró el producto con el SAP especificado.")

    def actualizar_producto(self, sap, cantidad=None, precio=None):#Metodo actualizar
        for producto in self.productos:
            if producto.get_sap() == sap:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print("Producto actualizado con éxito.")
                return
        print("No se encontró el producto con el SAP especificado.")

    def buscar_producto(self, nombre): #Metodo buscar
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_productos(self): #Metodo mostrar
        for producto in self.productos:
            print(f"Sap: {producto.get_sap()}")
            print(f"Nombre: {producto.get_nombre()}")
            print(f"Cantidad: {producto.get_cantidad()}")
            print(f"Precio: {producto.get_precio()}")
            print("")

    def guardar_inventario(self, inventario): #Metodo guardar
        with open(inventario, "w") as f:
            for producto in self.productos:
                f.write(f"{producto.get_sap()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")

    def importar_inventario(self, inventario): #Metodo importar
        if os.path.exists(inventario):
            with open(inventario, "r") as f:
                for linea in f:
                    sap, nombre, cantidad, precio = linea.strip().split(",")
                    self.agregar_producto(int(sap), nombre, int(cantidad), float(precio))
        else:
            print("El archivo no existe.")

# Definimos la funcion que ejecuta el programa
def main():
    inventario = Inventario()

    # Importar inventario desde archivo
    inventario.importar_inventario("inventario.txt")
# Bucle de acceso al menu.
    while True:
        print("Menú:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar productos")
        print("6. Guardar inventario")
        print("7. Importar inventario")
        print("8. Salir")
# Interantuamos con el usuario
        opcion = input("Ingrese una opción: ")
# Ejecutamos las opciones
        if opcion == "1": # Agregar Producto
            sap = int(input("Ingrese el Sap del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            inventario.agregar_producto(sap, nombre, cantidad, precio)

        elif opcion == "2": #Eliminar producto
            sap = int(input("Ingrese el Sap del producto que desea eliminar: "))
            inventario.eliminar_producto(sap)

        elif opcion == "3": #Actualizar producto
            sap = int(input("Ingrese el Sap del producto que desea actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            if cantidad != "":
                cantidad = int(cantidad)
            else:
                cantidad = None
            if precio != "":
                precio = float(precio)
            else:
                precio = None
            inventario.actualizar_producto(sap, cantidad, precio)

        elif opcion == "4": # Buscar Producto
            nombre = input("Ingrese el nombre del producto que desea buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if len(resultados) == 0:
                print("No se encontraron productos con el nombre especificado.")
            else:
                for producto in resultados:
                    print(f"Sap: {producto.get_sap()}")
                    print(f"Nombre: {producto.get_nombre()}")
                    print(f"Cantidad: {producto.get_cantidad()}")
                    print(f"Precio: {producto.get_precio()}")
                    print("")

        elif opcion == "5":#Mostrar producto
            inventario.mostrar_productos()

        elif opcion == "6": #Guardar inventario
            inventario.guardar_inventario("inventario.txt")
            print("Inventario guardado con éxito.")

        elif opcion == "7":#Importar inventario
            inventario.importar_inventario("inventario.txt")
            print("Inventario importado con éxito.")

        elif opcion == "8": #Salir del programa
            print("Saliendo del programa.")
            break #Salimos del bucle

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()