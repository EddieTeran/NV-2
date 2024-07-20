class Producto:
    def __init__(self, nombre, precio):
        # Inicializamos los atributos de la clase Producto
        self.nombre = nombre  # Encapsulamos el nombre
        self.precio = precio  # Encapsulamos el precio

    def __str__(self):
        # Representamos el objeto como una cadena
        return f"{self.nombre}: ${self.precio:.2f}"

class Caprichos:
    def __init__(self):
        # Inicializamos los atributos de la clase Caprichos
        self.productos = [
            Producto("Blusa", 32),
            Producto("Pantalon", 45),
            Producto("Camisas", 29),
            Producto("Brasier", 28),
            Producto("Medias", 8.20),
            Producto("zapatos",35.50),
        ]
        self.carrito = []

    def mostrar_productos(self):
        # Mostramos la lista de productos disponibles
        print("Artículos Caprichos Store")
        for i, producto in enumerate(self.productos):
            print(f"{i+1}.- {producto}")


    def agregar_producto(self, producto, cantidad):
        # Agregamos un producto al carrito
        sub_total = producto.precio * cantidad
        self.carrito.append({"producto": producto, "cantidad": cantidad, "sub_total": sub_total})
        print(f"Mostrar el total de su compra precione 7")
    def calcular_total(self):
        # Calculamos el total
        total = sum(item["sub_total"] for item in self.carrito)
        return total

    def aplicar_descuento(self, total):
        # Aplicamos un descuento del 10% al total
        descuento = total * 0.10
        return total - descuento

    def imprimir_factura(self):
        # Imprimimos la factura
        print("Lista de artículos seleccionados")
        for item in self.carrito:
            print(f"{item['producto'].nombre}: {item['cantidad']} x ${item['producto'].precio:.2f} = ${item['sub_total']:.2f}")
        total = self.calcular_total()
        print(f"Total sin descuento: ${total:.2f}")
        total_con_descuento = self.aplicar_descuento(total)
        print(f"Descuento 10%: ${total * 0.10:.2f}")
        print(f"Total a pagar: ${total_con_descuento:.2f}")
        print("""***GRACIAS POR PREFERIR 
      CAPRICHOS STORE***""")

def main():
    # Creamos una instancia de la clase Tienda
    tienda = Caprichos()
    # Mientras el usuario no seleccione la opción 7
    while True:
        # Mostramos los productos disponibles
        tienda.mostrar_productos()
        # Pedimos al usuario que seleccione un producto
        opcion = int(input("Seleccione el producto: "))
        # Si el usuario selecciona la opción 7, salimos del bucle
        if opcion == 7:
            break
        # Seleccionamos el producto correspondiente a la opción seleccionada
        producto = tienda.productos[opcion - 1]
        # Pedimos al usuario que ingrese la cantidad del producto que desea
        cantidad = int(input(f"Cuantos {producto.nombre} desea? "))
        # Agregamos el producto al carrito
        tienda.agregar_producto(producto, cantidad)
    # Imprimimos la factura
    tienda.imprimir_factura()

# Si el módulo se está ejecutando directamente
if __name__ == "__main__":
    main()