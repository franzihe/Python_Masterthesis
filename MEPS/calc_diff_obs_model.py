
# coding: utf-8

# In[ ]:

#%matplotlib inline
import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/weather_mast/')
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/MEPS/')
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/Retrieval_MEPS/')
#import netCDF4
import numpy as np
#import matplotlib.pyplot as plt
#import datetime
#import math

#import createFolder as cF
#import calc_date as cd
#import plot_sfc_spaghetti_ret as spagh
#import save_fig as SF
#import get_Haukeli_obs_data as obsDat
#import calc_48h_acc as acc
#import fill_values as fv
#import plot_vertical as pvert

import os

#import pandas as pd
#import matplotlib as mpl
#mpl.style.use('ggplot')


# In[1]:

def calc_diff(diff,variable,tot,Difference_0,Difference_1,               Difference_2, Difference_3, Difference_4,Difference_5,               Difference_6,Difference_7, Difference_8,Difference_9, var):
    #### calcualate the difference between DoFe and ensemble members and save daily values  
    
    if var == 'PP' or var == 'T2' or var == 'SP':
        for ens_memb in range(0,2):
       # print(ens_memb)
            if len(variable[ens_memb] ) == 0:
                diff[ens_memb] = np.empty(shape=(variable[0][:np.asarray(tot).shape[0],0].shape))
                diff[ens_memb][:] = np.nan
            else:
                diff[ens_memb] = variable[ens_memb][:np.asarray(tot).shape[0],0]-tot
    
        for ens_memb in range(2,10):
        #print(ens_memb)
            if len(variable[ens_memb] ) == 0:
                diff[ens_memb] = np.empty(shape=(variable[0][:np.asarray(tot).shape[0],0].shape))
                diff[ens_memb][:] = np.nan
            else: 
                diff[ens_memb] = variable[ens_memb][:np.asarray(tot).shape[0],0]-tot
            
           
    elif var == 'WD' or var == 'WS':
        for ens_memb in range(0,2):
       # print(ens_memb)
            if len(variable[ens_memb] ) == 0:
                diff[ens_memb] = np.empty(shape=(variable[0][:np.asarray(tot).shape[0]].shape))
                diff[ens_memb][:] = np.nan
            else:
                diff[ens_memb] = variable[ens_memb][:np.asarray(tot).shape[0]]-tot
    
        for ens_memb in range(2,10):
        #print(ens_memb)
            if len(variable[ens_memb] ) == 0:
                diff[ens_memb] = np.empty(shape=(variable[0][:np.asarray(tot).shape[0]].shape))
                diff[ens_memb][:] = np.nan
            else: 
                diff[ens_memb] = variable[ens_memb][:np.asarray(tot).shape[0]]-tot
        
    Difference_0.append(diff[0])
    Difference_1.append(diff[1])
    Difference_2.append(diff[2])
    Difference_3.append(diff[3])
    Difference_4.append(diff[4])
    Difference_5.append(diff[5])
    Difference_6.append(diff[6])
    Difference_7.append(diff[7])
    Difference_8.append(diff[8])
    Difference_9.append(diff[9])
    
    
    
    
    return(diff, Difference_0,Difference_1, Difference_2, Difference_3, Difference_4,Difference_5, Difference_6,Difference_7, Difference_8,Difference_9);#,all_day_max, all_day_min);



def diff_all_day(diff, all_day_max, all_day_min):
    day_diff = []
    for ens_memb in range(0,10):
        day_diff.append(diff[ens_memb])
    max_diff = []
    min_diff = []
    for i in range(0,np.asarray(day_diff).shape[1],3):
        max_diff.append(np.nanmax(np.asarray(day_diff)[:,i]))
        min_diff.append(np.nanmin(np.asarray(day_diff)[:,i]))
        
    
    all_day_max.append(max_diff)
    all_day_min.append(min_diff)
    
    return(all_day_max,all_day_min);


# In[ ]:



