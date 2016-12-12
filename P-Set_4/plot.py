
# coding: utf-8

# In[14]:

import matplotlib.pyplot as plt


# In[15]:

get_ipython().magic(u'matplotlib inline')


# In[16]:

data = []
with open('datafile_rt.txt') as f:
    for line in f:
        print f
        data_line = line.split()
        print data_line
        for i, d in enumerate (data_line):
            print d
            data.append(d)


# In[11]:

data_list = [float(d) for d in data]


# In[12]:

data_list


# In[17]:

fig, ax = plt.subplots()
ax.plot(data, 'ro')


# In[ ]:



