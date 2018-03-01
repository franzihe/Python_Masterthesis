
# coding: utf-8

# In[ ]:

import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
import fill_values as fv
import pandas as pd
import numpy as np
from scipy.integrate import simps


# In[ ]:
def find_station_yx(latitude, longitude, stn_lat, stn_lon):
# find the absolute value of the difference between the  station's lat/lon with every point in the grid. 
# This tells us how close a point is to the particular latitude and longitude.
    abslat = np.abs(latitude[:,:]-stn_lat)
    abslon= np.abs(longitude[:,:]-stn_lon)

# Now we need to combine these two results. We will use numpy.maximum, which takes two arrays and finds the local 
# maximum.
    c = np.maximum(abslon, abslat)

# If you don't like flattened arrays, you can also get the row/column index like this
    y, x = np.where(c == np.min(c))
    return(x,y);

# In[ ]:

def get_thickness(surface_air_pressure, 
                  air_temperature_0m, air_temperature_ml,
                  ap, b,
                 ens_memb,y,x):
    ### Calculuat the thickness of each layer in m or geop height
    
### 1) Connect model levels and surface values
# this is only done for pressure and temperature
# !!!! DO NOT DO THAT FOR THE OTHER VALUES, SINCE in model levels it is the mixing ration and at the surface [kg/m^2]

### Pressure
# transform hybrid sigma pressure coordinate in model levels to actual pressure
    surface_air_pressure, dt_sap = fv.mask_array(surface_air_pressure,ens_memb,y,x)
    p_sfc = pd.DataFrame.from_dict(surface_air_pressure[:,:])
    p_ml = pd.DataFrame.from_dict((ap[:] + b[:]*surface_air_pressure[:,:]))
    pressure = np.asarray(pd.concat([p_ml, p_sfc],axis = 1))

### Temperature
    air_temperature_0m, dt_at0m = fv.mask_array(air_temperature_0m,ens_memb,y,x)
    air_temperature_ml, dt_atml = fv.mask_array(air_temperature_ml,ens_memb,y,x)
    t_sfc = pd.DataFrame.from_dict(air_temperature_0m[:,:])
    t_ml = pd.DataFrame.from_dict(air_temperature_ml[:,:])
    temperature = np.asarray(pd.concat([t_ml,t_sfc],axis = 1))

### 2) to convert pressure-levels into actual heights use the hypsometric equation --> Temperature and pressure
# are needed. After J. E. Martin: Mid-Latitude Atmospheric Dynamics Eq. 3.6
    Rd = 287.    # gas constant for dry air [J kg^-1 K^-1]
    g = 9.81     # Standard gravity [m s^-2]

### calculate the pressure-weighted, column averaged temperature as from J. E. Martin: Mid-Latitude Atmospheric 
# Dynamics Book, Eq. below Eq. 3.6
    temp_mean = []
    for i in range(0, temperature.shape[1]-1):
        numT = simps(y=temperature[:,i:(i+2)], x=np.log(pressure[:,i:(i+2)]), dx = np.log(pressure[:,i:(i+2)]),even='last')
        denomT = simps(y=np.ones(temperature[:,i:(i+2)].shape), x = np.log(pressure[:,i:(i+2)]), dx = np.log(pressure[:,i:(i+2)]),even='last')
        t_mean = numT/denomT
        temp_mean.append(t_mean)
# get temperature and pressure, and value so that array zero contains low levels (transpose or flip)
    temp_mean = pd.DataFrame.from_dict(np.transpose((temp_mean)))
    temp_mean = np.fliplr(temp_mean)
    pres = np.fliplr(pressure)
    temperature = np.fliplr(temperature)

    thickness = []
    geop_th = []
    for i in range(0, pres.shape[1]):
        if (i+1) == pres.shape[1]:
            continue
        p1 = pres[:,i]
        p2 = pres[:,(i+1)]   
        dz = (Rd * temp_mean[:,i])/g * np.log((p1/p2))    # thickness in [m]
        dgeop = (Rd * temp_mean[:,i])* np.log((p1/p2))    # thickness in [J/kg]
        thickness.append(dz)
        geop_th.append(dgeop)
# transpose array, so that array starts at lower levels
#    thickness = pd.DataFrame.from_dict(np.transpose((thickness)))
    thickness = np.transpose(thickness)
    thickness = np.ma.masked_where(np.isnan(thickness), thickness)
 #   geop_th = pd.DataFrame.from_dict(np.transpose((geop_th)))
    geop_th = np.transpose(geop_th)
    geop_th = np.ma.masked_where(np.isnan(geop_th), geop_th)
    p_ml = np.fliplr(p_ml)
    p_ml = np.ma.masked_where(np.isnan(p_ml), p_ml)
    
    return(thickness, geop_th, p_ml)


def get_value_at_station(fn, var_ml,ens_memb,x,y):
    var_ml = fn.variables[var_ml]
    var_ml, dtype = fv.mask_array(var_ml,ens_memb,y,x)
    var_ml = pd.DataFrame.from_dict(var_ml[:,:])
    var_ml = np.fliplr(var_ml)
    var_ml = np.ma.masked_where(np.isnan(var_ml), var_ml)
    return(var_ml);
    
    
def get_netCDF_variable(f,var_name, var,dim):
    v_0m = f.createVariable(varname=var_name, datatype=var.dtype, dimensions=dim,
                                      fill_value = var.fill_value, zlib=True)
    v_0m[:] = var[:]
    return(v_0m)

