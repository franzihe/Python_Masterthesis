
# coding: utf-8

# In[1]:

import os


# In[2]:

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


# In[ ]:



