
# coding: utf-8

# In[ ]:

import sys
sys.path.append('/Volumes/SANDISK128/Documents/Thesis/Python/')
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
import save_fig as SF


# In[ ]:

# Plotting data on a map (Example Gallery) https://matplotlib.org/basemap/users/examples.html
def create_basemap():
    m = Basemap(projection='merc',             
                llcrnrlon=-80., urcrnrlon=50.,             
                llcrnrlat=15.,urcrnrlat=75.,             
                resolution='l')
    return(m);


# In[ ]:

### PLOT FIGURE
def create_figure(m,fillcon):
    fig = plt.figure(figsize = (20,14.15))
    ax = fig.add_subplot(1,1,1)

### Draw Latitude Lines
    m.drawparallels(np.arange(-90.,120.,10.),labels=[1,0,0,0],fontsize=20,linewidth=0.2)
### Draw Longitude Lines
    m.drawmeridians(np.arange(-180.,180.,10.),labels=[0,0,0,1],fontsize=20,linewidth=0.2)

### Draw Map

    if fillcon == 1:
        # AR, IWV
        m.drawcoastlines(color=[np.array([50,50,50])/champ])
        m.fillcontinents(color='grey',alpha=0.18)
    else:
        # DT, JTMSLP
        m.drawcoastlines()

    m.drawmapboundary()
    m.drawcountries()
    
    return(fig, ax);


# In[ ]:

### Define colorbar colors
champ = 255.
date_blue = np.array([1,74,159])/champ           # for the date

no01 = np.array([255,255,255])/champ
no02 = np.array([255,0,0])/champ
no03 = np.array([255,209,177])/champ
no04 = np.array([255,118,86])/champ


# In[ ]:

# Atmospheric River
def AR_colorbar():
# IVT
    no1 = no01
    no2 = np.array([250,255,0])/champ
    no3 = np.array([255,203,0])/champ
    no4 = np.array([255,121,0])/champ
    no5 = no02
    no6 = np.array([148,0,97])/champ
    no7 = np.array([101,0,137])/champ
# contour color between IVT levels    
    no8 = np.array([130,102,0])/champ
    
    I_map = colors.ListedColormap([no1, no2, no3, no4, no5, no6, no7])
    I_levels = np.arange(0,1900,250)
    I_norm = colors.BoundaryNorm(boundaries = I_levels, ncolors=I_map.N)
    
    return(I_levels, I_norm, I_map, no8);


# In[ ]:

# Dynamic Tropopause map

def DT_colorbar():
# potential Temperature
    no1 = np.array([231,231,231])/champ
    no2 = np.array([201,201,201])/champ
    no3 = np.array([171,171,171])/champ
    no4 = np.array([140,140,140])/champ
    no5 = np.array([110,110,110])/champ
    no6 = np.array([102,81,224])/champ
    no7 = np.array([105,115,224])/champ
    no8 = np.array([103,134,255])/champ
    no9 = np.array([132,159,254])/champ
    no10= np.array([178,202,255])/champ
    no11= np.array([217,241,255])/champ
    no12= no03
    no13= np.array([255,165,133])/champ
    no14= no04
    no15= np.array([255,62,12])/champ
    no16= no02
    no17= np.array([244,0,146])/champ
    no18= no3
    no19= no2
    no20= no1
    no21= no01
# barbcolor
    no22 = np.array([80,80,81])/champ
    
    PT_map = colors.ListedColormap([no1, no2, no3, no4, no5, no6, no7, no8, no9, no10,                                     no11, no12, no13, no14, no15, no16, no17, no18, no19, no20,                                     no21])
    PT_levels = np.arange(258,390,6)
    PT_norm = colors.BoundaryNorm(boundaries = PT_levels, ncolors=PT_map.N)
    
    return(PT_levels, PT_norm, PT_map, no22);


# In[ ]:

# Jet, Thickness, MSLP

def JTM_PW_colorbar():
# tot. precipitable water (grey scale)
    no1 = np.array([245,245,245])/champ
    no2 = np.array([222,222,222])/champ
    no3 = np.array([193,193,193])/champ
    no4 = np.array([164,164,164])/champ
    no5 = np.array([135,135,135])/champ
    no6 = np.array([106,106,106])/champ
    no7 = np.array([77,77,77])/champ
    
    PW_map = colors.ListedColormap([no1, no2, no3, no4, no5, no6, no7])
    PW_levels = np.arange(14.,78.,8.)
    PW_norm = colors.BoundaryNorm(boundaries = PW_levels, ncolors=PW_map.N)
    
    return(PW_levels, PW_norm, PW_map);


# In[ ]:

def JTM_wind_colorbar():
# 250 hPa wind speed (colored scale)
    no11 = no01
    no12 = np.array([196,225,255])/champ
    no13 = np.array([131,158,255])/champ
    no14 = no03
    no15 = no04
    no16 = np.array([239,102,178])/champ
    no17 = np.array([243,0,146])/champ
    
    U_map = colors.ListedColormap([no11, no12, no13, no14, no15, no16, no17])
    U_levels = np.arange(40,120,10)
    U_norm = colors.BoundaryNorm(boundaries = U_levels, ncolors=U_map.N)
    
    return(U_levels, U_norm, U_map);


# In[ ]:

def IWV_U850_colorbar():
# tot. precipitable water (colorbar)
    no1 = np.array([255,255,255])/champ
    no2 = np.array([70,0,255])/champ
    no3 = np.array([6,109,255])/champ
    no4 = np.array([0,196,38])/champ
    no5 = np.array([14,223,11])/champ
    no6 = np.array([255,228,0])/champ
    no7 = np.array([255,180,0])/champ
    no8 = np.array([255,94,0])/champ
    no9 = np.array([255,0,0])/champ
    no10 = np.array([225,0,0])/champ
    no11 = np.array([139,0,106])/champ
    no12 = np.array([102,0,137])/champ

# pressure lines
    no13 = np.array([16,16,16])/champ
    
    PW_map = colors.ListedColormap([no1, no2, no3, no4, no5, no6, no7, no8, no9, no10, no11])
    PW_levels = (np.append(np.arange(16,56,4),[62]))
    PW_norm = colors.BoundaryNorm(boundaries = PW_levels, ncolors=PW_map.N)

    return(PW_levels, PW_norm, PW_map, no13)


# In[ ]:

def add_colorbar(cs, cbaxes, lev_ticks, label, xticks):
    if len(lev_ticks) == 0:
        # AR, DT
        cbar = plt.colorbar(cs,orientation='horizontal', cax = cbaxes)
    else:
        cbar = plt.colorbar(cs,orientation='horizontal',cax = cbaxes, ticks=lev_ticks)
    
    cbar.ax.set_xlabel(label,fontsize = 22)
    cbar.ax.set_xticklabels(xticks)  # horizontal colorbar
    cbar.ax.tick_params(labelsize=20)
    return(cbar);


# In[ ]:

# Add colorbar
def add_colorbar_one(fig, cs, lev_ticks, label, xticks ):
    
    cbaxes = fig.add_axes([0.14, 0.05, .75, .045] )   #[left, bottom, width, height] 
        
    cbar = add_colorbar(cs, cbaxes, lev_ticks, label, xticks)

    return(cbar);


# In[ ]:

# Two colorbars at bottom
def add_colorbar_two(fig, cs1, cs2,  lev_ticks1, lev_ticks2, label1, label2, xticks1, xticks2):
    cbaxes1 = fig.add_axes([0.57, 0.05, 0.3, 0.045]) 
    cbaxes2 = fig.add_axes([0.15, 0.05, 0.3, 0.045]) 

    cbar1 = add_colorbar(cs1, cbaxes1, lev_ticks1, label1, xticks1)
    cbar2 = add_colorbar(cs2, cbaxes2, lev_ticks2, label2, xticks2)
    
    return(cbar1, cbar2)


# In[ ]:

# Add Textbox
def add_textbox(ax,calday, day, calmon, year, hour):
    ax.text(0.98,0.94, '%s, %s %s %s   %s$\,$UTC' %(calday, day, calmon, year, hour),     # x, y
            verticalalignment = 'bottom',  horizontalalignment='right',
            transform = ax.transAxes,
            color =date_blue, fontsize=26,
            bbox={'facecolor':'white','alpha':1., 'pad':10})


# In[ ]:

def plot_DTmap(m, plonsPT, platsPT, PT,
               plonsVO, platsVO, rel_vort,
               plonsU, platsU, wind_u, wind_v, 
               sfig, directory, figure_name, form,
               calday, day, calmon, year, time):
    fillcontinents = 0
    fig, ax = create_figure(m,fillcontinents)
### Plot contour lines for pot. temp and fill
    PT_levels, PT_norm, PT_map, PT_no22 = DT_colorbar()
    cs = m.contourf(plonsPT, platsPT, PT, PT_levels, norm = PT_norm, cmap = PT_map)
### Plot contour lines for layer averaged rel. vort 925-850 hPa
    thickness = np.arange(.5*10**(-4), 6*10**(-4),.5*10**(-4))
    CVO = m.contour(plonsVO, platsVO, rel_vort, thickness, colors='k')

### plot wind barbs
# use only every 20, 35 value from the wind
    m.barbs(plonsU[::20,::35], platsU[::20,::35], wind_u[::20,::35], wind_v[::20,::35], barbcolor=[PT_no22])

### Add one Colorbar
    lev_ticks = []
    label = 'Potential temperature [K]'
    xticks = ['','276', '294', '312', '330', '348', '366', '']
    add_colorbar_one(fig, cs, lev_ticks, label, xticks )


### Add Textbox
    add_textbox(ax, calday, day, calmon, year, time)
    
### Save

    if sfig == 1:
        SF.save_figure_landscape(directory, figure_name, form)



# In[ ]:

def plot_ARmap(m, plonsIVT, platsIVT, IVT,
              lon_flux, lat_flux, u_flux, v_flux,
              sfig, directory, figure_name, form,
               calday, day, calmon, year, time):
    fillcontinents = 1
    fig, ax = create_figure(m,fillcontinents)

### Plot contour lines for IVT and fill
    IVT_levels, IVT_norm, IVT_map, IVT_no8 = AR_colorbar()
    cs = m.contourf(plonsIVT, platsIVT, IVT, IVT_levels, norm = IVT_norm, cmap=IVT_map)
    CS2 = plt.contour(cs, levels = cs.levels, linewidths=0.4, colors=[IVT_no8])

# Add arrows to show the IVT vectors
# every 20, 35th value
# scale_units is ‘inches’, scale is 10000.0, and (u,v) = (400,300) = 500 kg/(ms), then the vector will be 
# U/scale = 0.05 inches long.
# For 0.6 inch == 1.524cm --> U(=500)/0.6 = 833.3
    ref_key = 500.   # equals U
    scale = 10*ref_key/0.6 
    Q = m.quiver(lon_flux[::700],lat_flux[::700],u_flux[::700],v_flux[::700],scale = scale,scale_units = 'inches',
             pivot='middle',zorder=6)
    qk = plt.quiverkey(Q, 0.9, 0.9, ref_key*10, '500$\,$kg$\,$m$^{-1}\,$s$^{-1}$', labelpos ='W', 
                   fontproperties = {'size': 20})

### Add one Colorbar 
    lev_ticks = []
    label = 'IWT [kg$\,$m$^{-1}\,$s$^{-1}$]'
    xticks = ['', '250', '500', '750', '1000', '1250', '1500']  
    cbar = add_colorbar_one(fig, cs, lev_ticks, label, xticks)
# Make a colorbar for the ContourSet returned by the contourf call.
# Add the contour line levels to the colorbar
    cbar.add_lines(CS2)

### Add Textbox
    add_textbox(ax, calday, day, calmon, year, time)

### Save
    if sfig == 1:
        SF.save_figure_landscape(directory, figure_name, form)




# In[ ]:

def plot_IWV_U850map(m, plonsPW, platsPW, PW,
              plonsMSL, platsMSL, MSL, 
              plonsU, platsU, wind_u, wind_v,
              sfig, directory, figure_name, form,
               calday, day, calmon, year, time):
    fillcontinents = 1
    fig, ax = create_figure(m,fillcontinents)
### Plot contour lines for precipitable water
    PW_levels, PW_norm, PW_map, PW_no13 = IWV_U850_colorbar()
    cp = m.contourf(plonsPW, platsPW, PW, PW_levels, norm = PW_norm, cmap = PW_map)

### Plot MSL pressure every 2 hPa
    clevs = np.arange(900,1100.,4.)
    cc = m.contour(plonsMSL, platsMSL, MSL, clevs, colors = [PW_no13], linewidths = 1.8, linestyles = 'dashed')
    plt.clabel(cc, fontsize=16, inline = 1, fmt ='%1.0f')

### Plot contour lines for 850-hPa wind 
# every 20,35 values from the wind
    cs = m.quiver(plonsU[::20,::35], platsU[::20,::35], wind_u[::20,::35], wind_v[::20,::35])#, Ulevels, norm = norm, cmap=Umap)

### Add one Colorbar
    lev_ticks = PW_levels
    label = 'TCWV [mm]'
    xtick = ['', '24', '28', '32', '36', '40', '44', '48', '52','62']
    add_colorbar_one(fig, cp, lev_ticks, label, xtick )

### Add Textbox
    add_textbox(ax, calday, day, calmon, year, time)    
### Save
    if sfig == 1:
        SF.save_figure_landscape(directory, figure_name, form)


# In[ ]:

def plot_JTHMSPL(m, plonsPW, platsPW, PW,
              plonsMSL, platsMSL, MSL, 
              plonsUV, platsUV, Uabs,
              plonsZ, platsZ, Z,
              sfig, directory, figure_name, form,
               calday, day, calmon, year, time):
    fillcontinents = 0
    fig, ax = create_figure(m,fillcontinents)
### Plot contour lines for precipitable water
    PW_levels, PW_norm, PW_map = JTM_PW_colorbar()
    cs1 = m.contourf(plonsPW, platsPW, PW, PW_levels, norm = PW_norm, cmap = PW_map)


### Plot contour lines for 250-hPa wind and fill
    U_levels, U_norm, U_map = JTM_wind_colorbar()
    cs2 = m.contourf(plonsUV, platsUV, Uabs, U_levels, norm = U_norm, cmap=U_map)

### Plot MSL pressure every 4 hPa
    clevs = np.arange(900,1100.,4.)
    cc = m.contour(plonsMSL, platsMSL, MSL, clevs, colors='k', linewidths = 1.8)
    plt.clabel(cc, fontsize=16, inline = 1, fmt ='%1.0f')

### Plot the 1000-500 hPa thickness
    thlevs1 = np.arange(450., 540., 6.)
    thlevs2 = np.arange(546., 650., 6.)

    cth1 = m.contour(plonsZ, platsZ, Z, thlevs1, colors='b', linewidths = 2., linestyles = 'dashed')
    cth2 = m.contour(plonsZ, platsZ, Z, thlevs2, colors='r', linewidths = 2., linestyles = 'dashed')
    plt.clabel(cth1, fontsize = 16, inline = 1, fmt = '%1.0f')
    plt.clabel(cth2, fontsize = 16, inline = 1, fmt = '%1.0f')


### Add two Colorbars
    lev_tick1 = []
    lev_tick2 = []
    label1 = label1 = 'U$_250\,hPa$ [m$\,$s$^{-1}$]'
    label2 = 'TCWV [mm]'
    xticks1 = ['', '50', '60', '70', '80', '90', '100']
    xticks2 = ['', '22', '30', '38', '46', '54', '62']
    add_colorbar_two(fig, cs1, cs2,  lev_tick1, lev_tick2, label1, label2, xticks1, xticks2)


### Add Textbox
    add_textbox(ax, calday, day, calmon, year, time)    
### Save
    if sfig == 1:
        SF.save_figure_landscape(directory, figure_name, form)

