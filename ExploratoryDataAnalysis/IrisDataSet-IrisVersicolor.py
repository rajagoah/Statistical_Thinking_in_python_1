import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#importing the data from the folder
iris_df = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Iris length dataset/IRIS.csv')

#printing head
print(iris_df.head(5))
print(iris_df['species'].unique())

#creating a dataframe to store the iris versicolor subset.
iris_df_versi = iris_df[iris_df['species'] == 'Iris-versicolor']
print(iris_df_versi.head(5))

#storing petal length of iris versicolor in a different variable
iris_versi_petal_length = list(iris_df_versi['petal_length'])
print(iris_versi_petal_length)

#setting the seaborn setting as default
sns.set()

#ploting the histogram on petal lengths of iris versicolor
plt.hist(iris_versi_petal_length)

#adding labels to the axis
plt.xlabel('petal lenght (cm)')
plt.ylabel('count')
plt.show()

#adjusting the bin size
#ideally the bin size should be the square root of the number of observations
n_bin = np.sqrt(len(iris_versi_petal_length))
n_bin = int(n_bin)  #converting to integer data type
print('size of bin ---> ',n_bin)

#adding the keyword argument bins
plt.hist(iris_versi_petal_length, bins = n_bin)


#***********************************BEE SWARM PLOT **************************************
#to avoid bining bias, we will use the bee swarm plot, available in the sea born library
sns.swarmplot(x='species', y='petal_length', data = iris_df)
plt.xlabel('species')
plt.ylabel('petal length (cm)')
plt.show()

#***********************************Emperical Cumulative distribution function **********
#to avoid obfuscation of data, when the data points are in large numbers, we can use
#ECDF plots to visualiae the data and understand the distribution
n = len(iris_versi_petal_length)
arr = np.arange(stop = n+1, start = 1)/n
print('the array is' , arr)

x_vers = np.sort(np.array(iris_versi_petal_length))
y_vers = arr

#calculating the ECDF curve
_=plt.plot(x_vers, y_vers, marker = '.', linestyle = 'none')

