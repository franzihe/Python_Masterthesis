
# coding: utf-8

# In[1]:

import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
import netCDF4
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import fill_values as fv
import calc_station_properties as cs

import createFolder as cF


# In[ ]:

def read_for_station(thredds,year,month,day,tid,stn_lon,stn_lat,ens_memb):
    fn = netCDF4.Dataset('%s/%s/%s/%s/meps_full_2_5km_%s%s%sT%sZ.nc' %(thredds,year,month,day,year,month,day,tid),'r')


## Latitudes
## [y = 949][x = 739]
    latitude = fn.variables['latitude']

## Longitudes 
## [y = 949][x = 739]
    longitude = fn.variables['longitude']



# Now find the absolute value of the difference between the  station's lat/lon with every point in the grid. 
    x,y = cs.find_station_yx(latitude, longitude, stn_lat, stn_lon)

######## with Vertical Levels ( height0 ) #################################
    air_temperature_0m = fn.variables['air_temperature_0m']
    surface_air_pressure = fn.variables['surface_air_pressure']


######## with Vertical Levels ( hybrid )#################################
## hybrid levels atmosphere_hybrid_sigma_pressure_coordinate
# formula: p(n,k,j,i) = ap(k) + b(k)*ps(n,j,i)
# positive: down
    air_temperature_ml= fn.variables['air_temperature_ml']
### variables to calculate pressure
    p0 = fn.variables['p0']    ## p0: p0
    ap = fn.variables['ap']    ## ap: ap
    b = fn.variables['b']      ## b: b

    dz, dgeop = cs.get_thickness(surface_air_pressure, 
                  air_temperature_0m, air_temperature_ml,
                  ap,b,
                 ens_memb,y,x,)

    del air_temperature_0m ,surface_air_pressure, air_temperature_ml


# Read in all values needed to present the microphysics
## Time
    time = fn.variables['time']
## heights
    height0 = fn.variables['height0']
    height1 = fn.variables['height1']
    hybrid = fn.variables['hybrid']


######## with Vertical Levels ( height0 ) #################################
    air_temperature_0m = cs.get_value_at_station(fn, 'air_temperature_0m',ens_memb,x,y)

    graupelfall_amount = cs.get_value_at_station(fn, 'graupelfall_amount',ens_memb,x,y)
    liquid_water_content_of_surface_snow = cs.get_value_at_station(fn, 'liquid_water_content_of_surface_snow',
                                                                       ens_memb,x,y)
    precipitation_amount_acc = cs.get_value_at_station(fn, 'precipitation_amount_acc',ens_memb,x,y)
    rainfall_amount = cs.get_value_at_station(fn, 'rainfall_amount',ens_memb,x,y)
    snowfall_amount = cs.get_value_at_station(fn, 'snowfall_amount',ens_memb,x,y)
    surface_air_pressure = cs.get_value_at_station(fn, 'surface_air_pressure',ens_memb,x,y)
    surface_geopotential = cs.get_value_at_station(fn, 'surface_geopotential',ens_memb,x,y)

#surface = [
 #         air_temperature_0m,                      ## surface temperature
  #        graupelfall_amount,                      ## graupelfall amount
   #       liquid_water_content_of_surface_snow,    ## Snow water equivalent
    #      precipitation_amount_acc,                ## accumulated  total precipitation
     #     rainfall_amount,                         ## instantanous rainfall at surface
      #    snowfall_amount,                         ## instantaneous snowfall amount at surface
       #   surface_air_pressure,                    ## ps: surface_air_pressure
        #  surface_geopotential                     ## Surface geopotential (fis) 
         #      ]

######## with Vertical Levels ( height1 )#################################
    air_temperature_2m = cs.get_value_at_station(fn,'air_temperature_2m',ens_memb,x,y)
    specific_humidity_2m = cs.get_value_at_station(fn,'specific_humidity_2m',ens_memb,x,y)
#two_meter = [
 #            air_temperature_2m,                   ## screen level temperature
  #           specific_humidity_2m                  ## screen level specific humidity
   #         ]


######## with Vertical Levels ( hybrid )#################################
## hybrid levels atmosphere_hybrid_sigma_pressure_coordinate
# formula: p(n,k,j,i) = ap(k) + b(k)*ps(n,j,i)
# positive: down
    air_temperature_ml = cs.get_value_at_station(fn,'air_temperature_ml',ens_memb,x,y)
    atmosphere_cloud_condensed_water_content_ml = cs.get_value_at_station(fn,'atmosphere_cloud_condensed_water_content_ml',
                                                                                ens_memb,x,y)
    atmosphere_cloud_ice_content_ml = cs.get_value_at_station(fn,'atmosphere_cloud_ice_content_ml',ens_memb,x,y)

    graupelfall_amount_ml = cs.get_value_at_station(fn,'graupelfall_amount_ml',ens_memb,x,y)
    pressure_departure = cs.get_value_at_station(fn,'pressure_departure',ens_memb,x,y)
    rainfall_amount_ml = cs.get_value_at_station(fn,'rainfall_amount_ml',ens_memb,x,y)
    snowfall_amount_ml = cs.get_value_at_station(fn,'snowfall_amount_ml',ens_memb,x,y)
    specific_humidity_ml = cs.get_value_at_station(fn,'specific_humidity_ml',ens_memb,x,y)
            
            
