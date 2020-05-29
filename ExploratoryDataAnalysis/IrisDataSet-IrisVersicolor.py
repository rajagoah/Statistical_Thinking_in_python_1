import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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
plt.show()