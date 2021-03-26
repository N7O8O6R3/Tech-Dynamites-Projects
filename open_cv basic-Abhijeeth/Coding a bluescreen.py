#!/usr/bin/env python
# coding: utf-8

# # color Theshold and blue screen

# In[28]:


import matplotlib.pyplot as plt
import numpy as np

import cv2


# In[29]:


#Readeing the image

img1=cv2.imread("blue.jpg")
img2=cv2.imread("space.jpg")


# In[30]:


plt.imshow(img1)
#As you see that the color is not exact becouse cv2
#module imports image not as RGB.


# In[31]:


print("The image is of type",type(img1),"withshape>",img1.shape)
#Convert to RGB


# In[32]:


img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)


# In[33]:


plt.imshow(img1)


# In[34]:


img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)


# In[70]:


# Definning bounds for Blue Color           
lower_blue=np.array([0,0,200])
upper_blue=np.array([255,255,255])
mask=cv2.inRange(img1,lower_blue,upper_blue)
plt.imshow(mask,cmap='gray')


# In[ ]:





# In[71]:


plt.imshow(mask,cmap='gray')


# In[72]:


masked=np.copy(img1)


# In[73]:


masked[mask!= 0]=[0,0,0]
plt.imshow(masked)


# In[74]:


img2[mask==0]=[0,0,0]


# In[75]:


plt.imshow(img2)


# In[76]:


result=img2+masked


# In[77]:


plt.imshow(result)


# # ===============COMPLETED=============

# 

# In[ ]:




