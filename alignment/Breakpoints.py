#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function below returns the number of breakpoints in this permutation.
def Breakpoints(string):
    string=string.split(' ')
    string_lst=[]
    string_lst.append(0)
    for i in string:
        if i[0]=='-':
            i=-1*int(i[1:])
            string_lst.append(i)
        else:
            i = int(i[1:])
            string_lst.append(i)
    string_lst.append(len(string_lst))
    num_of_breakpoints = 0
    for i in range(0, len(string_lst) - 1):
        if string_lst[i+1] - string_lst[i] != 1:
            num_of_breakpoints += 1
    return num_of_breakpoints

