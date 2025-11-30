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
