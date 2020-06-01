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

#************************************ PERCENTILES ***************************************
#creating a numpy array with percentile values
percentiles = np.array([2.5,25,50,75,97.5])

#calculating the percentiles
per_vers = np.percentile(iris_ver_len, percentiles)

#printing the percentiles
print(per_vers)