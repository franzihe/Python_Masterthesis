
# coding: utf-8

# In[ ]:

get_ipython().magic('matplotlib inline')
import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
import datetime
from datetime import date
import pandas as pd
import math
import numpy as np


import os


# In[ ]:
# 
# def create_Hauk_obs(txtdir, txt_filename):
#     Haukeli = pd.read_csv('%s/%s' %(txtdir, txt_filename),                    sep = ',',header=0)
#     dd = Haukeli['Date']
#     time = Haukeli['TimeStamp']     # Time Stamp
#     dofe1 = Haukeli['RA1'].astype(float)            # total accumulation from Geonor inside DOUBLE FENCE [mm] RA1
#     dofe2 = Haukeli['RA2'].astype(float)
#     dofe3 = Haukeli['RA3'].astype(float)
#     t = Haukeli['TA'].astype(float)            # Air temperature, PT100 [deg C] 
# 
#     speed = Haukeli['FF'].astype(float)         # wind speed 10 m @ mast 1 [m/s] FF
#     direction = Haukeli['DD'].astype(float)     # wind direction 10 m @mast 1 [deg] DD
#    
# ### exclude missing values
#     dofe1 = dofe1.where(dofe1 != -999.00)
#     dofe2 = dofe2.where(dofe2 != -999.00)
#     dofe3 = dofe3.where(dofe3 != -999.00)
#     t = t.where(t != -999.00)
#     speed = speed.where(speed != -999.00)
#     direction = direction.where(direction != -999.00)
#     
# ### calculate the U, V wind component for barb plot
# # http://colaweb.gmu.edu/dev/clim301/lectures/wind/wind-uv.html
# 
# # first calculate the mathematical wind direction in deg
#     md_deg = 270 - direction
#     for k in range(0,md_deg.shape[0]):
#         if md_deg[k] <0 :
#             md_deg[k] = md_deg[k] +360
#     md_rad = math.pi/180. * md_deg
#     u_wind = speed*np.cos(md_rad)
#     v_wind = speed*np.sin(md_rad)
#     
# # --------- connect values from double fence and calculate mean  -------------------------------------------------------------------------
# 
#     dofe = pd.concat([dofe1, dofe2, dofe3], axis = 1)
#     dofe = np.nanmean(dofe, axis = 1)
#     
# # --------- create array with all daily values in column  -------------------------------------------------------------------------
#     ### find date 
#     year = []
#     month = []
#     day = []
#     tid = []
#     ### find values
#     df1 = []
#     df2 = []
#     df3 = []
#     df = []
#     temp = []
#     wind_u = []
#     wind_v = []
#     for i in range(0,31):
#         idx = datetime.datetime.strptime(str(dd[i*1440]), '%Y%m%d')
#         year.append(int(idx.year))
#         month.append(int(idx.month))
#         day.append(int(idx.day))
#         tid.append(time[i*1440: (i+1)*1440])
#         df1.append(dofe1[i*1440: (i+1)*1440])
#         df2.append(dofe2[i*1440: (i+1)*1440])
#         df3.append(dofe3[i*1440: (i+1)*1440])
#         df.append(dofe[i*1440: (i+1)*1440])
#         temp.append(t[i*1440: (i+1)*1440])
#         wind_u.append(u_wind[i*1440: (i+1)*1440])
#         wind_v.append(v_wind[i*1440: (i+1)*1440])
# 
#     df1 = np.transpose(df1)
#     df2 = np.transpose(df2)
#     df3 = np.transpose(df3)
#     df = np.transpose(df)
#     temp = np.transpose(temp)
#     wind_u = np.transpose(wind_u)
#     wind_v = np.transpose(wind_v)
#     return(df, temp, wind_u, wind_v, year, month, day,tid);
# 
# 
# 
# def create_Hauk_obs_18(txtdir, txt_filename):
#     Haukeli = pd.read_csv('%s/%s' %(txtdir, txt_filename),                    sep = ',',header=0)
#     dd = Haukeli['Date']
#     time = Haukeli['TimeStamp']     # Time Stamp
#     dofe1 = Haukeli['RA1'].astype(float)            # total accumulation from Geonor inside DOUBLE FENCE [mm] RA1
#     dofe2 = Haukeli['RA2'].astype(float)
#     dofe3 = Haukeli['RA3'].astype(float)
#     t = Haukeli['TA'].astype(float)            # Air temperature, PT100 [deg C] 
# 
#     speed = Haukeli['FF'].astype(float)         # wind speed 10 m @ mast 1 [m/s] FF
#     direction = Haukeli['DD'].astype(float)     # wind direction 10 m @mast 1 [deg] DD
#     ### find date 
#     dd[::1440]
#     year = []
#     month = []
#     day = []
#     for i in range(0,31):
#         idx = datetime.datetime.strptime(str(dd[i*1440]), '%Y%m%d')
#         year.append(int(idx.year))
#         month.append(int(idx.month))
#         day.append(int(idx.day))
# ### exclude missing values
#     dofe1 = dofe1.where(dofe1 != -999.00)
#     dofe2 = dofe2.where(dofe2 != -999.00)
#     dofe3 = dofe3.where(dofe3 != -999.00)
#     t = t.where(t != -999.00)
#     speed = speed.where(speed != -999.00)
#     direction = direction.where(direction != -999.00)
#     
# ### calculate the U, V wind component for barb plot
# # http://colaweb.gmu.edu/dev/clim301/lectures/wind/wind-uv.html
# 
# # first calculate the mathematical wind direction in deg
#     md_deg = 270 - direction
#     for k in range(0,md_deg.shape[0]):
#         if md_deg[k] <0 :
#             md_deg[k] = md_deg[k] +360
#     md_rad = math.pi/180. * md_deg
#     u_wind = speed*np.cos(md_rad)
#     v_wind = speed*np.sin(md_rad)
#     
# # --------- connect values from double fence and calculate mean  -------------------------------------------------------------------------
# 
#     dofe = pd.concat([dofe1, dofe2, dofe3], axis = 1)
#     dofe = np.nanmean(dofe, axis = 1)
#     
#     # --------- create array with all daily values in column  -------------------------------------------------------------------------
#  
#     ### find date 
#     year = []
#     month = []
#     day = []
#     tid = []
#     ### find values
#     df1 = []
#     df2 = []
#     df3 = []
#     df = []
#     temp = []
#     wind_u = []
#     wind_v = []
#     for i in range(0,30):
#         idx = datetime.datetime.strptime(str(dd[i*1440+1080]), '%Y%m%d')
#         year.append(int(idx.year))
#         month.append(int(idx.month))
#         day.append(int(idx.day))
#         tid.append(time[i*1440 +1080: (i+1)*1440+1080])
#         df1.append(dofe1[i*1440 + 1080: (i+1)*1440+ 1080])
#         df2.append(dofe2[i*1440+ 1080: (i+1)*1440+ 1080])
#         df3.append(dofe3[i*1440+ 1080: (i+1)*1440+ 1080])
#         df.append(dofe[i*1440+ 1080: (i+1)*1440+ 1080])
#         temp.append(t[i*1440+ 1080: (i+1)*1440+ 1080])
#         wind_u.append(u_wind[i*1440+ 1080: (i+1)*1440+ 1080])
#         wind_v.append(v_wind[i*1440+ 1080: (i+1)*1440+ 1080])
# 
#     df1 = np.transpose(df1)
#     df2 = np.transpose(df2)
#     df3 = np.transpose(df3)
#     df = np.transpose(df)
#     temp = np.transpose(temp)
#     wind_u = np.transpose(wind_u)
#     wind_v = np.transpose(wind_v)
#     return(df, temp, wind_u, wind_v, year, month, day,tid);
#     
#     
#     
# # In[ ]:
# 
# def valid_values_wind(uwind, vwind, DateHour):
# ### get hour, day, month, year
#     hh = []
#     dy = []
#     mm = []
#     yr = []
#     for i in range(0,DateHour.shape[0]):
#         idx = datetime.datetime.strptime(str(DateHour[i]),'%d.%m.%Y-%H:%M')
#         hh.append(idx.hour)
#         dy.append(idx.day)
#         mm.append(idx.month)
#         yr.append(idx.year)
#     
#     
#     dt = []
#     Uvar = [] 
#     Vvar = []
#     hour = []
#     day = []
#     month = []
#     year = []
# ### arange daily values in an array    
#     for i in range(0,31):
#         dt.append(DateHour[i*24:(i+1)*24])
#         Uvar.append(uwind[i*24:(i+1)*24])
#         Vvar.append(vwind[i*24:(i+1)*24])
#         hour.append(hh[i*24:(i+1)*24])
#         day.append(dy[i*24:(i+1)*24])
#         month.append(mm[i*24:(i+1)*24])
#         year.append(yr[i*24:(i+1)*24])
#         
#     dt = (np.transpose(dt))
#     Uvar = (np.transpose(Uvar))
#     Vvar = (np.transpose(Vvar))
#     hour = (np.transpose(hour))
#     day = (np.transpose(day))
#     month = (np.transpose(month))
#     year = (np.transpose(year))
#     
# ### mask missing values with NaN
#     Uvariable = []
#     Vvariable = []
#     dt_variable = []
#     hour_variable = []
#     day_variable = []
#     month_variable = []
#     year_variable = []
#     for i in range(0,31):
#         
#         Uvariable.append(Uvar[~np.isnan(Uvar[:,i]),i])
#         Vvariable.append(Vvar[~np.isnan(Vvar[:,i]),i])
#         dt_variable.append(dt[~np.isnan(Vvar[:,i]),i])
#         hour_variable.append(hour[~np.isnan(Vvar[:,i]),i])
#         day_variable.append(day[~np.isnan(Vvar[:,i]),i])
#         month_variable.append(month[~np.isnan(Vvar[:,i]),i])
#         year_variable.append(year[~np.isnan(Vvar[:,i]),i])  
#         
#         
#     return(Uvariable, Vvariable, dt_variable, hour_variable, day_variable, month_variable, year_variable)
# 



# In[ ]:

def arange_daily(RR_1, DateHour):
    
### get hour, day, month, year
    hh = []
    dy = []
    mm = []
    yr = []
    for i in range(0,DateHour.shape[0]):
        idx = datetime.datetime.strptime(str(DateHour[i]),'%d.%m.%Y-%H:%M')
        hh.append(idx.hour)
        dy.append(idx.day)
        mm.append(idx.month)
        yr.append(idx.year)
    
    
    dt = []
    var = [] 
    hour = []
    day = []
    month = []
    year = []
### arange daily values in an array    
    for i in range(0,31):
        dt.append(DateHour[i*24:(i+1)*24])
        var.append(RR_1[i*24:(i+1)*24])
        hour.append(hh[i*24:(i+1)*24])
        day.append(dy[i*24:(i+1)*24])
        month.append(mm[i*24:(i+1)*24])
        year.append(yr[i*24:(i+1)*24])
        
    dt = (np.transpose(dt))
    var = (np.transpose(var))
    hour = (np.transpose(hour))
    day = (np.transpose(day))
    month = (np.transpose(month))
    year = (np.transpose(year))
    
    return(dt, var, hour, day, month, year)
    
    
def valid_values(RR_1, DateHour):
    dt, var, hour, day, month, year = arange_daily(RR_1, DateHour)
