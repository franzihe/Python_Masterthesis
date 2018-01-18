
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec



# In[2]:

### Define colorbar colors
champ = 255.
blue = np.array([1,74,159])/champ           # for the date
memb_col = np.array([99,99,99])/champ       # ensemble member color
vert_col = np.array([197,197,197])/champ    # vertical line for day marker




# In[3]:

def spaghetti_sfc(lead_time_sfc,SA_0m_filled,SA_0m_masked,var_name, title,fig_name,sfig):
    lead_time = dict()
    variable_to_plot = dict()
    for ens_memb in range(0,10):
        lead_time[ens_memb] = lead_time_sfc[SA_0m_masked[ens_memb]]
        variable_to_plot[ens_memb] = SA_0m_filled[ens_memb][SA_0m_masked[ens_memb]]

### Create figure of var_name at surface
    fig = plt.figure(figsize =(20,7))
    ax = plt.axes()
# Vertical line to show end of day
    ax.axvline(24,color = vert_col, linewidth = 3)
    ax.axvline(48,color = vert_col, linewidth = 3)

# Plot only values where not NAN 
    for ens_memb in range(1,10):
        ax.plot(lead_time[ens_memb],variable_to_plot[ens_memb],color = memb_col, 
            linestyle = '-',label = 'EM%s' %(ens_memb))
        ax.plot(lead_time[0],variable_to_plot[0],'k', linewidth = 4, label = 'best guess') 

### fine tuning
#plt.legend()
    ax.grid()

# yaxis
    ax.set_ylabel(var_name, fontsize = 30)
#ax.set_ylim(-10,3.5)
##T = np.arange(0,30,5)
#ax.set_yticks(T)
#ax.set_yticklabels(T,fontsize = 20)

# xaxis
    ax.set_xlim(0,66)
    ax.set_xlabel('lead time', fontsize = 30)
    ax.set_xticks(lead_time_sfc[0::6])
    ax.set_xticklabels(lead_time_sfc[0::6], fontsize = 20)

# title
    
    ax.set_title(title, fontsize=30, color =blue )
    if sfig == 1:
        plt.savefig('../MEPS_fig/%s/%s' %(var_name,fig_name))
        
#    plt.show()
    plt.close()


# In[ ]:



