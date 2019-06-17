#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt 
import pandas as pd


# In[14]:


data = pd.read_csv('dist_vs_force_pure', sep=' ', header=None)


# In[39]:


fig = plt.figure(figsize=(5,5))
plt.title('Polymer Pulled By External Force')
ax = fig.add_subplot(111)
ax.plot(data[0],data[1], label='Distance',linewidth=2.0)
ax.plot(data[0],data[2], label='External Force',linewidth=2.0)
plt.legend()
plt.xlabel('Time Step')
plt.savefig('./pic/result.svg')
plt.savefig('./pic/result.png')
plt.show()


# In[ ]:




