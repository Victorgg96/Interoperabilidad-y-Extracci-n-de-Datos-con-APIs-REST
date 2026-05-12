"""
Actividad 2: Interoperabilidad y Extracción de Datos con APIs REST
Endpoint: https://jsonplaceholder.typicode.com/users
Librería de red: urllib.request (stdlib, sin dependencias externas)
"""

import urllib.request
import urllib.error
import json

URL_API = "https://jsonplaceholder.typicode.com/users"


def obtener_usuarios(url: str) -> list:
    """Realiza la petición HTTP GET y retorna la lista de usuarios."""
    # --- Fase 1: Petición HTTP GET ---
    try:
        with urllib.request.urlopen(url) as respuesta:
            if respuesta.status != 200:
                raise RuntimeError(
                    f"Error HTTP: se esperaba 200, se recibió {respuesta.status}"
                )
            # --- Fase 2: Decodificación JSON ---
            # urlopen devuelve bytes; se decodifican a str y luego a estructura Python
            datos_bytes = respuesta.read()
            datos_json = json.loads(datos_bytes.decode("utf-8"))
            return datos_json
    except urllib.error.URLError as e:
        raise RuntimeError(f"No se pudo conectar con la API: {e.reason}") from e


def filtrar_campos(usuarios: list) -> list:
    """
    Fase 3: Filtrado — conserva únicamente name y company.name.
    Descarta: id, username, email, address, phone, website, geo, etc.
    """
    return [
        {
            "nombre": usuario["name"],
            "empresa": usuario["company"]["name"],
        }
        for usuario in usuarios
    ]


def imprimir_informe(registros: list) -> None:
    """Fase 4: Impresión del informe gerencial formateado en consola."""
    ANCHO = 56
    SEP = "=" * ANCHO

    print(SEP)
    print(" INFORME GERENCIAL - DIRECTORIO DE PERSONAL")
    print(SEP)
    print(f" {'#':<3} | {'Nombre completo':<28} | {'Empresa'}")
    print(f"{'-'*4}+{'-'*30}+{'-'*21}")

    for i, reg in enumerate(registros, start=1):
        nombre = reg["nombre"][:28]
        empresa = reg["empresa"][:20]
        print(f" {i:<3} | {nombre:<28} | {empresa}")

    print(SEP)
    print(f" Total de registros procesados: {len(registros)}")
    print(SEP)


if __name__ == "__main__":
    try:
        usuarios_raw = obtener_usuarios(URL_API)
        registros = filtrar_campos(usuarios_raw)
        imprimir_informe(registros)
    except RuntimeError as e:
        print(f"[ERROR] {e}")
