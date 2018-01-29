
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

def create_Hauk_obs(txtdir, txt_filename):
    Haukeli = pd.read_csv('%s/%s' %(txtdir, txt_filename),                    sep = ',',header=0)
    dd = Haukeli['Date']
    time = Haukeli['TimeStamp']     # Time Stamp
    dofe1 = Haukeli['RA1'].astype(float)            # total accumulation from Geonor inside DOUBLE FENCE [mm] RA1
    dofe2 = Haukeli['RA2'].astype(float)
    dofe3 = Haukeli['RA3'].astype(float)
    t = Haukeli['TA'].astype(float)            # Air temperature, PT100 [deg C] 

    speed = Haukeli['FF'].astype(float)         # wind speed 10 m @ mast 1 [m/s] FF
    direction = Haukeli['DD'].astype(float)     # wind direction 10 m @mast 1 [deg] DD
   
### exclude missing values
    dofe1 = dofe1.where(dofe1 != -999.00)
    dofe2 = dofe2.where(dofe2 != -999.00)
    dofe3 = dofe3.where(dofe3 != -999.00)
    t = t.where(t != -999.00)
    speed = speed.where(speed != -999.00)
    direction = direction.where(direction != -999.00)
    
### calculate the U, V wind component for barb plot
# http://colaweb.gmu.edu/dev/clim301/lectures/wind/wind-uv.html

# first calculate the mathematical wind direction in deg
    md_deg = 270 - direction
    for k in range(0,md_deg.shape[0]):
        if md_deg[k] <0 :
            md_deg[k] = md_deg[k] +360
    md_rad = math.pi/180. * md_deg
    u_wind = speed*np.cos(md_rad)
    v_wind = speed*np.sin(md_rad)
    
# --------- connect values from double fence and calculate mean  -------------------------------------------------------------------------

    dofe = pd.concat([dofe1, dofe2, dofe3], axis = 1)
    dofe = np.nanmean(dofe, axis = 1)
    
# --------- create array with all daily values in column  -------------------------------------------------------------------------
    ### find date 
    year = []
    month = []
    day = []
    tid = []
    ### find values
    df1 = []
    df2 = []
    df3 = []
    df = []
    temp = []
    wind_u = []
    wind_v = []
    for i in range(0,31):
        idx = datetime.datetime.strptime(str(dd[i*1440]), '%Y%m%d')
        year.append(int(idx.year))
        month.append(int(idx.month))
        day.append(int(idx.day))
        tid.append(time[i*1440: (i+1)*1440])
        df1.append(dofe1[i*1440: (i+1)*1440])
        df2.append(dofe2[i*1440: (i+1)*1440])
        df3.append(dofe3[i*1440: (i+1)*1440])
        df.append(dofe[i*1440: (i+1)*1440])
        temp.append(t[i*1440: (i+1)*1440])
        wind_u.append(u_wind[i*1440: (i+1)*1440])
        wind_v.append(v_wind[i*1440: (i+1)*1440])

    df1 = np.transpose(df1)
    df2 = np.transpose(df2)
    df3 = np.transpose(df3)
    df = np.transpose(df)
    temp = np.transpose(temp)
    wind_u = np.transpose(wind_u)
    wind_v = np.transpose(wind_v)
    return(df, temp, wind_u, wind_v, year, month, day,tid);



def create_Hauk_obs_18(txtdir, txt_filename):
    Haukeli = pd.read_csv('%s/%s' %(txtdir, txt_filename),                    sep = ',',header=0)
    dd = Haukeli['Date']
    time = Haukeli['TimeStamp']     # Time Stamp
    dofe1 = Haukeli['RA1'].astype(float)            # total accumulation from Geonor inside DOUBLE FENCE [mm] RA1
    dofe2 = Haukeli['RA2'].astype(float)
    dofe3 = Haukeli['RA3'].astype(float)
    t = Haukeli['TA'].astype(float)            # Air temperature, PT100 [deg C] 

    speed = Haukeli['FF'].astype(float)         # wind speed 10 m @ mast 1 [m/s] FF
    direction = Haukeli['DD'].astype(float)     # wind direction 10 m @mast 1 [deg] DD
    ### find date 
    dd[::1440]
    year = []
    month = []
    day = []
    for i in range(0,31):
        idx = datetime.datetime.strptime(str(dd[i*1440]), '%Y%m%d')
        year.append(int(idx.year))
        month.append(int(idx.month))
        day.append(int(idx.day))
### exclude missing values
    dofe1 = dofe1.where(dofe1 != -999.00)
    dofe2 = dofe2.where(dofe2 != -999.00)
    dofe3 = dofe3.where(dofe3 != -999.00)
    t = t.where(t != -999.00)
    speed = speed.where(speed != -999.00)
    direction = direction.where(direction != -999.00)
    
### calculate the U, V wind component for barb plot
# http://colaweb.gmu.edu/dev/clim301/lectures/wind/wind-uv.html

# first calculate the mathematical wind direction in deg
    md_deg = 270 - direction
    for k in range(0,md_deg.shape[0]):
        if md_deg[k] <0 :
            md_deg[k] = md_deg[k] +360
    md_rad = math.pi/180. * md_deg
    u_wind = speed*np.cos(md_rad)
    v_wind = speed*np.sin(md_rad)
    
# --------- connect values from double fence and calculate mean  -------------------------------------------------------------------------

    dofe = pd.concat([dofe1, dofe2, dofe3], axis = 1)
    dofe = np.nanmean(dofe, axis = 1)
    
    # --------- create array with all daily values in column  -------------------------------------------------------------------------
 
    ### find date 
    year = []
    month = []
    day = []
    tid = []
    ### find values
    df1 = []
    df2 = []
    df3 = []
    df = []
    temp = []
    wind_u = []
    wind_v = []
    for i in range(0,30):
        idx = datetime.datetime.strptime(str(dd[i*1440+1080]), '%Y%m%d')
        year.append(int(idx.year))
        month.append(int(idx.month))
        day.append(int(idx.day))
        tid.append(time[i*1440 +1080: (i+1)*1440+1080])
        df1.append(dofe1[i*1440 + 1080: (i+1)*1440+ 1080])
        df2.append(dofe2[i*1440+ 1080: (i+1)*1440+ 1080])
        df3.append(dofe3[i*1440+ 1080: (i+1)*1440+ 1080])
        df.append(dofe[i*1440+ 1080: (i+1)*1440+ 1080])
        temp.append(t[i*1440+ 1080: (i+1)*1440+ 1080])
        wind_u.append(u_wind[i*1440+ 1080: (i+1)*1440+ 1080])
        wind_v.append(v_wind[i*1440+ 1080: (i+1)*1440+ 1080])

    df1 = np.transpose(df1)
    df2 = np.transpose(df2)
    df3 = np.transpose(df3)
    df = np.transpose(df)
    temp = np.transpose(temp)
    wind_u = np.transpose(wind_u)
    wind_v = np.transpose(wind_v)
    return(df, temp, wind_u, wind_v, year, month, day,tid);