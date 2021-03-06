##6.1 K-means method
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import sklearn
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale
import sklearn.metrics as sm
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report

#set plotting params

iris = datasets.load_iris()

X = scale(iris.data)
#what does scale mean - standardize?
y = pd.DataFrame(iris.target)
#what is target from iris dataset?
variable_names = iris.feature_names
X[0:10,]
#print first 10 records of X

clustering = KMeans(n_clusters=3, random_state=5)
#create KMeans object with 3 clusters (3 cenrtoids - we know this b/c 
#there are 3 species of iris in dataset, so we'd think each will be a cluster)
#random_state = sets the seed 

clustering.fit(X)
#fit cluster to our X dataset

iris_df = pd.DataFrame(iris.data)
#create data frame
iris_df.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y.columns = ['Targets']

color_theme = np.array(['darkgray', 'lightsalmon', 'powderblue'])
#set color theme 
plt.subplot(1,2,1)
#one row, 2 columns, 1=in first plot among subplots
plt.scatter(x=iris_df.Petal_Length,y=iris_df.Petal_Width, c=color_theme[iris.target], s=50)
#plot length on x, width on y. c=color theme, select target variable (species names), size of markers is 50
plt.title('Ground Truth Classification')

plt.subplot(1,2,2)
#one row, 2 columns, 2 = second of 2 charts
plt.scatter(x=iris_df.Petal_Length,y=iris_df.Petal_Width, c=color_theme[clustering.labels_], s=50)
#identical scatterplot, but color according to PREDICTED species, not actual (clustering.labels_)
plt.title('K-Means Classification')

#the second plot looks slightly different from the first
#1. b/c mislabeled (colors don't correspond to the same thing)
# but, 2. some of the datapoints in the middle where there is lots of overlap
#do indeed seem to be misclassified. hope we talk about this...

relabel = np.choose(clustering.labels_, [2, 0, 1]).astype(np.int64)
#of clustering labels, we want 0 changed to 2, 1 to be changed to 0, and 2 changed to 1
#as integer datatype
plt.subplot(1,2,1)
plt.scatter(x=iris_df.Petal_Length,y=iris_df.Petal_Width, c=color_theme[iris.target], s=50)
plt.title('Ground Truth Classification')

plt.subplot(1,2,2)
plt.scatter(x=iris_df.Petal_Length,y=iris_df.Petal_Width, c=color_theme[relabel], s=50)
plt.title('K-Means Classification')
#color by relabel, not clustering label
#then, regenerate charts

#did pretty good job of clustering, but still need to score the model quantiatively
print(classification_report(y, relabel))
#classification_report function on y, and relabel - our predicted values

#output:
    #precision: measure of model's relevancy
    #recall: measure of completeness. 
    #in ML, want high levels of each

#for records predicted to have a 0 label, 100% of retrieved instances were relevant
#for records predicted to have 1 label, 74% relevant
#for records predicted to have 2 label, 77% relevant 
#overall, 83%

##6.2 Hierarchical methods 
import numpy as np
import pandas as pd

import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

X = cars.ix[:,(1,3,4,6)].values
#mpg, disp, hp, wt, want values
#ix is depracated.

y = cars.ix[:,(9)].values
#y = am (automatic/variable)

Z = linkage(X, 'ward')
#use ward linkage methods
#z is clustering results generated by scipy hierarchical clustering algorithm

#now, make dendogram 
dendrogram(Z, truncate_mode='lastp', p=12, leaf_rotation=45., leaf_font_size=15., show_contracted=True)
#create dendrogram. The rest of the options just make it easier to read/see
plt.title('Truncated Hierarchical Clustering Dendrogram')
plt.xlabel('Cluster Size')
plt.ylabel('Distance')
#graph cluster size v. distance b/w points 

plt.axhline(y=500)
#setting one line at 500 to count clusters: 2 clusters
plt.axhline(y=150)
#setting a second like at 150 to count clusters: 5 clusters
plt.show()

#am assumes 0 or 1 (auto/manual). that's why we might want to pick 2 clustesr
#by declaring this, we are saying that max distance is greater than 400
#(b/c above 400, there are only 2 clusters [below 400, there are 3, and then 
#even more branches into clusters])

k=2
#2 clusters

Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='ward')
#agglomerative clustering function from sklearn. num clusters = k (2)
#affinity = distance matrix as measure of similarity. first aff=euclidian
#but we'll mix and match
#linkage = ward
Hclustering.fit(X)
#now fit the model
sm.accuracy_score(y, Hclustering.labels_)
#now assess the score: how well do our clusters match up to y?
#0.78125 accuracy score. not bad

k=2

Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='complete')
Hclustering.fit(X)

sm.accuracy_score(y, Hclustering.labels_)
#change linkage to complete. score = 0.43

Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage='average')
Hclustering.fit(X)

sm.accuracy_score(y, Hclustering.labels_)
#change linkage to average. score = 0.78125

Hclustering = AgglomerativeClustering(n_clusters=k, affinity='manhattan', linkage='average')
Hclustering.fit(X)

sm.accuracy_score(y, Hclustering.labels_)
#change affinity to manhattan. score - 0.72

##BEST: euclidian/ward or euclidian/average (same score!)

#6.3 K-Nearest neighbor classification method
import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from pylab import rcParams

import urllib
#read data in using URL lib

import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

X_prime = cars.ix[:,(1,3,4,6)].values
y = cars.ix[:,9].values
#above = her code. ix is deprecated, so I did it this way below:

X_prime = cars[['mpg', 'disp', 'hp', 'wt']]
y = cars['am']

X = preprocessing.scale(X_prime)
#scale our vars w/ preprocessing scale function
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=17)
#now split into test and training sets. set aside 1/3 for test size
#random seed for replicability

clf = neighbors.KNeighborsClassifier()
#clf is K nearest neighbor object. why do they call it this?
clf.fit(X_train, y_train)
#fit method from x and y training
print(clf)
#print it 

y_expect = y_test
#rename y test to y expect - expected values
y_pred = clf.predict(X_test)
#gen y predict = contains labels that our model predicts for y var
print(metrics.classification_report(y_expect, y_pred))
#report how it did : precision, recall are key measures hrere

#recall: model completeness.
    #of all points lebeled 1, only 67% of results were relevant
    #of all, 87% relevant
    #high precision but low recall: few results returned, but many of the label 
    #predictions that were returned are correct
#high accuracy, low prediction