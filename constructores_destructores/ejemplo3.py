class Matriz:
    def __init__(self, nombre, fecha): # Constructor de la clase Matriz: Se llama cuando se crea una instancia.
        self.nombre = nombre # Inicializa los atributos
        self.fecha = fecha
        print(f"Inicializando Clase matriz {self.fecha}.")

class Sucursal1(Matriz): # Llamada al constructor de la superclase (Matriz)
    def __init__(self, nombre, fecha, codigo, ciudad): # Inicializa los atributos adicionales 'codigo' y 'ciudad'.
        super().__init__(nombre, fecha)
        self.codigo = codigo
        self.ciudad = ciudad
        print(f"Inicializando subclase {self.nombre}.")

    def __del__(self): # Destructor de la subclase: Se llama cuando una instancia está a punto de ser destruida.
        print(f"Subclase {self.nombre} borrada.")


dest3 = Sucursal1("", "","","") # Crear una instancia de la subclase Sucursal1
del dest3 # Eliminar la instancia (esto invocará el destructor)
