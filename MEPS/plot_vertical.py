
# coding: utf-8

# In[2]:

import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import colormaps as cmaps
import save_fig as SF
import datetime
from datetime import date


# In[3]:

### Define colorbar colors
champ = 255.
blue = np.array([1,74,159])/champ           # for the date
vert_col = np.array([197,197,197])/champ    # vertical line for day marker


# In[4]:

def dates_plt(time_ml):
    dt = []
    dd = []
    dm = []
    dy = []
    for i in range(0,time_ml.shape[0],6):
        dt.append(datetime.datetime.utcfromtimestamp(time_ml[i]).hour)
        dd.append(datetime.datetime.utcfromtimestamp(time_ml[i]).day)
        dm.append(datetime.datetime.utcfromtimestamp(time_ml[i]).month)
        dy.append(datetime.datetime.utcfromtimestamp(time_ml[i]).year)
        

    xt = []
    t1 = '%s-%s-%s' %(dy[0],dm[0],dd[0])
    xt.append(t1)
    for i in range(1,4):
         xt.append('%s' %dt[i])
    t2 = '%s-%s-%s' %(dy[4],dm[4],dd[4])
    xt.append(t2)
    for i in range(5,8):
        xt.append('%s' %dt[i])
    if np.asarray(dt).size >8:
        t3 = '%s-%s-%s' %(dy[8],dm[8],dd[8])
        xt.append(t3)
    elif np.asarray(dt).size >9:
        for i in range(9,12):
            xt.append('%s' %dt[i])
    else:
        xt
    return(xt);
    
# def dates_plt_18(time_ml):
#     dt = []
#     dd = []
#     dm = []
#     dy = []
#     for i in range(0,time_ml.shape[0],6):
#         dt.append(datetime.datetime.utcfromtimestamp(time_ml[i]).hour)
#         dd.append(datetime.datetime.utcfromtimestamp(time_ml[i]).day)
#         dm.append(datetime.datetime.utcfromtimestamp(time_ml[i]).month)
#         dy.append(datetime.datetime.utcfromtimestamp(time_ml[i]).year)
#         
# 
#     xt = []
#     for i in range(0,1):
#         xt.append('%s' %dt[i])
#     t1 = '%s-%s-%s' %(dy[1],dm[1],dd[1])
#     xt.append(t1)
#     for i in range(2,5):
#          xt.append('%s' %dt[i])
#     t2 = '%s-%s-%s' %(dy[5],dm[5],dd[5])
#     xt.append(t2)
#     for i in range(6,9):
#         xt.append('%s' %dt[i])
#     if np.asarray(dt).size >9:
#         t3 = '%s-%s-%s' %(dy[9],dm[9],dd[9])
#         xt.append(t3)
#     elif np.asarray(dt).size >10:
#         for i in range(10,12):
#             xt.append('%s' %dt[i])
#     else:
#         xt
#     return(xt);

def dates_plt_00(h_p00, m_p00, d_p00, y_p00, ini_day ):
    xt = []
    t1 = '%s-%s-%s' %(y_p00[0][ini_day-1], m_p00[0][ini_day-1], d_p00[0][ini_day-1])
    xt.append(t1)
    for i in range(6,24,6):
        xt.append('%s' %h_p00[i][ini_day-1])
        
    t2 = '%s-%s-%s' %(y_p00[0][ini_day], m_p00[0][ini_day], d_p00[0][ini_day])
    xt.append(t2)
    for i in range(6,24,6):
        xt.append('%s' %h_p00[i][ini_day])
    t3 = '%s-%s-%s' %(y_p00[0][ini_day+1], m_p00[0][ini_day+1], d_p00[0][ini_day+1])
    xt.append(t3)
    return(xt);




def dates_plt_18(h_p18, m_p18, d_p18, y_p18, ini_day):
    xt = []
    for i in range(0,1):
        xt.append('%s' %h_p18[i][ini_day-1])
    t1 = '%s-%s-%s' %(y_p18[6][ini_day-1], m_p18[6][ini_day-1], d_p18[6][ini_day-1])
    xt.append(t1)
    for i in range(12,24,6):
        xt.append('%s' %h_p18[i][ini_day-1])
    for i in range(0,1):
        xt.append('%s' %h_p18[i][ini_day])
    t2 = '%s-%s-%s' %(y_p18[6][ini_day], m_p18[6][ini_day], d_p18[6][ini_day])
    xt.append(t2)
    for i in range(12,24,6):
        xt.append('%s' %h_p18[i][ini_day])
    for i in range(0,1):
        xt.append('%s' %h_p18[i][ini_day+1])
    return(xt);
    
    
    
    
levels = np.arange(0,0.6,0.02)   # snowfall amount not divided by thickness
#levels = np.arange(0,9.5,0.32)     # snowfall amount divided by thickness
# In[ ]:

def plot_vertical_EM0_1(time, height,result, time_ml, var_name, unit, maxim, Xmax, title):
    fig = plt.figure(figsize=(20.,14.15))
    gs = GridSpec(2, 2)

