
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import colormaps as cmaps




# In[2]:

### Define colorbar colors
champ = 255.
blue = np.array([1,74,159])/champ           # for the date


# In[3]:

def plot_vertical_EM(lead_time, model_level,result,var_name, fig_name, title,sfig,directory, figure_name, form):
    # create meshgrid for contourf
    x = lead_time
    y = model_level
    X, Y = np.meshgrid(x, y)
    
    z_min = 0.
    
    fig = plt.figure(figsize=(8.27,11.69))
    gs = GridSpec(6, 2)

    ens_memb = 0

### first subplot
# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
    ax0 = plt.subplot(gs[0, :])
    im0 = ax0.contourf(X, Y, result[ens_memb].T, cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
# label for EM
    ax0.text(61,3, 'EM%s' %(ens_memb),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='left',
            #transform = ax0.transAxes,
            color = blue, fontsize=12,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    ax0.axis([x.min(), x.max(), y.min(), y.max()])

### 2nd subplot
    ax1 = plt.subplot(gs[1, :])
    im1 = ax1.contourf(X, Y, result[ens_memb+1].T, cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax1.text(61,3, 'EM%s' %(ens_memb+1),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='left',
            #transform = ax0.transAxes,
            color = blue, fontsize=12,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    ax1.axis([x.min(), x.max(), y.min(), y.max()])

### 3rd subplot
    ax2 = plt.subplot(gs[2, :-1])
    im2 = ax2.contourf(X, Y, result[ens_memb+2].T, cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax2.text(41.5,3, 'EM%s' %(ens_memb+2),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='left',
            #transform = ax0.transAxes,
            color = blue, fontsize=12,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([x.min(), 50, y.min(), y.max()])

### 4th subplot
    ax3 = plt.subplot(gs[2, -1:])
    im3 = ax3.contourf(X, Y, result[ens_memb+3].T, cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax3.text(41.5,3, 'EM%s' %(ens_memb+3),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='left',
            #transform = ax0.transAxes,
            color = blue, fontsize=12,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    ax3.axis([x.min(), 50, y.min(), y.max()])

### 5th subplot
    ax4 = plt.subplot(gs[3, :-1])
    im4 = ax4.contourf(X, Y, result[ens_memb+4].T, cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax4.text(41.5,3, 'EM%s' %(ens_memb+4),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='left',
            #transform = ax0.transAxes,
            color = blue, fontsize=12,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([x.min(), 50, y.min(), y.max()])

### 6th subplot
    ax5 = plt.subplot(gs[3, -1:])
    im5 = ax5.contourf(X, Y, result[ens_memb+5].T, cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax5.text(41.5,3, 'EM%s' %(ens_memb+5),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='left',
            #transform = ax0.transAxes,
            color = blue, fontsize=12,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([x.min(), 50, y.min(), y.max()])

### 7th subplot
    ax6 = plt.subplot(gs[4, :-1])
    im6 = ax6.contourf(X, Y, result[ens_memb+6].T, cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax6.text(41.5,3, 'EM%s' %(ens_memb+6),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='left',
            #transform = ax0.transAxes,
            color = blue, fontsize=12,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([x.min(), 50, y.min(), y.max()])

### 8th subplot
    ax7 = plt.subplot(gs[4, -1:])
    im7 = ax7.contourf(X, Y, result[ens_memb+7].T, cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax7.text(41.5,3, 'EM%s' %(ens_memb+7),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='left',
            #transform = ax0.transAxes,
            color = blue, fontsize=12,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([x.min(), 50, y.min(), y.max()])

### 9th subplot
    ax8 = plt.subplot(gs[5, :-1])
    im8 = ax8.contourf(X, Y, result[ens_memb+8].T, cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax8.text(41.5,3, 'EM%s' %(ens_memb+8),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='left',
            #transform = ax0.transAxes,
            color = blue, fontsize=12,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([x.min(), 50, y.min(), y.max()])

### 10th subplot
    ax9 = plt.subplot(gs[5, -1:])
    im9 = ax9.contourf(X, Y, result[ens_memb+9].T, cmap=cmaps.viridis)#, vmin=z_min, vmax=z_max)
    ax9.text(41.5,3, 'EM%s' %(ens_memb+9),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='left',
            #transform = ax0.transAxes,
            color = blue, fontsize=12,
            bbox={'facecolor':'white','alpha':.8, 'pad':1})
# set the limits of the plot to the limits of the data
    plt.axis([x.min(), 50, y.min(), y.max()])

#plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.subplots_adjust(hspace=0.5)

    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im0, cax=cbar_ax)

# title
    ax0.set_title(title,  color =blue )

# labels
    ax1.set_xlabel('lead time')
    ax0.set_ylabel('height')
    ax1.set_ylabel('height')
    ax2.set_ylabel('height')
    ax4.set_ylabel('height')
    ax6.set_ylabel('height')
    ax8.set_ylabel('height')
    
    if sfig == 1:
    	SF.save_figure_landscape_a4(directory, figure_name, form)
    else:
        plt.show()
        


#    plt.show()
#    plt.close()


# In[ ]:



