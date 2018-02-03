
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import plot_vertical as pvert 


# In[2]:

### Define colorbar colors
champ = 255.
blue = np.array([1,74,159])/champ           # for the date
memb_col = np.array([99,99,99])/champ       # ensemble member color
vert_col = np.array([197,197,197])/champ    # vertical line for day marker
dofe = np.array([64,180,233])/champ         # color for double fence measurement




# In[ ]:
def spaghetti_sfc_dofe(lead_time_sfc, variable, dofence_60, time_sfc, Xmax, day, var_name, unit, title, tid, doublefence):
    fig = plt.figure(figsize=(20,7))
    ax = plt.axes()
# Vertical line to show end of day
    ax.axvline(0,color = vert_col, linewidth = 3)
    ax.axvline(24,color = vert_col, linewidth = 3)
    ax.axvline(48,color = vert_col, linewidth = 3)
    if doublefence == 1:
## double fence    
        plt.plot(np.arange(0,Xmax), np.asarray(dofence_60)[:,(int(day)-1)], marker = 'H', markersize=20, 
            color = dofe, linestyle = 'None', label = 'double fence')
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
    ax.set_ylabel('%s %s %s' %(var_name[0], var_name[1], unit), fontsize = 30)
    ax.set_ylim(-0.5,80)
    T = np.arange(0,90,10)
    ax.set_yticks(T)
    ax.set_yticklabels(T,fontsize = 22)

# xaxis
    a = lead_time_sfc[0][0:48]
    ax.set_xlim(-0.5,Xmax+0.5)
    ax.set_xlabel('time', fontsize = 30)
    ax.set_xticks(np.arange(0,Xmax+1,6))
    if tid == '18':
        dates = pvert.dates_plt_18(time_sfc)
    if tid == '00':
        dates = pvert.dates_plt(time_sfc)
    ax.set_xticklabels(dates, rotation = 25, fontsize = 22)
# title
    ax.set_title(title, fontsize=30, color =blue )
# tight layout
    plt.tight_layout()




def spaghetti_sfc_dofe_Morten(lead_time_sfc, variable, dofence_60, time_sfc, Xmax, day, var_name, unit, title, tid):
    fig = plt.figure(figsize=(20,7))
    ax = plt.axes()
# Vertical line to show end of day
    ax.axvline(0,color = vert_col, linewidth = 3)
    ax.axvline(24,color = vert_col, linewidth = 3)
    ax.axvline(48,color = vert_col, linewidth = 3)
## double fence    
#### Morten
    plt.plot(np.arange(0,Xmax), np.asarray(dofence_60)[:Xmax,(int(day)-1)], marker = 'o', markersize=20, 
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
    ax.set_ylabel('%s %s %s' %(var_name[0], var_name[1], unit), fontsize = 30)
    ax.set_ylim(-0.5,65)
    T = np.arange(0,70,10)
    ax.set_yticks(T)
    ax.set_yticklabels(T,fontsize = 22)

# xaxis
    b = np.arange(0,Xmax+5,5)
    ax.set_xlim(-0.5,Xmax-0.5)
    ax.set_xlabel('lead time', fontsize = 30)
    ax.set_xticks(np.arange(0,Xmax,5))

    ax.set_xticklabels(b, fontsize = 22)
# title
    ax.set_title(title, fontsize=30, color ='k' )
# tight layout
    plt.tight_layout()
      