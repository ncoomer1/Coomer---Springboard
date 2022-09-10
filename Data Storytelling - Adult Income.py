#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns


# In[2]:


data = pd.read_csv(r"C:\Users\nicol\Desktop\Storytelling - Adult Income Dataset\adult.csv")


# In[3]:


data.head()


# In[4]:


data.info()


# In[5]:


data.shape


# In[6]:


data['income']=data['income'].map({'<=50K':0, '>50K':1})


# In[7]:


data['income'].value_counts()


# In[8]:


data['workclass']=data['workclass'].str.replace('?', 'Private')


# In[9]:


data['native-country']=data['native-country'].str.replace('?', 'United-States')


# In[10]:


data.describe()


# In[11]:


data['workclass'].value_counts()


# In[12]:


data['occupation']=data['occupation'].replace('?', 'Prof-specialty')


# In[13]:


data.isnull().sum()


# In[14]:


data.describe()


# In[15]:


data.describe(include=['object'])


# # Relationship Analysis

# In[16]:


sns.pairplot(data)


# # Distribution across sectors
What is the average level of education in each sector?
# In[18]:


data.groupby('workclass')['educational-num'].mean().sort_values().plot(kind='barh')
plt.xlabel('Number of schooling years')
plt.title('Educational profile for different workclasses')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

It appears that state-level governmental workers had the most years of schooling, while those who never worked had the least amount of schooling at a little over 7 years.What is the average income in each sector?
# In[19]:


plt.figure(figsize=(8,8))
sns.countplot('workclass',hue='income', data=data)
plt.xticks(fontsize=8, rotation=60)
plt.title('Income Distribution in Different Workclasses')

More self-employed workers earn over $50,000 than under $50,000.Is there a dominant workclass? If so, which one?
# In[20]:


plt.figure(figsize=(8,8))
sns.countplot('workclass',data=data)
plt.xticks(fontsize=10, rotation=60)
plt.title('Workclass Distribution')

The majority of respondants work in the private sector.Does education make a difference?
# In[21]:


plt.figure(figsize=(8,8))
sns.countplot('education',hue='income', data=data)
plt.xticks(fontsize=8, rotation=60)
plt.title('Income Distribution based on different education levels')

Masters and Doctorate level employees appear to benefit the most when it comes to salary.What is the income distribution for different occupations?
# In[22]:


plt.figure(figsize=(8,8))
sns.countplot(y='occupation',hue='income', data=data)
plt.xticks(fontsize=8, rotation=60)
plt.title('Income Distribution for different occupations')

Executive/Managerial employees seem to benefit the most - appearing to have the least salary disparity.
# In[ ]:




