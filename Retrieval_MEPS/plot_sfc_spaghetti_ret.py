
# coding: utf-8

# In[1]:
import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/MEPS/')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import plot_vertical as pvert 
import matplotlib as mpl
mpl.style.use('ggplot')



# In[2]:

### Define colorbar colors
champ = 255.
blue = np.array([1,74,159])/champ           # for the date
memb_col = np.array([99,99,99])/champ       # ensemble member color
vert_col = np.array([197,197,197])/champ    # vertical line for day marker
#dofe = np.array([64,180,233])/champ         # color for double fence measurement
dofe = np.array([125,98,179])/champ

fontsize = 30.
tick_fs = fontsize-2
label_fs = fontsize


# In[ ]:
def spaghetti_sfc_dofe(lead_time_sfc, variable, dofence_60, #time_sfc, 
              acc_ret,
              Xmax, day, var_name, 
              h_p18, m_p18, d_p18, y_p18, ini_day,
            unit, title, tid, doublefence):
    
    fig = plt.figure(figsize=(20,7))
    ax = plt.axes()
# Vertical line to show end of day
    ax.axvline(0,color = vert_col, linewidth = 3)
    ax.axvline(24,color = vert_col, linewidth = 3)
    ax.axvline(48,color = vert_col, linewidth = 3)
    if doublefence == 1:
## double fence    
#        plt.plot(np.arange(0,Xmax), np.asarray(dofence_60)[:,(int(day)-1)], marker = 'H', markersize=20, 
 #           color = dofe, linestyle = 'None', label = 'double fence')
        plt.plot(np.arange(0,Xmax), dofence_60, marker = 'H', markersize=20, 
            color = dofe, linestyle = 'None', label = 'double fence')
## ensemble member         
    for ens_memb in range(2,10):
        ax.plot(lead_time_sfc[ens_memb][:Xmax], variable[ens_memb][:Xmax], color = memb_col,
           linestyle = '-', label='_nolegend_')
    ax.plot(lead_time_sfc[1][:Xmax], variable[1][:Xmax], color = memb_col,
           linestyle = '-', label = 'ensemble member')
    ax.plot(lead_time_sfc[0][:Xmax], variable[0][:Xmax], 'k', linewidth = 4, label = 'best guess')
    
## retrieval
    ax.plot(np.arange(0, np.asarray(acc_ret).shape[0]/60,1/60), acc_ret, linestyle = (0, (3, 1, 1, 1)), 
         color = 'orange', label = 'retrieved snowfall',linewidth=6)
### fine tuning
    lgd = plt.legend(loc='upper left',fontsize=fontsize)
    frame = lgd.get_frame()
    frame.set_facecolor('white')
#    ax.grid()

# yaxis
    ax.set_ylabel('%s %s %s' %(var_name[0], var_name[1], unit), fontsize=label_fs)
    ax.set_ylim(-0.5,80)
    T = np.arange(0,90,10)
    ax.set_yticks(T)
    ax.set_yticklabels(T,fontsize = tick_fs)

# xaxis
    a = lead_time_sfc[0][0:48]
#    ax.set_xlim(-0.5,Xmax+0.5)
    ax.set_xlim(-0.5,Xmax-0.5)
    ax.set_xlabel('time', fontsize=label_fs)
    ax.set_xticks(np.arange(0,Xmax,6))
    if tid == '18':
#        dates = pvert.dates_plt_18(time_sfc)
        dates = pvert.dates_plt_18(h_p18, m_p18, d_p18, y_p18, ini_day)
    if tid == '00':
#        dates = pvert.dates_plt(time_sfc)
        dates = pvert.dates_plt_00(h_p18, m_p18, d_p18, y_p18, ini_day)
    ax.set_xticklabels(dates, rotation = 25, fontsize = tick_fs)
# title
    ax.set_title(title, fontsize=fontsize, color =blue )
# tight layout
    plt.tight_layout()




def spaghetti_sfc_dofe_Morten(lead_time_sfc, variable, dofence_60, #time_sfc, 
                 Xmax, day, var_name, unit, title, tid):
    fig = plt.figure(figsize=(20,7))
    ax = plt.axes()
# Vertical line to show end of day
    ax.axvline(0,color = vert_col, linewidth = 3)
    ax.axvline(24,color = vert_col, linewidth = 3)
    ax.axvline(48,color = vert_col, linewidth = 3)
## double fence    
#### Morten
    plt.plot(np.arange(0,np.asarray(dofence_60[:Xmax]).shape[0]), dofence_60[:Xmax], marker = 'o', markersize=20, 
            color = 'k', linestyle = 'None', label = 'double fence')


## ensemble member         
    for ens_memb in range(2,10):
        ax.plot(lead_time_sfc[ens_memb][:Xmax], variable[ens_memb][:Xmax], color = memb_col,
           linestyle = '-', label='_nolegend_')
    ax.plot(lead_time_sfc[1][:Xmax], variable[1][:Xmax], color = memb_col,
           linestyle = '-', label = 'ensemble member')
    ax.plot(lead_time_sfc[0][:Xmax], variable[0][:Xmax], 'k', linewidth = 4, label = 'best guess')



### fine tuning
    lgd = plt.legend(loc='upper left',fontsize=26)
    ax.grid()

# yaxis
    ax.set_ylabel('%s %s %s' %(var_name[0], var_name[1], unit), fontsize = fontsize)
    ax.set_ylim(-0.5,65)
    T = np.arange(0,70,10)
    ax.set_yticks(T)
    ax.set_yticklabels(T,fontsize = tick_fs)

# xaxis
    b = np.arange(0,Xmax+5,5)
    ax.set_xlim(-0.5,Xmax-0.5)
    ax.set_xlabel('lead time', fontsize = label_fs)
    ax.set_xticks(np.arange(0,Xmax,5))

    ax.set_xticklabels(b, fontsize = tick_fs)
# title
    ax.set_title(title, fontsize=fontsize, color ='k' )
# tight layout
    plt.tight_layout()


#######################################
def spaghetti_sfc_dofe_wind(lead_time_sfc, lead_time_em, variable, dofence_60, #time_sfc, 
              acc_ret, uwind,vwind, uwind_dofe, vwind_dofe,
              Xmax, day, var_name, 
              h_p18, m_p18, d_p18, y_p18, ini_day,
            unit, title, tid, doublefence):
          
#    fig = plt.figure(figsize=(20,11))
    fig = plt.figure(figsize=(18.,12.5))
    gs = GridSpec(11,1)
    ax0 = fig.add_subplot(gs[:7,:])
    
# Vertical line to show end of day
    ax0.axvline(0,color = vert_col, linewidth = 3)
    ax0.axvline(24,color = vert_col, linewidth = 3)
    ax0.axvline(48,color = vert_col, linewidth = 3)
    
    
    
    
    if doublefence == 1:
## double fence    
#        plt.plot(np.arange(0,Xmax), np.asarray(dofence_60)[:,(int(day)-1)], marker = 'H', markersize=20, 
 #           color = dofe, linestyle = 'None', label = 'double fence')
        ax0.plot(np.arange(0,Xmax), dofence_60, marker = 'H', markersize=20, 
            color = dofe, linestyle = 'None', label = 'double fence')
## ensemble member         
    for ens_memb in range(2,10):
        ax0.plot(lead_time_em[ens_memb][:Xmax], variable[ens_memb][:Xmax], color = memb_col,
           linestyle = '-', label='_nolegend_')
    ax0.plot(lead_time_em[1][:Xmax], variable[1][:Xmax], color = memb_col,
           linestyle = '-', label = 'ensemble member')
    ax0.plot(lead_time_em[0][:Xmax], variable[0][:Xmax], 'k', linewidth = 4, label = 'best guess')
    
## retrieval
    ax0.plot(np.arange(0, np.asarray(acc_ret).shape[0]/60,1/60), acc_ret, linestyle = (0, (3, 1, 1, 1)), 
         color = 'orange', label = 'retrieved snowfall',linewidth=6)
