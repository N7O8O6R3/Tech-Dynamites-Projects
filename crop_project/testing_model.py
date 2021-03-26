#!/usr/bin/env python
# coding: utf-8

# In[1]:


from joblib import load


# In[2]:


model=load("Crop.joblib")


# In[4]:


feature=([[0.25421252, 0.27579609, 0.01636317, 3.55194693, 0.95636671,
       0.64209145, 0.14771821]])
result=model.predict(feature)


# In[6]:


print(result[0])


# In[ ]:




