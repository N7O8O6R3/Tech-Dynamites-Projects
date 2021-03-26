#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


# In[58]:


df=pd.read_csv('Crop_recommendation.csv')


# In[59]:


df.head()


# In[60]:


df.info()


# In[61]:


df.describe()


# In[62]:


import matplotlib.pyplot as plt


# In[63]:


#get_ipython().run_line_magic('matplotlib', 'inline')


# In[64]:


from sklearn.model_selection import train_test_split
train_set, test_set  = train_test_split(df, test_size=0.2, random_state=42)
print(f"Rows in train set: {len(train_set)}\nRows in test set: {len(test_set)}\n")


# In[65]:


train_set.head()


# In[66]:


test_set.head()


# In[67]:


df.hist(bins=50,figsize=(20,15))


# In[68]:


from sklearn.pipeline import Pipeline


# In[69]:


#scaling the features
# 1)min max scaling
#     (value-min)/(max-min)
#     we can use min-maxScaler
# 2)standardization
#     (value-mean)/std
#     we can use StandardScaler for this


# In[70]:


from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


# In[71]:


my_pipeline=Pipeline([
#     ('imputer',SimpleImputer(strategy="median")),
    ('std_scaler',StandardScaler()),
])


# In[72]:


train_set_label=train_set["label"].copy()
train_set.drop('label', inplace=True, axis=1)


# In[73]:


train_set.head()


# In[74]:


train_set_label.head()


# In[76]:


test_set_label=test_set["label"].copy()
test_set.drop('label', inplace=True, axis=1)


# In[80]:


#train_set=my_pipeline.fit_transform(train_set)


# In[82]:


train_set


# In[49]:


#df_label.head()


# In[83]:


from sklearn.svm import SVC as svc
from sklearn.linear_model import LogisticRegression


# In[84]:


model=svc()
mod=LogisticRegression()


# In[85]:


model.fit(train_set,train_set_label)


# In[86]:


mod.fit(train_set,train_set_label)


# In[87]:


#test_set=my_pipeline.fit_transform(test_set)


# In[88]:


print(model.score(test_set,test_set_label))


# In[89]:


mod.score(test_set,test_set_label)


# In[92]:


#test_set[2]


# In[94]:


model.predict(([[0.25421252, 0.27579609, 0.01636317, 3.55194693, 0.95636671,
       0.64209145, 0.14771821]]))


# In[97]:


from joblib import dump,load


# In[98]:


dump(model,"Crop.joblib")

feature=([[0.25421252, 0.27579609, 0.01636317, 3.55194693, 0.95636671,
       0.64209145, 0.14771821]])
result=model.predict(feature)
print("Done")
print(result[0])


# In[ ]:




