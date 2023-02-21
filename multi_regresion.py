#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


dataset = pd.read_csv('21centry2.csv',encoding = 'unicode_escape')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# In[3]:



print(y)


# In[4]:


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(sparse=False), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))


# In[5]:


#from sklearn.impute import SimpleImputer
#imputer=SimpleImputer(missing_values=np.Çmimisipaskërkesës)
#imputer=fit(X[:,3])


# In[6]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# In[7]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[8]:


y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


# In[ ]:





# In[ ]:





# In[ ]:




