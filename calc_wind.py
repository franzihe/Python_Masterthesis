
# coding: utf-8

# In[ ]:

import numpy as np
import math




# In[ ]:

def totalwind(wind_u, wind_v):
    V = np.sqrt(wind_u**2 + wind_v**2)
    theta_deg = (180./math.pi)*np.arctan2(wind_v,wind_u)    
    #convert this wind vector to the meteorological convention of the direction the wind is coming from:
    theta_deg_from = theta_deg + 180.
    # convert angle from "trig" to cardinal
    theta = 90. - theta_deg_from
    return(V,theta);

