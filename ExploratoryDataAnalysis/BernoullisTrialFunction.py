#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 12:38:16 2020

@author: aakarsh.rajagopalan

The Bernoullis trial has 2 parameters:
    1. n --> number of occurrences (events)
    2. p --> probability of success of an event
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def perform_bern_trial(n,p):
    
    #creating a counter variable to store the number of successes
    n_success_counter = 0
    
    #creating a for loop to iterate through events to calculate the numnber of successes
    for i in range(n):
        random_number = np.random.random()
        
        #condition to check if the even succeeded
        if p > random_number:
            n_success_counter += 1
    
    return n_success_counter

if __name__ == "__main__":
    #identifying the number of defaults out of 100 loans
    #probability of a default is 0.05
    
    #initializing an empty array to store the number of defaults
    n_defaults = np.empty(1000)
    
    #enumerator to run the 'perform_bern_Trial function a 1000 times
    for i in range(1000):
        n_defaults[i] = perform_bern_trial(n=100, p = 0.05)
    
    #setting sns as default 
    sns.set()
    
    #plotting a histogram to show the probability 
    _ = plt.hist(n_defaults,  color = 'green', stacked = True)
    _ = plt.xlabel('number of defaults')
    _ = plt.ylabel('probability')
    _ = plt.show()
