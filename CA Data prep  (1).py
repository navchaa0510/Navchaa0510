#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.read_csv("aps_failure_set.csv")


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.isnull().sum()


# In[17]:


df.fillna(df.median(), inplace=True)


# In[20]:


df.drop_duplicates(inplace=True)


# In[19]:


new_df.shape


# In[27]:


df.dropna(inplace=True)


# In[11]:


new_df.isnull().sum()


# In[12]:


new_df=df.dropna(axis=1)


# In[13]:


new_df.shape


# In[23]:


df.describe(include="all")


# In[26]:


a = True 
b = False
c = bool(0) # boolean from integer
d = bool("Hello") # boolean from string
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# In[ ]:




