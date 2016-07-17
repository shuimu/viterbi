
# coding: utf-8

# In[65]:

import re
import scipy
import numpy
import pandas
import matplotlib as plt

## input 
states = ('Healthy', 'Fever')
observations = ('normal', 'cold', 'dizzy')
start_probability = {'Healthy': 0.6, 'Fever': 0.4}
transition_probability = {
   'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
   'Fever' : {'Healthy': 0.4, 'Fever': 0.6}
   }
emission_probability = {
   'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
}


# In[66]:

M = [ {} for y in range(4)]
M[0]['Healthy'] = start_probability['Healthy']
M[0]['Fever'] =  start_probability['Fever']
# print M
for i in range(3):
    for j in start_probability.keys():
        M[i+1][j] = 0
        if i == 0:
            M[i+1][j] = M[i][j]*emission_probability[j][observations[i]]
            continue
        for k in start_probability.keys():
            M[i+1][j] = max(M[i+1][j], 
                            M[i][k]*
                            transition_probability[k][j]*
                            emission_probability[j][observations[i]])
print M


# In[ ]:



