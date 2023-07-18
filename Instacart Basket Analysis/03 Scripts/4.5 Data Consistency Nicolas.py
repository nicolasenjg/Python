#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import pandas as pd
import numpy as np
import os


# In[2]:


path=r'C:\Users\Nico\Desktop\Curso Data Analytics\Module 4\Instacart Basket Analysis'


# In[3]:


df_prods = pd.read_csv(os.path.join(path, '02 Data', 'Original Data', 'products.csv'), index_col = False)


# In[6]:


df_ords = pd.read_csv(os.path.join(path, '02 Data', 'Prepared Data', 'orders_wrangled.csv'), index_col = False)


# In[7]:


df_ords.describe()


# In[8]:


# create a data frame
df_test = pd.DataFrame()


# In[9]:


# Create a mix type column

df_test['mix'] = ['a','b', 1, True]


# In[10]:


df_test.head()


# In[11]:


# Check for mixed types
for col in df_test.columns.tolist():
 weird = (df_test[[col]].applymap(type) != df_test[[col]].iloc[0].apply(type)).any(axis = 1)
 if len (df_test[weird]) > 0:
   print (col)


# In[12]:


df_test['mix'] = df_test['mix'].astype('str')


# In[13]:


# Finding missing values

df_prods.isnull().sum()


# In[14]:


df_prods.isnull()


# In[15]:


# Create df just with the Items with missing values
df_nan = df_prods[df_prods['product_name'].isnull()==True]


# In[16]:


df_nan


# In[17]:


# Create a new variable that acts like a flag based on the missing value.


# In[18]:


df_prods.shape


# In[19]:


# same to create df_nan but False instead of true
df_prods_clean = df_prods[df_prods['product_name'].isnull()==False]


# In[21]:


df_prods_clean.shape


# In[22]:


#Finding duplicates
df_dups=df_prods_clean[df_prods_clean.duplicated()]


# In[23]:


df_dups


# In[24]:


df_prods_clean.shape


# In[25]:


#droping duplicates
df_prods_clean_no_dups = df_prods_clean.drop_duplicates()


# In[26]:


df_prods_clean_no_dups.shape


# In[27]:


# exporting clean data
df_prods_clean_no_dups.to_csv(os.path.join(path, '02 Data', 'Prepared Data', 'products_checked.csv'))


# # Tasks

# ### Data consistency

# In[28]:


df_ords.describe()
# there are not inconsistencies


# In[29]:


# Check for mixed types
for col in df_ords.columns.tolist():
 weird = (df_ords[[col]].applymap(type) != df_ords[[col]].iloc[0].apply(type)).any(axis = 1)
 if len (df_ords[weird]) > 0:
   print (col)
   #no mix were found


# In[30]:


# Finding missing values

df_ords.isnull().sum()


# In[31]:


# 206209 orservations found


# In[34]:


# I decided to not do anything since the missing values are most likely to be from first time users that wont have previous information 
#stored in th data base, this also give us information


# In[35]:


#Finding duplicates
df_dups_ords=df_ords[df_ords.duplicated()]


# In[36]:


df_dups_ords


# In[37]:


df_dups_ords.size


# In[38]:


# there is no duplicates


# In[39]:


# exporting clean data
df_ords.to_csv(os.path.join(path, '02 Data', 'Prepared Data', 'orders_checked.csv'))


# In[ ]:




