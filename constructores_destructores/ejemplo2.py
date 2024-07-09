class Auto:
    def __init__(self, nombre): # Constructor: Se llama cuando se crea una instancia de la clase.
        self.nombre = nombre  # Inicializa los atributos del objeto
        print(f" Inicializando clase Auto {self.nombre}.")

    def __del__(self): # Destructor: Se llama cuando una instancia está a punto de ser destruida.
        print(f" Clase {self.nombre} borrada.")

dest2 = Auto("") # Crear una instancia de la clase
del  dest2

              