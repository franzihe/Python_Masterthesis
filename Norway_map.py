
# coding: utf-8

# # Get a location map of Norway, including Haukeliseter station

# In[1]:

import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap, shiftgrid
import numpy as np

get_ipython().magic('matplotlib inline')



# In[2]:

lonH = 7.2143      # location Haukeliseter
latH = 59.8118


lonK = 20.409571     # location Kiruna
latK = 67.841000

lonN = 9.539730     # location Norway country name
latN = 61.575658

lonS = 16.913194     # location Sweden country name
latS = 64.872623 

lonM = 15.       # location of MEPS centrum
latM = 63.5


# In[3]:

fig = plt.figure(figsize=(15,12.5))
ax = fig.add_subplot(1,1,1)



m = Basemap(projection='merc',             llcrnrlon=0., urcrnrlon=30.,             llcrnrlat=55.,urcrnrlat=70.,             resolution='l')

### Draw Latitude Lines
m.drawparallels(np.arange(-90.,120.,5.),labels=[1,0,0,0],fontsize=10,linewidth=0.2)


### Draw Longitude Lines
m.drawmeridians(np.arange(-180.,180.,5.),labels=[0,0,0,1],fontsize=10,linewidth=0.2)


m.drawcoastlines()
m.drawcountries()
m.fillcontinents(lake_color='cornflowerblue')
m.drawmapboundary(fill_color = 'cornflowerblue')
#m.printcountries()
#plonH,platH = m(lonH,latH)
#plonK,platK = m(lonK,latK)
#plonN,platN = m(lonN,latN)
#plonS,platS = m(lonS,latS)




def plt_txt_st(lon,lat,name):
    x,y = m(lon,lat)
    plt.text(x,y,name,fontsize = 20, fontweight = 'bold',
        ha='left',va='bottom',color='k')
    m.plot(x,y,'o',markersize=16)

name = 'Haukeliseter'
plt_txt_st(lonH,latH,name)

name = 'Kiruna'
plt_txt_st(lonK,latK,name)

name = 'model center'
plt_txt_st(lonM,latM,name)


def plt_txt_con(lon,lat,name):
    x,y = m(lon,lat)
    plt.text(x,y,name,fontsize = 25, fontstyle='italic',
            ha='center')

name = 'Norway'
plt_txt_con(lonN,latN,name)

name = 'Sweden'
plt_txt_con(lonS,latS,name)


plt.savefig('../Observations/figs/locations.png')



# In[ ]:



