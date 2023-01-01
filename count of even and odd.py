#!/usr/bin/env python
# coding: utf-8

# In[24]:


#count of even and odd
 

even=0
odd=0
for num in range(1,10):
    if (num % 2==0):
        even=even+1
        print("{0} is even".format(num))
    else:
        print("{0} is odd".format(num))


# In[37]:


odd=0
even=0
for num in range(1,10):
    if (num%2==0):
        even=even+1
    else:
        odd=odd+1
print("even numbers = {} & odd numbers = {}".format(even,odd))        


# In[ ]:




