#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[7]:


dataset=pd.read_csv('21centry2.csv',encoding = 'unicode_escape')
X=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values


# In[8]:


from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X,y)  


# In[12]:


from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)
X_poly=poly_reg.fit_transform(X)
lin_reg_2=LinearRegression()
lin_reg_2.fit(X_poly,y)


# In[16]:


plt.scatter(X,y,color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)),color='blue')
plt.title('home(Linear Regression)')
plt.xlabel('')
plt.ylabel('')
plt.show()


# In[15]:


lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))


# In[ ]:


#congratulation :)


# In[ ]:





# In[ ]:





# In[ ]:




