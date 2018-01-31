import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from collections import Counter

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch08/08_01/enrollment_forecast.csv'
enroll = pd.read_csv(address)
enroll.columns = ['year','roll','unem', 'hgrad', 'inc']
#roll = enrollment
enroll.head()

sb.pairplot(enroll)
#look to see if assumptinos of linear regression are met
#using unem even if not clearly linear viz relationship
print enroll.corr()
#unem and hsgrad have low corr (0.17), so we can use both as predictors
enroll_data = enroll[['hgrad', 'unem']]
enroll_target = enroll[['roll']]

X, y = scale(enroll_data), enroll_target
#first, we scale them. X=scaled vars of enrl_data (predicted featues)
#calling target y

missing_values = X==np.NAN
X[missing_values == True]
#create object called missing)values which is boolean returns for whether 
#X has a missing value
#then filter dataset w/ that return - only shows missing values
#returns nothing, so no missing values

LinReg = LinearRegression(normalize=True)
#call linear regression function, normalize vars before doing it 
LinReg.fit(X,y)
#fit predictors, predictant
print LinReg.score(X,y)
#print score for model 
#what the heck does that mean??
#multiple r2 of the model. how well regression line matches real values
#we get a value of 0.84, pretty good 
#(Can't see the coefficients here or significance levels!)
#Might be a good idea to use this method for the aribnb data & see how performs

##8.2 - Logistic Regression
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy.stats import spearmanr

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.preprocessing import scale 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.head()

cars_data = cars[['drat', 'carb']]
#these are the focal predictors we want
y = cars[['am']]

#first check model assumptions for them
sb.regplot(x='drat', y='carb', data=cars, scatter=True)
#plot drat against carb to see if they are categorical
#they only take on set positions, b/c they are categorical

#next, look for independence b/w two predictor vars
drat = cars['drat']
carb = cars['carb']

spearmanr_coefficient, p_value =  spearmanr(drat, carb)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)
#spearman r for ordinal variables 
#value of -0.125, so low correlation

cars.isnull().sum()
#use isnull method and sum to return sum of missing values for each column
#in cars dataframe
#no missing values

sb.countplot(x='am', data=cars, palette='hls')
#countplot makes sure that our variable is binary or ordinal
#but like... we should just know that (facepalm)

cars.info()
#we want 50 obvs per predictor - here we have two predictors, so we want 100 obvs
#we only have an n of 31 so this isn't great. don't meet this assumption
#sample size too small

#next, scale data
X = scale(cars_data)
print(X)
print(y)

LogReg = LogisticRegression()
#create logistic regression object

LogReg.fit(X,y)
#fit logreg to our variables
print LogReg.score(X,y)
#print r2 value = 0.81, not bad

#do classification report to evaluate the model on precision & recall
y_pred = LogReg.predict(X)
#generate predicted values from our model
from sklearn.metrics import classification_report
#import classification report from metric module
print(classification_report(y, y_pred))
#show how we did, comparing the predicted y to the real y
#Precision = 0.82, recall = 0.81. adequate model


##8.3 Naive Bayes Classifiers 
import numpy as np
import pandas as pd

import urllib

import sklearn
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
raw_data = urllib.urlopen(url)
#use urlopen function to read from URL
dataset = np.loadtxt(raw_data, delimiter=",")
#loadtxt helps us read this the same as csv files, by specifying delimeter
print dataset[0]

#now, need to isolate predictive vars from dataset. 
#we are just going to use the 48 features on word frequency counts (b/c other features on different scales)
#so no preprocessing is necessary

X = dataset[:,0:48]

y = dataset[:, -1]
#spam/not spam are 0/1 (1 meaning spam)
#this is confusing to me b/c featuers are unlabeled... not sure what this dataset is

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=17)
#bootstrapping (?) the data
# 33% of data test, the rest train
#set seed

#continuous vars describing continuous counts of words, so multinomial good choice
#can also try bernoulli w/ binning to convert frequency counts to binary values
#we do bernoulli first. 

BernNB = BernoulliNB(binarize=True)
#make our data binary
BernNB.fit(X_train, y_train)
#fit training data to this model
print(BernNB)

y_expect = y_test
#rename y test to y expect
y_pred = BernNB.predict(X_test)
#generate predicted labels
# predicting whether spam or no
print accuracy_score(y_expect, y_pred)
#accuracy score is 0.86

#now, we do the same w/ multinomial one
MultiNB = MultinomialNB()

MultiNB.fit(X_train, y_train)
print(MultiNB)

y_pred = MultiNB.predict(X_test)
#predict y from X test data
print accuracy_score(y_expect, y_pred)
#score is 0.87 - better than bernoulli

#features all numeric, so technically can do gaussian too
GausNB = GaussianNB()
GausNB.fit(X_train, y_train)
print(GausNB)

y_pred = GausNB.predict(X_test)
#now predict spam using gaussian method on x_test
print accuracy_score(y_expect, y_pred)
#0.81 is accuracy score. so worst one (but all are pretty good actually)

#Can we improve bernoulli from trial and error?
BernNB = BernoulliNB(binarize=0.1)
#messing around w/ this score to optimize
BernNB.fit(X_train, y_train)
print(BernNB)
​
y_expect = y_test
y_pred = BernNB.predict(X_test)
print accuracy_score(y_expect, y_pred)
#redo - accuracy score now is 0.89 - good improvement that makes bernoulli best

#Lesson: adjust your model parameter settings to get best performance from model!
