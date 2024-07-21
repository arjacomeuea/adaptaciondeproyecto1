import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script sea absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    # Defina la ruta base donde se encuentra el script
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'SEMANA 2/Abstracción.py',
        '2': 'Semana 3/Programación Orientada a Objetos.py',
        '3': 'EjemplosMundoReal_POO/Boleto de Avion.py',
        '4': 'Semana 5/Cálculo del área de un círculo.py',
        '5': 'Semana 6/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '6': 'Semana 7/Manejo de Archivos.py',
    }

    while True:
        print("\nMenú Principal - Tablero de mandos")
        for tecla in opciones:
            print(f"{tecla} - {opciones[tecla]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = opciones[eleccion]
            mostrar_codigo(os.path.join(ruta_base, ruta_script))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()