
# coding: utf-8

# In[ ]:

import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')


import pygrib
from scipy import ndimage
from mpl_toolkits.basemap import shiftgrid
import numpy as np
import math


import calc_wind as totalwind


# In[ ]:

def opengrib(yyyy, mm, dd, tt, pm, path):
    grib = '%s/%s/param_%s_%s%s%s_%s00.grib' % (path,pm,pm,yyyy,mm,dd,tt)
    grbs = pygrib.open(grib)
    return(grbs);


# In[ ]:

def selectgrb(grbs, sN, tOL, lv):
    val = grbs.select()[0]
    val = grbs.select(shortName = sN, typeOfLevel = tOL, level = lv)[0]
    val = val.values
    return(val);


# In[ ]:

def shiftgrb(grb,val,m):
    lat,lon = grb.latlons()
    lons = lon[0,:]
    val,lons = shiftgrid(180., val, lons, start = False)
    lats = lat[:,0]
    
    lons,lats = np.meshgrid(lons,lats)
    plons,plats = m(lons,lats)
    return(plons,plats,val);
    #return(plons,plats,lons,lats,val);


# In[ ]:

def closegrb(grbs):
    grbs.close()


# In[ ]:

def DT_values(pathPV2000, pathPL,year,mon,day,time):
### OPEN FILES
    # pathPV2000 = '../test_dataECMWF/SCA/PV2000'

### PT
    parameter = 'pt'
    grbsPT = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathPV2000)

### Wind
    parameter = 'uv'
    grbsUV = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathPV2000)

### Vorticity (relative)
    # pathPL = '../test_dataECMWF/SCA/pl'
    parameter = 'vo'
    grbsVO = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathPL)
#

### GET FILE DATA
    tOL = 'potentialVorticity'
    lv = 2000
### PT
    sN = 'pt'
    grbPT = grbsPT.select()[0]
    PT = selectgrb(grbsPT, sN, tOL, lv)

### Wind 
# U component of wind
    sN = 'u'
    grbUV = grbsUV.select()[0]
    wind_u = selectgrb(grbsUV, sN, tOL, lv)
# V component of wind
    sN = 'v'
    wind_v = selectgrb(grbsUV, sN, tOL, lv)

### Vorticity (relative)
# 925 hPa
    sN = 'vo'
    tOL = 'isobaricInhPa'
    grbVO = grbsVO.select()[0]
    lv = [850, 900, 925]

    RV = dict()
    for i in lv:
        RV[i] = selectgrb(grbsVO, sN, tOL, i)
    
### calculating 925-850 hPa layer-averaged cyclonic relative vorticity (every 0.5 x10^-4 s-1)
# all three layers divided by number of layers
    rel_vort = (RV[850]+RV[900]+RV[925])/3          # arithmetric mean
    rel_vort = ndimage.filters.gaussian_filter(rel_vort, sigma = 2)
    
    closegrb(grbsPT)
    closegrb(grbsUV)
    closegrb(grbsVO)
    
    return(grbPT, PT, grbUV, wind_u, wind_v, grbVO, rel_vort)


# In[ ]:

def AR_values(pathPL, pathSFC, year,mon,day,time):

### PT
    parameter = 'q'
    grbsSH = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathPL)

### Wind
    parameter = 'uv'
    grbsUV = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathPL)

### get the file values into python
# find the first grib message with a matching name:
    grbSH = grbsSH.select()[0]
    grbUV = grbsUV.select()[0]

## specific humidity
# from Rutz et al. - 2014:
# The integration is done using data at the surface, 50-hPa intervals from the surface to 500 hPa,

# specific humidity q
    SH = dict()
