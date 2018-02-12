
# coding: utf-8

# In[ ]:

import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
import matplotlib.pyplot as plt
import numpy as np 

import autolabel_bar as ab
from matplotlib import gridspec



### define colors 
champ = 255
blue = np.array([1,74,159])/champ           # for the date


#############################################
# In[ ]:


# def plot_TPU(fig,  min_60val, df_val, df_60,
#             min_15_mask, t_mean_mask, #t_mean,
#             X_mask,Y_mask,uwind_mask, vwind_mask,
#             calday, day, calmon, year, fs):
#     
#     UTC = [1/60*float(0),        1/60*float(3),        1/60*float(6),        1/60*float(9),        1/60*float(12),        1/60*float(15),        1/60*float(18),        1/60*float(21),        1/60*float(24)]
#     timer = ['00Z', '03Z','06Z','09Z','12Z','15Z','18Z','21Z','24Z']
#     prec_tick = np.arange(0,round(np.nanmax(df_60))+0.5,0.5)
# #    T = np.arange(round(np.nanmin(t_mean)-1),round(np.nanmax(t_mean)+1),2)
#     T = np.arange(-12,6.5,2)
# 	
# 
#     barfont = fs-6
#     yfont = fs
#     tickfont = fs-2
#     legenfont = fs+2
#     
#     gs = gridspec.GridSpec(7,1)
#     ax1 = fig.add_subplot(gs[:6,:])
#         
# # Precipitation
#     bar = ax1.bar(min_60val,df_val,width=1/60.,align='edge',label = 'DF accumulation', color='lightblue',
#               edgecolor ='deepskyblue')
#     ab.autolabel(bar, ax1,barfont)
#     ax1.grid()
#     plt.setp(ax1.get_xticklabels(), visible=False)
#         
#     
#     # Temperature
#     ax2 = ax1.twinx()
#     line = ax2.plot(min_15_mask, t_mean_mask,color = 'r',label='Temp',linewidth = 4)
#     ax2.axhline(y = 0., c ='darkgray', linewidth = 2.5, zorder = 0, linestyle = '--')
#     ax2.axhline(y = -7.5, c ='darkgreen', linewidth = 2, zorder = 0, linestyle = '--')
#     
#     
#     
#     # labeling Precip
#     ax1.set_ylabel('Accumulation [mm]',fontsize = yfont)
#     ax1.set_yticklabels(prec_tick,fontsize = tickfont)
#     ax1.set_xticks(UTC)
#     ax1.set_xticklabels(timer, fontsize=tickfont)
#     ax1.set_xlim([0,24*1/60])
#     ax1.set_ylim([0.,np.nanmax(df_60)+1])
#     ax1.legend(loc='upper left', fontsize=legenfont )
#     plt.setp(ax1.get_yticklabels(), visible=False)
# 
#     # labeling Temp
#     ax2.set_yticks(T)
#     ax2.set_ylabel('Temperature [$^\circ$C]',fontsize = yfont)
#     ax2.tick_params(axis='both', which= 'major', labelsize=tickfont)
# ##ax2.set_xticklabels(timer, fontsize=20)
#     ax2.legend(loc='upper right', fontsize = legenfont )
# #ax2.spines['right'].set_color('r')
# #ax2.yaxis.label.set_color('r')
# #ax2.tick_params(axis='y',colors='r')
#     
# # Wind
# # share x only
#     ax3 = plt.subplot(gs[6,:])#, sharex=ax1)
# 
#     ax3.barbs(X_mask,Y_mask,uwind_mask, vwind_mask, length = 9, pivot='middle')
# #ax3.barbs(X,Y,u_wind[::60,8], v_wind[::60,8], length = 10, pivot='middle')
# # labeling Wind
#     ax3.axes.get_yaxis().set_visible(False)
#     ax3.tick_params(axis='both', which= 'major', labelsize=tickfont)
#     ax3.set_xticks(UTC)
#     ax3.set_xticklabels(timer, fontsize=tickfont)
#     ax3.set_xlim([0,24*1/60])
#     ax3.set_ylim([-0.001,0.001])
#     ax3.grid()
#         
#  #   ax1.set_title('%s, %s %s %g' %(calday, (day), calmon, (*year)),fontsize=fs, color=blue)
#     ax1.set_title('%s, %s %s %s' %(calday, (day), calmon, year), fontsize=fs, color=blue)
#     ### Save
#     


# In[ ]:

def plot_TPU(fig, h_precip, precip, 
              h_temp, temp, 
              h_wind, Y_wind, uwind, vwind,
             calday, dd, calmon, year, fs):
    
    prec_tick = np.arange(0,5.,0.5)
    T = np.arange(-12,6.5,2)

    barfont = fs-6
    yfont = fs
    tickfont = fs-2
    legenfont = fs+2


    gs = gridspec.GridSpec(7,1)
    ax1 = fig.add_subplot(gs[:6,:])
      
# Precipitation
    bar = ax1.bar(h_precip, precip, width=1,align='center',label = 'DF accumulation', color='lightblue',
              edgecolor ='deepskyblue')
    ab.autolabel(bar, ax1,barfont)
    ax1.grid()
    plt.setp(ax1.get_xticklabels(), visible=False)
        
    
# Temperature
    ax2 = ax1.twinx()
    line = ax2.plot(h_temp, temp, color = 'r',label='Temp',linewidth = 4)
    ax2.axhline(y = 0., c ='darkgray', linewidth = 2.5, zorder = 0, linestyle = '--')
    ax2.axhline(y = -6., c ='darkgreen', linewidth = 2, zorder = 0, linestyle = '--')


# labeling Precip and Temp
    ax1.set_ylabel('Accumulation [mm]',fontsize = yfont)
    ax1.set_yticklabels(prec_tick,fontsize = tickfont)
    ax1.set_xticks(h_wind)
    ax1.set_xticklabels(h_wind, fontsize=tickfont)
    ax1.set_xlim([-0.5,23.5])
    ax1.set_ylim([0.,5.])
    ax1.legend(loc='upper left', fontsize=legenfont )
    plt.setp(ax1.get_yticklabels(), visible=False)

    # labeling Temp
    ax2.set_yticks(T)
    ax2.set_ylabel('Temperature [$^\circ$C]',fontsize = yfont)
    ax2.tick_params(axis='both', which= 'major', labelsize=tickfont)
    ax2.legend(loc='upper right', fontsize = legenfont )


# Wind
# share x only
    ax3 = plt.subplot(gs[6,:])#, sharex=ax1)

    ax3.barbs(h_wind, Y_wind, uwind, vwind, length = 9, pivot='middle')
# labeling Wind
    ax3.axes.get_yaxis().set_visible(False)
    ax3.tick_params(axis='both', which= 'major', labelsize=tickfont)
    ax3.set_xticks(h_wind)
    ax3.set_xticklabels(h_wind, fontsize=tickfont)
    ax3.set_xlim([-0.5,23.5])
    ax3.set_ylim([-0.001,0.001])
    ax3.grid()

    ax1.set_title('%s, %s %s %s' %(calday, (dd), calmon, year),fontsize=fs, color=blue)
 

   

