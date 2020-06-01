#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:02:48 2020

@author: aakarsh.rajagopalan
"""
# importing packages
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

#reading from the url
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
wine_df = pd.read_csv(url, sep = ';')

#printing head
print(wine_df.head(5))

#extracting column names
print(wine_df[:0])

#identifying the size of the dataset (number of rows)
print('the number of rows is, ', wine_df.shape)

# we'll perform the exploratory data analysis using the ECDF 

#****************** FIXED ACIDITY #******************
x_FA =  np.sort(np.array(wine_df['fixed acidity']))

#calculating the number of elements in the array
leng = len(x_FA)

#calculating the Y axis
y_FA = np.arange(start = 1, stop = leng + 1)/leng

#producing the ECDF
_ = plt.plot(x_FA, y_FA, marker = '.', linestyle = 'none')
_ = plt.margins(0.2)

#labeling the axis
plt.xlabel('Fixed acidity')
plt.ylabel('ECDF')

#****************** VOLATILE ACIDITY #******************
x_VA = np.sort(np.array(wine_df['volatile acidity']))

#calculating the length
leng = len(x_VA)

#calculating y_VA
y_VA = np.arange(start = 1, stop = leng + 1)/leng

#producing ECDF
_ = plt.plot(x_VA, y_VA, marker = '.',linestyle = 'none' )
_ = plt.margins(0.2)

#labeling
_ = plt.xlabel('Volatile acidity')
_ = plt.ylabel('ECDF')

#****************** CITRIC ACID #******************
x_CA = np.sort(np.array(wine_df['citric acid']))

#calculating the length
leng = len(x_CA)

#calculating y_VA
y_CA = np.arange(start = 1, stop = leng + 1)/leng

#producing ECDF
_ = plt.plot(x_CA, y_CA, marker = '.',linestyle = 'none' )
_ = plt.margins(0.2)

#labeling
_ = plt.xlabel('Citric acid')
_ = plt.ylabel('ECDF')

#****************** RESIDUAL SUGAR #******************
x_RS = np.sort(np.array(wine_df['residual sugar']))

#calculating the length
leng = len(x_RS)

#calculating y_VA
y_RS = np.arange(start = 1, stop = leng + 1)/leng

#producing ECDF
_ = plt.plot(x_RS, y_RS, marker = '.',linestyle = 'none' )
_ = plt.margins(0.2)

#labeling
_ = plt.xlabel('Residual Sugar')
_ = plt.ylabel('ECDF')

#****************** CHLORIDES #******************
x_CL = np.sort(np.array(wine_df['chlorides']))

#calculating the length
leng = len(x_CL)

#calculating y_VA
y_CL = np.arange(start = 1, stop = leng + 1)/leng

#producing ECDF
_ = plt.plot(x_CL, y_CL, marker = '.',linestyle = 'none' )
_ = plt.margins(0.2)

#labeling
_ = plt.xlabel('Chlorides')
_ = plt.ylabel('ECDF')

