##4.2 Explanatory Factor Analysis##
import pandas as pd
import numpy as np

import sklearn
from sklearn.decomposition import FactorAnalysis

from sklearn import datasets
#built in datasets are toy datasets you can use for practice
# Iris dataset: 4 numeric vars describing 3 species of flowers

iris =  datasets.load_iris()
#load built-in Iris dataset
#call datasets.load_name of data set to load it
X = iris.data
#this is 4 numeric vars that make up the dataset
variable_names = iris.feature_names
#column headers
X[0:10,]
#print first 10 records in all columns

factor = FactorAnalysis().fit(X)
#fit factor analysis
pd.DataFrame(factor.components_, columns=variable_names)
#find  the factor components with max variance
#this gives us a better understaninding of our output
#pd.DataFrame is data frame constructor

##4.3 PCA##
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import pylab as plt
import seaborn as sb
from IPython.display import Image
from IPython.core.display import HTML 
from pylab import rcParams

import sklearn
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets

#set data viz parameters
# do PCA on iris dtaset

iris = datasets.load_iris()
X = iris.data
variable_names = iris.feature_names
X[0:10,]
#same as above

pca = decomposition.PCA()
#instantiate a PCA object called fit method to find principal components 
iris_pca = pca.fit_transform(X)
#call transform method to pca

pca.explained_variance_ratio_
#see how much variance is explained by the componentes we found
#first component explains 92.4% of variation alone
#first 2 components means we only lose 2.3% of dataset variance

#let's take only the first 2 components

pca.explained_variance_ratio_.sum()
#calculate cumulative variance
#we got a value of 1. this means 100% of dataset's variance is explained by
#the components we returned 
#BUT we don't want 100% of info back - some is noise, redundancy, outliers

comps = pd.DataFrame(pca.components_, columns=variable_names)
comps
#call data frame consturctor, pass in pca.components_
#pass in variable names
#make it comps

sb.heatmap(comps)
# first 2 components (numbers 0 and 1 in heatmap) contain 97% of variance
#first principal componenent is strongly positively correlated w/ petal length
# & moderately positively correlated w/ sepal length & petal width 

#can use these as IV's for ML algorithms. 