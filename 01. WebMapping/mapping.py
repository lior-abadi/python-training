import pandas
import folium
import io

# Data Input Volcanoes
data   = pandas.read_csv("volcanoes.txt")
lat    = list(data["LAT"])
lon    = list(data["LON"])
name   = list(data["NAME"])
height = list(data["ELEV"])

html = """ <h4> Volcano Info: </h4>
Height: %s m
"""

#Map Creation & Layers
map = folium.Map(location=[38.58,-99.09], zoom_start=5.2, tiles = "Stamen Terrain")
fg1= folium.FeatureGroup(name="Volcanoes")
fg2= folium.FeatureGroup(name="Contry Borders")

# Elevation Color function:
def color_producer(elevation):
    if elevation < 1000:
            return "green"
    elif elevation > 1000 and elevation < 3000:
            return "orange"
    else:
            return "red"

# Adding the points to the map
for lt, ln, nm, el in zip(lat, lon, name, height):
    strEl  = str(round(el))
    strGlobal = strEl + " mts"
    fg1.add_child(folium.CircleMarker(location=[lt,ln], radius = 8, popup=(nm), tooltip=strGlobal,
                    fill_color = color_producer(el), color="grey", fill_opacity=0.7))

fg2.add_child(folium.GeoJson(data=io.open("world.json", "r", encoding="utf-8-sig").read(),
                            style_function = lambda x: {"fillColor":"white" if x['properties']['POP2005'] < 100000000
                                                       else "orange" if 100000000 <= x['properties']['POP2005'] < 200000000 else "red"} ))

map.add_child(fg1)
map.add_child(fg2)

map.add_child(folium.LayerControl())
map.save("Map1.html")
