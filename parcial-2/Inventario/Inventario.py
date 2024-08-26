# Importamos las bibliotecas
import json
import os

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        # Inicializamos los atributos
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Método especial para representar el objeto como una cadena
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def get_id(self):
        # Método para obtener el ID del producto
        return self.id

    def get_nombre(self):
        # Método para obtener el nombre del producto
        return self.nombre

    def get_cantidad(self):
        # Método para obtener la cantidad del producto
        return self.cantidad

    def get_precio(self):
        # Método para obtener el precio del producto
        return self.precio

    def set_cantidad(self, cantidad):
        # Método para establecer la cantidad del producto
        self.cantidad = cantidad

    def set_precio(self, precio):
        # Método para establecer el precio del producto
        self.precio = precio


# Definimos la clase Inventario:
class Inventario:
    def __init__(self):
        # Inicializamos el inventario como un diccionario vacío
        self.productos = {}

    def agregar_producto(self, producto):
        # Método para agregar un producto al inventario
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        # Método para eliminar un producto del inventario por ID
        if id in self.productos:
            del self.productos[id]
        else:
            print("No se encontró el producto con el ID especificado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        # Método para actualizar la cantidad o precio de un producto
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)
        else:
            print("No se encontró el producto con el ID especificado.")

    def buscar_producto(self, nombre):
        # Método para buscar productos por nombre
        resultados = [producto for producto in self.productos.values() if producto.get_nombre().lower() == nombre.lower()]
        return resultados

    def mostrar_productos(self):
        # Método para mostrar todos los productos en el inventario
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        # Método para guardar el inventario en un archivo JSON
        datos = []
        for producto in self.productos.values():
            datos.append({
                "id": producto.get_id(),
                "nombre": producto.get_nombre(),
                "cantidad": producto.get_cantidad(),
                "precio": producto.get_precio()
            })
        with open(archivo, "w") as f:
            json.dump(datos, f)

    def cargar_inventario(self, archivo):
        # Método para cargar el inventario desde un archivo JSON
        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                datos = json.load(f)
                for producto in datos:
                    self.agregar_producto(Producto(producto["id"], producto["nombre"], producto["cantidad"], producto["precio"]))
        else:
            print("No se encontró el archivo de inventario.")


# Definimos la función main
def main():
    inventario = Inventario()
    archivo_inventario = "inventario.json"
# Definimos un bucle para interactuar con el usuario
    while True:
        print("\nMenú de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            inventario.agregar_producto(Producto(id, nombre, cantidad, precio))
        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            precio = float(input("Ingrese el nuevo precio del producto: "))
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con el nombre especificado.")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            inventario.guardar_inventario(archivo_inventario)
            print("Inventario guardado con éxito.")
        elif opcion == "7":
            inventario.cargar_inventario(archivo_inventario)
            print("Inventario cargado con éxito.")
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()