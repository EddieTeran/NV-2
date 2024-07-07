"""Definimos la clase padre (Juguetes)
  y dos clases hija (Muñeca y Coche).
  a la clase Juguetes le definimops (nombre y precio) como atributos privados
  y el método jugar que sobrescribe en las clases derivadas.

Polimorfismo lo insertamos en la función (jugar_con_juguete),
 que puede recibir un objeto de cualquier clase que herede de Juguetes
 y un número variable de argumentos adicionales."""

# Clase Padre: Juguetes
class Juguetes:
    def __init__(self, nombre, precio):
        self.__nombre = nombre  # Atributo privado
        self.__precio = precio  # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def jugar(self):
        print("El juguete se puede jugar")

# Clase heredada
class Muñeca(Juguetes):
    def __init__(self, nombre, precio, ropa):
        super().__init__(nombre, precio)  # Llamada al constructor de la clase base
        self.__ropa = ropa  # Atributo privado

    def get_ropa(self):
        return self.__ropa

    def jugar(self):  # Método sobrescrito
        print("La muñeca se puede vestir y jugar")

    def cambiar_ropa(self, nueva_ropa):
        self.__ropa = nueva_ropa
        print(f" Me veo genial con mi {nueva_ropa}")

    def cambiar_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
        print(f"Que bien ahora soy {nuevo_nombre}")

# Clase heredada
class Carro(Juguetes):
    def __init__(self, nombre, precio, velocidad):
        super().__init__(nombre, precio)  # Llamada al constructor de la clase padre
        self.__velocidad = velocidad  # Atributo privado

    def get_velocidad(self):
        return self.__velocidad

    def jugar(self):  # Método sobrescrito
        print("El coche se puede conducir")

    def acelerar(self):
        print(f"El coche acelera a {self.__velocidad} km/h")

# Polimorfismo con argumentos múltiples
def jugar_con_juguete(juguete, *args):
    print(f"Estoy jugando con {juguete.get_nombre()}!")
    if args:
        print(f"Estoy {', '.join(args)} con él")

def crear_muñeca():
    print("vamos a crear tu muñeca")
    nombre = input("Nombre de la muñeca: ")
    precio = float(input("Precio de la muñeca: "))
    ropa = input("Vestimenta de la muñeca: ")
    return Muñeca(nombre, precio, ropa)

def crear_carro():
    nombre = input("Ingrese la marca del auto: ")
    precio = float(input("Precio del auto: "))
    velocidad = int(input("Velocidad del auto: "))
    return Carro(nombre, precio, velocidad)

def jugar_con_muñeca(muñeca):
    print("¿Qué quieres hacer con la muñeca?")
    print("1. Cambiar ropa")
    print("2. Cambiar nombre")
    print("3. Jugar")

    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        nueva_ropa = input("Cuál sera mi look de hoy?: ")
        muñeca.cambiar_ropa(nueva_ropa)

    elif opcion == 2:
        cambiar_nombre = input("como me llamaras?: ")
        muñeca.cambiar_nombre(cambiar_nombre)


    elif opcion == 3:
        muñeca.jugar()

def jugar_con_carro(carro):
    print("¿Qué quieres hacer con el coche?")
    print("1. Acelerar")
    print("2. Jugar")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        carro.acelerar()
    elif opcion == 2:
        carro.jugar()

def main():
    print("Vamos a Jugar!")
    while True:
        print("1. Si")
        print("2. No")

        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print("¿con que quieres jugar?")
            print("1. Muñeca")
            print("2. Carro")
            tipo_juguete = int(input("Ingrese una opción: "))
            if tipo_juguete == 1:
                muñeca = crear_muñeca()
                jugar_con_muñeca(muñeca)
            elif tipo_juguete == 2:
                carro = crear_carro()
                jugar_con_carro(carro)
        elif opcion == 2:
            print("Vuelve Pronto!")
            break

if __name__ == "__main__":
    main()