#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
print("randomly choice any number b|w 1--5 digit")
print("if your choice number is equal to computer choice number then you win nor you are loss")
i=0
while i<3:
    computer_choice=random.randint(1,3)
    user_choice=int(input("enter the your guest number"))
    if computer_choice==user_choice:
        print("congratulation you are win")
        break
        
    else:
        print("sorry you are loss")
    print("user choice number is: ",user_choice)
    print("computer choice number is:",computer_choice)
    print("TRY AGAIN")
i=i+1
print("user choice number is: ",user_choice)
print("computer choice number is:",computer_choice)




# In[ ]:





# In[ ]:




