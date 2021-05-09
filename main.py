import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import folium
from folium.plugins import HeatMap
from json import dumps
import shapefile



cols = [
    'ClientCity',
    'TestThroughputMbpsDownload',
]
    
df = pd.read_csv ('./data/2021-04-01_Mlab_data_start.csv', usecols=cols, nrows=5)


ds = df.sort_values(by=['ClientCity', 'TestThroughputMbpsDownload'], ascending=True, kind='mergesort')

print(ds)         
fp = "Municipal_Boundaries_SHP_Geographic//CITY.shp"
fp2 = "Municipal_Boundaries_SHP_Geographic//RURAL.shp"
fp3 = "Municipal_Boundaries_SHP_Geographic//OCTEXT.shp"
fp4 = "Municipal_Boundaries_SHP_Geographic//TOWN.shp"
fp6 = "Municipal_Boundaries_SHP_Geographic//VILLAGE.shp"
fp7 = "Municipal_Boundaries_SHP_Geographic//SVILLAGE.shp"
fp8 = "Municipal_Boundaries_SHP_Geographic//HAMLETPT.shp"

#reading the file stored in variable fp
map_df = gpd.read_file(fp)
map_df2 = gpd.read_file(fp2)
map_df3 = gpd.read_file(fp3)
map_df4 = gpd.read_file(fp4)

# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
# map_df.plot()

x = map_df.plot(color='red')
y = map_df2.plot(ax=x,color='green', edgecolors='black')
z = map_df3.plot(ax=y,color='pink')
 
map_df4.plot(ax=z, color='none', edgecolors='b')
# plt.show()






# # read the shapefile
# geojson_data = shapefile.Reader('myshpfile.geojson').__geo_interface__
# print(geojson_data)

# read the shapefile
reader = shapefile.Reader("Municipal_Boundaries_SHP_Geographic//HAMLETPT.shp")
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
    atr = dict(zip(field_names, sr.record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature", \
    geometry=geom, properties=atr)) 
   
    # write the GeoJSON file
   
geojson = open("hamletpt.json", "w")
geojson.write(dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
geojson.close()