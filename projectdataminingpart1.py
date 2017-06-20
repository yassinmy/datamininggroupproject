
# coding: utf-8

# In[9]:

import pandas as pd
import numpy as np
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pylab as pl


# In[10]:

data = pd.read_csv(r'https://raw.githubusercontent.com/yassinmy/datamininggroupproject/master/xAPI-Edu-Data.csv')


# In[11]:

data.info()


# In[26]:

dataint = data[['VisITedResources','Discussion', 'raisedhands']]
dataint.hist()
plt.show();


# In[29]:

data.groupby('gender').Discussion.agg(['mean'])


# In[30]:

data.groupby(['gender','Class']).Discussion.agg(['mean'])


# In[32]:

data['Class'].unique()
class_group = data.groupby('Class').apply(lambda x: len(x))
class_group

class_group.plot(kind='barh', grid=True)
plt.ylabel('Class Level')
plt.xlabel('No of Student')
plt.title('No of Student for Level of Class')


# In[35]:

absent = data.groupby(['Class', 'StudentAbsenceDays']).size()
absent


# In[39]:

absent.plot(kind='bar', grid=False)
plt.xlabel('Class Level-Absence Status')
plt.ylabel('No of Student')
plt.title('No of Student for Level of Class per Absence Status')


# In[18]:

data.head(n=2).T


# In[19]:

data.describe()


# In[20]:

categorical_features = (data.select_dtypes(include=['object']).columns.values)
categorical_features


# In[21]:

numerical_features = data.select_dtypes(include = ['float64', 'int64']).columns.values
numerical_features


# In[23]:

pivot = pd.pivot_table(data,
            values = ['raisedhands', 'VisITedResources', 'AnnouncementsView', 'Discussion'],
            index = ['gender', 'NationalITy', 'PlaceofBirth'], 
                       columns= ['ParentschoolSatisfaction'],
                       aggfunc=[np.mean], 
                       margins=True).fillna('')
pivot


# In[25]:

pivot = pd.pivot_table(data,
            values = ['raisedhands', 'VisITedResources', 'AnnouncementsView', 'Discussion'],
            index = ['gender', 'NationalITy', 'PlaceofBirth'], 
                       columns= ['ParentschoolSatisfaction'],
                       aggfunc=[np.mean, np.std], 
                       margins=True)
cmap = sns.cubehelix_palette(start = 1.5, rot = 1.5, as_cmap = True)
plt.subplots(figsize = (30, 20))
sns.heatmap(pivot,linewidths=0.2,square=True )


# In[ ]:



