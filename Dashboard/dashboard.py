import os

def mostrar_codigo(ruta_script):
    # Obtenemos la ruta absoluta del script
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Abre el archivo del script en modo de lectura
        with open(ruta_script_absoluta, 'r') as archivo:
            # Imprimir el código del script
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        # Maneja error de archivo no encontrado
        print("El archivo no se encontró.")
    except Exception as e:
        # Maneja cualquier otro error
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Obtiene la ruta  del script
    ruta_base = os.path.dirname(__file__)

    # Definir un diccionario de opciones de script
    opciones = {
        '1': "C:/Users/ediso/NV-2/Ejer-POO.py",
        "2": "C:/Users/ediso/NV-2/clases_herencia_polimorfismo/conceptos_poo.py",
        "3": "C:/Users/ediso/NV-2/constructores_destructores/ejemplo1.py",
        "4": "C:/Users/ediso/NV-2/EjemplosMundoReal_POO/Caprichos-POO.py",
        "5": "C:/Users/ediso/NV-2/Identificadores/snake_case.py",
        "6": "C:/Users/ediso/NV-2/Tradicional-vs-POO/2.2.Temperaturas.POO.py"
    }

    ruta_script = ""

    # Bucle principal del menú
    while True:
        # Imprime el menú principal
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("7 - Ejecutar script seleccionado")
        print("0 - Salir")

        # para obtener la entrada del usuario
        eleccion = input("Elige un script para ver su código, '3' para ejecutar o '0' para salir: ")
        if eleccion == '0':
            # Salir del programa
            break
        elif eleccion in opciones:
            # Entra a la ruta  del script seleccionado
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            # Mnos muetra el código
            mostrar_codigo(ruta_script)
        elif eleccion == '7':
            # EEjecuta el codigo seleccionado
            if ruta_script:
                try:
                    os.system(f"python {ruta_script}")
                except Exception as e:
                    print(f"Error al ejecutar el archivo: {e}")
            else:
                print("No se ha seleccionado un archivo para ejecutar.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutamos el dashboard
if __name__ == "__main__":
    mostrar_menu()