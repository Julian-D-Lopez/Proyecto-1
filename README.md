
# 🗺️ Visualización de Ruta GPX con Fotografías EXIF (Mapa 2D y 3D)

## 📌 Descripción del Proyecto

Este proyecto en **Python** permite:

* Leer un archivo **GPX** que contiene la ruta de un recorrido.
* Leer fotografías `.jpg` que contienen metadatos **EXIF con coordenadas GPS**.
* Visualizar:

  * 📍 La ruta en un **mapa 2D interactivo**.
  * 🏔 La ruta en un **mapa 3D con elevación**.
  * 📷 Las fotografías ubicadas exactamente donde fueron tomadas.

El resultado son dos archivos HTML interactivos:

* `mapa_2d.html`
* `mapa_3d.html`

---

## 🧠 Conceptos Técnicos Utilizados

### 🔹 GPX (GPS Exchange Format)

Archivo en formato XML que almacena:

* Latitud
* Longitud
* Altitud
* Puntos de recorrido (tracks)

### 🔹 EXIF (Exchangeable Image File Format)

Metadatos embebidos en imágenes `.jpg` que pueden contener:

* Coordenadas GPS
* Fecha de captura
* Información de cámara

---

## 🛠️ Tecnologías y Librerías

| Librería | Función                           |
| -------- | --------------------------------- |
| `gpxpy`  | Leer y parsear archivo GPX        |
| `exif`   | Extraer metadatos GPS de imágenes |
| `folium` | Generar mapa 2D interactivo       |
| `plotly` | Generar mapa 3D interactivo       |
| `os`     | Manejo de archivos y carpetas     |

---

## 📂 Estructura del Proyecto

```
Proyecto 1/
│
├── GpxProyect.py
├── ruta.gpx
├── fotos/
│   ├── foto1.jpg
│   ├── foto2.jpg
│   └── ...
├── mapa_2d.html
└── mapa_3d.html
```

---

## ⚙️ Instalación

### 1️⃣ Instalar Python (3.9 o superior)

Verificar versión:

```bash
python --version
```

---

### 2️⃣ Instalar dependencias

```bash
pip install folium gpxpy plotly exif
```

---

## ▶️ Ejecución

Desde la carpeta del proyecto:

```bash
python GpxProyect.py
```

Salida esperada:

```
Puntos GPX cargados: 539
Fotos con GPS válido: 5
mapa 2D generado.
mapa 3D generado.
```

---

## 🌍 Resultado

### 📍 Mapa 2D

* Línea azul → Ruta recorrida.
* Marcadores rojos → Ubicación de las fotos.

Generado con `Folium`.

---

### 🏔 Mapa 3D

* Ruta con altitud real.
* Puntos rojos donde fueron tomadas las fotos.

Generado con `Plotly 3D`.

---

## 🧮 Lógica General del Algoritmo

1. Leer archivo GPX.
2. Extraer:

   * Latitudes
   * Longitudes
   * Altitudes
3. Leer carpeta de fotos.
4. Extraer coordenadas EXIF.
5. Convertir coordenadas DMS a decimal.
6. Generar mapa 2D.
7. Generar mapa 3D.
8. Exportar a HTML interactivo.

---

## 🎯 Justificación Técnica

Se utiliza GPX porque:

* Permite representar la trayectoria completa.
* Contiene información estructurada de altitud.
* Es estándar para datos GPS.

EXIF se usa para:

* Obtener ubicación exacta donde se tomó cada fotografía.

La combinación permite una visualización geoespacial completa.

---

## 📈 Posibles Mejoras Futuras

* Mostrar la imagen dentro del popup del mapa.
* Calcular distancia total recorrida.
* Calcular velocidad promedio.
* Agregar animación temporal del recorrido.
* Asociar cada foto al punto GPX más cercano.

---

## 👨‍💻 Autor
Julian David Lopez Rubiano - Universidad Distrital Francisco Jose de Caldas
Proyecto académico desarrollado en Python para visualización geoespacial de rutas turísticas con integración de metadatos fotográficos.


