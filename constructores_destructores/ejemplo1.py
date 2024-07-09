class Agenda:

    def __init__(self, nombre): # Constructor: Se llama cuando se crea una instancia de la clase.
        self.nombre = nombre # Inicializa los atributos del objeto.
        print(f"Inicializando agenda {self.nombre}.")

    def __del__(self):# Destructor: Se llama cuando una instancia está a punto de ser destruida.
        print(f" Agenda {self.nombre} destruida.")

# Crear una instancia de la clase
dest1 = Agenda("")  # Crear una instancia de la clase

# Eliminar la instancia (esto invocará el destructor)
del dest1