# Wind
    wind_u = dict()       # U component of wind
    wind_v = dict()       # V component of wind
    V_lv = dict()            # total wind vector
    theta_lv = dict()        # wind direction
    IVT_lv = dict()       # Flux in each level trapezodial 
    dIVT_lv = dict()      # f(x) in integral 

    for i in range(750,1000,50):       # ECMWF has only levels 1000-850 in 50hPa
        lv = i + 50
        SH[lv] = selectgrb(grbsSH, 'q', 'isobaricInhPa', lv) 
        wind_u[lv] = selectgrb(grbsUV, 'u', 'isobaricInhPa', lv)
        wind_v[lv] = selectgrb(grbsUV, 'v', 'isobaricInhPa', lv)
        V_lv[lv], theta_lv[lv] = totalwind.totalwind(wind_u[lv],wind_v[lv])
        dIVT_lv[lv] = (SH[lv] * V_lv[lv])
    
    for i in range(100,800,100):       # ECMWF has from 700 - 100 hPa only in 100hPa steps
        lv = i
        SH[lv] = selectgrb(grbsSH, 'q', 'isobaricInhPa', lv)
        wind_u[lv] = selectgrb(grbsUV, 'u', 'isobaricInhPa', lv)
        wind_v[lv] = selectgrb(grbsUV, 'v', 'isobaricInhPa', lv)
        V_lv[lv], theta_lv[lv] = totalwind.totalwind(wind_u[lv],wind_v[lv])
        dIVT_lv[lv] = (SH[lv] * V_lv[lv])
    
    for lv in range(800,1000,50):       # ECMWF has only levels 1000-850 in 50hPa
        IVT_lv[lv+25] = (SH[lv] * V_lv[lv] + SH[lv+50] * V_lv[lv+50]) / 2 *5000.
    
    for lv in range(100,800,100):       # ECMWF has from 700 - 100 hPa only in 100hPa steps
        IVT_lv[lv+50] = (SH[lv] * V_lv[lv] + SH[lv+100] * V_lv[lv+100])/2 *10000.
        
## calculate the IVT
    g = 9.81      # gravitational acceleration [m s^-2]


    IVT = (1/g)*(IVT_lv[150] + IVT_lv[250] + IVT_lv[350] + IVT_lv[450] + IVT_lv[550] + IVT_lv[650] +              IVT_lv[750] + IVT_lv[825] + IVT_lv[875] + IVT_lv[925] + IVT_lv[975] )

# calculate IVT components
    x_IVT = dict()
    y_IVT = dict()
    x_tr = dict()    # trapezoidal integegrated x value
    y_tr = dict()    # trapezoidal integegrated y 

    for lv in range(800,1050,50):       # ECMWF has only levels 1000-850 in 50hPa
        x_IVT[lv] =  -abs(dIVT_lv[lv])* np.sin((math.pi/180)*(theta_lv[lv]))
        y_IVT[lv] =  -abs(dIVT_lv[lv])* np.cos((math.pi/180)*(theta_lv[lv]))

    
    for lv in range(100,800,100):       # ECMWF has from 700 - 100 hPa only in 100hPa steps
        x_IVT[lv] =  -abs(dIVT_lv[lv])* np.sin((math.pi/180)*(theta_lv[lv]))
        y_IVT[lv] =  -abs(dIVT_lv[lv])* np.cos((math.pi/180)*(theta_lv[lv]))

    for lv in range(800,1000,50):       # ECMWF has only levels 1000-850 in 50hPa
        x_tr[lv+25] = (x_IVT[lv] + x_IVT[lv+50]) / 2 *5000.
        y_tr[lv+25] = (y_IVT[lv] + y_IVT[lv+50]) / 2 *5000.
    
    for lv in range(100,800,100):       # ECMWF has from 700 - 100 hPa only in 100hPa steps
        x_tr[lv+50] = (x_IVT[lv] + x_IVT[lv+100]) *10000. 
        y_tr[lv+50] = (y_IVT[lv] + y_IVT[lv+100]) *10000. 

    
    IVT_u = (x_tr[150] +  x_tr[250] + x_tr[350] + x_tr[450] + x_tr[550] +             x_tr[650] + x_tr[750] + x_tr[825] + x_tr[875] +             x_tr[925] + x_tr[975]  )


    IVT_v = (y_tr[150] +  y_tr[250] + y_tr[350] + y_tr[450] + y_tr[550] +             y_tr[650] + y_tr[750] + y_tr[825] + y_tr[875] +             y_tr[925] + y_tr[975]  )

    closegrb(grbsSH)
    closegrb(grbsUV)
    return(grbUV, IVT, IVT_u, IVT_v);


# In[ ]:

def larger250(IVT, IVT_u, IVT_v, plonsIU, platsIV):
### find only values larger 250 to plot the IVT flux
    larger250 = np.where(IVT[:,:] >= 250.)
 #   print('Values bigger than 250 =', IVT[larger250])
  #  print('The rows are ', larger250[0])
   # print('The columns are ', larger250[1])



    u_flux = IVT_u[larger250[0],larger250[1]]
    v_flux = IVT_v[larger250[0],larger250[1]]


    lon_flux = plonsIU[larger250[0],larger250[1]]
    lat_flux = platsIV[larger250[0],larger250[1]]
    
    return(lon_flux, lat_flux, u_flux, v_flux)


# In[ ]:

def IWV_U850_values(pathPL, pathSFC, year,mon,day,time):
### Wind
    parameter = 'uv'
    grbsUV = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathPL)
### Mean Sea Level Pressure
    parameter = 'msl'
    grbsMSL = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathSFC)

### Precipitable Water
    parameter = 'tcwv'
    grbsPW = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathSFC)

### GET FILE DATA
    tOL = 'isobaricInhPa'
    lv = 850
## Wind
# U component of wind
    sN = 'u'
    grbUV = grbsUV.select()[0]
    wind_u = selectgrb(grbsUV, sN, tOL, lv)
# V component of wind
    sN = 'v'
    wind_v = selectgrb(grbsUV, sN, tOL, lv)
## Mean sea level pressure
    tOL = 'surface'
    lv = 0
    sN = 'msl'
    grbMSL = grbsMSL.select()[0]
    MSL = selectgrb(grbsMSL, sN, tOL, lv)

### converst MSL from Pa --> hPa
    MSL = 0.01 * MSL
## Total colum water vapour
    sN = 'tcwv'
    grbPW = grbsPW.select()[0]
    PW = selectgrb(grbsPW, sN, tOL, lv)
    
    closegrb(grbsUV)
    closegrb(grbsMSL)
    closegrb(grbsPW)
    
    return(grbUV, wind_u, wind_v, grbMSL, MSL, grbPW, PW)


# In[ ]:

def JTHMSLP_values(pathPL, pathSFC, year,mon,day,time):
### Wind
    parameter = 'uv'
    grbsUV = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathPL)

### Geopotential
    parameter = 'z'
    grbsZ = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathPL)

### Mean Sea Level Pressure
    parameter = 'msl'
    grbsMSL = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathSFC)

### Precipitable Water
    parameter = 'tcwv'
    grbsPW = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = pathSFC)

### GET FILE DATA
    tOL = 'isobaricInhPa'
    lv = 250
## Wind
# U component of wind
    sN = 'u'
    grbUV = grbsUV.select()[0]
    wind_u = selectgrb(grbsUV, sN, tOL, lv)
# V component of wind
    sN = 'v'
    wind_v = selectgrb(grbsUV, sN, tOL, lv)
### Calculate wind speed
    Uabs = np.sqrt(wind_u**2 + wind_v**2)

## Geopotential

# 1000 hPa
    sN = 'z'
    lv = 1000
    grbZ = grbsZ.select()[0]
    G1000 = selectgrb(grbsZ, sN, tOL, lv)

# 500 hPa
    lv = 500
    G500 = selectgrb(grbsZ, sN, tOL, lv)
### convert Geopotential to height
# https://en.wikipedia.org/wiki/Geopotential
    a = 6.378*10**6     # average radius of the earth  [m]
    G = 6.673*10**(-11) # gravitational constant       [Nm2/kg2]
    ma = 5.975*10**24   #  mass of the earth           [kg]

    Z1000 = (-a**2 * G1000)/(a*G1000 - G* ma) 
    Z500 = (-a**2 * G500)/(a*G500 - G* ma) 

    Z = (Z500 - Z1000)/10
## Mean sea level pressure
    tOL = 'surface'
    lv = 0
    sN = 'msl'
    grbMSL = grbsMSL.select()[0]
    MSL = selectgrb(grbsMSL, sN, tOL, lv)
### converst MSL from Pa --> hPa
    MSL = 0.01 * MSL
## Total colum water vapour
    sN = 'tcwv'
    grbPW = grbsPW.select()[0]
    PW = selectgrb(grbsPW, sN, tOL, lv)
    
    closegrb(grbsUV)
    closegrb(grbsZ)
    closegrb(grbsMSL)
    closegrb(grbsPW)
    
    return(grbUV, Uabs, grbZ, Z, grbMSL, MSL, grbPW, PW);