## Wind MEPS
    ax1 = plt.subplot(gs[7:8,:])
    ax1.grid()
    ax1.axvline(0,color = vert_col, linewidth = 3)
    ax1.axvline(24,color = vert_col, linewidth = 3)
    ax1.axvline(48,color = vert_col, linewidth = 3)  
    ax1.barbs(lead_time_sfc[:(Xmax-1)], np.zeros((lead_time_sfc[:(Xmax-1)]).shape[0]),
                uwind, vwind, length = 7, pivot = 'middle',linewidth=1.5)
             
## Wind double fence
    ax2 = plt.subplot(gs[8:9,:])
    ax2.grid()
    ax2.axvline(0,color = vert_col, linewidth = 3)
    ax2.axvline(24,color = vert_col, linewidth = 3)
    ax2.axvline(48,color = vert_col, linewidth = 3)
    ax2.barbs(lead_time_sfc[:(Xmax-1)], np.zeros((lead_time_sfc[:(Xmax-1)]).shape[0]),
                uwind_dofe, vwind_dofe, length = 7, pivot ='middle',linewidth=1.5)
    

### fine tuning
    lgd = ax0.legend(loc='upper left',fontsize=fontsize)
    frame = lgd.get_frame()
    frame.set_facecolor('white')
#    ax0.grid()

# yaxis
    ax0.set_ylabel('%s %s %s' %(var_name[0], var_name[1], unit), fontsize = label_fs)
    ax0.set_ylim(-0.5,80)
    T = np.arange(0,90,10)
    ax0.set_yticks(T)
    ax0.set_yticklabels(T,fontsize = fontsize)

# xaxis
    a = lead_time_sfc[0:48]
    ax0.set_xlim(-0.5,Xmax-0.5)
    ax0.set_xticks(np.arange(0,Xmax,6))
    plt.setp(ax0.get_xticklabels(), visible=False) 
# labeling Wind
    ax1.set_ylabel('gust',fontsize=label_fs)
    ax2.set_ylabel('10m',fontsize =label_fs)
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax1.get_yticklabels(), visible=False)
    plt.setp(ax2.get_yticklabels(), visible=False)

    
    ax1.set_xticks(lead_time_sfc[:(Xmax)])
    ax2.set_xticks(lead_time_sfc[:(Xmax)])
    ax1.set_xlim([-0.5,Xmax-0.5])
    ax1.set_ylim([-0.5,0.5])
    
    ax2.set_xlim([-0.5,Xmax-0.5])
    ax2.set_ylim([-0.5,0.5])

    ax1.set_xticks(np.arange(0,Xmax,6))
    ax2.set_xticks(np.arange(0,Xmax,6))
    if tid == '18':
        dates = pvert.dates_plt_18(h_p18, m_p18, d_p18, y_p18, ini_day)
    if tid == '00':
        dates = pvert.dates_plt_00(h_p18, m_p18, d_p18, y_p18, ini_day)
#    ax2.set_xticklabels(dates, rotation = 25, fontsize = 24)
    ax1.tick_params(axis='both', which= 'major', labelsize=24)
    ax2.tick_params(axis='both', which= 'major', labelsize=24)
 #   ax2.set_xlabel('time', fontsize = 26)
    
#    mpl.style.use('classic')
    ax3 = plt.subplot(gs[9:10,:])
    plt.setp(ax3.get_yticklabels(), visible=False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['top'].set_visible(False)
    ax3.spines['left'].set_visible(False)
    ax3.set_xticks(lead_time_sfc[:(Xmax)])
    ax3.set_xlim([-0.5,Xmax-0.5])
    ax2.set_ylim([-0.00005,0.00005])
    ax3.set_xticks(np.arange(0,Xmax,6))
    ax3.set_xticklabels(dates, rotation = 25, fontsize = tick_fs)
    ax3.set_xlabel('time', fontsize = label_fs)
# title
    ax0.set_title(title, fontsize=fontsize, color =blue )
# tight layout
    plt.tight_layout()      