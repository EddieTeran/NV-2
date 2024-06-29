""" Este programa permite calcular las áreas y perímetros de las 4 figuras geometricas detalladas.
ademas utilizamos identificadores descriptivos snake_case para variables y funciones.

Clase base figura_geometrica:
Esta clase proporciona una estructura común para todas las figuras geométricas.
Define atributos para almacenar información relevante, como lados, apotema, base, altura, área y perímetro.

Clases Heredadas
*Clase pentagono:
Implementa los métodos específicos para calcular el perímetro y el área de un pentágono.

*Clase hexagono
Utiliza la fórmula adecuada para el cálculo.

*Clase trapecio:
Utiliza la fórmula correspondiente para el cálculo.

*Clase paralelogramo:
Utiliza las fórmulas apropiadas para estos cálculos.

Tambien damos uso al bucle while true o "do while para selñeccionar la figura a calcular."""


# Clase base para figuras geométricas
class figura_geometrica:  # Funciones y variables: snake_case
    def __init__(self):
        # Inicializamos atributos para almacenar valores de lado, apotema, base, base mayor, base menor, altura, área y perímetro
        self.lado = None
        self.apotema = None
        self.base = None
        self.base_mayor = None
        self.base_menor = None
        self.altura = None
        self.area = None
        self.perimetro = None

    # Método para calcular perímetro (no implementado en la clase base)
    def calcular_perimetro(self):  # Funciones y variables: snake_case
        pass

    # Método para calcular área (no implementado en la clase base)
    def calcular_area(self):  # Funciones y variables: snake_case e
        pass


# Clase pentágono que hereda de figura_geometrica
class pentagono(figura_geometrica):  # Funciones y variables: snake_case
    def __init__(self):
        super().__init__()  # Llamamos al constructor de la clase base

    # Método para calcular perímetro de un pentágono
    def calcular_perimetro(self):  # Funciones y variables: snake_case
        self.perimetro = self.lado * 5  # Fórmula para calcular perímetro de un pentágono

    # Método para calcular área de un pentágono
    def calcular_area(self):  # Funciones y variables: snake_case
        self.area = self.perimetro * self.apotema / 2  # Fórmula para calcular área de un pentágono


# Clase hexágono que hereda de figura_geometrica
class hexagono(figura_geometrica):  # Funciones y variables: snake_case
    def __init__(self):
        super().__init__()  # Llamamos al constructor de la clase base

    # Método para calcular perímetro de un hexágono
    def calcular_perimetro(self):  # Funciones y variables: snake_case
        self.perimetro = self.lado * 6  # Fórmula para calcular perímetro de un hexágono

    # Método para calcular área de un hexágono
    def calcular_area(self):  # Funciones y variables: snake_case
        self.area = (self.perimetro * self.apotema) / 2  # Fórmula para calcular área de un hexágono


# Clase trapecio que hereda de figura_geometrica
class trapecio(figura_geometrica):  # Funciones y variables: snake_case
    def __init__(self):
        super().__init__()  # Llamamos al constructor de la clase base

    # Método para calcular perímetro de un trapecio
    def calcular_perimetro(self):  # Funciones y variables: snake_case
        self.perimetro = self.base_mayor + self.base_menor + self.lado + self.lado  # Fórmula para calcular perímetro de un trapecio

    # Método para calcular área de un trapecio
    def calcular_area(self):  # Funciones y variables: snake_case
        self.area = (self.base_mayor + self.base_menor) / 2 * self.altura  # Fórmula para calcular área de un trapecio


# Clase paralelogramo que hereda de figura_geometrica
class paralelogramo(figura_geometrica):
    def __init__(self):
        super().__init__()  # Llamamos al constructor de la clase base

    # Método para calcular perímetro de un paralelogramo
    def calcular_perimetro(self):  # snake case
        self.perimetro = 2 * (self.base + self.lado)  # Fórmula para calcular perímetro de un paralelogramo

    # Método para calcular área de un paralelogramo
    def calcular_area(self):  # snake case
        self.area = self.base * self.altura  # Fórmula para calcular área de un paralelogramo


# Función principal
def main():
    while True:
        # Mostramos menú de opciones
        print("1: pentagono")
        print("2: hexagono")
        print("3: trapecio")
        print("4: paralelogramo")
        print("5: salir")
        opcion = int(input("elige una opción: "))

        # Procesamos opción seleccionada
        if opcion == 1:
            figura = pentagono()
            figura.lado = int(input("lado: "))
            figura.apotema = int(input("apotema: "))
            figura.calcular_perimetro()
            figura.calcular_area()
            print("perimetro:", figura.perimetro, "cm2")
            print("area:", figura.area, "cm2")

        elif opcion == 2:
            figura = hexagono()
            figura.lado = int(input("lado: "))
            figura.apotema = int(input("apotema: "))
            figura.calcular_perimetro()
            figura.calcular_area()
            print("perimetro:", figura.perimetro, "cm2")
            print("area:", figura.area, "cm2")

        elif opcion == 3:
            figura = trapecio()
            figura.base_mayor = int(input("base mayor: "))
            figura.base_menor = int(input("base menor: "))
            figura.altura = int(input("altura: "))
            figura.lado = int(input("lado: "))
            figura.calcular_perimetro()
            figura.calcular_area()
            print("perimetro:", figura.perimetro, "cm2")
            print("area:", figura.area, "cm2")

        elif opcion == 4:
            figura = paralelogramo()
            figura.base = int(input("base: "))
            figura.altura = int(input("altura: "))
            figura.lado = int(input("lado: "))
            figura.calcular_perimetro()
            figura.calcular_area()
            print("perimetro:", figura.perimetro, "cm2")
            print("area:", figura.area, "cm2")

        else:
            print("salir")
            break


if __name__ == "__main__":
    main()