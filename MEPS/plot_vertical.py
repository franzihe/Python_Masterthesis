
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import colormaps as cmaps
import save_fig as SF



# In[2]:

### Define colorbar colors
champ = 255.
blue = np.array([1,74,159])/champ           # for the date


# In[3]:

def plot_vertical_EM(time, height,result,var_name, unit, fig_name, title,sfig,directory, figure_name, form):
    # calculate max value for levels
    maxim = []
    for ens_memb in range(0,10):
        maxi = np.nanmax(result[ens_memb])
        maxim.append(maxi)
    maxim = np.asarray(maxim)
    np.nanmax(maxim)
    
    
    
    
    fig = plt.figure(figsize=(14.15,20.))
    gs = GridSpec(6, 2)

    ens_memb = 0
    levels = np.arange(0,np.nanmax(maxim),0.015)
#    levels = np.arange(0,np.nanmax(maxim),0.25)
### first subplot
# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
    X = time[ens_memb]
    Y = np.transpose(height[ens_memb])
    ax0 = plt.subplot(gs[0, :])
    im0 = ax0.contourf(X, Y, result[ens_memb].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
# label for EM
    ax0.text(X.max()-0.5,X.min()+50, 'EM%s' %(ens_memb),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    ax0.axis([X.min(), X.max(), Y.min(), 3500.])

### 2nd subplot
    X = time[ens_memb+1]
    Y = np.transpose(height[ens_memb+1])
    ax1 = plt.subplot(gs[1, :])
    im1 = ax1.contourf(X, Y, result[ens_memb+1].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax1.text(X.max()-0.5,X.min()+50, 'EM%s' %(ens_memb+1),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    ax1.axis([X.min(), X.max(), Y.min(), 3500.])

### 3rd subplot
    X = time[ens_memb+2]
    Y = np.transpose(height[ens_memb+2])
    ax2 = plt.subplot(gs[2, :-1])
    im2 = ax2.contourf(X, Y, result[ens_memb+2].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax2.text(X.max()-0.5,X.min()+50, 'EM%s' %(ens_memb+2),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), X.max(), Y.min(), 3500.])

### 4th subplot
    X = time[ens_memb+3]
    Y = np.transpose(height[ens_memb+3])
    ax3 = plt.subplot(gs[2, -1:])
    im3 = ax3.contourf(X, Y, result[ens_memb+3].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax3.text(X.max()-0.5,X.min()+50, 'EM%s' %(ens_memb+3),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    ax3.axis([X.min(), X.max(), Y.min(), 3500.])

### 5th subplot
    X = time[ens_memb+4]
    Y = np.transpose(height[ens_memb+4])
    ax4 = plt.subplot(gs[3, :-1])
    im4 = ax4.contourf(X, Y, result[ens_memb+4].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax4.text(X.max()-0.5,X.min()+50, 'EM%s' %(ens_memb+4),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), X.max(), Y.min(), 3500.])

### 6th subplot
    X = time[ens_memb+5]
    Y = np.transpose(height[ens_memb+5])
    ax5 = plt.subplot(gs[3, -1:])
    im5 = ax5.contourf(X, Y, result[ens_memb+5].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax5.text(X.max()-0.5,X.min()+50, 'EM%s' %(ens_memb+5),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), X.max(), Y.min(), 3500.])

### 7th subplot
    X = time[ens_memb+6]
    Y = np.transpose(height[ens_memb+6])
    ax6 = plt.subplot(gs[4, :-1])
    im6 = ax6.contourf(X, Y, result[ens_memb+6].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax6.text(X.max()-0.5,X.min()+50, 'EM%s' %(ens_memb+6),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), X.max(), Y.min(), 3500.])

### 8th subplot
    X = time[ens_memb+7]
    Y = np.transpose(height[ens_memb+7])
    ax7 = plt.subplot(gs[4, -1:])
    im7 = ax7.contourf(X, Y, result[ens_memb+7].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax7.text(X.max()-0.5,X.min()+50, 'EM%s' %(ens_memb+7),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), X.max(), Y.min(), 3500.])

### 9th subplot
    X = time[ens_memb+8]
    Y = np.transpose(height[ens_memb+8])
    ax8 = plt.subplot(gs[5, :-1])
    im8 = ax8.contourf(X, Y, result[ens_memb+8].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax8.text(X.max()-0.5,X.min()+50, 'EM%s' %(ens_memb+8),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), X.max(), Y.min(), 3500.])

