# coding: utf-8

# # Dynamic Tropopause Map
# 
#  http://www.met.nps.edu/~hmarcham/2012.html#DT
#  The dynamic tropopause map contains
#  DT (1.5-PVU surface)
#     - potential temperature (shaded, K)
#     - wind barbs (knots)
#     - 925-850hPa layer-averaged cyclonic relative vorticity (black contours, every 0.5 x 10^-4 s^-1)
# 
# 
# 
#  http://apps.ecmwf.int/codes/grib/param-db
#  #### Parameters from ECMWF
#     - name = 'Potential temperature',      shortName = 'pt',     [K]
#     - name = 'U component of wind',        shortName = 'u',      [m s^-1]
#     - name = 'V component of wind',        shortName = 'v',      [m s^-1]
#     - name = 'Vorticity (relative)',       shortName = 'vo',     [s^-1]
# 
# 

# https://software.ecmwf.int/wiki/display/CKB/How+to+plot+GRIB+files+with+Python+and+matplotlib


import pygrib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap, shiftgrid
import numpy as np
from scipy import ndimage
from datetime import date
import calendar
#get_ipython().magic('matplotlib inline')


# In[ ]:

### define colors for colorbar
champ = 255
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
no12= np.array([255,209,177])/champ
no13= np.array([255,165,133])/champ
no14= np.array([255,118,86])/champ
no15= np.array([255,62,12])/champ
no16= np.array([255,0,0])/champ
no17= np.array([244,0,146])/champ
no18= np.array([171,171,171])/champ
no19= np.array([201,201,201])/champ
no20= np.array([231,231,231])/champ
no21= np.array([255,255,255])/champ

no22 = np.array([80,80,81])/champ



m = Basemap(projection='merc',             llcrnrlon=-60., urcrnrlon=50.,             llcrnrlat=30.,urcrnrlat=75.,             resolution='l')



def opengrib(yyyy, mm, dd, tt, pm, path):
    grib = '%s/%s/param_%s_%s%s%s_%s00.grib' % (path,pm,pm,yyyy,mm,dd,tt)
    grbs = pygrib.open(grib)
    return(grbs);



def selectgrb(grbs, sN, tOL, lv):
    val = grbs.select()[0]
    val = grbs.select(shortName = sN, typeOfLevel = tOL, level = lv)[0]
    val = val.values
    return(val);



def shiftgrb(grb,val):
    lat,lon = grb.latlons()
    lons = lon[0,:]
    val,lons = shiftgrid(180., val, lons, start = False)
    lats = lat[:,0]
    
    lons,lats = np.meshgrid(lons,lats)
    plons,plats = m(lons,lats)
    return(plons,plats,val);



# use only every 20, 35 value from the wind
### Wind
def windsel(grbUV,wind_u,wind_v):
    latUV,lonUV = grbUV.latlons()
    lonsUV = lonUV[0,:]
    wind_u,lonsUV = shiftgrid(180.,wind_u,lonsUV,start=False)
    latsUV = latUV[:,0]

    # use only every 20, 35 value from the wind
    UVlats = np.zeros((64,),dtype =float)
    UVlons = np.zeros((74,),dtype =float)
    u_wind = np.zeros((64,2560), dtype = float)
    v_wind = np.zeros((64,2560), dtype = float)
    u_wind2 = np.zeros((64,74),dtype = float)
    v_wind2 = np.zeros((64,74),dtype = float)

    

    for i in range(0,64):
        UVlats[i] = latsUV[i*20]
        u_wind[i,:] = wind_u[i*20,:]
        v_wind[i,:] = wind_v[i*20,:]

    for k in range(0,74):
        UVlons[k] = lonsUV[k*35]   
        u_wind2[:,k] = u_wind[:,k*35]
        v_wind2[:,k] = v_wind[:,k*35]
    
    UVlons,UVlats = np.meshgrid(UVlons,UVlats)
    plonsUV, platsUV = m(UVlons,UVlats)
    return(plonsUV,platsUV,u_wind2,v_wind2);



year = '2016'
mon = '12'
#day = '11'
#time = '06'

for day in range(10,29):
	day = str(day)
	for time in range(0,24,6):
		if time == 0:
			time = '00'
		elif time == 6:
			time = '06'
		time = str(time)
		
		path = '../NORSTORE/SCA/pv2000'
### Potential temperature
		parameter = 'pt'
		grbsPT = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = path)
#	
### Wind
		parameter = 'uv'
		grbsUV = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = path)
	
### Vorticity (relative)
		path = '../NORSTORE/SCA/pl'
		parameter = 'vo'
		grbsVO = opengrib(yyyy = year, mm = mon, dd = day, tt = time, pm = parameter, path = path)
#
### Dates for plotting
		yr = int(year)
		mo = int(mon)
		dy = int(day)
		my_date = date(yr,mo,dy)
		calday = calendar.day_name[my_date.weekday()]
		calmon = calendar.month_abbr[mo]
#
		tOL = 'potentialVorticity'
		lv = 2000
### Potential temperature
		sN = 'pt'
		grbPT = grbsPT.select()[0]
		PT = selectgrb(grbsPT, sN, tOL, lv)
#
### Wind 
# U component of wind
		sN = 'u'
		grbUV = grbsUV.select()[0]
		wind_u = selectgrb(grbsUV, sN, tOL, lv)

# V component of wind
		sN = 'v'
		wind_v = selectgrb(grbsUV, sN, tOL, lv)
#
### Vorticity (relative)
# 925 hPa
		sN = 'vo'
		tOL = 'isobaricInhPa'
		lv = 925
		grbVO = grbsVO.select()[0]
		RV925 = selectgrb(grbsVO, sN, tOL, lv)
#
# 900 hPa
		lv = 900
		RV900 = selectgrb(grbsVO, sN, tOL, lv)
#
# 850 hPa
		lv = 850
		RV850 = selectgrb(grbsVO, sN, tOL, lv)
#
### calculating 925-850 hPa layer-averaged cyclonic relative vorticity (every 0.5 x10^-4 s-1)
# all three layers divided by number of layers
		rel_vort = (RV925+RV900+RV850)/3                         # arithmetric mean
		rel_vort = ndimage.filters.gaussian_filter(rel_vort, sigma = 2)
#
		plonsPT, platsPT, PT = shiftgrb(grbPT,PT)
		plonsVO, platsVO, rel_vort = shiftgrb(grbVO,rel_vort)
#
		plonsUV, platsUV, u_wind2, v_wind2 = windsel(grbUV,wind_u,wind_v)
#
### PLOT FIGURE
		fig = plt.figure(figsize=(15,12.5))
		ax = fig.add_subplot(1,1,1)
#
### Draw Latitude Lines
		m.drawparallels(np.arange(-90.,120.,10.),labels=[1,0,0,0],fontsize=10,linewidth=0.2)
#
### Draw Longitude Lines
		m.drawmeridians(np.arange(-180.,180.,10.),labels=[0,0,0,1],fontsize=10,linewidth=0.2)
#
### Draw Map
		m.drawcoastlines()
		m.drawmapboundary()
		m.drawcountries()
#
### Plot contour lines for pot. temp and fill
		levels = np.arange(258,390,6)
		cmap = colors.ListedColormap([no1, no2, no3, no4, no5, no6, no7, no8, no9, no10,                               no11, no12, no13, no14, no15, no16, no17, no18, no19, no20,                              no21])
		norm = colors.BoundaryNorm(boundaries = levels, ncolors=cmap.N)
		cs = m.contourf(plonsPT,platsPT,PT,levels,norm=norm,cmap=cmap)
#
### Plot contour lines for layer averaged rel. vort 925-850 hPa
		thickness = np.arange(.5*10**(-4), 6*10**(-4),.5*10**(-4))
		CVO = m.contour(plonsVO,platsVO,rel_vort,thickness,colors='k')
#
### plot wind barbs
		plt.barbs(plonsUV,platsUV,u_wind2,v_wind2,barbcolor=[no22]) #darkslategray
#
### Add Colorbar
		cbaxes = fig.add_axes([0.14, 0.05, 0.75, 0.03]) 
		cbar = plt.colorbar(cs,orientation='horizontal',cax = cbaxes)#, cax = cbaxes)#, shrink=0.5)
		cbar.ax.set_xlabel('potential vorticity')
#
### Add Textbox
		ax.text(0.98,0.95, '%s, %s %s %s   %s$\,$UTC' %(calday, day, calmon, year, time),
       		verticalalignment = 'bottom',  horizontalalignment='right',
       		transform = ax.transAxes,
       		color ='blue', fontsize=16,
       		bbox={'facecolor':'white','alpha':1., 'pad':10})
#
### Title
#		fig.suptitle('Dynamic Tropopause Map at 2 PVU', fontsize=16, fontweight='bold') 
#		ax.set_title('wind barbs (m$\,$s$^{-1}$), \n potential temperature (K, shaded according to colorbar), \n 925-850$\,$hPa layer-averaged cyclonic relative vorticity (black contours, every 0.5 x 10$^{-4}$$\,$s$^{-1}$) \n',             fontsize=13)
#
### Save
		plt.savefig('../synoptic_figs/DynTropo/%s%s%s_%s.png' % (year, mon, day,time))
## with header
#		plt.savefig('../synoptic_figs/DynTropo/%s%s%s_%s_header.png' % (year, mon, day,time))
#plt.savefig('dyn_tropo.png')     # Set the output file name

	#plt.show()
		plt.close(fig)

