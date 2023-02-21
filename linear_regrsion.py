 #!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[7]:


dataset = pd.read_csv('21centry1.csv',encoding = 'unicode_escape')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# In[8]:


print(X)


# In[9]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


# In[10]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[11]:


y_pred = regressor.predict(X_test)


# In[12]:


plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('SIPERFAQJA VS CMIMI (Training set)')
plt.xlabel('SIPERFAQJA')
plt.ylabel('CMIMI')
plt.show()


# In[13]:


plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[ ]:




