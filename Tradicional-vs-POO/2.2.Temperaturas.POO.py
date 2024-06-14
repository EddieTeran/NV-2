class ClimaSemanal:
    # Constructor de la clase, inicializa una lista vacía para almacenar temperaturas
    def __init__(self):
        self.__temperaturas = []  # Atributo privado

    # Método público para ingresar temperaturas para cada día de la semana
    def ingresar_temperatura(self):
        # Recorre cada día de la semana
        for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]:
            while True:
                try:
                    # Pide al usuario que ingrese la temperatura para cada día
                    temperatura = float(input(f"Por favor ingrese la temperatura del {dia}: "))
                    # Agrega la temperatura a la lista
                    self.__temperaturas.append(temperatura)
                    break
                except ValueError:
                    print("Ingrese un número entero o decimal")

    # Método público para calcular el promedio semanal de temperatura
    def calcular_promedio_semanal(self):
        # Calcula la suma de todas las temperaturas
        total = sum(self.__temperaturas)
        # Calcula el promedio dividiendo la suma por el número de temperaturas
        promedio = total / len(self.__temperaturas)
        # Devuelve el promedio de temperatura
        return promedio

# Crear una instancia de la clase ClimaSemanal
clima_poo = ClimaSemanal()

# Llamar al método para ingresar temperaturas (solo necesitas llamarlo una vez)
clima_poo.ingresar_temperatura()

# Llamar al método para calcular el promedio semanal de temperatura
promedio_poo = clima_poo.calcular_promedio_semanal()

# Imprimir el promedio semanal de temperaturas
print(f"El promedio semanal de temperaturas es: {round(promedio_poo,2)}")