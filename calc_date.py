
# coding: utf-8

# In[1]:

from datetime import date
import calendar


# In[ ]:

### Dates for plotting
def get_dayname(year, mon, day):
    yr = int(year)
    mo = int(mon)
    dy = int(day)
    my_date = date(yr,mo,dy)
    calday = calendar.day_name[my_date.weekday()]
    calmon = calendar.month_abbr[mo]

    return(calday, calmon);

