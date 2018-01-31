#9. Web-based data viz with plotly
#NOTE: THIS ONE IS BS B/C CAN'T DO IT ALONG W/ HER
! pip install plotly
! pip install cufflinks

import numpy as np
import pandas as pd

import cufflinks as cf

import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

tls.set_credentials_file(username='bigdatagal', api_key='hvginfgvwe')
#student membership: $59/yr/user
#CAN'T DO THIS. B/C UNWILLING TO PURCHASE. 
#CAN'T BELIEVE THIS IS PART OF THE LESSON -_-

#A very basic line chart 
a = np.linspace(start=0, stop=36, num=36)

np.random.seed(25)
b = np.random.uniform(low=0.0, high=1.0, size=36)

trace = go.Scatter(x=a, y=b)

data = [trace]

py.iplot(data, filename='basic-line-chart')

#Line chart with more than one var plotted
x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,0,4,3,2,1]
z = [10,9,8,7,6,5,4,3,2,1]

trace0 = go.Scatter(x=x, y=y, name='List Object', line = dict(width=5))
trace1 = go.Scatter(x=x, y=z, name='List Object 2', line = dict(width=10,))

data = [trace0, trace1]

layout = dict(title='Double Line Chart', xaxis= dict(title='x-axis'), yaxis= dict(title='y-axis'))
print layout

fig = dict(data=data, layout=layout)
print fig

py.iplot(fig, filename='styled-line-chart')

##9.2: Statistical charts
address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg

mpg.iplot(kind='histogram', filename='simple-histogram-chart')

cars_data = cars.ix[:,(1,3,4)].values

cars_data_std = StandardScaler().fit_transform(cars_data)

cars_select = pd.DataFrame(cars_data_std)
cars_select.columns = ['mpg', 'disp', 'hp']

cars_select.iplot(kind='histogram', filename='multiple-histogram-chart')

cars_select.iplot(kind='histogram', subplots=True, filename='subplot-histograms')

cars_select.iplot(kind='histogram', subplots=True, shape=(3,1), filename='subplot-histograms')

cars_select.iplot(kind='histogram', subplots=True, shape=(1, 3), filename='subplot-histograms')

#Box plots
cars_select.iplot(kind='box', filename='box-plots')

#Scatter plots
fig = {'data':[{'x':cars_select.mpg, 'y':cars_select.disp, 'mode':'markers','name':'mpg'},
              {'x':cars_select.hp, 'y':cars_select.disp,'mode':'markers', 'name':'hp'}]
      , 'layout':{'xaxis':{'title':''}, 'yaxis':{'title':'Standardized Displacement'}}}
py.iplot(fig, filename='grouped-scatter-plot')


#9.3. Plot.ly in Jupyter
address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch09/09_03/States.csv'
states = pd.read_csv(address)
states.columns = ['code','region','pop','satv', 'satm', 'percent', 'dollars', 'pay']
states.head()

states['text'] = 'SATv '+states['satv'].astype(str) + 'SATm '+states['satm'].astype(str) +'<br>'+\
'State '+states['code']

data = [dict(type='choropleth', autocolorscale=False, locations = states['code'], z= states['dollars'], locationmode='USA-states', text = states['text'], colorscale = 'custom-colorscale', colorbar= dict(title="thousand dollars"))]
data

layout = dict(title='State Spending on Public Education, in $k/student', 
              geo = dict(scope='usa', projection=dict(type='albers usa'), showlakes = True, lakecolor = 'rgb(66,165,245)',),)
layout

fig = dict(data=data, layout=layout)

py.iplot(fig, filename='d3-choropleth-map')

#9.4 
#Choropleth maps
address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch09/09_03/States.csv'
states = pd.read_csv(address)
states.columns = ['code','region','pop','satv', 'satm', 'percent', 'dollars', 'pay']
states.head()

states['text'] = 'SATv '+states['satv'].astype(str) + 'SATm '+states['satm'].astype(str) +'<br>'+\
'State '+states['code']

data = [dict(type='choropleth', autocolorscale=False, locations = states['code'], z= states['dollars'], locationmode='USA-states', text = states['text'], colorscale = 'custom-colorscale', colorbar= dict(title="thousand dollars"))]
data

layout = dict(title='State Spending on Public Education, in $k/student', 
              geo = dict(scope='usa', projection=dict(type='albers usa'), showlakes = True, lakecolor = 'rgb(66,165,245)',),)
layout

fig = dict(data=data, layout=layout)

py.iplot(fig, filename='d3-choropleth-map')

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch09/09_03/snow_inventory.csv'
snow = pd.read_csv(address)
snow.columns = ['stn_id', 'lat', 'long', 'elev', 'code']

data = [dict(type='scattergeo', locationmode='USA-states', lon= snow_sample['long'], lat = snow_sample['lat'],
             marker = dict(size=12, autocolorscale=False, colorscale='custom-colorscale', color = snow_sample['elev'],
                           colorbar=dict(title = 'Elevation (m)')))]

layout = dict(title='NOAA Weather Snowfall Station Elevations', colorbar= True, 
              geo = dict(scope='usa', projection= dict(type='albers usa'), showland=True, landcolor= "rgb(250,250,250)",
                         subunitcolor = "rgb(217,217,217)", countrycolor = "rgb(217,217,217)", countrywidth = 0.5, subunitwidth = 0.5),)

fig = dict(data=data, layout=layout)

py.iplot(fig, validate=False, filename='d3-elevation')

snow_sample = snow.sample(n=200, random_state=25, axis=0)
snow_sample.head()
