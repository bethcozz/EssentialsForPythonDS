####CHAPTER 1####
import numpy as np
import pandas as pd

from pandas import Series
from pandas import DataFrame

series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'])

series_obj

# ['label-index']
# ( WHAT THIS DOES ) 
# When you write square brackets with a label-index inside them, this tells Python to select and 
# retrieve all records with that label-index.
series_obj['row 7']

# [integer index] 
# ( WHAT THIS DOES )
# When you write square brackets with an integer index inside them, this tells Python to select and 
# retrieve all records with the specified integer index.
series_obj[[0,7]]

np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)), 
                   index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6'],
                   columns=['column 1', 'column 2', 'column 3', 'column 4', 'column 5', 'column 6'])
DF_obj
#use random number gen to get 36 random values.
#reshape method: puts numbers in matrix w/ 6 rows and 6 columns
#index argument creates an index for the dataset
#index alone does rows, columns= does columns

# object_name.ix[[row indexes], [column indexes]]
# ( WHAT THIS DOES )
# When you call the .ix[] special indexer, and pass in a set of row and colum indexes, this tells 
# Python to select and retrieve only those specific rows and columns.
DF_obj.ix[['row 2', 'row 5'], ['column 5', 'column 2']]

#data slicing- returns a slice of several values from a dataset

# ['starting label-index':'ending label-index'] 
# ( WHAT THIS DOES )
# Data slicing allows you to select and retrieve all records from the starting label-index, to the 
# ending label-index, and every record in between.
series_obj['row 3':'row 7'] #colon says run all of them, and everything in between


# object_name < scalar value
# ( WHAT THIS DOES )
# You can use comparison operators (like greater than or less than) to return True / False values for 
# all records, to indicate how each element compares to a scalar value. 
DF_obj < .2

#scalar = just a number

# object_name[object_name > scalar value] 
# ( WHAT THIS DOES )
# You can also use comparison operators and scalar values for indexing, to return only the records 
# that satisfy the comparison expression you write.
series_obj[series_obj > 6]

#return all rows with values greater than 6

# ['label-index', 'label-index', 'label-index'] = scalar value
# ( WHAT THIS DOES )
# Setting is where you select all records associated with the specified label-indexes and set those 
# values equal to a scalar.
series_obj['row 1', 'row 5', 'row 8'] = 8


#specifying label indexes for rows we want to retrieve 

#MISSING - LESSON 2
 #np.nan #how python denotes missing vals 

series_obj = Series(['row 1', 'row 2', np.nan, 'row 4','row 5', 'row 6', np.nan, 'row 8'])
series_obj

# object_name.isnull()
# ( WHAT THIS DOES )
# The .isnull() method returns a Boolean value that describes (True or False) whether an element in a 
# Pandas object is a null value.
series_obj.isnull()

#isnull = returns true/false values to show which vals are missing from a dataset

np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj

## .ix indicator is dprecated, should not use it

# object_name.fillna(numeric value)
# ( WHAT THIS DOES )
# The .fillna method() finds each missing value from within a Pandas object and fills it with the 
# numeric value that you've passed in.
filled_DF = DF_obj.fillna(0)
filled_DF

# object_name.fillna(dict)
# ( WHAT THIS DOES )
# You can pass a dictionary into the .fillna() method. The method will then fill in missing values 
# from each column Series (as designated by the dictionary key) with its own unique value 
# (as specified in the corresponding dictionary value).
filled_DF = DF_obj.fillna({0: 0.1, 5: 1.25})
filled_DF

#for vals in col 0, fill in with 0.1. for vals in col 5, fill in in 1.25

#how useful? requries importing 3 vars, but 1 has lots of missing vals. still want to import data from that var, set missing vals equal to approx to make your predictive application work

#fill forward - missing vals filled w/ the last nominal value from within that column

np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj.ix[3:5, 0] = np.nan
DF_obj.ix[1:4, 5] = np.nan
DF_obj

#counting how many values are missing = isnull

# object_name.isnull().sum()
# ( WHAT THIS DOES )
# To generate a count of how many missing values a DataFrame has per column, just call the .isnull() 
# method off of the object, and then call the .sum() method off of the matrix of Boolean values it 
# returns.
DF_obj.isnull().sum()

#call isnull method on our object, sum method on the isnull

# object_name.dropna()
# ( WHAT THIS DOES )
# To identify and drop all rows from a DataFrame that contain ANY missing values, simply call the 
# .dropna() method off of the DataFrame object. NOTE: If you wanted to drop columns that contain 
# any missing values, you'd just pass in the axis=1 argument to select and search the DataFrame 
# by columns, instead of by row.
DF_no_NaN = DF_obj.dropna(axis=1)
DF_no_NaN

#dropNA method = drops any row with missing values

