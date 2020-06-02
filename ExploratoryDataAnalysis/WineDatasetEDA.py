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
plt.show()

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
plt.show()

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
plt.show()

#plotting RESIDUAL SUGAR, CHLORIDES based on quality in box plot mode
#****************** RESIDUAL SUGAR #******************
sb.boxplot(x = 'quality', y = 'residual sugar', data = wine_df)

#labeling
_ = plt.xlabel('Quality')
_ = plt.ylabel('Residual Sugar')
plt.show()

#****************** CHLORIDES #******************
sb.boxplot(x = 'quality', y = 'chlorides', data = wine_df)

#labeling
_ = plt.xlabel('quality')
_ = plt.ylabel('chlorides')
plt.show()

#plotting SULPHATES based on quality in box plot mode
#****************** SULPHATES #******************
sb.swarmplot(x = 'quality', y = 'sulphates', data = wine_df)

#labeling
_ = plt.xlabel('quality')
_ = plt.ylabel('Sulphates')

plt.show()

