# Actividad 2: Interoperabilidad y Extracción de Datos con APIs REST

Cliente Python que consume la API pública JSONPlaceholder, extrae el directorio de usuarios y genera un informe gerencial en consola.

---

## Requisitos

- Python 3.8 o superior
- Sin dependencias externas — solo librería estándar (`urllib`, `json`)

---

## Cómo ejecutar

```bash
python cliente_rest.py
```

---

## Salida esperada

```
════════════════════════════════════════════════════════
 INFORME GERENCIAL — DIRECTORIO DE PERSONAL
════════════════════════════════════════════════════════
 #   | Nombre completo               | Empresa
────+──────────────────────────────+─────────────────────
 1   | Leanne Graham                 | Romaguera-Crona
 2   | Ervin Howell                  | Deckow-Crist
 3   | Clementine Bauch              | Romaguera-Jacobson
 4   | Patricia Lebsack              | Robel-Corkery
 5   | Chelsey Dietrich              | Keebler LLC
 6   | Mrs. Dennis Schulist          | Considine-Lockman
 7   | Kurtis Weissnat               | Johns Group
 8   | Nicholas Runolfsdottir V      | Abernathy Group
 9   | Glenna Reichert               | Yost and Sons
 10  | Clementina DuBuque            | Hoeger LLC
════════════════════════════════════════════════════════
 Total de registros procesados: 10
════════════════════════════════════════════════════════
```

---

## Estructura del proyecto

```
Actividad2-API-REST/
├── cliente_rest.py      # Script principal
├── README.md            # Este archivo
├── reporte.md           # Reporte académico completo
├── .gitignore           # Exclusiones de Git
└── evidencias/          # Capturas de pantalla (adjuntar manualmente)
    ├── .gitkeep
    ├── 01_endpoint_navegador.png
    ├── 02_ejecucion_script.png
    └── 03_informe_consola.png
```

---

## Subir a GitHub (PowerShell)

```powershell
cd "C:\Users\vican\OneDrive\Escritorio\Claude Code\Actividad2-API-REST"
git init
git add .
git commit -m "Actividad 2: Cliente REST con JSONPlaceholder"
git branch -M main
git remote add origin https://github.com/[USUARIO]/[REPO].git
git push -u origin main
```

> Reemplaza `[USUARIO]` con tu nombre de usuario de GitHub y `[REPO]` con el nombre del repositorio que hayas creado.
