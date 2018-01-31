##Chapter 5: Outlier Analysis##
#5.1 extreme value analysis using univariate methods

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams

df = pd.read_csv(
    filepath_or_buffer='~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch05/05_01/iris.data.csv',
    header=None,
    sep=',')
#column delimited values
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']

X = df.ix[:,0:4].values
#select first 4 cols of iris data
y = df.ix[:,4].values
#select target: species names - only last col in data set
df[:5]

df.boxplot(return_type='dict')
#call boxplot method on datafram
#type is dictionary: makes pythong happy?
plt.plot()
#outliers in sepal width - above 4 or less than 2.5

Sepal_Width = X[:,1]
#isolate sepal width var, select second col from df
iris_outliers = (Sepal_Width > 4)
#find outliers w/ more than 4, returns T/F values
df[iris_outliers]
#this shows us the outliers

Sepal_Width = X[:,1]
iris_outliers = (Sepal_Width < 2.05)
#we also want the outiers w/ low values
df[iris_outliers]

pd.options.display.float_format = '{:.1f}'.format
#another way to find outliers besides boxplts
#set display so that only get 1 decimal point
X_df = pd.DataFrame(X)
#create data frame for our X var
print X_df.describe()
#describe it

#IQR: distance b/w 1st and 3rd quartile. 
# 3.3-2.8 for index 1 (our var w/ outliers)
# diff = 0.5
#1.5*!QR = 0.75

#for 1st quart: 2.8 - 0.75 = 2.05
#our min val is less than that, suspicious as outlier
#for 3rd quart: 3.3 +0.75 = 4.05
#max val is higher than that, so suspicous as outlier 

##5.2: Multivariate analysis for outlier detection
#bring in pandas, matplotlib, rcparams, seaborn
#set parameters

df = pd.read_csv(
    filepath_or_buffer='~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch05/05_01/iris.data.csv',
    header=None,
    sep=',')

df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']
data = df.ix[:,0:4].values
target = df.ix[:,4].values
df[:5]

sb.boxplot(x='Species', y='Sepal Length', data=df, palette='hls')
#ix is deprecated - use .loc or .iloc instead

#graph species against sepal length - plotting two vars in one box plot
sb.pairplot(df, hue='Species', palette='hls')
#now, color data points based on species label

#we know sepl width is suspicious - can see one red dot outlier in this
#scatterplot matrix.

#5.3. DBSCAN: a linear projection method for multivariate data
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter

df = pd.read_csv(
    filepath_or_buffer='~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch05/05_01/iris.data.csv',
    header=None,
    sep=',')

df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']
data = df.ix[:,0:4].values
target = df.ix[:,4].values
df[:5]

model = DBSCAN(eps=0.8, min_samples=19).fit(data)
print model
#number of samples = number of observations? or what??
#fit model to our dataset

outliers_df = pd.DataFrame(data)
#creating new dataframe

print Counter(model.labels_)
#counter shows how many data points are assigned each label
#labels are 1, 0 and -1
#94 have value 1, 50 have value 0, 6 have value -1
# -1 are outliers, which is about 4% of the sample

print outliers_df[model.labels_ ==-1]
#print outlier records with model labels== -1

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1]) 

colors = model.labels_
#colors to be assigned to model labels (outlier or not)

ax.scatter(data[:,2], data[:,1], c=colors, s=120)
#want third column, y value index position one
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Width')
plt.title('DBScan for Outlier Detection')

#DBSCAN finds that there are 2 core samples: the red and pink samples
#on this viz. those in black (the 6 outlier data points) are non-core samples, 
#in sparse areas. 
