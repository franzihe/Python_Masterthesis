
# coding: utf-8

# In[1]:

#%matplotlib inline
import sys
#sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
#sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/weather_mast/')
#sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/MEPS/')
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/Retrieval_MEPS/')
#import netCDF4
import numpy as np
import matplotlib.pyplot as plt
#import datetime
#import math

#import createFolder as cF
#import calc_date as cd
import plot_sfc_spaghetti_ret as spagh
#import save_fig as SF
#import get_Haukeli_obs_data as obsDat
#import calc_48h_acc as acc
#import fill_values as fv
#import plot_vertical as pvert

import os

#import pandas as pd
import matplotlib as mpl
mpl.style.use('ggplot')


# In[ ]:

champ = 255.
no1 = np.array([79,94,26])/champ
no2 = np.array([131,156,45])/champ
no3 = np.array([71,153,112])/champ
no4 = np.array([77,111,157])/champ
no5 = np.array([157,58,55])/champ
no6 = np.array([211,120,50])/champ
no7 = np.array([218,181,70])/champ

colors = [no1, no2, no3, no4, no5, no6, no7]


# In[2]:

def plt_variable(lead_time_sfc,wd_MEPS,WD,time_EM_mean, model_var_mean,var,xdays,title):
    
    fig = plt.figure(figsize=(20,7))
    ax = plt.axes()
# Vertical line to show end of day
    ax.axvline(0,color = spagh.vert_col, linewidth = 3)
    ax.axvline(24,color = spagh.vert_col, linewidth = 3)
    ax.axvline(48,color = spagh.vert_col, linewidth = 3)




### ensemble member
    for ens_memb in range(2,10):
        ax.plot(lead_time_sfc[ens_memb],wd_MEPS[ens_memb],color = spagh.memb_col,
           linestyle='-', label='_nolegend_')
    ax.plot(lead_time_sfc[1], wd_MEPS[1], color = spagh.memb_col,
           linestyle = '-', label = 'ensemble member')
    ax.plot(lead_time_sfc[0], wd_MEPS[0], 'k', linewidth = 4, label = 'deterministic')

### observation
    plt.plot(np.arange(0,np.asarray(WD).shape[0]), WD,  markersize=20,  linestyle='--', 
         label = 'observation', linewidth= 4)
### ensemble mean
    ax.plot(time_EM_mean[:], np.asarray(model_var_mean)[:], color='dodgerblue', linewidth = 3.5, 
            linestyle = '--', label = 'ensemble mean') 

### fine tuning
    lgd = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.37),
          fancybox=True, shadow=True, ncol=3, fontsize=spagh.label_fs)
    frame = lgd.get_frame()
    frame.set_facecolor('white')

# xaxis
    a = lead_time_sfc[0][0:48]
    ax.set_xlim(-0.5,49-0.5)
    ax.set_xlabel('time', fontsize=spagh.label_fs)
    ax.set_xticks(np.arange(0,49,3))
  #  dates = pvert.dates_plt_00(hour, mm, dy, yr, ini_day)
    
    ax.set_xticklabels(xdays, rotation = 25, fontsize = spagh.tick_fs)
