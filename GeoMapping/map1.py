import folium
import pandas as pd

df= pd.read_csv("Volcanoes.csv")

lat = list(df["LAT"])
lon = list(df["LON"])
ele = list(df["ELEV"])
# print(df['ELEV'].describe()) Some data exploration

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright") #Create Map object

fgv = folium.FeatureGroup(name="Volcanoes") #Create Map groups for volcanoes

#Add pointer layer
for latitude, longitude,el in zip(lat,lon,ele): #Add multiple circle markers to Volcanoes in USA using for loop

    fgv.add_child(folium.CircleMarker(location = [latitude, longitude], radius=6, popup=str(el)+" m", fill_color=color_producer(el), fill= 'true', color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population") #Create Map groups for population


#Now adding GeoJson polygon layer
fgp.add_child(folium.GeoJson(data = open("world.json",'r', encoding='utf-8-sig').read(),
                            style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000<= x['properties']['POP2005'] < 20000000 else 'red'})) #Style_function is used to change color of polygons which is default green

map.add_child(fgv)
map.add_child(fgp)

#Adding layer control which creates button to switch off Volcanoes group and/or Population group
map.add_child(folium.LayerControl())

map.save("Map1.html")