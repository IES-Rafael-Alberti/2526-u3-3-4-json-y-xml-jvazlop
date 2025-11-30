import json
import os
import shutil

ARCHIVO_ORIGEN = "datos_usuarios_orig.json"
ARCHIVO_DESTINO = "datos_usuarios.json"


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresione una tecla para continuar . . . ")

def mostrar_datos(datos):
    """
    Muestra los usuarios del diccionario 'datos'.
    """
    usuarios = datos.get("usuarios", [])

    if not usuarios:
        print("\nERROR El archivo JSON no contiene usuarios!")
        return

    print("\n--- Contenido Actual del JSON ---")
    for u in usuarios:
        print(f"ID: {u['id']}, Nombre: {u['nombre']}, Edad: {u['edad']}")
    print("--- Fin del Contenido ---")

def inicializar_datos(archivo_origen=ARCHIVO_ORIGEN, archivo_destino=ARCHIVO_DESTINO):
    """
    Copia el archivo JSON origen al destino validando primero su formato.
    """
    if not os.path.exists(archivo_origen):
        print(f"ERROR El archivo origen '{archivo_origen}' no existe. No se realizó la copia.")
        return False

    try:
        # Validar formato JSON
        with open(archivo_origen, "r", encoding="utf-8") as f:
            json.load(f)

    except json.JSONDecodeError:
        print(f"ERROR El archivo origen '{archivo_origen}' tiene un formato JSON inválido.")
        return False
    except Exception as e:
        print(f"ERROR inesperado: {e}")
        return False

    # Copiar archivo
    shutil.copyfile(archivo_origen, archivo_destino)
    print(f"Datos inicializados desde '{archivo_origen}' a '{archivo_destino}'.")
    return True