### 10th subplot
    X = time[ens_memb+9]
    Y = np.transpose(height[ens_memb+9])
    ax9 = plt.subplot(gs[5, -1:])
    im9 = ax9.contourf(X, Y, result[ens_memb+9].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax9.text(X.max()-0.5,X.min()+50, 'EM%s' %(ens_memb+9),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), X.max(), Y.min(), 3500.])

#plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.subplots_adjust(hspace=0.355)

    fig.subplots_adjust(right=0.8)
    # Add Colorbar
    cbaxes = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    cbar = plt.colorbar(im0, orientation = 'vertical', cax=cbaxes)
    cbar.ax.set_ylabel('%s %s %s' %(var_name[0], var_name[1], unit), fontsize = 22)
    cbar.ax.tick_params(labelsize = 20)
	
# title
    ax0.set_title(title,  color =blue, fontsize = 26)

# labels
    ax0.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off',labelsize = 18) 
    ax1.set_xlabel('lead time', fontsize = 18)
    ax1.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on',labelsize = 18) 
    ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 18) 
    ax3.tick_params(axis='both',which='both',bottom='on',top='off',left = 'off',labelbottom='off', labelleft = 'off',labelsize = 18)  
    ax4.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 18) 
    ax5.tick_params(axis='both',which='both',bottom='on',top='off',left = 'off',labelbottom='off', labelleft = 'off',labelsize = 18)  
    ax6.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 18) 
    ax7.tick_params(axis='both',which='both',bottom='on',top='off',left = 'off',labelbottom='off', labelleft = 'off',labelsize = 18)
    ax8.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on', labelsize = 18) 
    ax9.tick_params(axis='both',which='both',bottom='on',top='off',left = 'off',labelbottom='on', labelleft = 'off',labelsize = 18) 
    ax8.set_xlabel('lead time', fontsize = 18)
    ax9.set_xlabel('lead time', fontsize = 18)
    ax0.set_ylabel('height', fontsize = 18)
    ax1.set_ylabel('height', fontsize = 18)
    ax2.set_ylabel('height', fontsize = 18)
    ax4.set_ylabel('height', fontsize = 18)
    ax6.set_ylabel('height', fontsize = 18)
    ax8.set_ylabel('height', fontsize = 18)
    ax0.set_yticks(np.arange(0,3500.,1000.))
    ax1.set_yticks(np.arange(0,3500.,1000.))
    ax2.set_yticks(np.arange(0,3500.,1000.))
    ax3.set_yticks(np.arange(0,3500.,1000.))
    ax4.set_yticks(np.arange(0,3500.,1000.))
    ax5.set_yticks(np.arange(0,3500.,1000.))
    ax6.set_yticks(np.arange(0,3500.,1000.))
    ax7.set_yticks(np.arange(0,3500.,1000.))
    ax8.set_yticks(np.arange(0,3500.,1000.))
    ax9.set_yticks(np.arange(0,3500.,1000.))
    
    
    if sfig == 1:
    	SF.save_figure_portrait(directory, figure_name, form)
    else:
        plt.show()
        


#    plt.show()
#    plt.close()


# In[ ]:

def plot_vertical_EM_48h(time, height, result, var_name, unit, fig_name, title,sfig,directory, figure_name, form):
    # calculate max value for levels
    maxim = []
    for ens_memb in range(0,10):
        maxi = np.nanmax(result[ens_memb])
        maxim.append(maxi)
    maxim = np.asarray(maxim)
    np.nanmax(maxim)
    fig = plt.figure(figsize=(14.15,20.))
    gs = GridSpec(10, 2)

    ens_memb = 0
    levels = np.arange(0,np.nanmax(maxim),0.015)
    #levels = np.arange(0,np.nanmax(maxim),0.25)
### first subplot
# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
    X = time[ens_memb]
    Y = np.transpose(height[ens_memb])
    ax0 = plt.subplot(gs[0, :])
    im0 = ax0.contourf(X, Y, result[ens_memb].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
# label for EM
    ax0.text(time[ens_memb+2].max()-0.5,X.min()+50, 'EM%s' %(ens_memb),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    ax0.axis([X.min(), time[ens_memb+2].max(), Y.min(), 3500.])

### 2nd subplot
    X = time[ens_memb+1]
    Y = np.transpose(height[ens_memb+1])
    ax1 = plt.subplot(gs[1, :])
    im1 = ax1.contourf(X, Y, result[ens_memb+1].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax1.text(time[ens_memb+2].max()-0.5,X.min()+50, 'EM%s' %(ens_memb+1),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    ax1.axis([X.min(), time[ens_memb+2].max(), Y.min(), 3500.])

### 3rd subplot
    X = time[ens_memb+2]
    Y = np.transpose(height[ens_memb+2])
    ax2 = plt.subplot(gs[2, :])
    im2 = ax2.contourf(X, Y, result[ens_memb+2].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax2.text(time[ens_memb+2].max()-0.5,X.min()+50, 'EM%s' %(ens_memb+2),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), time[ens_memb+2].max(), Y.min(), 3500.])

### 4th subplot
    X = time[ens_memb+3]
    Y = np.transpose(height[ens_memb+3])
    ax3 = plt.subplot(gs[3, :])
    im3 = ax3.contourf(X, Y, result[ens_memb+3].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax3.text(time[ens_memb+2].max()-0.5,X.min()+50, 'EM%s' %(ens_memb+3),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    ax3.axis([X.min(), time[ens_memb+2].max(), Y.min(), 3500.])

### 5th subplot
    X = time[ens_memb+4]
    Y = np.transpose(height[ens_memb+4])
    ax4 = plt.subplot(gs[4, :])
    im4 = ax4.contourf(X, Y, result[ens_memb+4].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax4.text(time[ens_memb+2].max()-0.5,X.min()+50, 'EM%s' %(ens_memb+4),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), time[ens_memb+2].max(), Y.min(), 3500.])

### 6th subplot
    X = time[ens_memb+5]
    Y = np.transpose(height[ens_memb+5])
    ax5 = plt.subplot(gs[5, :])
    im5 = ax5.contourf(X, Y, result[ens_memb+5].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax5.text(time[ens_memb+2].max()-0.5,X.min()+50, 'EM%s' %(ens_memb+5),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), time[ens_memb+2].max(), Y.min(), 3500.])

### 7th subplot
    X = time[ens_memb+6]
    Y = np.transpose(height[ens_memb+6])
    ax6 = plt.subplot(gs[6, :])
    im6 = ax6.contourf(X, Y, result[ens_memb+6].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax6.text(time[ens_memb+2].max()-0.5,X.min()+50, 'EM%s' %(ens_memb+6),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), time[ens_memb+2].max(), Y.min(), 3500.])

### 8th subplot
    X = time[ens_memb+7]
    Y = np.transpose(height[ens_memb+7])
    ax7 = plt.subplot(gs[7, :])
    im7 = ax7.contourf(X, Y, result[ens_memb+7].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax7.text(time[ens_memb+2].max()-0.5,X.min()+50, 'EM%s' %(ens_memb+7),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), time[ens_memb+2].max(), Y.min(), 3500.])

### 9th subplot
    X = time[ens_memb+8]
    Y = np.transpose(height[ens_memb+8])
    ax8 = plt.subplot(gs[8, :])
    im8 = ax8.contourf(X, Y, result[ens_memb+8].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax8.text(time[ens_memb+2].max()-0.5, X.min()+50, 'EM%s' %(ens_memb+8),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), time[ens_memb+2].max(), Y.min(), 3500.])

### 10th subplot
    X = time[ens_memb+9]
    Y = np.transpose(height[ens_memb+9])
    ax9 = plt.subplot(gs[9, :])
    im9 = ax9.contourf(X, Y, result[ens_memb+9].T, levels,cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax9.text(time[ens_memb+2].max()-0.5,X.min()+50, 'EM%s' %(ens_memb+9),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            #transform = ax0.transAxes,
            color = blue, fontsize = 18,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([X.min(), time[ens_memb+2].max(), Y.min(), 3500.])

#plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.subplots_adjust(hspace=0.355)

    fig.subplots_adjust(right=0.8)

# Add Colorbar
    cbaxes = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    cbar = plt.colorbar(im0, orientation = 'vertical', cax=cbaxes)
    cbar.ax.set_ylabel('%s %s %s' %(var_name[0], var_name[1], unit), fontsize = 22)
    cbar.ax.tick_params(labelsize = 20)

# title
# title
    ax0.set_title(title,  color =blue, fontsize = 26)

# labels
    ax0.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off',labelsize = 18) 
    ax1.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off',labelsize = 18) 
    ax2.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 18) 
    ax3.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 18)      
    ax4.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 18) 
    ax5.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 18)  
    ax6.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 18) 
    ax7.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 18)
    ax8.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='off', labelsize = 18) 
    ax9.tick_params(axis='both',which='both',bottom='on',top='off',labelbottom='on', labelsize = 18) 
    ax0.set_ylabel('height', fontsize = 18)
    ax1.set_ylabel('height', fontsize = 18)
    ax2.set_ylabel('height', fontsize = 18)
    ax4.set_ylabel('height', fontsize = 18)
    ax4.set_ylabel('height', fontsize = 18)
    ax5.set_ylabel('height', fontsize = 18)
    ax6.set_ylabel('height', fontsize = 18)
    ax7.set_ylabel('height', fontsize = 18)
    ax8.set_ylabel('height', fontsize = 18)
    ax9.set_ylabel('height', fontsize = 18)
    ax9.set_xlabel('lead time', fontsize = 18)



    ax0.set_yticks(np.arange(0,3500.,1000.))
    ax0.set_xticks(np.arange(0,48,5))

    ax1.set_yticks(np.arange(0,3500.,1000.))
    ax1.set_xticks(np.arange(0,48,5))
    ax2.set_yticks(np.arange(0,3500.,1000.))
    ax2.set_xticks(np.arange(0,48,5))
    ax3.set_yticks(np.arange(0,3500.,1000.))
    ax3.set_xticks(np.arange(0,48,5))
    ax4.set_yticks(np.arange(0,3500.,1000.))
    ax4.set_xticks(np.arange(0,48,5))
    ax5.set_yticks(np.arange(0,3500.,1000.))
    ax5.set_xticks(np.arange(0,48,5))
    ax6.set_yticks(np.arange(0,3500.,1000.))
    ax6.set_xticks(np.arange(0,48,5))
    ax7.set_yticks(np.arange(0,3500.,1000.))
    ax7.set_xticks(np.arange(0,48,5))
    ax8.set_yticks(np.arange(0,3500.,1000.))
    ax8.set_xticks(np.arange(0,48,5))
    ax9.set_yticks(np.arange(0,3500.,1000.))
    ax9.set_xticks(np.arange(0,48,5))
    if sfig == 1:
        SF.save_figure_portrait(directory, figure_name, form)
    else:
        plt.show()