import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = gpd.read_file('reg1_eco_l4.zip')

print(df.head())

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

#Restrict to North America.
ax = world[world.continent == 'North America'].plot(
    color='white', edgecolor='black')

#Plot the dataframe on a map of North America
df.plot(ax=ax, color='blue')

plt.show()

#Plot the dataframe isolated on New England 
gdf = gpd.read_file(gpd.datasets.get_path('nybb'))
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

#Categorize by state
ax = df.plot(column='STATE_NAME', categorical=True, legend=True,              legend_kwds={'loc': 'center left', 'bbox_to_anchor':(1,0.5),
                         'fmt': "{:.0f}"}) # fmt is ignored for categorical data

#Categorize by ecological feature
ax = df.plot(column='US_L4NAME', categorical=True, legend=True,              legend_kwds={'loc': 'center left', 'bbox_to_anchor':(1,0.5),
                         'fmt': "{:.0f}"}) # fmt is ignored for categorical data

#Categorize by broad ecoregion
ax = df.plot(column='NA_L1NAME', categorical=True, legend=True,              legend_kwds={'loc': 'center left', 'bbox_to_anchor':(1,0.5),
                         'fmt': "{:.0f}"}) # fmt is ignored for categorical data