# object_name.dropna()
# ( WHAT THIS DOES )
# To identify and drop all rows from a DataFrame that contain ANY missing values, simply call the 
# .dropna() method off of the DataFrame object. NOTE: If you wanted to drop columns that contain 
# any missing values, you'd just pass in the axis=1 argument to select and search the DataFrame 
# by columns, instead of by row.
DF_no_NaN = DF_obj.dropna()
DF_no_NaN
#in this version, drops ANY row with a missing value. but if you put axis=1
#drops COLUMNS with missing data, not ROWS ***

# object_name.dropna(how='all')
# ( WHAT THIS DOES )
# To identify and drop only the rows from a DataFrame that contain ALL missing values, simply 
# call the .dropna() method off of the DataFrame object, and pass in the how='all' argument.
DF_obj.dropna(how='all')
#only drops rows that contain ALL missing values
#since none of our rows have ALL missing values, this won't drop anything 

DF_obj = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                  'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                  'column 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']})
DF_obj

# object_name.duplicated()
# ( WHAT THIS DOES )
# The .duplicated() method searches each row in the DataFrame, and returns a True or False value to 
#indicate whether it is a duplicate of another row found earlier in the DataFrame.

DF_obj.duplicated()

# object_name.drop_duplicates()
# ( WHAT THIS DOES )
# To drop all duplicate rows, just call the drop_duplicates() method off of the DataFrame.
DF_obj.drop_duplicates()

DF_obj = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                  'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                  'column 3': ['A', 'A', 'B', 'B', 'C', 'D', 'C']})
DF_obj

# object_name.drop_duplicates(['column_name'])
# ( WHAT THIS DOES )
# To drop the rows that have duplicates in only one column Series, just call the drop_duplicates() 
# method off of the DataFrame, and pass in the label-index of the column you want the de-duplication 
# to be based on. This method will drops all rows that have duplicates in the column you specify.
DF_obj.drop_duplicates(['column 3'])

#CONCATENATE & TRANSFORM

DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
DF_obj

DF_obj_2 = pd.DataFrame(np.arange(15).reshape(5,3))
DF_obj_2

# pd.concat([left_object, right_object], axis=1)
# ( WHAT THIS DOES )
# The concat() method joins data from seperate sources into one combined data table. If you want to 
# join objects based on their row index values, just call the pd.concat() method on the objects you 
# want joined, and then pass in the axis=1 argument. The axis=1 argument tells Python to concatenate 
# the DataFrames by adding columns (in other words, joining on the row index values).
pd.concat([DF_obj, DF_obj_2], axis =1)

#concat merges data table. can do it by row index (axis=1) or column index (don't pass an axis argument)

pd.concat([DF_obj, DF_obj_2])

# object_name.drop([row indexes])
# ( WHAT THIS DOES )
# You can easily drop rows from a DataFrame by calling the .drop() method and passing in the index 
# values for the rows you want dropped.
DF_obj.drop([0,2])
#rows 0 and 2 have been dropped

DF_obj.drop([0,2], axis=1)

series_obj = Series(np.arange(6))
series_obj.name = "added_variable"
series_obj

#JOIN data frames
# DataFrame.join(left_object, right_object)
# ( WHAT THIS DOES )
# You can use .join() method two join two data sources into one. The .join() method works by joining 
# the two sources on their row index values.
variable_added = DataFrame.join(DF_obj, series_obj)
variable_added
#this just adds another variable/column to it

#append = add rows to the bottom of a table
added_datatable = variable_added.append(variable_added, ignore_index=False)
added_datatable
#created a second copy of the original table
# ignore index - don't want pandas to reindex the data table
# better to reindex it tho

added_datatable = variable_added.append(variable_added, ignore_index=True)
added_datatable
#this gives new index = new number for each row 
# i.e., goes on to 6, 7, 8, etc. instead of repeating 1,2,3,4,5, after getting to 5

# object_name.sort_values(by=[index value], ascending=[False])
# ( WHAT THIS DOES )
# To sort rows in a DataFrame, either in ascending or descending order, call the .sort_values() 
# method off of the DataFrame, and pass in the by argument to specify the column index upon which 
# the DataFrame should be sorted.
DF_sorted = DF_obj.sort_values(by=[5], ascending=[False])
DF_sorted

# we are sorting in ascending order by column 5 (in descending order)

#GROUPING AND AGGREGATION
# if fruit==orange 

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
#convert external cars dataset into  data frame object

cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.head()
#cars.head() gives snapshot of first few entries on cars

# object_name.groupby('Series_name')
# ( WHAT THIS DOES )
# To group a  DataFrame by its values in a particular column, call the .groupby() method off of the DataFrame, and then pass
# in the column Series you want the DataFrame to be grouped by.
cars_groups = cars.groupby(cars['cyl'])
cars_groups.mean()

#groupby. create var called cars_groups, cyl variable is how we want to group data
#then take mean for each cyl subgroup


