
# coding: utf-8

# In[ ]:

import numpy as np
import matplotlib.pyplot as plt


# In[ ]:

date_blue = np.array([1,74,159])/255.
memb_col = np.array([99,99,99])/255.       # ensemble member color

fontsize = 22.
tick_fs = fontsize-2
label_fs = fontsize

yl1 = ['', 0.2, '', 0.6, '',1. ,'',1.4,'',1.8,
          '',2.2,'',2.6,'', 3.]
yl2 = [0., '' , 2000.0, '' , 4000., '' , 6000., '', 8000.,'',9000.]

times = [0,'','',3,'','',6,'','',9,'','',
             12,'','',15,'','',18,'','',21,'','',24]
             
xticks1 = np.arange(0,60*60*25,60*60)
xticks2 = np.arange(0,25)

yticks1 = np.arange(0,3200.,200)
yticks2 = np.arange(0,7000.,1000)

def plt_ce_image(fig,ax0,time, height, variable, levels, v_min, v_max, xmax, ymax, xticks, yticks, cb_ticks, var_label):
    
    
    im0 = ax0.contourf(time, height, variable, levels, 
                       cmap = 'jet', 
                       extend = 'max', alpha = 1.0, 
                       vmin = v_min, vmax = v_max, origin = 'lower')

# set the limits of the plot to the limits of the data
    ax0.axis([0., xmax, 0., ymax])

# labels 
    labels_x(ax0,xticks)
    labels_y(ax0,yticks,yl1,'height [km]')
# add colorbar   
    add_colorbar(fig,im0, ax0, cb_ticks,var_label)

# tight layout
    plt.tight_layout(pad=1.4,  h_pad=2.5)



def add_colorbar(fig,im0,ax0,cb_ticks,var_label):
    cbar = fig.colorbar(im0, ax=ax0, ticks = cb_ticks, orientation = 'horizontal', pad=0.15, fraction = 0.08, shrink = 2.5)
    cbar.ax.tick_params(labelsize= tick_fs-2)
    cbar.ax.set_xlabel(var_label,fontsize = label_fs-2)


# In[ ]:

def labels_x(ax,xticks):  
# labels
    ax.set_xticks(xticks)
    ax.set_xticklabels(times, fontsize = tick_fs)
    ax.set_xlabel('time [hours]', fontsize = label_fs)



# In[ ]:


def labels_y(ax,yticks,yl,label_txt):
    # labels
    ax.set_yticks(yticks)
    ax.set_yticklabels(yl, fontsize = label_fs)
    ax.set_ylabel(label_txt, fontsize = label_fs)


    

