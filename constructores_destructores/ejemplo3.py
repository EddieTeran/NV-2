class Matriz:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        print(f"Inicializando Clase matriz {self.fecha}.")

class Sucursal1(Matriz):
    def __init__(self, nombre, fecha, codigo, ciudad):
        super().__init__(nombre, fecha)
        self.codigo = codigo
        self.ciudad = ciudad
        print(f"Inicializando subclase {self.nombre}.")

    def __del__(self):
        print(f"Subclase {self.nombre} borrada.")


dest3 = Sucursal1("", "","","")
del dest3
