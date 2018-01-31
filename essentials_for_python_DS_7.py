#7.2 Network Analysis with NetworkX - Working w/ graph objects

! pip install networkx
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import networkx as nx

G = nx.Graph()
nx.draw(G)
#empty graph
#deprecation warnings!

G.add_node(1)
nx.draw(G)
#add 1 node

G.add_nodes_from([2,3,4,5,6,8,9,12,15,16])
nx.draw(G)
#gives circle of empty nodes

G.add_edges_from([(2,4),(2,6),(2,8),(2,12),(2,16),(3,6),(3,9), (3,12),(3,15),(4,8),(4,12),(4,16),(6,12),(8,16)])
nx.draw(G)
#add edges connecting points 2 and 4, 2 and 6, 2 and 8, 2 and 16, etc.

nx.draw_circular(G)
#draw a circular graph on G

nx.draw_spring(G)
#graph layout transformed to a string layout

nx.draw_circular(G, node_color='bisque', with_labels=True)
#with labels = True, change color to 'bisque'
#nodes 1 and 5 are not connected to anything

G.remove_node(1)
nx.draw_circular(G, node_color='bisque', with_labels=True)
#took out node 1

sum_stats = nx.info(G)
#this gives a summary of our graph - nodes, edges, degree (connectedness) nx.info
print sum_stats

print nx.degree(G)
#shows how many edges each node is connected to

#graph generator is easier to use
G = nx.complete_graph(25)
#with 25 nodes
nx.draw(G, node_color='bisque', with_labels=True)
#with bisque color and labels for each node

G = nx.gnc_graph(7, seed=25)
#7 nodes, with seed set at 25
nx.draw(G, node_color='bisque', with_labels=True)

ego_G = nx.ego_graph(G, 3, radius=5)
#ego networks - we are passing in object G,
#with 3 nodes that graph should center around, radius of 5
nx.draw(G, node_color='bisque', with_labels=True)
#similar structure to social network 
#contains direction:
#if Twitter, person at node 5 follows node 4 and node 0
#person at node 0 has a lot of followers

##7.3 simulate a social network
import numpy as np
import pandas as pd

import networkx as nx

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

DG = nx.gn_graph(7, seed=25)
#directional graph with 7 nodes, seed 

for line in nx.generate_edgelist(DG, data=False): print(line)
#loop: for each line in nx.gen_edgelist(DG graph, data=False): print each line
#returned string object w/ lines generated for the graphs:
#lines generated from: 1 to 0, 2 to 0, 3 t0 2, 4 to 3, 5 to 0, 6 to 4

print DG.node[0]
#when you print 0 now, it's an empty attribute dictionary: {}
#but, now we label the nodes:
DG.node[0]['name'] = 'Alice'
print DG.node[0]
#now it says {'name' : 'Alice'}

DG.node[1]['name'] = 'Bob'
DG.node[2]['name'] = 'Claire'
DG.node[3]['name'] = 'Dennis'
DG.node[4]['name'] = 'Esther'
DG.node[5]['name'] = 'Frank'
DG.node[6]['name'] = 'George'
#now we attach names to all values in DG object

DG.add_nodes_from([(0,{'age':25}),(1,{'age':31}),(2,{'age':18}),(3,{'age':47}),(4,{'age':22}),
                   (5,{'age':23}),(6,{'age':50})])
print DG.node[0]
#next, can add values to each node - age!
#pass in a list of dictionaries, with age as key
#node 0 is 25, node 1 is 31, node 2 is age 18, etc. 

DG.node[0]['gender'] = 'f'
DG.node[1]['gender'] = 'm'
DG.node[2]['gender'] = 'f'
DG.node[3]['gender'] = 'm'
DG.node[4]['gender'] = 'f'
DG.node[5]['gender'] = 'm'
DG.node[6]['gender'] = 'm'
#here, we can attach attribute of gender to these nodes

nx.draw_circular(DG, node_color='bisque', with_labels=True)
#deprecation warning: axes.hold is deprecated

#node 1, 2, and 5 all flow to node 0. they follow Alice, but she doesn't follow them back

labeldict = {0: 'Alice',1:'Bob',2:'Claire',3:'Dennis',4:'Esther',5:'Frank',6:'George'}
#create label dictionary with names and node numbers
nx.draw_circular(DG, labels=labeldict, node_color='bisque', with_labels=True)
##**this could be a good and relatively easy project to replicate w/ real data
#labels = labeldict. Alice is most popular

#if we want to lose the directionality, we call to_undirected on DG object
G = DG.to_undirected()

nx.draw_spectral(G, labels=labeldict, node_color='bisque', with_labels=True)
#draw spectral (not circular)
#now that direction is gone, it could be that alice follows frank, claire, and bob
#and they don't follow her back - making her least important in network
#dimensionality is very important for social network graphs!

##7.4 Social Network Analysis Metrics
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import networkx as nx

DG = nx.gn_graph(7, seed = 25)

for line in nx.generate_edgelist(DG, data=False):
    print(line)

DG.node[0]['name'] = 'Alice'
DG.node[1]['name'] = 'Bob'
DG.node[2]['name'] = 'Claire'
DG.node[3]['name'] = 'Dennis'
DG.node[4]['name'] = 'Esther'
DG.node[5]['name'] = 'Frank'
DG.node[6]['name'] = 'George'
#copy paste from last session 

G = DG.to_undirected()
# now we have 2 versions, one directed and one undirected 

print nx.info(DG)
#avg degree of incoming connection is .85
#avg degree of outgoing connection is .85
#but thinking of alice, she has 3 incoming and 0 outgoing
# --> therefore might be most influential node

DG.degree()
#this gives dictionary w/ # of connections for each node 

#how to identify successor nodes:
nx.draw_circular(DG, node_color='bisque', with_labels=True)
#first, draw circular node 
#node 3 has 2 neighbors, nodes 2 and 4
#if you remove node 3, node 4 is only connected to node 6, not rest of network
#but, 2 would still be connected to node 0 (most influential)
#looks like node 2 would be node 3's successor

DG.successors(3)
#python predicts 2, as we thought
DG.neighbors(4)
#returns a list of all outbound corrections in directed graph, only node 3
G.neighbors(4)
#on undirected graph, returns all connections that a node has (3 and 6)

