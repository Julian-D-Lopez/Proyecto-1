#Se tiene un archivo GPX con la ruta de una persona en su recorrido por la zona turística.
# La persona tomó varias fotografías y las almacenó en su celular cuidando que la metadata 
# tuviese la ubicación (EXIF).

#Elaborar un programa en Python que analice el archivo GPX, y lo visualice y muestre cada una de 
# las fotografías en el  lugar del mapa que presenta el sitio donde fue tomada.

#La visualización debe tener un mapa 2D y un mapa 3D.

import folium
import os   
import folium
from exif import Image
from datetime import datetime
import plotly.graph_objects as go

#leer archivo GPX
with open("ruta.gpx", "r", encoding="utf-8") as file:
    gpx = gpxpy.parse(file)

latitudes = []
longitudes = []
altitudes = []

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            latitudes.append(point.latitude)
            longitudes.append(point.longitude)
            altitudes.append(point.elevation if point.elevation else 0)
print("Puntos GPX cargados:", len(latitudes))      

#Leer fotos y Exif

carpeta_fotos = "fotos"
fotos_con_gps = []

for nombre in os.listdir(carpeta_fotos):
    if nombre.lower().endswith(".jpg"):
        ruta_imagen = os.path.join(carpeta_fotos, nombre)

        with open(ruta_imagen, "rb") as img_file:
            img = Image(img_file)

            if hasattr(img, "gps_latitude") and hasattr(img, "gps_longitude"):

                lat = img.gps_latitude
                lon = img.gps_longitude

                # Ignorar (0,0,0)
                if lat != (0.0, 0.0, 0.0) and lon != (0.0, 0.0, 0.0):

                    lat_decimal = lat[0] + lat[1]/60 + lat[2]/3600
                    lon_decimal = lon[0] + lon[1]/60 + lon[2]/3600

                    if img.gps_latitude_ref == "S":
                        lat_decimal = -lat_decimal
                    if img.gps_longitude_ref == "W":
                        lon_decimal = -lon_decimal

                    fotos_con_gps.append((nombre, lat_decimal, lon_decimal))

print("Fotos con GPS válido:", len(fotos_con_gps))

#Mapa 2D con Folium
mapa = folium.Map(location=[latitudes[0], longitudes[0]], zoom_start=16)
coordenadas = list(zip(latitudes, longitudes))
folium.PolyLine(coordenadas, color="blue").add_to(mapa)

#fotos
for foto in fotos_con_gps:
    nombre, lat, lon = foto
    folium.Marker(
        location=[lat, lon],
        popup=nombre,
        icon=folium.Icon(color="red")
    ).add_to(mapa)

mapa.save("mapa_2d.html")   
print("mapa 2D generado.")

#Mapa 3D con Plotly

fig = go.Figure()
fig.add_trace(go.Scatter3d(
    x=longitudes,
    y=latitudes,
    z=altitudes,
    mode='lines',
    name = 'ruta',
))

#fotos 3d

for foto in fotos_con_gps:
    nombre, lat, lon = foto
    fig.add_trace(go.Scatter3d(
        x=[lon],
        y=[lat],
        z=[alt],
        mode='markers',
        marker=dict(size=5, color='red'),
        name=nombre
    ))
fig.write_html("mapa_3d.html")
print("mapa 3D generado.")