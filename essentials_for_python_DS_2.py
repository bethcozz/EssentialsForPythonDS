####CHAPTER 2####
#python -m pip install --upgrade pip 
# pip install Seaborn

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

#%matplotlib inline #this means prit inside jupityr notebook
rcParams['figure.figsize'] = 5, 4 #changes style. set figure size to 5x4i
sb.set_style('whitegrid') #white grid is background style

#before plot, need to create array objects for python to chart
x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

plt.plot(x, y)

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = cars['mpg']

mpg.plot()
#plots just the mpg var

df = cars[['cyl', 'wt', 'mpg']]
df.plot()
#make subset of cars dataset just including cyc wt and mpg

plt.bar(x, y)
#uses same data as line grap above

mpg.plot(kind='bar')
#make bar chart using pandas data

mpg.plot(kind='barh')
#make horizontal bar chart using pandas data
#double or single quotes both work

x = [1,2,3,4,0.5]
plt.pie(x)
plt.show()
#plt.show prints it

plt.savefig('pie_chart.jpeg')
plt.show()
#save data viz as jpeg file

#%pwd
#where is my working directory?

# '/Users/elizabethcozzolino/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch02/02_01'

###2.2 Object oriented graphing###

#defining axes, ticks, and grids:
x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

fig = plt.figure()
#create blank figure object

ax = fig.add_axes([.1, .1, 1, 1])
#add axis to this figure - this shows where
#left side: .1
#bottom: .1
#width: 1
#height: 1

ax.plot(x,y)
#ax = figure object
#plot x and y on the ax.plot

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1]) 

ax.set_xlim([1,9])
#set limits to x axis
ax.set_ylim([0,5])
#set limits to y axis
#calling set_ylim method onto our 'ax' object

ax.set_xticks([0,1,2,4,5,6,8,9,10])
#set ticks on x axis to be 0-10
ax.set_yticks([0,1,2,3,4,5])
#set y ticks to be 0-5

ax.plot(x,y)
#call method plot and do it on the ax object


fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1]) 

ax.set_xlim([1,9])
ax.set_ylim([0,5])

ax.grid()
#call grid method off ax object
ax.plot(x, y)
#plot with gridlines behind it

fig = plt.figure()
#first generate blank figure object
fig, (ax1, ax2) = plt.subplots(1,2)
#calling subplots method
#two axes, ax1 and ax 2
#call subplots funtion, call 1 row, 2 columns 

ax1.plot(x)
#plot just x
ax2.plot(x,y)
#plot both x and y

##FORMATTING YOUR PLOT. 2.3##
import seaborn as sb

rcParams['figure.figsize'] = 5, 4 #this is the size of the plot
sb.set_style('whitegrid') #this is the style: white grid


x = range(1, 10)
y = [1,2,3,4,0.5,4,3,2,1]
#same as above, using these numbers as examples

plt.bar(x, y)
#call bar graph function : plt.bar

wide = [0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.5, 0.5, 0.5]
#widths of the bars in our bar chart
color = ['salmon']
#color of our bars
plt.bar(x, y, width=wide, color=color, align='center')
#on our bar plot:
    #graph x and y
    #use widths defined in 'wide'
    #use color defined in 'color'
    #alignment: center aligned

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

df = cars[['cyl', 'mpg','wt']]
#create subset of the cars data set containing only cycl mpg and wt
df.plot()    
#plot df

color_theme = ['darkgray', 'lightsalmon', 'powderblue']
#setting a color theme for this 
#plotting 3 vars, need to pass in a color for each one
df.plot(color=color_theme)
#apply parameters from color theme to df plot

z = [1,2,3,4,0.5]
#create new list object called z
#elements to plot on pie chart
plt.pie(z)
#function pie, passing in z object
plt.show()
#show the pie chart

#now customize colors
color_theme = ['#A9A9A9', '#FFA07A', '#B0E0E6', '#FFE4C4', '#BDB76B']
#grab hexcodes for the colors that you want
#need 5 colors for 5 elements of pie chart
plt.pie(z, colors = color_theme)
#add in colors=color_theme to apply your colors 
#this is colors not color (plotted above)
plt.show()

#customizing line styles
x1 = range(0,10)
y1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#creating these elements to plt against each other

plt.plot(x, y)
#plot x, y from above example
plt.plot(x1,y1)
#plot second line, just created now

plt.plot(x, y, ls = 'steps', lw=5)
#new arguments
    #ls = line style = steps
    #lw = line width = 5
plt.plot(x1,y1, ls='--', lw=10)
    #ls = '--'
    #lw = 10

#change marker styles
plt.plot(x, y, marker = '1', mew=20)
    #marker = 1 (comes from table of styles)
    #mew = marker width
plt.plot(x1,y1, marker = '+', mew=15)
    #marker style = +
    #marker width = 15

##2.4 LABELS & ANNOTATIONS##
    #a. functional method
x = range(1,10)
y = [1,2,3,4,0.5,4,3,2,1]
#same numbers as previous examples
plt.bar(x,y)
#plot on bar graph

plt.xlabel('your x-axis label')
#function: plt.xlabel 'string of what you want to label x'
plt.ylabel('your y-axis label')
#plt.ylable 'string of what you want to label y'

z = [1 , 2, 3, 4, 0.5]
veh_type = ['bicycle', 'motorbike','car', 'van', 'stroller']
#need a label for each element in the pie chart
#write as a list
plt.pie(z, labels= veh_type)
#plot z, with labels as we defined in object 'veh_type'
plt.show()
#show me this graph

#now, object-oriented method
address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
#same as in previous examples

mpg = cars.mpg
#isolating the element mpg from the cars list
fig = plt.figure()
#create a figure
ax = fig.add_axes([.1, .1, 1, 1])
#add axes, pass in the location of where we want the axes
mpg.plot()

ax.set_xticks(range(32))
#set tick marks ranging from 1-31

ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
#.set_xticklabels = pass in the strings you want to use to label the items
# in cars dataset, use car_names variable for the chart
# rotation=60, meaning 60 degrees
# make font size medium

ax.set_title('Miles per Gallon of Cars in mtcars')
#add a title to the chart: miles per gallon of cars
#pass the string with the title you want to use for the chart
ax.set_xlabel('car names')
#label x axis - car names
ax.set_ylabel('miles/gal')
#label y axis -miles/gal

#Adding a legend to your plot: functional method
plt.pie(z)
#pass in z object to plt.pie function
plt.legend(veh_type, loc='best')
#pass legend function
#location = best, upper right, upper left, lower right, etc. 
#all options in documentation
plt.show()

#object-oriented method
fig = plt.figure()
#add fig object
ax = fig.add_axes([.1,.1,1,1])
#add axes, specify position
mpg.plot()
#plot our mpg variable

ax.set_xticks(range(32))
#same labels from plot earlier

ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title('Miles per Gallon of Cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

ax.legend(loc='best')
#add legend method off of ax object
#best = put in best looking place

#  How to Annotate Plot
mpg.max()
#if we want to plot max, need to find out what the max value is
#call max method off mpg variable = 33.8

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
mpg.plot()
ax.set_title('Miles per Gallon of Cars in mtcars')
ax.set_ylabel('miles/gal')

ax.set_ylim([0,45])
#increase max val of y axis to 45 to give us room for our annotation

ax.annotate('Toyota Corolla', xy=(19,33.9), xytext = (21,35),
           arrowprops=dict(facecolor='black', shrink=0.05))
#.annotate is method being called off ax object
# first pass in string for label in our annotation: Toyota Corrolla
# pass in xy to show location where you're annotating
#record 19 of max value, and 33.9
#xytest we want at 21 over, 35 up
#arrorprops = specifies what kind of arrow we want to point to our object
#make it black, shrink it by half 

##2.5 Data viz for time series##
address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch02/02_05/Superstore-Sales.csv'
df = pd.read_csv(address, index_col='Order Date', parse_dates=True)
df.head()

#set index column equal to order date column - order by order date 
#parse dates- tells python that order date is a date
#df.head() - print first few rows

df['Order Quantity'].plot()
#plot order quantity over time
#this graph looks bad. too many records
#let's take 100 random records and plot that instead

df2 = df.sample(n=100, random_state=25, axis=0)
#call sample method on our object df, get 100 samples
#set seed, random_State=25
#tell python we want to take rows - axis=0
#call this df2

plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Superstore Sales')
#label axes and give title to the graph

df2['Order Quantity'].plot()
#plot the graph
#much clearer to see the time series

#Statistical graphs

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from pandas.tools.plotting import scatter_matrix

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.index = cars.car_names
mpg = cars['mpg']
#isolate mpg variable - select mpg label index

mpg.plot(kind='hist')
# call plot method, pas argument kind=hist

plt.hist(mpg)
plt.plot()
#another way to create a hist

#seaborn is great for statistical plotting
sb.distplot(mpg)
#also gives automatic trend line

#plot scatterplot
cars.plot(kind='scatter', x='hp', y='mpg', c=['darkgray'], s=150)
# x var =hp, y var = mpg. color = dark gray, marker size to be 150

#use seaborn to plot:
sb.regplot(x='hp', y='mpg', data=cars, scatter=True)
#regular plot. data=cars, use cars dataset to plot. scatter it
#again, automatic trendline

sb.pairplot(cars)
#sb is easiest way to do scatterplt matrix

cars_df = pd.DataFrame((cars.ix[:,(1,3,4,6)].values), columns = ['mpg', 'disp', 'hp', 'wt'])
#access values in columns 1, 3, 4, and 6. columns = names of vars
cars_target = cars.ix[:,9].values
#isolate target var: am (automatic/manual)
target_names = [0, 1]
#values are either 0 or 1

cars_df['group'] = pd.Series(cars_target, dtype="category")
#making it color vars
#new variable is group
#group is series object. we build from cars_target 
#dyype= category - means this is a categorical variable
sb.pairplot(cars_df, hue='group', palette='hls')
#pass in hue=group - pick color based on group
#palette - hls, pre-built color palette
#this plot tells us that cars that weigh more have automatic transmission
#cars w/ automatic transmission get less mpg
#manual get more mpg

#BOXPLOTS
cars.boxplot(column='mpg', by='am')
#plot mpg by transmission type
cars.boxplot(column='wt', by='am')
#plot wt by type of transmission

#in seaborn:
sb.boxplot(x='am', y='mpg', data=cars, palette='hls')
#set your x and y (transmission type and mpg)
#pull data from cars data set
#use hls prebuilt palette