### mask missing values with NaN
    variable = []
    dt_variable = []
    hour_variable = []
    day_variable = []
    month_variable = []
    year_variable = []
    for i in range(0,31):

        idx = np.where(var[:,i] == -9999)
        var[idx,i] = np.nan
        
        variable.append(var[~np.isnan(var[:,i]),i])
        dt_variable.append(dt[~np.isnan(var[:,i]),i])
        hour_variable.append(hour[~np.isnan(var[:,i]),i])
        day_variable.append(day[~np.isnan(var[:,i]),i])
        month_variable.append(month[~np.isnan(var[:,i]),i])
        year_variable.append(year[~np.isnan(var[:,i]),i])
        
    return(variable, dt_variable, hour_variable, day_variable, month_variable, year_variable)
          


def arange_daily_18UTC(RR_1, DateHour):
    
### get hour, day, month, year
    hh = []
    dy = []
    mm = []
    yr = []
    for i in range(0,DateHour.shape[0]):
        idx = datetime.datetime.strptime(str(DateHour[i]),'%d.%m.%Y-%H:%M')
        hh.append(idx.hour)
        dy.append(idx.day)
        mm.append(idx.month)
        yr.append(idx.year)
    
    
    dt = []
    var = [] 
    hour = []
    day = []
    month = []
    year = []
### arange daily values in an array    
    for i in range(0,30):
        dt.append(DateHour[i*24 +18 : (i+1)*24 +18])
        var.append(RR_1[i*24 +18 : (i+1)*24 +18])
        hour.append(hh[i*24 +18 : (i+1)*24 +18])
        day.append(dy[i*24 +18 : (i+1)*24 +18])
        month.append(mm[i*24 +18 : (i+1)*24 +18])
        year.append(yr[i*24 +18 : (i+1)*24 +18])
        
    dt = (np.transpose(dt))
    var = (np.transpose(var))
    hour = (np.transpose(hour))
    day = (np.transpose(day))
    month = (np.transpose(month))
    year = (np.transpose(year))
    return(dt, var, hour, day, month, year);
    
    
def valid_values_18UTC(RR_1, DateHour):
    dt, var, hour, day, month, year = arange_daily_18UTC(RR_1, DateHour)
### mask missing values with NaN
    variable = []
    dt_variable = []
    hour_variable = []
    day_variable = []
    month_variable = []
    year_variable = []
    for i in range(0,30):

        idx = np.where(var[:,i] == -9999)
        var[idx,i] = np.nan
        
        variable.append(var[~np.isnan(var[:,i]),i])
        dt_variable.append(dt[~np.isnan(var[:,i]),i])
        hour_variable.append(hour[~np.isnan(var[:,i]),i])
        day_variable.append(day[~np.isnan(var[:,i]),i])
        month_variable.append(month[~np.isnan(var[:,i]),i])
        year_variable.append(year[~np.isnan(var[:,i]),i])
        
    return(variable, dt_variable, hour_variable, day_variable, month_variable, year_variable)
