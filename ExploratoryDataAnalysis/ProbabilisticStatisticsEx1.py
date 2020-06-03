#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:12:05 2020

@author: aakarsh.rajagopalan
"""
import numpy as np
import matplotlib.pyplot as plt

#providing the seed number of the random number generating function
_ = np.random.seed(42)

#initializing an empty array with 100,000 entries
random_nums_array = np.empty(100000)

#creating a for loop to start storing random numbers per iteration in the above array
for i in range(100000):
    random_nums_array[i] = np.random.random()

#ploting to a histogram
_ = plt.hist(random_nums_array, color = 'green')

#labeling
_ = plt.xlabel('random nums')
_ = plt.ylabel('number of occurrences')

#applying margin
_ = plt.margins(.2)

_ = plt.show()