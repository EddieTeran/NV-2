class Auto:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f" Inicializando clase Auto {self.nombre}.")

    def __del__(self):
        print(f" Clase {self.nombre} borrada.")

dest2 = Auto("")
del  dest2

              