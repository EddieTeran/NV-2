class Agenda:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Inicializando agenda {self.nombre}.")

    def __del__(self):
        print(f" Agenda {self.nombre} borrada.")

# Crear una instancia de la clase
dest1 = Agenda("")

# Eliminar la instancia (esto invocará el destructor)
del dest1
