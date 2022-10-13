#!/usr/bin/env python
# coding: utf-8

# In[44]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# In[36]:


df=pd.read_csv('netflix.csv')


# In[37]:


df.shape


# In[38]:


df.columns


# In[39]:


df.head()


# In[102]:


df.drop_duplicates()


# In[45]:


df.sort_values(by="release_year",ascending=True)


# In[94]:


labels = ['TV Shows', 'Movies']
colors = sns.color_palette('rocket_r')
plt.figure(figsize=(8,3))
plt.pie(df['type'].value_counts().sort_values(), labels = labels, colors = colors, autopct='%1.2f%%', explode=[0.1,0.1], startangle=90)
plt.title("Netflix Show Types")
plt.axis('equal')
plt.show()


# In[104]:


#Top 20 countries producing the most content for Netflix:
plt.figure(figsize=(15,7))
graph = sns.barplot(x=df.country.value_counts()[:20].index , y=df.country.value_counts()[:20].values )
graph.set_xticklabels(df.country.value_counts()[:20].index, rotation=40)
for a in graph.containers:
    graph.bar_label(a);


# In[99]:


#Visualization in US
df.new=df[(df['type']=='Movie')][['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
       'release_year', 'rating', 'duration', 'listed_in', 'description']]
US=df.new[df['country']=='United States']
US


# In[ ]:





# In[ ]:





# In[107]:


US['release_year'].value_counts(ascending=False).iloc[0:10].plot(kind='bar')
print("\n Total Movie Release - USA (2017-2021)")


# In[100]:


plt.figure(figsize=(10,8))
sns.countplot(x="rating", data=US, palette="rocket_r")
plt.title("Rating for NetFlix");


# In[101]:


(US['rating'].value_counts()/US.shape[0])*100


# In[113]:



plt.figure(figsize=(15,7))
fav_actor= sns.barplot(x=US.cast.value_counts()[:20].index , y=US.cast.value_counts()[:20].values )
fav_actor.set_xticklabels(US.cast.value_counts()[:20].index, rotation=40)
for f in fav_actor.containers:
    fav_actor.bar_label(f);


# In[ ]:





# In[ ]:




