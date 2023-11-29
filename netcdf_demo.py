#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:31:50 2023

@author: palomacartwright
"""

# Introduction to working with netCDF files

# import packages
import pandas as pd
import numpy as np
import xarray as xr

# The underlying data in the xarray.DataArray is a numpy.ndarray that holds the variable values. 
# So we can start by making a numpy.ndarray with our mock temperature data:
    
temp_data = np.array([np.zeros((5,5)), 
                      np.ones((5,5)), 
                      np.ones((5,5))*2]).astype(int)

temp_data

"""
We could think this is “all” we need to represent our data. But if we stopped at this point,
we would need to remember that the numbers in this array represent the temperature in degrees Celsius (doesn’t seem too bad), 
remember that the first dimension of the array represents time, the second latitude and the third longitude (maybe ok), 
and keep track of the range of values that time, latitude, and longitude take (not so good).

Keeping track of all this information separately could quickly get messy and could make it challenging to share our data and analyses. 
This is what the netCDF data model and xarray aim to simplify. 
We can get data and its descriptors together in an xarray.DataArray by adding the dimensions over which the variable is 
being measured and including attributes that appropriately describe dimensions and variables.

To specify the dimensions of our upcoming xarray.DataArray, 
we must examine how we’ve constructed the numpy.ndarray holding the temperature data. 
Our dimensions were:

date coordinates are 2022-09-01, 2022-09-02, 2022-09-03
latitude coordinates are 70, 60, 50, 40, 30 (notice decreasing order)
longitude coordinates are 60, 70, 80, 90, 100 (notice increasing order)

"""
# names of the dimensions in the required order
dims = ('time', 'lat', 'lon')

# create coordinates to use for indexing along each dimension 
coords = {'time' : pd.date_range("2022-09-01", "2022-09-03"),
          'lat' : np.arange(70, 20, -10),
          'lon' : np.arange(60, 110, 10)}  

# Next we add the metadata

# attributes (metadata) of the data array 
attrs = { 'title' : 'temperature across weather stations',
          'standard_name' : 'air_temperature',
          'units' : 'degree_c'}

# Finally we put it all together 
# initialize xarray.DataArray
temp = xr.DataArray(data = temp_data, 
                    dims = dims,
                    coords = coords,
                    attrs = attrs)

"""
You can index arrays by numbers and by labels 

temp[0,1,2]
temp.sel(time="2022-09-01", lat = 40, lon = 80)

Next lets perform an average over time
"""

avg_temp = temp.mean(dim = "time")

avg_temp.attrs = {'title': 'average temperature over three days'}

avg_temp


"""

So now we have two xarray Data Arrays and we can combine them to give us an xarray Dataset 

"""


# make dictionaries with variables and attributes
data_vars = {'avg_temp': avg_temp,
            'temp': temp}

attrs = {'title':'temperature data at weather stations: daily and and average',
        'description':'simple example of an xarray.Dataset'}

# create xarray.Dataset
temp_dataset = xr.Dataset( data_vars = data_vars,
                        attrs = attrs)











