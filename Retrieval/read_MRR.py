
# coding: utf-8

# In[ ]:

import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/MEPS')
import netCDF4
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import colormaps as cmaps
import calc_date as cd
import save_fig as SF
import createFolder as cF
import calc_station_properties as cs
from matplotlib import gridspec



# In[ ]:

nc_dir = '../../Data/MRR/original_data/'

s_nc = 1
nc_save_dir = '../../Data/MRR/processed_MRR/'
cF.createFolder(nc_save_dir)

sfig = 1
fig_dir = '../../Figures/MRR_ref/'
cF.createFolder(fig_dir)
form = 'png'



year = '2016'
mon = '12'
t = ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
#t = ['24']

fs = 22
#file_out = 'VMRR_data_%s%s%s.txt' %(year,mon,day)


# In[ ]:

date_blue = np.array([1,74,159])/255.           # for the date

def plt_refl(tid, h_mid, avgref, calday, day, calmon, year):
### plot reflectivity
    levels = np.arange(-10,30,0.2)

    fig = plt.figure(figsize=(20,7))
    gs = gridspec.GridSpec(7,1)

    ax0 = fig.add_subplot(gs[:6,:])
    CS = ax0.contourf(np.asarray(tid), np.asarray(h_mid) , np.asarray(avgref), 
                  levels, cmap='jet')
# add colorbar
    cbaxes = fig.add_axes([0.14, 0.1, .75, .02] )   #[left, bottom, width, height] 
    cbar = plt.colorbar(CS, orientation = 'horizontal', cax=cbaxes)
    cbar.ax.set_xlabel('MRR reflectivity [dBz]', fontsize = 22)
    cbar.ax.tick_params(labelsize = 20)

# labels
    times = [0, 3, 6, 9,12, 15, 18, 21, 24]
    ax0.set_xticks(np.arange(0,60*60*25,3*60*60))
    ax0.set_xticklabels(times, fontsize = 20)
    ax0.set_xlabel('time [hours]', fontsize = 22)

    ax0.set_ylabel('height [km]', fontsize = 22)
    ax0.set_ylim(0,3.5)
    ax0.set_yticks(np.arange(0,3500.,500.))
    yl = [0., '' , 1.0, '' , 2., '' , 3.]
    ax0.set_yticklabels(yl, fontsize = 20)
    
    
# textbox
    ax0.text(0.02,0.96, '%s, %s %s %s' %(calday, day, calmon, year), verticalalignment = 'top',  
         horizontalalignment='left',
             transform = ax0.transAxes,
            color =date_blue, fontsize=fs,
           bbox={'facecolor':'white','alpha':1., 'pad':10})



# In[ ]:

def read_and_mask(fn,var_name, fill_value):
    #### Read in variable 'Ze' (time = 1440,range = 31)
    var = fn.variables[var_name]
# fill value, where Ze = -9999, fill_value = -50.
    mask = np.ma.getmaskarray(var[:,:])
    var = np.ma.array(var[:,:], mask = mask, fill_value = fill_value)
    var = var.filled()
    return(var);


# In[ ]:





