import geopandas as gpd
import csv
import pandas as pd
import matplotlib.pyplot as plt

#reading dataset
df = pd.read_csv('statewise-eng.csv')

#loading the shapefile path
shapefile_path = 'Indian_States.shp'
gdf = gpd.read_file(shapefile_path)

print(df.columns)
print(gdf.columns)


#merging the dataset with geopandas dataframe 
merged_data = gdf.merge(df, on= 'st_nm', how='left')

#creating the choropleth map
ax= merged_data.plot(column = ('Percentage of English Speaking People in India'), cmap ='OrRd', legend = True, figsize = (12,8))

#customizing the map appearance
ax.set_title('English Speaking People in India')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

#the map
plt.show()