# title
    ax.set_title(title, fontsize=spagh.fontsize, color =spagh.blue )    
    
    if var == 'WD':
        # Horizontal line to show Wind direction
        ax.axhline(90,color=spagh.vert_col, linewidth= 3)
        ax.axhline(180,color=spagh.vert_col, linewidth= 3)
        ax.axhline(270,color=spagh.vert_col, linewidth= 3)
        ax.axhline(360,color=spagh.vert_col, linewidth= 3)
        # yaxis
        ax.set_ylabel('Wind direction', fontsize=spagh.label_fs)
        ax.set_ylim(-0.5,360)
        T = np.arange(0,361,45)
        ax.set_yticks(T)
        ax.set_yticklabels(['N', '', 'E', '','S', '', 'W', '' , 'N'],fontsize = spagh.tick_fs)
    elif var == 'WS':
        # yaxis
        ax.set_ylabel('Wind speed [m$\,$s$^{-1}$]', fontsize = spagh.label_fs)
        ax.set_ylim(0,30)
        ax.set_yticks(np.arange(0,32.5,2.5))
        ax.set_yticklabels([0, '', 5, '',10,'',15,'',20,'',25,'',30], fontsize=spagh.label_fs)
    elif var == 'T2':
        ax.axhline(0,color=spagh.vert_col, linewidth= 3)
        # yaxis
        ax.set_ylabel('Air Temperature [$^\circ$C]', fontsize=spagh.label_fs)
        ax.set_ylim(-9,6)
        T = np.arange(-9,7)
        ax.set_yticks(T)
        ax.set_yticklabels([-9, '' , '', -6, '' , '', -3, '' , '', 0, 
                            '' , '', 3, '' , '', 6], fontsize=spagh.tick_fs)
    elif var == 'SP':
        # yaxis
        ax.set_ylabel('Sea Level Pressure [hPa]', fontsize=spagh.label_fs)
        ax.set_ylim(975, 1040)
        ax.set_yticks(np.arange(975,1045,5))
        ax.set_yticklabels(['' , 980,'', '','', 1000, '','','', 1020, '','','', 1040], fontsize=spagh.tick_fs)
    elif var == 'PP':
        # yaxis
        ax.set_ylabel('Precipitation amount [mm]', fontsize=spagh.label_fs)
        ax.set_ylim(-0.5,80)
        ax.set_yticks(np.arange(0,90,5))
        ax.set_yticklabels([0, '',10,'',20,'',30,'',40,'',50,'',60,'',70,'',80,'',90],fontsize = spagh.tick_fs)


        

# tight layout
    plt.tight_layout()
    
    return(lgd)




# In[3]:

def plt_scatter_obs_model(tot, precipitation_amount_acc,colors,var,label):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    
#    ax.plot([-0.5, 80], [-0.5, 80.], linestyle='-',color=spagh.memb_col)
    for ens_memb in range(0,1):
        if len(precipitation_amount_acc[ens_memb]) == 0:
            continue
        else:
            ax.scatter(tot,precipitation_amount_acc[ens_memb][:np.asarray(tot).shape[0]],color=colors, 
                   alpha = 0.7, s = 150,
                      label=label)
    for ens_memb in range(1,2):
        if len(precipitation_amount_acc[ens_memb]) == 0:
            continue
        else:
            ax.scatter(tot,precipitation_amount_acc[ens_memb][:np.asarray(tot).shape[0]],color=colors, 
                   alpha = 0.7, s = 150,
                      label='_nolegend_')
            
    for ens_memb in range(2,10):
        if len(precipitation_amount_acc[ens_memb]) == 0:
            continue
        else:
            ax.scatter(tot[::3],precipitation_amount_acc[ens_memb][:np.asarray(tot).shape[0]],color=colors, 
                   alpha = 0.7, s = 150,
                      label='_nolegend_')
### fine tuning
    lgd = ax.legend(loc='lower right',
         #fancybox=True, shadow=True, #ncol=3, 
          fontsize=spagh.label_fs-8)
    frame = lgd.get_frame()
    frame.set_facecolor('white')
    plt.setp(lgd.get_texts(), color=spagh.blue)
    
    
    
    if var == 'WD':
        ax.plot([0, 360], [0, 360.], linestyle='-',color=spagh.memb_col) 
        # Horizontal line to show Wind direction
        ax.axhline(90,color=spagh.vert_col, linewidth= 3)
        ax.axhline(180,color=spagh.vert_col, linewidth= 3)
        ax.axhline(270,color=spagh.vert_col, linewidth= 3)
        ax.axhline(360,color=spagh.vert_col, linewidth= 3)
        # Vertical line to show Wind direction
        ax.axvline(90,color=spagh.vert_col, linewidth= 3)
        ax.axvline(180,color=spagh.vert_col, linewidth= 3)
        ax.axvline(270,color=spagh.vert_col, linewidth= 3)
        ax.axvline(360,color=spagh.vert_col, linewidth= 3)
        # yaxis
        ax.set_ylim(0,360)
        ax.set_yticks(np.arange(0,361,45)) 
        ax.set_yticklabels(['N', '', 'E', '', 'S','','W','','N'],fontsize = spagh.tick_fs)
        # xaxis
        ax.set_xlim(0,360)
        ax.set_xticks(np.arange(0,361,45))  
        ax.set_xticklabels(['N', '', 'E', '', 'S','','W','','N'], fontsize = spagh.tick_fs)
        # title
        ax.set_title('Wind direction', fontsize=spagh.fontsize) 
    elif var == 'WS':
        ax.plot([0, 30], [0, 30.], linestyle='-',color=spagh.memb_col) 
        # yaxis
        ax.set_ylim(0,30)
        ax.set_yticks(np.arange(0,32.5,2.5))
        ax.set_yticklabels([0, '', 5, '',10,'',15,'',20,'',25,'',30], fontsize=spagh.label_fs)
        # xaxis
        ax.set_xlim(0,30)
        ax.set_xticks(np.arange(0,32.5,2.5))
        ax.set_xticklabels([0, '', 5, '',10,'',15,'',20,'',25,'',30], fontsize=spagh.label_fs)
        # title
        ax.set_title('Wind speed [m$\,$s$^{-1}$]', fontsize=spagh.fontsize) 
    elif var == 'T2':
        ax.plot([-9,6], [-9,6], linestyle='-',color=spagh.memb_col) 
        ax.axhline(0,color=spagh.vert_col, linewidth= 3)
        ax.axvline(0,color=spagh.vert_col, linewidth= 3)
        # yaxis
        ax.set_ylim(-9,6)
        T = np.arange(-9,7)
        ax.set_yticks(T)
        ax.set_yticklabels([-9, '' , '', -6, '' , '', -3, '' , '', 0, 
                            '' , '', 3, '' , '', 6], fontsize=spagh.tick_fs)
        # xaxis
        ax.set_xlim(-9,6)
        ax.set_xticks(T)
        ax.set_xticklabels([-9, '' , '', -6, '' , '', -3, '' , '', 0, 
                            '' , '', 3, '' , '', 6], fontsize=spagh.tick_fs)
        # title
        ax.set_title('Air Temperature [$^\circ$C]', fontsize=spagh.fontsize) 
    elif var == 'SP':
        ax.plot([975,1040], [975,1040], linestyle='-',color=spagh.memb_col) 
        # yaxis
        ax.set_ylim(975, 1040)
        ax.set_yticks(np.arange(975,1045,5))
        ax.set_yticklabels(['' , 980,'', '','', 1000, '','','', 1020, '','','', 1040], fontsize=spagh.tick_fs)
        # xaxis
        ax.set_xlim(975, 1040)
        ax.set_xticks(np.arange(975,1045,5))
        ax.set_xticklabels(['' , 980,'', '','', 1000, '','','', 1020, '','','', 1040], fontsize=spagh.tick_fs)
        # title
        ax.set_title('Sea Level Pressure [hPa]', fontsize=spagh.fontsize)
    elif var == 'PP':
        ax.plot([0,90], [0,90], linestyle = '-', color=spagh.memb_col)
        # yaxis
        ax.set_ylim(0,80)
        ax.set_yticks(np.arange(0,90,5))
        ax.set_yticklabels([0, '',10,'',20,'',30,'',40,'',50,'',60,'',70,'',80,'',90],fontsize = spagh.tick_fs)
        # xaxis
        ax.set_xlim(0,80)
        ax.set_xticks(np.arange(0,90,5))
        ax.set_xticklabels([0, '',10,'',20,'',30,'',40,'',50,'',60,'',70,'',80,'',90],fontsize = spagh.tick_fs)
        ax.set_title('Precipitation amount [mm]', fontsize=spagh.fontsize)

        
    ax.set_ylabel('MEPS forecast', fontsize=spagh.label_fs)
    ax.set_xlabel('observation', fontsize=spagh.label_fs)


# tight layout
    plt.tight_layout()


# In[4]:

def plt_scatter_diff(diff, lead_time_sfc, tot,colors, var,label):
    
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
# Vertical line to see if too high or too little
    ax.axvline(0, color =spagh.vert_col, linewidth=3)

# Horizontal line to show end of day
    ax.axhline(0,color = spagh.vert_col, linewidth = 3)
    ax.axhline(24,color = spagh.vert_col, linewidth = 3)
    ax.axhline(48,color = spagh.vert_col, linewidth = 3)

    
    for ens_memb in range(0,1):
        ax.scatter(diff[ens_memb],np.arange(0,49),
                   color=colors, alpha = 0.7, s = 150,
                    label=label) 
    for ens_memb in range(1,10):
        ax.scatter(diff[ens_memb],np.arange(0,49),
                   color=colors, alpha = 0.7, s = 150)#,
              #label='_nolegend_')
    
### fine tuning
    lgd = ax.legend(loc='lower right',
         #fancybox=True, shadow=True, #ncol=3, 
          fontsize=spagh.label_fs-8)
    frame = lgd.get_frame()
    frame.set_facecolor('white')
    plt.setp(lgd.get_texts(), color=spagh.blue)
    
# yaxis
    a = lead_time_sfc[0][0:48]
    ax.set_ylim(-0.5,49-0.5)
    ax.set_ylabel('forecast time', fontsize=spagh.label_fs)
    ax.set_yticks(np.arange(0,49))
    
    xdays = [0, '', '', 3, '' , '',
        6,'','', 9,'','',12,'','',15,'','',18,'','',
         21, '','',
        24, '','',27, '','', 30, '','',
        33,'','', 36,'','',39,'','',42,'','',45,'','',
        48]
    ax.set_yticklabels(xdays, #rotation = 25, 
                   fontsize = spagh.tick_fs)

    if var == 'WD':
        # Horizontal line to show Wind direction
        ax.axvline(45,color=spagh.vert_col, linewidth= 3)
        ax.axvline(90,color=spagh.vert_col, linewidth= 3)
        ax.axvline(90+45,color=spagh.vert_col, linewidth= 3)
        ax.axvline(180,color=spagh.vert_col, linewidth= 3)
        ax.axvline(-45,color=spagh.vert_col, linewidth= 3)
        ax.axvline(-90,color=spagh.vert_col, linewidth= 3)
        ax.axvline(-90-45,color=spagh.vert_col, linewidth= 3)
        ax.axvline(-180,color=spagh.vert_col, linewidth= 3)
        # xaxis
        ax.set_xlim(-112.5,112.5)
        ax.set_xticks(np.arange(-112.5,135,22.5))  
        ax.set_xticklabels([ '', '-90', '', '-45','','0','','45','','90'], fontsize = spagh.tick_fs)
        # title
        ax.set_title('Wind direction', fontsize=spagh.fontsize) 
        ax.set_xlabel('Difference [$^\circ$]' , fontsize=spagh.label_fs)
    elif var == 'WS':
        # xaxis
        ax.set_xlim(-10,15)
        ax.set_xticks(np.arange(-10,17.5,2.5))
        ax.set_xticklabels([-10,'', -5, '',0, '', 5, '',10,'',15], fontsize=spagh.label_fs)
        # title
        ax.set_title('Wind speed', fontsize=spagh.fontsize) 
        ax.set_xlabel('Difference [m$\,$s$^{-1}$]' , fontsize=spagh.label_fs)
        
    elif var == 'T2':
        # xaxis
        ax.set_xlim(-9,4)
        ax.set_xticks(np.arange(-9,5))
        ax.set_xticklabels([-9, '' , '', -6, '' , '', -3, '' , '', 0, 
                            '' , '', 3, '' , ''], fontsize=spagh.tick_fs)
        # title
        ax.set_title('Air Temperature', fontsize=spagh.fontsize) 
        ax.set_xlabel('Difference [$^\circ$C]' , fontsize=spagh.label_fs)
        
    elif var == 'SP':
        # xaxis
        ax.set_xlim(-8, 8)
        ax.set_xticks(np.arange(-8,9))
        ax.set_xticklabels([-8,'' , -6,'', -4,'',-2,'', 0, '',2,'',4,'',6,'',8], fontsize=spagh.tick_fs)
        # title
        ax.set_title('Sea Level Pressure', fontsize=spagh.fontsize)
        ax.set_xlabel('Difference [hPa]' , fontsize=spagh.label_fs)
    elif var == 'PP':
        # xaxis
        ax.set_xlim(-15,45)
        ax.set_xticks(np.arange(-15,45,5))
        ax.set_xticklabels(['', -10, '', 0, '', 10, '', 20, '',30, '',40],fontsize = spagh.tick_fs)
        ax.set_title('Precipitation amount' , fontsize=spagh.fontsize)
        ax.set_xlabel('Difference [mm]' , fontsize=spagh.label_fs)

        
# tight layout
    plt.tight_layout()
    
    
#    return(lgd);


# In[ ]:

def plt_all_day_diff(Difference,lead_time_sfc,tot,var,day_range,
                         in_day, cal_mon,
                              cal_year,in_hh):
    #### Plot difference of all days in scatter plot

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
# Vertical line to see if too high or too little
    ax.axvline(0, color =spagh.vert_col, linewidth=3)