# title
    fig.suptitle(title, y=0.95, color =blue, fontsize = 26)
    
    for ens_memb in range(0,2):
        if len(result[ens_memb]) == 0:
            continue
        
### first 2 ens_memb
        ax0 = plt.subplot(gs[ens_memb, :])
        im0 = ax0.contourf(time[ens_memb], np.transpose(height[ens_memb]), result[ens_memb].T, levels,cmap=cmaps.viridis)
        ax0.text(Xmax-0.5, Xmax+50, 'EM%s' %(ens_memb),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 22,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
        ax0.axis([time[ens_memb].min(), Xmax, height[ens_memb].min(), 3000.])
#        ax0.yaxis.grid()
# Vertical line to show end of day
        ax0.axvline(24,color = vert_col, linewidth = 3)
        ax0.axvline(48,color = vert_col, linewidth = 3)
    
# label ticks for plotting
        dates = dates_plt(time_ml)
        yl = [0., '' , 1.0, '' , 2., '' , 3.]
# labels
        ax0.set_xticks(np.arange(0,Xmax+1,6))
        if ens_memb == 1:
            ax0.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',labelsize = 20)
            ax0.set_xticklabels(dates, rotation = 25, fontsize = 20)
            ax0.set_xlabel('time', fontsize = 22)
        else:
            ax0.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off',labelsize = 20)
    
        ax0.set_ylabel('height [km]', fontsize = 22)
        ax0.set_yticks(np.arange(0,3500.,500.))
        ax0.set_yticklabels(yl, fontsize = 20)
    
    plt.subplots_adjust(hspace = 0.08)
# Add Colorbar
    cbaxes = fig.add_axes([0.14, 0.03, .75, .02] )   #[left, bottom, width, height] 
    cbar = plt.colorbar(im0, orientation = 'horizontal', cax=cbaxes)
    cbar.ax.set_xlabel('%s %s %s' %(var_name[0], var_name[1], unit), fontsize = 22)
    cbar.ax.tick_params(labelsize = 20)



# In[ ]:

def plot_vertical_EM0_9(time, height,result, time_ml, var_name, unit, maxim, title):
    fig = plt.figure(figsize=(14.15,20.))
    gs = GridSpec(6, 2)

# title
    fig.suptitle(title,y=0.9,  color =blue, fontsize = 20)
#levels = np.arange(0,np.nanmax(maxim),0.015)
### first 2 ens_memb
    for ens_memb in range(0,2):
        if len(result[ens_memb]) == 0:
            continue 

        ax0 = plt.subplot(gs[ens_memb, :])
        im0 = ax0.contourf(time[ens_memb], np.transpose(height[ens_memb]), result[ens_memb].T, levels,cmap=cmaps.viridis)
        ax0.text(time[ens_memb].max()-0.5, time[ens_memb].min()+50, 'EM%s' %(ens_memb),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 20,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
        ax0.axis([time[ens_memb].min(), time[ens_memb].max(),  height[ens_memb].min(), 3000.])
#        ax0.yaxis.grid()
# Vertical line to show end of day
        ax0.axvline(24,color = vert_col, linewidth = 3)
        ax0.axvline(48,color = vert_col, linewidth = 3)
    
# label ticks for plotting
        dates = dates_plt(time_ml)
        yl = [0., '' , 1.0, '' , 2., '' , 3.]
# labels
        ax0.set_xticks(np.arange(0,time[ens_memb].max()+1,6))
        if ens_memb == 1:
            ax0.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',labelsize = 16)
            ax0.set_xticklabels(dates, rotation = 25, fontsize = 16)
#        ax0.set_xlabel('time', fontsize = 20)
        else:
            ax0.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off',labelsize = 16)
    
        ax0.set_ylabel('height [km]', fontsize = 20)
        ax0.set_yticks(np.arange(0,3500.,500.))
        ax0.set_yticklabels(yl, fontsize = 16)
    
    plt.subplots_adjust(hspace = 0.5)
# Add Colorbar
    cbaxes = fig.add_axes([0.14, 0.03, .75, .02] )   #[left, bottom, width, height] 
    cbar = plt.colorbar(im0, orientation = 'horizontal', cax=cbaxes)
    cbar.ax.set_xlabel('%s %s %s' %(var_name[0], var_name[1], unit), fontsize = 20)
    cbar.ax.tick_params(labelsize = 18)

    pos = []
    pos.append(0)
    pos.append(0)
    for i in range(2,6):
        pos.append(i)
        pos.append(i)
### left column:
    for ens_memb in range(2,10,2):
        if len(result[ens_memb]) == 0:
            continue
     
        ax2 = plt.subplot(gs[pos[ens_memb], :-1])
        im2 = ax2.contourf(time[ens_memb], np.transpose(height[ens_memb]), result[ens_memb].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
        ax2.text(time[ens_memb].max()-0.5, time[ens_memb].min()+50, 'EM%s' %(ens_memb),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 20,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})

# set the limits of the plot to the limits of the data
        ax2.axis([time[ens_memb].min(), time[ens_memb].max(),  height[ens_memb].min(), 3000.])
#        ax2.yaxis.grid()
# Vertical line to show end of day
        ax2.axvline(24,color = vert_col, linewidth = 3)
        ax2.axvline(48,color = vert_col, linewidth = 3)
# label ticks for plotting
        if np.asarray(dates).size <= 8.:
            dates2 = [dates[0], '', '','',dates[4], '', '','']
        else:
            dates2 = [dates[0], '', '','',dates[4], '', '','',dates[8]]
            

# labels
        ax2.set_xticks(np.arange(0,time[ens_memb].max()+1,6))
        ax2.set_ylabel('height [km]', fontsize = 20)
        ax2.set_yticks(np.arange(0,3500.,500.))
        ax2.set_yticklabels(yl, fontsize = 18)
        if ens_memb == 8:
            ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on', labelsize = 16) 
            ax2.set_xticklabels(dates2, rotation = 25, fontsize = 16)
            ax2.set_xlabel('time', fontsize = 20)
        else:
            ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 16) 
    
# right column    
    for ens_memb in range(3,10,2):
        if len(result[ens_memb]) == 0:
            continue
        
        ax3 = plt.subplot(gs[pos[ens_memb], -1:])
        im2 = ax3.contourf(time[ens_memb], np.transpose(height[ens_memb]), result[ens_memb].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
        ax3.text(time[ens_memb].max()-0.5, time[ens_memb].min()+50, 'EM%s' %(ens_memb),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 20,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})

# set the limits of the plot to the limits of the data
        ax3.axis([time[ens_memb].min(), time[ens_memb].max(),  height[ens_memb].min(), 3000.])
#        ax3.yaxis.grid()
# Vertical line to show end of day
        ax3.axvline(24,color = vert_col, linewidth = 3)
        ax3.axvline(48,color = vert_col, linewidth = 3)
# label ticks for plotting

# labels
        ax3.set_xticks(np.arange(0,time[ens_memb].max()+1,6))
        ax3.set_ylabel('height [km]', fontsize = 20)
        ax3.set_yticks(np.arange(0,3500.,500.))
        ax3.set_yticklabels(yl, fontsize = 18)
        if ens_memb == 9:
            ax3.tick_params(axis='both',which='both',bottom='on',top='off',left = 'off',labelbottom='on', labelleft = 'off',labelsize = 16) 
            ax3.set_xticklabels(dates2, rotation = 25, fontsize = 16)
            ax3.set_xlabel('time', fontsize = 20)
        else:
            ax3.tick_params(axis='both',which='both',bottom='on',top='off',left = 'off',labelbottom='off', labelleft = 'off',labelsize = 16)
    


# In[ ]:

def plot_vertical_EM0_9_48h(time, height,result, time_ml, var_name, unit, maxim, Xmax, title):
    fig = plt.figure(figsize=(14.15,20.))
    gs = GridSpec(10, 2)

# title
    fig.suptitle(title, y =0.9, color =blue, fontsize = 20)
#    levels = np.arange(0,np.nanmax(maxim),0.015)
    for ens_memb in range(0,10):
        if len(result[ens_memb]) == 0:
            continue
        
### first all ens_memb
        ax0 = plt.subplot(gs[ens_memb, :])
        im0 = ax0.contourf(time[ens_memb], np.transpose(height[ens_memb]), result[ens_memb].T, levels,cmap=cmaps.viridis)
        ax0.text(Xmax-0.5, Xmax+50, 'EM%s' %(ens_memb),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 20,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
        ax0.axis([time[ens_memb].min(), Xmax, height[ens_memb].min(), 3000.])
#        ax0.yaxis.grid()
# Vertical line to show end of day
        ax0.axvline(24,color = vert_col, linewidth = 3)
        ax0.axvline(48,color = vert_col, linewidth = 3)
    
# label ticks for plotting
        dates = dates_plt(time_ml)
        yl = [0., '' , 1.0, '' , 2., '' , 3.]
# labels
        ax0.set_xticks(np.arange(0,Xmax+1,6))
        if ens_memb == 9:
            ax0.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',labelsize = 16)
            ax0.set_xticklabels(dates, rotation = 25, fontsize = 16)
            ax0.set_xlabel('time', fontsize = 20)
        else:
            ax0.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off',labelsize = 16)
        if ens_memb == 4:
            plt.ylabel('height [km]', fontsize = 20)
#    ax0.set_ylabel('height [km]', fontsize = 22)
        ax0.set_yticks(np.arange(0,3500.,500.))
        ax0.set_yticklabels(yl, fontsize = 16)


    
    plt.subplots_adjust(hspace = 0.15)
# Add Colorbar
    cbaxes = fig.add_axes([0.14, 0.03, .75, .02] )   #[left, bottom, width, height] 
    cbar = plt.colorbar(im0, orientation = 'horizontal', cax=cbaxes)
    cbar.ax.set_xlabel('%s %s %s' %(var_name[0], var_name[1], unit), fontsize = 20)
    cbar.ax.tick_params(labelsize = 18)


