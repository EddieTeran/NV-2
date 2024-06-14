def ingresar_temperaturas():
    temperaturas = {}
    for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]:
        temperatura = float(input(f"Por favor ingrese la temperatura del {dia}: "))
        temperaturas[dia] = temperatura
    return temperaturas

def calcular_promedio(temperaturas):
    suma = sum(temperaturas.values())
    promedio = suma / len(temperaturas)
    return promedio

def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print("Temperaturas semanales:")
    for dia, temperatura in temperaturas.items():
        print(f"{dia}: {temperatura}°C")
    print(f"Promedio semanal: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
