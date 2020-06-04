#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 15:09:58 2020

@author: aakarsh.rajagopalan
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#creating the ecdf function
def ecdf(data):
    
    #declaring the x axis variable
    x = np.sort(data)
    
    #cal the length of array
    n = len(data)
    
    #declaring the y axis variable
    y = np.arange(start = 1, stop = n+1) / n
    
    return x,y

if __name__ == "__main__":
    
    #populating an array 'n_defaults' with the values returned by the np.random.binomial()
    #function
    """ the difference between the exercises 'BernoullisTrial.py' and this one is that,
        in this code, the n_defaults array is getting is value populated through a built in function
        in the .random() module.
        In the BernoullisTrial.py code, the n_default had to be:
            1. first initialised to a set size
            2. then a loop had to be used to generate random numbers, the result of which
            would be stored in the bove array.
        
    """
    
    n_defaults = np.random.binomial(n = 100, p = 0.05, size = 10000)
    
    #sending n_defaults to the ecdf function to get the x and y axis
    x, y = ecdf(n_defaults)
    
    #plotting ecdf graph
    _ = plt.plot(x, y, marker = '.', linestyle = 'none')
    _ = plt.xlabel('number of defaults')
    _ = plt.ylabel('ECDF')
    _ - plt.margins(0.2)
    _ = plt.show()
    
