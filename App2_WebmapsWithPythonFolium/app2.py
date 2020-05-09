import folium
import pandas as pd

map = folium.Map(location=[20.29,85.82],zoom_start=6,tiles = "Stamen Terrain")


df = pd.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])

def colour_producer(elev):
    if elev < 1000:
        return 'green'
    elif elev >=1000 and elev < 3000:
        return 'orange'
    else:
        return 'red'

html = """<h4>Volcano information:</h4>
Height: %s mtrs
"""
fgv = folium.FeatureGroup(name="Volacnoes")
for lt, ln, el in zip(lat,lon,elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fgv.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color=colour_producer(el))))

fgp = folium.FeatureGroup(name="Populations")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' 
if x['properties']['POP2005'] < 10000000 
else 'orange' if  100000000 >= x['properties']['POP2005'] < 200000000
else 'yellow'}
))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")






