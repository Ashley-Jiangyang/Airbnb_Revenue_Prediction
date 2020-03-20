#!/usr/bin/env python
# coding: utf-8

# # Geographical Plot 

# In[1]:


# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns   
import folium
from folium.plugins import HeatMap


# Import data
listings_eda = pd.read_csv("listings_clean_eda.csv") 

# define base plot
def generateBaseMap(default_location=[47.623601, -122.328874], default_zoom_start=12):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
    return base_map

# Heatmap for yearly revenue grouped by geographical location
base_map_yield = generateBaseMap()
HeatMap(data=listings_eda[['latitude', 'longitude', 'yearly_revenue']].groupby(['latitude', 'longitude']).median().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(base_map_yield)
base_map_yield

