#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime, time

import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("C:/Users/User/Downloads/My Uber Drives - 2016.csv")


# In[3]:


df.head()


# In[4]:


df.columns = df.columns.str.replace("*","")


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


df.shape


# In[8]:


df.describe()


# In[9]:


df.isnull().sum()


# In[10]:


plt.figure(figsize=(15,10))
sns.heatmap(df.isnull())


# In[11]:


df.dropna(axis=0, subset=['END_DATE','CATEGORY','START','STOP'], how='all', inplace=True)


# In[12]:


df.isnull().sum()


# In[13]:


df['PURPOSE'].fillna(method = 'ffill', inplace = True)


# In[14]:


df.isnull().sum()


# In[15]:


df['START_DATE'] = pd.to_datetime(df['START_DATE'], errors='coerce')
df['END_DATE'] = pd.to_datetime(df['END_DATE'], errors='coerce')


# In[16]:


df.info()


# In[17]:


df['CATEGORY'].value_counts()


# In[18]:


df['CATEGORY'].value_counts().plot(kind='bar', color='r')


# In[19]:


start_point = df.START.value_counts()
start_point


# In[20]:


start_point.head()


# In[21]:


start_point[start_point>10].plot(kind = 'pie')


# In[22]:


plt.figure(figsize=(20,20))
start_point[start_point<=10].plot(kind = 'pie')


# In[23]:


stop_point = df.STOP.value_counts()
stop_point


# In[24]:


stop_point.head()


# In[25]:


stop_point[stop_point>10].plot(kind = 'pie')


# In[26]:


plt.figure(figsize = (20,20))
stop_point[stop_point<=10].plot(kind = 'pie')


# In[27]:


miles = df.MILES.value_counts()
miles


# In[28]:


miles[miles > 10].plot(kind = 'bar')


# In[29]:


plt.figure(figsize = (6, 6))
miles[miles > 10].plot(kind = 'pie')


# In[30]:


df.PURPOSE.value_counts().plot(kind = 'bar')


# In[31]:


plt.figure(figsize = (15, 10))
sns.countplot(df['PURPOSE'])


# In[32]:


df


# In[33]:


df['MINUTES'] = df.END_DATE - df.START_DATE


# In[34]:


df.head()


# In[35]:


df['MINUTES'] = df['MINUTES'].dt.total_seconds()/60


# In[36]:


df.head()


# In[37]:


plt.figure(figsize = (15, 5))
plt.subplot(1,2,1)
sns.boxplot(data = df, x = df['PURPOSE'], y = df['MILES'])
plt.xticks(rotation = 45)

plt.subplot(1,2,2)
sns.boxplot(data = df, x = df['PURPOSE'], y = df['MINUTES'])
plt.xticks(rotation = 45)


# In[38]:


plt.figure(figsize = (15, 5))
plt.subplot(1,2,1)
sns.boxplot(data = df, x = df['PURPOSE'], y = df['MILES'], showfliers = False)
plt.xticks(rotation = 45)

plt.subplot(1,2,2)
sns.boxplot(data = df, x = df['PURPOSE'], y = df['MINUTES'], showfliers = False)
plt.xticks(rotation = 45)


# In[39]:


pd.DataFrame({'Min': df.groupby(['PURPOSE'])['MILES'].min(),
             'Mean': df.groupby(['PURPOSE'])['MILES'].mean(),
             'Max': df.groupby(['PURPOSE'])['MILES'].max()})


# In[40]:


pd.DataFrame({'Min': df.groupby(['PURPOSE'])['MINUTES'].min(),
             'Mean': df.groupby(['PURPOSE'])['MINUTES'].mean(),
             'Max': df.groupby(['PURPOSE'])['MINUTES'].max()})


# In[41]:


df.groupby('PURPOSE')['MILES'].describe()


# In[42]:


df.columns


# In[43]:


def round(x):
    if x['START'] == x['STOP']:
        return 'Yes'
    else:
        return 'No'


# In[44]:


df['ROUND_TRIP'] = df.apply(round, axis = 1)


# In[45]:


df.head()


# In[46]:


sns.countplot(df['ROUND_TRIP'])


# In[47]:


df.head()


# In[48]:


df['MONTH'] = pd.DatetimeIndex(df['START_DATE']).month


# In[49]:


dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'July', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}


# In[50]:


df.head()


# In[51]:


plt.figure(figsize = (15, 7))
sns.countplot(df['MONTH'])


# In[52]:


pd.set_option('display.max_rows',None)


# In[53]:


df.groupby(['MONTH','PURPOSE'])['ROUND_TRIP'].count()


# In[54]:


sns.lineplot(data = df, x = df['MINUTES'], y = df['MILES'])


# In[55]:


sns.countplot(data = df, x = df['PURPOSE'], hue = 'CATEGORY')
plt.xticks(rotation = 45)


# In[56]:


df.describe()


# In[ ]:




