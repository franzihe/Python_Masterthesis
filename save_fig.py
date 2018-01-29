
# coding: utf-8

# In[ ]:

import matplotlib.pyplot as plt


# In[ ]:

### Save Figure
def save_figure_landscape_a4(directory, figure_name, form):
    plt.savefig('%s/%s' % (directory, figure_name), orientation = 'landscape',
           papertype = 'a4', format = form)


# In[ ]:

def save_figure_portrait(directory, figure_name,form):
    plt.savefig('%s/%s' % (directory, figure_name), orientation = 'portrait',
           papertype = 'a4', format = form )


def save_figure_landscape(directory, figure_name, form):
    plt.savefig('%s/%s' % (directory, figure_name), orientation = 'landscape', format = form)