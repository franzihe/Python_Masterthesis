
# coding: utf-8

# In[ ]:

import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
import numpy as np
import matplotlib.pyplot as plt

import createFolder
import weather_map_plot_fct as PF
import ECMWF_grb as grib
import calc_date


# In[ ]:

year = '2016'
mon = '12'
#day = '10'
#time = '00'



# In[ ]:

pathPV2000 = '../../NORSTORE/SCA/pv2000'
pathPL = '../../NORSTORE/SCA/pl'
pathSFC = '../../NORSTORE/SCA/sfc'


# In[ ]:

directory_DT = '../../synoptic_figs/DynTropo'
directory_AR = '../../synoptic_figs/Atm_Riv'
directory_IWV = '../../synoptic_figs/TCWV_U850'
directory_JTM = '../../synoptic_figs/Geopot_Jet'
createFolder.createFolder(directory_DT)
createFolder.createFolder(directory_AR)
createFolder.createFolder(directory_IWV)
createFolder.createFolder(directory_JTM)


# In[ ]:


form = 'png'
savefigure = 1


# In[ ]:

for day in range(16,29):
    day = str(day)
    for time in range(0,24,6):
        if time ==0:
            time = '00'
        elif time == 6:
            time = '06'
        time = str(time)
        

### Dates for plotting
        calday, calmon = calc_date.get_dayname(year, mon, day)
        figure_name = '%s%s%s_%s.png' % (year, mon, day,time)


# DT
        grbPT, PT, grbUV_DT, wind_u_DT, wind_v_DT, grbVO, rel_vort = grib.DT_values(pathPV2000, pathPL, 
                                                                                    year,mon,day,time)
# AR
        grbUV_AR, IVT, IVT_u, IVT_v = grib.AR_values(pathPL, pathSFC, year,mon,day,time)

# IWV - U850
        grbUV_IWV, wind_u_IWV, wind_v_IWV, grbMSL_IWV, MSL_IWV, grbPW_IWV, PW_IWV = grib.IWV_U850_values(pathPL, 
                                                                                   pathSFC, year,mon,day,time)

# JTHMSLP
        grbUV_JTM, Uabs, grbZ, Z, grbMSL_JTM, MSL_JTM, grbPW_JTM, PW_JTM = grib.JTHMSLP_values(pathPL, pathSFC, 
                                                                                               year,mon,day,time)

# Plotting data on a map (Example Gallery) https://matplotlib.org/basemap/users/examples.html
        m = PF.create_basemap()

### Latitudes, Longitudes and shiftgrid

# DT
        lonsPT,latsPT, PT = grib.shiftgrb(grbPT,PT,m)
        lonsVO,latsVO, RelVo = grib.shiftgrb(grbVO,rel_vort,m)
        lonsU_DT,latsU_DT, wind_u_DT = grib.shiftgrb(grbUV_DT,wind_u_DT,m)
        lonsV_DT,latsV_DT, wind_v_DT = grib.shiftgrb(grbUV_DT,wind_v_DT,m)

# AR
        lonsIVT,latsIVT, IVT = grib.shiftgrb(grbUV_AR,IVT,m)
        lonsIU,latsIU, IVT_u = grib.shiftgrb(grbUV_AR,IVT_u,m)
        lonsIV,latsIV, IVT_v = grib.shiftgrb(grbUV_AR,IVT_v,m)
# find values larger 250 
        lon_flux, lat_flux, u_flux, v_flux = grib.larger250(IVT, IVT_u, IVT_v, lonsIU, latsIV)


# IWV - U850
        lonsU_IWV,latsU_IWV, wind_u_IWV = grib.shiftgrb(grbUV_IWV,wind_u_IWV, m)
        lonsV_IWV,latsV_IWV, wind_v_IWV = grib.shiftgrb(grbUV_IWV,wind_v_IWV, m)
        lonsMSL_IWV,latsMSL_IWV, MSL_IWV = grib.shiftgrb(grbMSL_IWV,MSL_IWV, m)
        lonsPW_IWV,latsPW_IWV, PW_IWV = grib.shiftgrb(grbPW_IWV,PW_IWV, m)

# JTHMSLP
        lonsUV_JTM,latsUV_JTM, Uabs = grib.shiftgrb(grbUV_JTM,Uabs,m)
        lonsZ,latsZ, Z = grib.shiftgrb(grbZ,Z,m)
        lonsMSL_JTM,latsMSL_JTM, MSL_JTM = grib.shiftgrb(grbMSL_JTM,MSL_JTM,m)
        lonsPW_JTM,latsPW_JTM, PW_JTM = grib.shiftgrb(grbPW_JTM,PW_JTM,m)

### Plotting Map
# DT
        PF.plot_DTmap(m, lonsPT, latsPT, PT,
               lonsVO, latsVO, RelVo,
               lonsU_DT, latsU_DT, wind_u_DT, wind_v_DT, 
               savefigure, directory_DT, figure_name, form,
               calday, day, calmon, year, time)


        plt.close()

# AR
        m = PF.create_basemap()
        PF.plot_ARmap(m, lonsIVT, latsIVT, IVT,
              lon_flux, lat_flux, u_flux, v_flux,
              savefigure, directory_AR, figure_name, form,
               calday, day, calmon, year, time)

        plt.close()

# IWV - U850

        m = PF.create_basemap()
        PF.plot_IWV_U850map(m, lonsPW_IWV, latsPW_IWV, PW_IWV,
              lonsMSL_IWV, latsMSL_IWV, MSL_IWV, 
              lonsU_IWV, latsU_IWV, wind_u_IWV, wind_v_IWV,
              savefigure, directory_IWV, figure_name, form,
               calday, day, calmon, year, time)

        plt.close()
        
# Jet - Thickness - MSLP

        m = PF.create_basemap()
        PF.plot_JTHMSPL(m, lonsPW_JTM, latsPW_JTM, PW_JTM,
              lonsMSL_JTM, latsMSL_JTM, MSL_JTM, 
              lonsUV_JTM, latsUV_JTM, Uabs,
              lonsZ,latsZ, Z,
              savefigure, directory_JTM, figure_name, form,
               calday, day, calmon, year, time)

        plt.close()
        
        print('figure: %s saved' % (figure_name))

# In[ ]:



