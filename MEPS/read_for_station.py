
# coding: utf-8

# In[ ]:

import sys
sys.path.append('/uio/hume/student-u48/franzihe/Documents/Thesis/Python')
#sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
import netCDF4
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import fill_values as fv
import calc_station_properties as cs

import createFolder as cF


# In[ ]:

def read_for_station(thredds,year,month,day,tid,stn_lon,stn_lat,var_name,level,ens_memb):
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

    if level == 'ml':
######## with Vertical Levels ( hybrid )#################################
## hybrid levels atmosphere_hybrid_sigma_pressure_coordinate
# formula: p(n,k,j,i) = ap(k) + b(k)*ps(n,j,i)
# positive: down
        air_temperature_ml= fn.variables['air_temperature_ml']
### variables to calculate pressure
        p0 = fn.variables['p0']    ## p0: p0
        ap = fn.variables['ap']    ## ap: ap
        b = fn.variables['b']      ## b: b

        dz, dgeop, p_ml = cs.get_thickness(surface_air_pressure, 
                  air_temperature_0m, air_temperature_ml,
                  ap,b,
                 ens_memb,y,x)


        del air_temperature_0m ,surface_air_pressure, air_temperature_ml


# Read in all values needed to present the microphysics
## Time
    time_arr = fn.variables['time']
## heights
    height0_arr = fn.variables['height0']
    height1_arr = fn.variables['height1']
    height6_arr = fn.variables['height6']
    hybrid_arr = fn.variables['hybrid']

       
######## with Vertical Levels ( height0 ) #################################
    if level == 'sfc': 
        air_temperature_0m = cs.get_value_at_station(fn, 'air_temperature_0m',ens_memb,x,y)
        graupelfall_amount = cs.get_value_at_station(fn, 'graupelfall_amount',ens_memb,x,y)
        liquid_water_content_of_surface_snow = cs.get_value_at_station(fn, 'liquid_water_content_of_surface_snow',
                                                                       ens_memb,x,y)
        precipitation_amount_acc = cs.get_value_at_station(fn, 'precipitation_amount_acc',ens_memb,x,y)
        rainfall_amount = cs.get_value_at_station(fn, 'rainfall_amount',ens_memb,x,y)
        snowfall_amount = cs.get_value_at_station(fn, 'snowfall_amount',ens_memb,x,y)
        surface_air_pressure = cs.get_value_at_station(fn, 'surface_air_pressure',ens_memb,x,y)
        surface_geopotential = cs.get_value_at_station(fn, 'surface_geopotential',ens_memb,x,y)


######## with Vertical Levels ( height1 )#################################
    if level == '2m':
        air_temperature_2m = cs.get_value_at_station(fn,'air_temperature_2m',ens_memb,x,y)
        specific_humidity_2m = cs.get_value_at_station(fn,'specific_humidity_2m',ens_memb,x,y)

######## with Vertical Levels ( height1 )#################################
    if level == '10m':
        x_wind_10m = cs.get_value_at_station(fn,'x_wind_10m',ens_memb,x,y)
        y_wind_10m = cs.get_value_at_station(fn,'y_wind_10m',ens_memb,x,y)

######## with Vertical Levels ( hybrid )#################################
## hybrid levels atmosphere_hybrid_sigma_pressure_coordinate
# formula: p(n,k,j,i) = ap(k) + b(k)*ps(n,j,i)
# positive: down
    if level == 'ml':
        air_temperature_ml = cs.get_value_at_station(fn,var_name,ens_memb,x,y)
            


### write netCDF file

    
    
    if level == 'ml':
        f = netCDF4.Dataset('%s/%s/%s_%s/%s/%s%s%s_%s_%s.nc' %(dirnc, stn_name,level,tid, var_name,year, month, day, tid, ens_memb), 'w')
     #   f = netCDF4.Dataset('%s/%s/%s_%s/%s%s%s_%s_%s.nc' %(dirnc, stn_name,level,tid, year, month, day, tid, ens_memb), 'w')

    if level == 'sfc' or level == '2m' or level == '10m':
        f = netCDF4.Dataset('%s/%s/%s_%s/%s%s%s_%s_%s.nc' %(dirnc, stn_name,level, tid, year, month, day, tid, ens_memb), 'w')

### create dimensions
    f.createDimension('time', time_arr.shape[0])
    f.createDimension('height0', height0_arr.shape[0])
    f.createDimension('height1', height1_arr.shape[0])
    f.createDimension('height6', height6_arr.shape[0])
    f.createDimension('hybrid', hybrid_arr.shape[0])

    t = f.createVariable('time', time_arr.dtype,'time',zlib = True)

    t[:] = time_arr[:]