#model_levels = [
 #              air_temperature_ml,                            ## air temperature model levels
  #             atmosphere_cloud_condensed_water_content_ml,   ## atmospheric cloud condensed water
   #            atmosphere_cloud_ice_content_ml,               ## cloud ice in model levels
    #           graupelfall_amount_ml,                         ## instantaneous graupel in model levels
     #          pressure_departure,                            ## nonhydrostatic departure from hydrostatic pressure
      #         rainfall_amount_ml,                            ## instantaneous rain in model levels
       #        snowfall_amount_ml,                            ## instantaneous snow in model levels
        #       specific_humidity_ml,                           ## specific humidity model levels
         #      dz,
          #     dgeop
           #    ]


### write netCDF file

    f = netCDF4.Dataset('%s/%s/%s%s%s_%s_%s.nc' %(dirnc, stn_name,year, month, day, tid, ens_memb), 'w')

### create dimensions
    f.createDimension('time', time.shape[0])
    f.createDimension('height0', height0.shape[0])
    f.createDimension('height1', height1.shape[0])
    f.createDimension('hybrid', hybrid.shape[0])

    t = f.createVariable('time', time.dtype,'time',zlib = True)

    t[:] = time[:]



######## with Vertical Levels ( height0 ) #################################
    h = f.createVariable('height0', height0.dtype, 'height0', zlib=True)

    h[:] = height0[:]
    dim = ('time', 'height0')
    at_0m = cs.get_netCDF_variable(f,'air_temperature_0m', air_temperature_0m,dim)
    ga_0m = cs.get_netCDF_variable(f,'graupelfall_amount', graupelfall_amount,dim)
    lwc_0m = cs.get_netCDF_variable(f,'liquid_water_content_of_surface_snow', liquid_water_content_of_surface_snow,dim)
    pr_0m = cs.get_netCDF_variable(f,'precipitation_amount_acc',precipitation_amount_acc,dim)
    ra_0m = cs.get_netCDF_variable(f,'rainfall_amount',rainfall_amount,dim)
    sa_0m = cs.get_netCDF_variable(f,'snowfall_amount',snowfall_amount,dim)
    ps = cs.get_netCDF_variable(f,'surface_air_pressure',surface_air_pressure,dim)
    geop = cs.get_netCDF_variable(f,'surface_geopotential',surface_geopotential,dim)

######## with Vertical Levels ( height1 )#################################
    h1 = f.createVariable('height1', height1.dtype, 'height1', zlib=True)

    h1[:] = height1[:]
    dim = ('time', 'height1')
    at_2m = cs.get_netCDF_variable(f,'air_temperature_2m', air_temperature_2m,dim)
    sh_2m = cs.get_netCDF_variable(f,'specific_humidity_2m',specific_humidity_2m,dim)

######## with Vertical Levels ( hybrid )#################################
    hyb = f.createVariable('hybrid', hybrid.dtype, 'hybrid', zlib=True)

    hyb[:] = hybrid[:]
    dim = ('time','hybrid')
    at_ml = cs.get_netCDF_variable(f,'air_temperature_ml',air_temperature_ml,dim)
    ccw_ml = cs.get_netCDF_variable(f,'atmosphere_cloud_condensed_water_content_ml',
                                atmosphere_cloud_condensed_water_content_ml,dim)
    cic_ml = cs.get_netCDF_variable(f,'atmosphere_cloud_ice_content_ml',atmosphere_cloud_ice_content_ml, dim)
    ga_ml = cs.get_netCDF_variable(f,'graupelfall_amount_ml',graupelfall_amount_ml,dim)
    pd_ml = cs.get_netCDF_variable(f,'pressure_departure',pressure_departure,dim)
    ra_ml = cs.get_netCDF_variable(f,'rainfall_amount_ml',rainfall_amount_ml,dim)
    sa_ml = cs.get_netCDF_variable(f,'snowfall_amount_ml',snowfall_amount,dim)
    sh_ml = cs.get_netCDF_variable(f,'specific_humidity_ml',specific_humidity_ml,dim)
    dz_ml = cs.get_netCDF_variable(f,'layer_thickness',dz,dim),
    dgeop_ml = cs.get_netCDF_variable(f,'geop_layer_thickness',dgeop,dim)


    f.close()
    fn.close()

#########################################################################################
# In[2]:

year = '2016'
month = '12'
#day = '20'
time = '00'
stn_lat = 59.8
stn_lon = 7.2
stn_name = 'Haukeliseter'
dirnc = '../../MEPS_data'
cF.createFolder('%s/%s/' %(dirnc,stn_name))
thredds  = 'http://thredds.met.no/thredds/dodsC/meps25epsarchive'


# In[ ]:

t = [
#    1, 2, 3, 
 #   4, 5, 6 , 
  #  7, 8, 9,10, 11,
   # 12,13,14,15,    
    #17,18,19,20, 
    21,22,23,
    24,25,26,
    27,28,29,30, 
    31
    ]


# In[ ]:

for day in t:
    if day < 10:
        day = '0%s' %(day)
    else:
        day = '%s' %day
    for ens_memb in range(0,10):
        read_for_station(thredds,year,month,day,time,stn_lon,stn_lat,ens_memb)
        print('file written: %s%s%s_%s_%s.nc' %(year,month,day,time,ens_memb))

