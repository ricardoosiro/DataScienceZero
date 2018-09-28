#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print (i + j)
    print (i)
print( "done looping")


# In[ ]:


long_winded_computation = (1 + 2 + 3 + 4 + 5 +6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15)
print(long_winded_computation)
list_of_lists = [[1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9]]


# In[ ]:


import re
my_regex = re.compile("[0-9]+", re.I)
print(my_regex)


# In[ ]:


not_tab_string = r"\t"
print(len(not_tab_string))


# In[ ]:


try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero")


# In[ ]:


my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
print(my_list)
my_list[1] = 3
print(my_list)
print(my_tuple)
try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")
    print(TypeError)


# In[ ]:


def sum_and_product(x, y):
    return (x+y),(x*y)

sp = sum_and_product(2, 3)
print(sp)
s, p = sum_and_product(5, 10)
print(s,p)


# In[19]:


empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim":95}
print(grades)
joels_grade = grades["Joel"]
print(joels_grade)


# In[ ]:





# In[ ]:




