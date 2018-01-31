import numpy as np
from numpy.random import randn
#import random number generator

np.set_printoptions(precision=2)
#show only 2 digits after decimal point

#create arrays using a list
a = np.array([1,2,3,4,5,6])
a
#creat array a

b = np.array([[10,20,30], [40,50,60]])
b
#create array b, which looks like:
 #   [10, 20, 30]
 #   [40, 50, 60]

#Create arrays via assignment
np.random.seed(25)
c = 36*np.random.randn(6)
c
#gives 6 random numbers
#randn = generates positive and negative random numbers

d = np.arange(1,35)
d
#puts in values b/w 1 and 34

#matrix = 2 dimensional array
#Arithmatic on arrays and matrices:

a * 10
c + a
c - a
c * a
c / a

aa = np.array([[2.,4.,6.], [1.,3.,5.], [10.,20.,30.]])
aa

bb = np.array([[0.,1.,2.], [3.,4.,5.], [6.,7.,8.]])
bb

aa*bb

np.dot(aa,bb)
#this is formal matrix multiplication 
#with numpy, np.dot is the function you call on arrays
#takes dot product of arrays, reduces to single matrix object

##3.2 Descriptives#3
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats
#scipy is new library, stats is new module

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

cars.head()
cars.sum()
#summarized columns
cars.sum(axis=1)
#summarized rows (horizontal count)

cars.median()
#finds median of full data frame (shows median for each column)
cars.mean()

cars.max()
#find max value for each var

mpg = cars.mpg
mpg.idxmax()
#what's index value of row w/ maximum value?
#it's the 19th row

cars.std()
#describes standard deviation for each column in dataframe (variable)

cars.var()
#returns variance for each var/column

gear = cars.gear
gear.value_counts()
#shows how many unique values are present in a dataset
#gear variable has 3 unique values: 3, 4, and 5. Output:
        #3    15
        #4    12
        #5     5
#Name: gear, dtype: int64
#15 cars have 3 gears, 12 cars have 4 gears, 5 cars have 5 gears

cars.describe()
#returns full statistical description of each variable 

#3.3 - summarize categorical variables#
#uses just numpy and pandas, and cars dataset

# object_name.value_counts()
# ( WHAT THIS DOES )
# The .value_counts() method makes a count of all unique values in an array or Series object. 
carb = cars.carb
carb.value_counts()

# object_name.groupby('column_index')
# ( WHAT THIS DOES )
# To group a DataFrame by its values in a particular column, call the .groupby() 
# method off of the DataFrame, and then pass
# in the index value of the column Series you want the DataFrame to be grouped by.
cars_cat = cars[['cyl','vs','am','gear','carb']]
#creating subgroup for just categorical vars, called cars_cat
cars_cat.head()

gears_group = cars_cat.groupby('gear')
#call groupby method on cars.cat, pass in name of gear var
gears_group.describe()
#then describe this new dataframe

# pd.Series(x_variable, dtype)
# ( WHAT THIS DOES )
# To create a Series of categorical data type, call the pd.Series() function on the array or Series that holds the data you
# want the new Series object to contain. When you pass in the dtype="category" argument, this tells Python to assign the new
# Series a data type of "category". Here we create a new categorical Series from the gear variable, and then assign it to a
# new column in the cars DataFrame, called 'group'.
cars['group'] = pd.Series(cars.gear, dtype="category")
#assign new variable a datatype of category
#creating a new variable from gear, then add back to cars dataset
#call series constructor, calling from gears var in cars data frame, but want it to be 

cars['group'].dtypes
#.dtypes says what type of data it is
cars['group'].value_counts()

# pd.crosstab(y_variable, x_variable)
# ( WHAT THIS DOES )
# To create a cross-tab, just call the pd.crosstab() function on the variables you want included in 
# the output table.
pd.crosstab(cars['am'], cars['gear'])
#gives us a cross b/w am and gears

##3.4 Parametric Models##
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats.stats import pearsonr
#this is new - pearsonr

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

sb.pairplot(cars)
#create scatterplot using seaborn

X = cars[['mpg', 'hp', 'qsec','wt']]
sb.pairplot(X)
#create scatterplot of selected vars, X, using seaborn
#consider model assumptions. normal dist, linear rel, continuous, numeric
# these vars aren't exactly normally distributed, but could be close enough
# most of these have closely linear relationship
# continuous, numeric. categorical vars look v. different in scatterplots
# e.g., binary or categorical vars can't use Pearson 
# can see some outliers in these histograms

mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']

pearsonr_coefficient, p_value = pearsonr(mpg, hp)
#calculate R for mpg and hp, and show p-value
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)
#print label, with 3 decimal places: -0.77
pearsonr_coefficient, p_value = pearsonr(mpg, qsec)
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)
#0.419
pearsonr_coefficient, p_value = pearsonr(mpg, wt)
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)
# -.87

#mpg wt has strongest linear corr, mpgqsec has moderate
#this can establish whether or not var pairs meet assumptions of more advanced models

#Shortcuts: panda and sb
corr = X.corr()
corr
#.corr method shows correlations of X
sb.heatmap(corr,xticklabels=corr.columns.values, yticklabels=corr.columns.values)
#generate a heatmap to show which ones are more/less correlated w/ each other
#heatmap function, pass in corr object
# add x and y ticklabels to show what these numbers mean
#darker shades of red show strong degree of positive corr, while dark
#blue has strong degree of negative linear corr

#NONPARAMETRIC CORRELATION#
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats import spearmanr
from scipy.stats import chi2_contingency


address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.head()

sb.pairplot(cars)

X = cars[['cyl', 'vs', 'am', 'gear']]
sb.pairplot(X)
#take subplot of cars dataset
#these variables are ordinal and assume only set # of possible vals
# nonlinearly relation: yes
# non-normal dist: oh yes

cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']
#isolate these vars so we can perform the Spearman Rank Corr on them
spearmanr_coefficient, p_value = spearmanr(cyl, vs)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)
#-0.814
spearmanr_coefficient, p_value = spearmanr(cyl, am)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)
#-0.522
spearmanr_coefficient, p_value = spearmanr(cyl, gear)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)
#-0.56

#Chi2 test
table = pd.crosstab(cyl, am)
#call crosstab function on our 2 vars of inteerest

#import contingency function
chi2, p, dof, expected = chi2_contingency(table.values)
#we want chi2, p val, dof, and expected
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)
#Chi-square Statistic 8.741 p_value 0.013

table = pd.crosstab(cars['cyl'], cars['vs'])
chi2, p, dof, expected = chi2_contingency(table.values)
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)
#Chi-square Statistic 21.340 p_value 0.000

table = pd.crosstab(cars['cyl'], cars['gear'])
chi2, p, dof, expected = chi2_contingency(table.values)
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)
#Chi-square Statistic 18.036 p_value 0.001

#Conclusion: these are correlated!

#3.6 Scaling data
address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg
plt.plot(mpg)
#range 10-33, avg around 20
cars[['mpg']].describe()
mpg_matrix = mpg.values.reshape(-1,1)
#scale b/w 0 and 1
scaled = preprocessing.MinMaxScaler()
#scaled output = prepossessing 
scaled_mpg = scaled.fit_transform(mpg_matrix)
#transform to matrix
plt.plot(scaled_mpg)

mpg_matrix = mpg.reshape(-1,1)
scaled = preprocessing.MinMaxScaler(feature_range=(0,10))
#this is how you customize the range for this feature (mpg)
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)

standardized_mpg = scale(mpg, axis=0, with_mean=False, with_std=False)
#this gives original variable back, b/c with_mean and with_std are both false
plt.plot(standardized_mpg)

standardized_mpg = scale(mpg)
plt.plot(standardized_mpg)
#var now has standard normal distribution