######## with Vertical Levels ( height0 ) #################################
    if level == 'sfc':
        h = f.createVariable('height0', height0_arr.dtype, 'height0', zlib=True)
        h[:] = height0_arr[:]
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
    if level == '2m':
        h1 = f.createVariable('height1', height1_arr.dtype, 'height1', zlib=True)

        h1[:] = height1_arr[:]
        dim = ('time', 'height1')
        at_2m = cs.get_netCDF_variable(f,'air_temperature_2m', air_temperature_2m,dim)
        sh_2m = cs.get_netCDF_variable(f,'specific_humidity_2m',specific_humidity_2m,dim)

######## with Vertical Levels ( height6 )#################################
    if level == '10m':
        h6 = f.createVariable('height6', height6_arr.dtype, 'height6', zlib=True)

        h6[:] = height6_arr[:]
        dim = ('time', 'height6')
        xwind_10m = cs.get_netCDF_variable(f,'x_wind_10m', x_wind_10m,dim)
        ywind_10m = cs.get_netCDF_variable(f,'y_wind_10m', y_wind_10m,dim)
 

######## with Vertical Levels ( hybrid )#################################
    if level == 'ml':
        hyb = f.createVariable('hybrid', hybrid_arr.dtype, 'hybrid', zlib=True)
        

        hyb[:] = hybrid_arr[:]
        dim = ('time','hybrid')

        at_ml = cs.get_netCDF_variable(f,var_name,air_temperature_ml,dim)
        dz_ml = cs.get_netCDF_variable(f,'layer_thickness',dz,dim)
        dgeop_ml = cs.get_netCDF_variable(f,'geop_layer_thickness',dgeop,dim)
        pres_ml = cs.get_netCDF_variable(f, 'pressure_ml', p_ml, dim)


    f.close()
    fn.close()


# In[ ]:

year = '2016'
month = '12'
time = '00'
stn_lat = 59.8
stn_lon = 7.2
stn_name = 'Haukeliseter'
dirnc = '../../Data/MEPS'

var_name = [ 
               'air_temperature_ml',                            ## air temperature model levels
 #              'atmosphere_cloud_condensed_water_content_ml',   ## atmospheric cloud condensed water
  #             'atmosphere_cloud_ice_content_ml',               ## cloud ice in model levels
   #            'graupelfall_amount_ml',                         ## instantaneous graupel in model levels
    #           'pressure_departure',                            ## nonhydrostatic departure from hydrostatic pressure
 #              'rainfall_amount_ml',                            ## instantaneous rain in model levels
  #             'snowfall_amount_ml',                            ## instantaneous snow in model levels
     #          'specific_humidity_ml',                          ## specific humidity model levels
      #         'x_wind_ml',                                     ## zonal wind model levels
       #        'y_wind_ml'                                      ## meridional wind model levels
               
               ]

level = [ #[
    'ml',
#    'sfc', 
 #   '2m',
  #  '10m'
]

thredds  = 'http://thredds.met.no/thredds/dodsC/meps25epsarchive'


# In[ ]:

t = [
   # 20,21,
    22,23,24,25,26,27,
    19,18,17, 
#    28,29,30,31,
 #   15,14,13,12,
  #  11,10,9,8,7,
   # 6,5,4,3,2,1
    ]


# In[ ]:

for lv in level:
    if lv == 'sfc' or lv == '2m' or lv == '10m':
        var_name = []
        cF.createFolder('%s/%s/%s_%s/' %(dirnc, stn_name,lv,time))
        for day in t:
            if day < 10:
                day = '0%s' %(day)
            else:
                day = '%s' %day
            for ens_memb in range(0,10):
                read_for_station(thredds,year,month,day,time,stn_lon,stn_lat,var_name,lv, ens_memb)
                print('file written: %s/%s%s%s_%s_%s.nc' %(lv,year,month,day,time,ens_memb))
    elif lv == 'ml':
      for name in var_name:
	cF.createFolder('%s/%s/%s_%s/%s/' %(dirnc, stn_name,lv,time,name))
        for day in t:
            if day < 10:
                day = '0%s' %(day)
            else:
                day = '%s' %day
            for ens_memb in range(0,10):
	      read_for_station(thredds,year,month,day,time,stn_lon,stn_lat,name,lv, ens_memb)
              print('file written: %s/%s%s%s_%s_%s.nc' %(name,year,month,day,time,ens_memb))
    