# Horizontal line to show end of day
    ax.axhline(0,color = spagh.vert_col, linewidth = 3)
    ax.axhline(24,color = spagh.vert_col, linewidth = 3)
    ax.axhline(48,color = spagh.vert_col, linewidth = 3)


    for ens_memb in range(0,1):
        for i in day_range:
            plt.scatter(np.asarray(Difference[ens_memb])[i,:],lead_time_sfc[ens_memb][:np.asarray(tot).shape[0]],
                        color = colors[i],
                    alpha = 0.8, s = 200,
                  label='%s %s %s 0%s UTC' %(in_day[i],
                                        cal_mon[i],cal_year[i],in_hh[i]) )
    
    for ens_memb in range(1,10):
        for i in day_range:
            plt.scatter(np.asarray(Difference[ens_memb])[i,:],np.arange(0,49),color = colors[i],
                alpha = 0.8, s = 200,label='_nolegend_' )   
            
    ### fine tuning
    lgd = ax.legend(loc='center left',bbox_to_anchor=(1, .75),
         fancybox=True, shadow=True, #ncol=3, 
          fontsize=spagh.label_fs-4)
    lgd.set_title( title= 'initialised:')#, fontsize=spagh.label)
    lgd.get_title().set_fontsize(spagh.label_fs-4)
    plt.setp(lgd.get_texts(), color=spagh.blue)


#lgd = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.37),
 #         fancybox=True, shadow=True, ncol=3, fontsize=spagh.label_fs)
    frame = lgd.get_frame()
    frame.set_facecolor('white')
    
# yaxis
#a = lead_time_sfc[0][0:48]
    ax.set_ylim(-0.5,49-0.5)
    ax.set_ylabel('forecast time', fontsize=spagh.label_fs)
    ax.set_yticks(np.arange(0,49))
    
    xdays = [0, '', '', 3, '' , '',
        6,'','', 9,'','',12,'','',15,'','',18,'','',
         21, '','',
        24, '','',27, '','', 30, '','',
        33,'','', 36,'','',39,'','',42,'','',45,'','',
        48]
    ax.set_yticklabels(xdays, #rotation = 25, 
                   fontsize = spagh.tick_fs)


    if var == 'WD':
        # Horizontal line to show Wind direction
        ax.axvline(45,color=spagh.vert_col, linewidth= 3)
        ax.axvline(90,color=spagh.vert_col, linewidth= 3)
        ax.axvline(90+45,color=spagh.vert_col, linewidth= 3)
        ax.axvline(180,color=spagh.vert_col, linewidth= 3)
        ax.axvline(-45,color=spagh.vert_col, linewidth= 3)
        ax.axvline(-90,color=spagh.vert_col, linewidth= 3)
        ax.axvline(-90-45,color=spagh.vert_col, linewidth= 3)
        ax.axvline(-180,color=spagh.vert_col, linewidth= 3)
        # xaxis
        ax.set_xlim(-112.5,112.5)
        ax.set_xticks(np.arange(-112.5,135,22.5))  
        ax.set_xticklabels([ '', '-90', '', '-45','','0','','45','','90'], fontsize = spagh.tick_fs)
        # title
        ax.set_title('Wind direction', fontsize=spagh.fontsize) 
        ax.set_xlabel('Difference [$^\circ$]' , fontsize=spagh.label_fs)
    elif var == 'WS':
        # xaxis
        ax.set_xlim(-10,15)
        ax.set_xticks(np.arange(-10,17.5,2.5))
        ax.set_xticklabels([-10,'', -5, '',0, '', 5, '',10,'',15], fontsize=spagh.label_fs)
        # title
        ax.set_title('Wind speed', fontsize=spagh.fontsize) 
        ax.set_xlabel('Difference [m$\,$s$^{-1}$]' , fontsize=spagh.label_fs)
        
    elif var == 'T2':
        # xaxis
        ax.set_xlim(-9,4)
        ax.set_xticks(np.arange(-9,5))
        ax.set_xticklabels([-9, '' , '', -6, '' , '', -3, '' , '', 0, 
                            '' , '', 3, '' , ''], fontsize=spagh.tick_fs)
        # title
        ax.set_title('Air Temperature', fontsize=spagh.fontsize) 
        ax.set_xlabel('Difference [$^\circ$C]' , fontsize=spagh.label_fs)
        
    elif var == 'SP':
        # xaxis
        ax.set_xlim(-8, 8)
        ax.set_xticks(np.arange(-8,9))
        ax.set_xticklabels([-8,'' , -6,'', -4,'',-2,'', 0, '',2,'',4,'',6,'',8], fontsize=spagh.tick_fs)
        # title
        ax.set_title('Sea Level Pressure', fontsize=spagh.fontsize)
        ax.set_xlabel('Difference [hPa]' , fontsize=spagh.label_fs)
    elif var == 'PP':
        # xaxis
        ax.set_xlim(-15,45)
        ax.set_xticks(np.arange(-15,45,5))
        ax.set_xticklabels(['', -10, '', 0, '', 10, '', 20, '',30, '',40],fontsize = spagh.tick_fs)
        ax.set_title('Precipitation amount' , fontsize=spagh.fontsize)
        ax.set_xlabel('Difference [mm]', fontsize=spagh.fontsize)

