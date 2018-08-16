
# coding: utf-8

# # Create maps using Etopo1 and matplotlib
# http://www.trondkristiansen.com/?page_id=846
# 
# 
# https://www.ngdc.noaa.gov/mgg/global/global.html

# In[7]:

import os, sys, datetime, string
import numpy as np
from netCDF4 import Dataset
import numpy.ma as ma
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, shiftgrid#, NetCDFFile
from pylab import *
import laplaceFilter
import mpl_util
import matplotlib.colors as colors

import netCDF4


# In[8]:

def findSubsetIndices(min_lat,max_lat,min_lon,max_lon,lats,lons):
    """Array to store the results returned from the function"""
    res=np.zeros((4),dtype=np.float64)
    minLon=min_lon; maxLon=max_lon
    distances1 = []; distances2 = []
    indices=[]; index=1
    for point in lats:
        s1 = max_lat-point # (vector subtract)
        s2 = min_lat-point # (vector subtract)
        distances1.append((np.dot(s1, s1), point, index))
        distances2.append((np.dot(s2, s2), point, index-1))
        index=index+1
        
    distances1.sort()
    distances2.sort()
    indices.append(distances1[0])
    indices.append(distances2[0])

    distances1 = []; distances2 = []; index=1

    for point in lons:
        s1 = maxLon-point # (vector subtract)
        s2 = minLon-point # (vector subtract)
        distances1.append((np.dot(s1, s1), point, index))
        distances2.append((np.dot(s2, s2), point, index-1))
        index=index+1

    distances1.sort()
    distances2.sort()
    indices.append(distances1[0])
    indices.append(distances2[0])

    """ Save final product: max_lat_indices,min_lat_indices,max_lon_indices,min_lon_indices"""
    minJ=indices[1][2]
    maxJ=indices[0][2]
    minI=indices[3][2]
    maxI=indices[2][2]
    res[0]=minI; res[1]=maxI; res[2]=minJ; res[3]=maxJ;
    return res


# In[9]:

def makeMap(lonStart,lonEnd,latStart,latEnd,name,stLon,stLat,zoom):
    fig = plt.figure(figsize=(9,8))
    """Get the etopo2 data"""
    #etopo1name='ETOPO1_Ice_g_gmt4.grd'
    etopo1name = 'ETOPO1_Bed_g_gmt4.grd'
    etopo1 = Dataset(etopo1name,'r')
    
    lons = etopo1.variables["x"][:]
    lats = etopo1.variables["y"][:]

    res = findSubsetIndices(latStart-5,latEnd+5,lonStart-40,lonEnd+10,lats,lons)
    lon,lat=np.meshgrid(lons[int(res[0]):int(res[1])],lats[int(res[2]):int(res[3])])
    print( "Extracted data for area %s : (%s,%s) to (%s,%s)"%(name,lon.min(),lat.min(),lon.max(),lat.max()))
    bathy = etopo1.variables["z"][int(res[2]):int(res[3]),int(res[0]):int(res[1])]
    bathySmoothed = laplaceFilter.laplace_filter(bathy,M=None)
    
    levels =[3, 100,  200,  300,  400,  500,  600,  700,  800,  900, 1000, 1250, 1500,]

    if lonStart< 0 and lonEnd < 0:
        lon_0= - (abs(lonEnd)+abs(lonStart))/2.0
    else:
        lon_0=(abs(lonEnd)+abs(lonStart))/2.0

    if zoom == 'zoom':
        resolution = 'i'
    else:
        resolution = 'l'
    map = Basemap(llcrnrlat=latStart,urcrnrlat=latEnd,            llcrnrlon=lonStart,urcrnrlon=lonEnd,            rsphere=(6378137.00,6356752.3142),            resolution=resolution,area_thresh=1000.,projection='lcc',            lat_1=latStart,lon_0=lon_0)

    x, y = map(lon,lat)
    map.drawcoastlines()
    map.drawcountries()
    map.drawmapboundary(fill_color='gainsboro')
    if zoom != 'zoom':
        map.drawmeridians(np.arange(lons.min(),lons.max(),10),labels=[0,0,0,1],fontsize=16)
        map.drawparallels(np.arange(lats.min(),lats.max(),4),labels=[1,0,0,0],fontsize=16)
    else:
        map.drawmeridians(np.arange(lons.min(),lons.max(),3),labels=[0,0,0,1],fontsize=16)
        map.drawparallels(np.arange(lats.min(),lats.max(),2),labels=[1,0,0,0],fontsize=16)
    #map.etopo()




    CS1 = map.contourf(x,y,bathySmoothed,levels,
                  # cmap=mpl_util.LevelColormap(levels,cmap=IVTmap),
                   cmap = 'binary',
                    extend='max',
                    alpha=1.0,
                    origin='lower')

    CS1.axis='tight'
    """Plot the station as a position dot on the map"""
    xpt,ypt = map(stLon,stLat)
    map.plot([xpt],[ypt],'ro', markersize=10)
    if zoom == 'zoom':
        dist = 10000
    else:
        dist = 100000
    plt.text(xpt+dist,ypt+dist,name,fontsize = 20, fontweight = 'bold',
        ha='left',va='bottom',color='r')



    ## model center
    #longitude_of_central_meridian =  15.0
    #latitude_of_projection_origin = 63.0
    #"""Plot the MEPS model center as a position dot on the map"""
    #xpt,ypt = map(longitude_of_central_meridian,latitude_of_projection_origin)
    #map.plot([xpt],[ypt],color = 'orange', marker = 'o', markersize=10)
    #plt.text(xpt+100000,ypt+100000,'MEPS center',fontsize = 20, fontweight = 'bold',
     #       ha='left',va='bottom',color='orange')


#     if zoom != 'zoom':
#     
#     ### plot MEPS area
#         for i in range(0,lato.shape[0],12):
#             xs, ys = map(lono[i], lato[i])
#             map.plot(xs,ys, color = 'orange', marker = 'o', markersize = 10, linestyle = '-', linewidth = 10)
#         for i in range(0,lato2.shape[0],12):
#             xs2, ys2 = map(lono2[i], lato2[i])
#             map.plot(xs2,ys2, color = 'orange', marker = 'o', markersize = 10, linestyle = '-', linewidth = 10)
# 
#         xs, ys = map(lono[739], lato[739])
#         map.plot(xs,ys, color = 'orange', marker ='o', markersize = 10, linestyle = '-', linewidth = 10, label = 'MEPS domain')
#         lgd = plt.legend(loc='lower left',fontsize=18)

    #plt.title('Area %s'%(name))
    #plotfile='figures/map_'+str(name)+'.pdf'
    #plt.savefig(plotfile,dpi=150,orientation='portrait')
    #map.drawmapscale(-7., 35.8, -3.25, 39.5, 500, barstyle='fancy')

    #map.drawmapscale(-0., 35.8, -3.25, 39.5, 500, fontsize = 14)


    ### Add Colorbar
#    cbaxes = fig.add_axes([0.14, 0.03, .75, .006] )   #[left, bottom, width, height] 
    cbaxes = fig.add_axes([0.83, 0.15, .035, 0.7] )   #[left, bottom, width, height] 
    cbar = plt.colorbar(CS1,orientation='vertical',cax = cbaxes,ticks=levels[::2])#, cax = cbaxes)#, shrink=0.5)
    cbar.ax.set_ylabel('elevation [m]',fontsize = 18)
    cbar.ax.tick_params(labelsize=16)
    
    
    # tight layout
#    plt.tight_layout()



# In[10]:

thredds  = 'http://thredds.met.no/thredds/dodsC/meps25epsarchive'
year = '2016'
month = '12'
day = '20'
tid = '00'
fn = netCDF4.Dataset('%s/%s/%s/%s/meps_full_2_5km_%s%s%sT%sZ.nc' %(thredds,year,month,day,year,month,day,tid),'r')
latitude = fn.variables['latitude']
longitude = fn.variables['longitude']
lato = np.concatenate((latitude[0,:],latitude[-1,:]), axis = 0)
lono = np.concatenate((longitude[0,:], longitude[-1,:]), axis = 0)

lato2 = np.concatenate((latitude[:,0],latitude[:,-1]), axis = 0)
lono2 = np.concatenate((longitude[:,0], longitude[:,-1]), axis = 0)





