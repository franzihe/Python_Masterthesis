
# coding: utf-8

# In[ ]:

import numpy as np



# In[ ]:
# 
# def accumulation_dt60_for48h(df):
# #### connect two days together to calculate the accumulation within 48hours #########
#     acc48 = []
#     for i in range(0,(np.asarray(df).shape[1]-1)):
#         df1 = np.asarray(df)[:,i]
#         df2 = np.asarray(df)[:,i+1]
#         b = (np.concatenate((df1,df2),axis=0))
#         acc48.append(b)
#     acc48 = np.transpose(acc48)
# 
# #### total accumulation in 48hours #######
#     tot = []
#     tot.append(np.zeros(acc48.shape[1]))
#     for i in range(0,acc48.shape[0]-1):
#         di = tot[(i)] + np.diff([np.asarray(acc48)[(i),:], np.asarray(acc48)[(i+1),:]],axis = 0)
#         tot = np.concatenate((tot, di),axis = 0)
# 
# #### total accumulation over 48h, every 60 min #####
#     tot_60 = []
#     for i in range(0,48):
#         tidx = tot[i*60+59,:] - tot[0*60,:]
#         tot_60.append(tidx)
#         
#     return(tot_60);




def accumulation_dt60_for48h(df, ini_day):
    acc48 = []
    for i in range(0,(np.asarray(df).shape[0]-1)):
        if len(np.asarray(df)[:][i]) == 0:
             np.asarray(df)[:][i] = np.nan
        elif len(np.asarray(df)[:][i+1]) == 0:
            np.asarray(df)[:][i+1] = np.nan
        df1 = np.asarray(df)[:][i]
        df2 = np.asarray(df)[:][i+1]
        b = (np.concatenate((df1,df2),axis=0))
        acc48.append(b)

#### total accumulation in 48hours each 60 minutes#######
    acc48_arr = np.asarray(acc48[:][(ini_day-1)])
    tot = []
    tot.append(0.0)
    for i in range(0, acc48_arr.shape[0]):
        di =  np.nansum( [tot[i], acc48_arr[:][i]], axis = 0)
        tot.append(di)
        
    return(tot);