# tight layout
    plt.tight_layout()
    return(lgd);


def plt_scatter_all_days(obs_Pres,Pressure_all_day,var,day_range, in_day, cal_mon,
                              cal_year,in_hh,x_obs,intercept_obs,gradient_obs):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)

    for i in day_range:
        plt.scatter(np.asarray(obs_Pres)[i,:],
                np.asarray(Pressure_all_day[0])[i,:np.asarray(obs_Pres).shape[1]],color=colors[i],
               alpha = 0.7, s = 150,
                      label= '%s %s %s 0%s UTC' %(in_day[i],
                                        cal_mon[i],cal_year[i],in_hh[i]))
    
        for ens_memb in range(1,10):
            plt.scatter(np.asarray(obs_Pres)[i,:],
                np.asarray(Pressure_all_day[ens_memb])[i,:np.asarray(obs_Pres).shape[1]],color=colors[i],
               alpha = 0.7, s = 150,
                      label='_nolegend_')
        if var == 'WD':
            ax.plot([0, 360], [intercept_obs[i],intercept_obs[i] + gradient_obs[i]*360],  
                    color =colors[i],linewidth = 3.,
            alpha=0.8,)
        elif var == 'WS':
            ax.plot([0, 30], [intercept_obs[i],intercept_obs[i] + gradient_obs[i]*30],  
                    color =colors[i],linewidth = 3.,
            alpha=0.8,)
        elif var == 'T2':
            ax.plot([-9,6], [intercept_obs[i] + gradient_obs[i]*(-9), intercept_obs[i] + gradient_obs[i]*6],  
                    color =colors[i],linewidth = 3.,
            alpha=0.8,)
        elif var == 'SP':
            ax.plot([975,1040], [intercept_obs[i] + gradient_obs[i]*(975), intercept_obs[i] + gradient_obs[i]*1040],  
                    color =colors[i],linewidth = 3.,
            alpha=0.8,)
        elif var == 'PP':
            ax.plot([0,90], [intercept_obs[i],intercept_obs[i] + gradient_obs[i]*90],  
                    color =colors[i],linewidth = 3.,
            alpha=0.8,)
#        ax.plot(x_obs[i], intercept_obs[i] + gradient_obs[i]*x_obs[i],  
#                    color =colors[i],linewidth = 5.,
#            alpha=0.8, )
        ax.text(0.55,0.58-i/12, 'y = {:.2f} + {:.2f}x'.format(intercept_obs[i], gradient_obs[i]),
            verticalalignment ='top', horizontalalignment='left', color = colors[i],
             transform = ax.transAxes, fontsize = spagh.label_fs-4,
             bbox={'facecolor':'white','alpha':.8,'pad':10})
        
