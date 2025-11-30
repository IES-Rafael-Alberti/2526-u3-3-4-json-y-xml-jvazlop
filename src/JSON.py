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

def cargar_json(ruta):
    """
    Carga un archivo JSON y devuelve un diccionario.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        print(f"WARNING: El archivo '{ruta}' no existe.")
        return None

    except json.JSONDecodeError:
        print(f"WARNING: El archivo '{ruta}' tiene un formato JSON inválido o está vacío.")
        return None

def guardar_json(datos, ruta):
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"ERROR guardando JSON: {e}")

def main():
    limpiar_consola()


    inicializar_datos()


    datos = cargar_json(ARCHIVO_DESTINO)
    if datos is None:
        datos = {"usuarios": []}

    mostrar_datos(datos)
    pausar()

    usuarios = datos["usuarios"]
    usuario = next((u for u in usuarios if u["id"] == 1), None)

    if usuario:
        usuario["edad"] += 1
        print("\nUsuario con ID 1 actualizado.")
    else:
        print("\nERROR Usuario con ID 1 no encontrado.")

    mostrar_datos(datos)
    pausar()

    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}


    ids = {u["id"] for u in usuarios}
    nuevo_id = nuevo_usuario["id"]
    if nuevo_id in ids:
        nuevo_id = max(ids) + 1
        nuevo_usuario["id"] = nuevo_id

    usuarios.append(nuevo_usuario)

    print("\nUsuario Pedro añadido con éxito.")
    mostrar_datos(datos)
    pausar()

    existe = any(u["id"] == 2 for u in usuarios)

    if existe:
        datos["usuarios"] = [u for u in usuarios if u["id"] != 2]
        print("\nUsuario con ID 2 eliminado.")
    else:
        print("\nERROR Usuario con ID 2 no encontrado.")

    mostrar_datos(datos)
    pausar()


    guardar_json(datos, ARCHIVO_DESTINO)
    print("\nOperaciones completadas. Archivo actualizado.")


if __name__ == "__main__":
    main()
