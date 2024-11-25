#!/usr/bin/env python
# coding: utf-8

# In[ ]:


question_list=["what is the boiling point of water","What is blockchain technology?"]
option_list=[["75"," 90","100","101","c"],
             [" A decentralized database"," A centralized ledger system"," A cloud storage service"," A type of machine learning model","d"] 
            ]
level=[1000,2000,3000,4000,5000,6000,70000]
amount=0
i=0
while(i<len(question_list)):
    
    print(question_list[i])
   # print(option_list[i])
    options=option_list[i]
    print(f"a   {options[0]}        b {options[1]}")
    print(f"c   {options[2] }       d {options[3]}")
    correct_ans=input("enter the correct answer")
    if correct_ans==options[-1]:
        print(f"you are win {level[i]}")
        if level==4:
            amount=10000
    else:
        print(" wrong answer")
    i=i+1

    




# In[ ]:





# In[ ]:




