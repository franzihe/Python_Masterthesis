
# coding: utf-8

# In[ ]:

import numpy as np



# In[ ]:

#perform linear interpolation of the values in the gap
def interpolate_gaps(values, limit=None):
    """
    Fill gaps using linear interpolation, optionally only fill gaps up to a
    size of `limit`.
    """
    values = np.asarray(values)
    i = np.arange(values.size)
    valid = np.isfinite(values)
    filled = np.interp(i, i[valid], values[valid])

    if limit is not None:
        invalid = ~valid
        for n in range(1, limit+1):
            invalid[:-n] &= invalid[n:]
        filled[invalid] = np.nan

    return filled


# In[ ]:
def fill_values(variable, ml, ens_emb):
    for ml in range(0,1):
        if np.ma.is_masked(variable[:,ml,ens_memb,y[0],x[0]]):
            mask = np.ma.getmaskarray(variable[:,ml,ens_memb,y[0],x[0]])        
            marr = np.ma.array(variable[:,ml,ens_memb,y[0],x[0]], mask = mask, fill_value = np.nan)
            F = marr.filled(np.nan)
            intF = interpolate_gaps(F, limit = 2)
            filled.append(intF) 
        else:
            filled = variable[:,ml,ens_memb,y[0],x[0]] 
            
def mask_array(variable,ens_memb,y,x):
    if np.ma.is_masked(variable[:,:,ens_memb,y[0],x[0]]):
        mask = np.ma.getmaskarray(variable[:,:,ens_memb,y[0],x[0]])  
        fill_value = np.nan
        marr = np.ma.array(variable[:,:,ens_memb,y[0],x[0]], mask = mask, fill_value = fill_value)
        dtype = marr.filled().dtype
        filled = marr.filled()
    else:
        fill_value = np.nan
        marr = variable[:,:,ens_memb,y[0],x[0]]
        filled = marr
        dtype = marr.dtype
    return(filled, dtype)
    
              
# fill array with nan and interpolate if limit of nan is below 2
# for values at surface
def filled_val_sfc(temp_0m,ens_memb):
    if np.ma.is_masked(temp_0m[:,0,ens_memb,0,0]):
        mask = np.ma.getmaskarray(temp_0m[:,0,ens_memb,0,0])
        marr = np.ma.array(temp_0m[:,0,ens_memb,0,0], mask = mask, fill_value = np.nan)
        x = marr.filled(np.nan)
       # filled = x
        filled = interpolate_gaps(x,limit = 2)
    else:
        filled = temp_0m[:,0,ens_memb,0,0]
    return(filled)


# In[ ]:

def filled_val_ml(SA_lev,ens_memb):
    filled = np.empty((SA_lev.shape[0],SA_lev.shape[1]))
    filled[:] = np.nan
    for ml in range(0,65):
        if np.ma.is_masked(SA_lev[:,ml,0,0,0]):
            mask = np.ma.getmaskarray(SA_lev[:,ml,0,0,0])
            marr = np.ma.array(SA_lev[:,ml,0,0,0], mask = mask, fill_value = np.nan)
            x = marr.filled(np.nan)
#        filled = x
            interp_x = interpolate_gaps(x,limit = 2)
            filled[:,ml] = interp_x
        else:
            filled[:,ml] = SA_lev[:,ml,0,0,0]
    return(filled)

def fill_nan(var):
    if np.ma.is_masked(var):
        mask = np.ma.getmaskarray(var)
        marr = np.ma.array(var, mask = mask, fill_value = np.nan)
        x = marr.filled(np.nan)
    else:
        x = var
    return(x);