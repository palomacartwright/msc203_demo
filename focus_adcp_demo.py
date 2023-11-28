#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:04:44 2023

@author: palomacartwright
"""

import xarray as xr

import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt
import cartopy.feature as cfeature



font = {'family' : 'Avenir',
        'weight' : 'normal',
        'size'   : 25}



adcp_data = xr.open_dataset('focus_adcp_new.nc')



"""

Now we can explore the dataset and see what variables are available 


adcp_data['time']
adcp_data['lat']
adcp_data['lon']

Plot the adcp data 
"""

fig1, (ax1, bx1) = plt.subplots(2, 1, figsize=(10,8), sharex = True)

var = ['u', 'v']

for i, vari in enumerate(var): 
    adcp_data[vari].plot(y='depth', ylim=(800,0), vmin=-2, vmax=2, cmap='cmo.balance', ax=[ax1, bx1][i])




fig, ax = plt.subplots(figsize=(20,11), subplot_kw={'projection':ccrs.PlateCarree()})
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN)
ax.set_extent([-80.5,-78.5,27.5,25])

gl = ax.gridlines(lw =0, 
                  draw_labels=True)

ax.plot(adcp_data.lon, adcp_data.lat, c='k')
quivplt = adcp_data.isel(time=np.arange(0, len(adcp_data.time), 8),
                           depth = slice(0,100)).mean('depth').plot.quiver(x='lon',
                                                                           y='lat',
                                                                           u='u', v='v', 
                                                                           scale=8,
                                                                           pivot='tail', 
                                                                           hue='tr_temp',
                                                                           cmap='autumn_r')                                                                         
                                                                           
                                                                           
                                                                           
'''
Bathymetry stuff if we have time 

'''               

# bathy = xr.open_dataset('gebco_bathy.nc')
# bathy = bathy.interp(lon=np.arange(-80.5,-78.5,.05),lat=np.arange(25,27.5,.05))    

# roi_lon = slice(-82, -78)
# roi_lat = slice(24, 28)

# # Extract bathymetry data for the ROI
# land_mask = bathy['elevation'] > 0
# bathymetry_roi = bathy['elevation'].sel(lon=roi_lon, lat=roi_lat).where(~land_mask)                                                        

# bathymetry_roi.plot.contourf(ax=ax, levels=15, cmap='Blues_r')
                                                                           
                                                                
                                                                          