### fine tuning
    lgd = ax.legend(loc='center left',bbox_to_anchor=(1, .75),
         fancybox=True, shadow=True, #ncol=3, 
          fontsize=spagh.label_fs-4)
    lgd.set_title( title= 'initialised:')#, fontsize=spagh.label)
    lgd.get_title().set_fontsize(spagh.label_fs-4)
    plt.setp(lgd.get_texts(), color=spagh.blue)


    frame = lgd.get_frame()
    frame.set_facecolor('white')
    
    if var == 'WD':
        ax.plot([0, 360], [0, 360.], linestyle='-',color=spagh.memb_col) 
        # Horizontal line to show Wind direction
        ax.axhline(90,color=spagh.vert_col, linewidth= 3)
        ax.axhline(180,color=spagh.vert_col, linewidth= 3)
        ax.axhline(270,color=spagh.vert_col, linewidth= 3)
        ax.axhline(360,color=spagh.vert_col, linewidth= 3)
        # Vertical line to show Wind direction
        ax.axvline(90,color=spagh.vert_col, linewidth= 3)
        ax.axvline(180,color=spagh.vert_col, linewidth= 3)
        ax.axvline(270,color=spagh.vert_col, linewidth= 3)
        ax.axvline(360,color=spagh.vert_col, linewidth= 3)
        # yaxis
        ax.set_ylim(0,360)
        ax.set_yticks(np.arange(0,361,45)) 
        ax.set_yticklabels(['N', '', 'E', '', 'S','','W','','N'],fontsize = spagh.tick_fs)
        # xaxis
        ax.set_xlim(0,360)
        ax.set_xticks(np.arange(0,361,45))  
        ax.set_xticklabels(['N', '', 'E', '', 'S','','W','','N'], fontsize = spagh.tick_fs)
        # title
        ax.set_title('Wind direction', fontsize=spagh.fontsize) 
    elif var == 'WS':
        ax.plot([0, 30], [0, 30.], linestyle='-',color=spagh.memb_col) 
        # yaxis
        ax.set_ylim(0,30)
        ax.set_yticks(np.arange(0,32.5,2.5))
        ax.set_yticklabels([0, '', 5, '',10,'',15,'',20,'',25,'',30], fontsize=spagh.label_fs)
        # xaxis
        ax.set_xlim(0,30)
        ax.set_xticks(np.arange(0,32.5,2.5))
        ax.set_xticklabels([0, '', 5, '',10,'',15,'',20,'',25,'',30], fontsize=spagh.label_fs)
        # title
        ax.set_title('Wind speed [m$\,$s$^{-1}$]', fontsize=spagh.fontsize) 
    elif var == 'T2':
        ax.plot([-9,6], [-9,6], linestyle='-',color=spagh.memb_col) 
        ax.axhline(0,color=spagh.vert_col, linewidth= 3)
        ax.axvline(0,color=spagh.vert_col, linewidth= 3)
        # yaxis
        ax.set_ylim(-9,6)
        T = np.arange(-9,7)
        ax.set_yticks(T)
        ax.set_yticklabels([-9, '' , '', -6, '' , '', -3, '' , '', 0, 
                            '' , '', 3, '' , '', 6], fontsize=spagh.tick_fs)
        # xaxis
        ax.set_xlim(-9,6)
        ax.set_xticks(T)
        ax.set_xticklabels([-9, '' , '', -6, '' , '', -3, '' , '', 0, 
                            '' , '', 3, '' , '', 6], fontsize=spagh.tick_fs)
        # title
        ax.set_title('Air Temperature [$^\circ$C]', fontsize=spagh.fontsize) 
    elif var == 'SP':
        ax.plot([975,1040], [975,1040], linestyle='-',color=spagh.memb_col) 
        # yaxis
        ax.set_ylim(975, 1040)
        ax.set_yticks(np.arange(975,1045,5))
        ax.set_yticklabels(['' , 980,'', '','', 1000, '','','', 1020, '','','', 1040], fontsize=spagh.tick_fs)
        # xaxis
        ax.set_xlim(975, 1040)
        ax.set_xticks(np.arange(975,1045,5))
        ax.set_xticklabels(['' , 980,'', '','', 1000, '','','', 1020, '','','', 1040], fontsize=spagh.tick_fs)
        # title
        ax.set_title('Sea Level Pressure [hPa]', fontsize=spagh.fontsize)
    elif var == 'PP':
        ax.plot([0,90], [0,90], linestyle = '-', color=spagh.memb_col)
        # yaxis
        ax.set_ylim(0,80)
        ax.set_yticks(np.arange(0,90,5))
        ax.set_yticklabels([0, '',10,'',20,'',30,'',40,'',50,'',60,'',70,'',80,'',90],fontsize = spagh.tick_fs)
        # xaxis
        ax.set_xlim(0,80)
        ax.set_xticks(np.arange(0,90,5))
        ax.set_xticklabels([0, '',10,'',20,'',30,'',40,'',50,'',60,'',70,'',80,'',90],fontsize = spagh.tick_fs)
        ax.set_title('Precipitation amount [mm]', fontsize=spagh.fontsize)
    
    
        
    ax.set_ylabel('MEPS forecast', fontsize=spagh.label_fs)
    ax.set_xlabel('observation', fontsize=spagh.label_fs)


    # tight layout
    plt.tight_layout()
    
    return(lgd);

