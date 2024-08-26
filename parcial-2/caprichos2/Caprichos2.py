class Caprichos:
    def __init__(self, sap, nombre, cantidad, precio):
        # Inicializa un objeto Caprichos con sus atributos
        self.sap = sap
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Devuelve una representación de cadena del objeto Caprichos
        return f"SAP: {self.sap}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def get_sap(self):
        # Devuelve el SAP del producto
        return self.sap

    def get_nombre(self):
        # Devuelve el nombre del producto
        return self.nombre

    def get_cantidad(self):
        # Devuelve la cantidad del producto
        return self.cantidad

    def get_precio(self):
        # Devuelve el precio del producto
        return self.precio

    def set_cantidad(self, cantidad):
        # Establece una nueva cantidad para el producto
        self.cantidad = cantidad

    def set_precio(self, precio):
        # Establece un nuevo precio para el producto
        self.precio = precio
class Inventario:
    def __init__(self, archivo_inventario):
        # Inicializa un objeto Inventario con un archivo de inventario
        self.productos = []
        self.archivo_inventario = archivo_inventario
        self.cargar_inventario_desde_archivo()

    def agregar_producto(self, capricho):
        # Agrega un nuevo producto al inventario
        for c in self.productos:
            if c.get_sap() == capricho.get_sap():
                print("Error: El SAP del capricho ya existe.")
                return
        self.productos.append(capricho)
        self.guardar_inventario_en_archivo()
        print("Producto agregado con éxito.")

    def eliminar_producto(self, sap):
        # Elimina un producto del inventario por su SAP
        for c in self.productos:
            if c.get_sap() == sap:
                self.productos.remove(c)
                self.guardar_inventario_en_archivo()
                print("producto eliminado con éxito.")
                return
        print("Error: No se encontró el producto con el SAP especificado.")

    def actualizar_producto(self, sap, cantidad=None, precio=None):
        # Actualiza un producto del inventario por su SAP
        for c in self.productos:
            if c.get_sap() == sap:
                if cantidad is not None:
                    c.set_cantidad(cantidad)
                if precio is not None:
                    c.set_precio(precio)
                self.guardar_inventario_en_archivo()
                print("Producto actualizado con éxito.")
                return
        print("Error: No se encontró el producto con el SAP especificado.")

    def buscar_producto(self, nombre):
        # Busca productos en el inventario por nombre
        resultados = [c for c in self.productos if nombre.lower() in c.get_nombre().lower()]
        if resultados:
            for c in resultados:
                print(c)
        else:
            print("No se encontraron productos con el nombre especificado.")

    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario
        for c in self.productos:
            print(c)

    def cargar_inventario_desde_archivo(self):
        # Carga el inventario desde un archivo de texto
        try:
            with open(self.archivo_inventario, 'r') as f:
                for linea in f:
                    sap, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos.append(Caprichos(int(sap), nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            print("No se encontró el archivo de inventario. Creando uno nuevo...")
            with open(self.archivo_inventario, 'w') as f:
                pass
        except PermissionError:
            print("Error: No se tiene permiso para leer el archivo de inventario.")

    def guardar_inventario_en_archivo(self):
        # Guarda el inventario en un archivo de texto
        try:
            with open(self.archivo_inventario, 'w') as f:
                for c in self.productos:
                    f.write(f"{c.get_sap()},{c.get_nombre()},{c.get_cantidad()},{c.get_precio()}\n")
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo de inventario.")
def main():
    # Inicializa el archivo de inventario y crea un objeto Inventario
    archivo_inventario = 'inventario.txt'
    inventario = Inventario(archivo_inventario)

    while True:
        # Muestra el menú de opciones
        print("\nMenú de Inventario:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar producto")
        print("6. Salir")

        # Pide al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agrega un nuevo producto al inventario
            sap = int(input("Ingrese el SAP del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            capricho = Caprichos(sap, nombre, cantidad, precio)
            inventario.agregar_producto(capricho)

        elif opcion == "2":
            # Elimina un producto del inventario por su SAP
            sap = int(input("Ingrese el SAP del producto a eliminar: "))
            inventario.eliminar_producto(sap)

        elif opcion == "3":
            # Actualiza un producto del inventario por su SAP
            sap = int(input("Ingrese el SAP del producto a actualizar: "))
            cantidad = int(input("Ingrese la nueva cantidad (opcional): ") or None)
            precio = float(input("Ingrese el nuevo precio (opcional): ") or None)
            inventario.actualizar_producto(sap, cantidad, precio)

        elif opcion == "4":
            # Busca productos en el inventario por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            # Muestra todos los productos en el inventario
            inventario.mostrar_inventario()

        elif opcion == "6":
            # Sale del programa
            print("Saliendo del sistema...")
            break

        else:
            # Opción inválida
            print("Opción inválida. Intente nuevamente.")
if __name__ == "__main__":
    main()