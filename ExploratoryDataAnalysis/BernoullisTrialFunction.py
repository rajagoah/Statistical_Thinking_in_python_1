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
    n_success = perform_bern_trial(10, 0.5)
    print(n_success)
    
