#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing the iris data set
iris_df = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Iris length dataset/IRIS.csv')

#filtering a list with only the Iris Versicolors length
iris_ver_len = list(iris_df[iris_df['species']=='Iris-versicolor']['petal_length'])

print(iris_ver_len)

#calculating the mean petal length
print('Mean petal length of I. Versicolor is ',np.mean(iris_ver_len),'cm')

#************************************ ECDF **********************************************
#calculating the length of the iris_ver_len
leng = len(iris_ver_len)

#creating the x  and y variable
x_vers = np.sort(np.array(iris_ver_len))
y_vers = np.arange(start = 1, stop = leng+1)/leng

#plotting the ECDF
_ = plt.plot(x_vers, y_vers, marker = '.', linestyle = 'None')

#labeling the plot
plt.xlabel('petal length cm')
plt.ylabel('ECDF')

#providing margins
plt.margins(0.2)
#************************************ PERCENTILES ***************************************
#creating a numpy array with percentile values
percentiles = np.array([2.5,25,50,75,97.5])

#calculating the percentiles
per_vers = np.percentile(iris_ver_len, percentiles)

#printing the percentiles
print(per_vers)

#overlaying the percentile information on the same ECDF plot
_ = plt.plot(per_vers, percentiles/100, color = 'red', marker = 'D', linestyle='none')
