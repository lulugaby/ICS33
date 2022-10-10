from performance import Performance
from goody import irange
from graph_goody import random_graph,spanning_tree

# Put script below to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder
n = 0
def r_graph(x):
    global n 
    n = random_graph(x, lambda x:x*10)

x = 1000 
while x <= 128000:
    p = Performance(lambda: spanning_tree(n), lambda: r_graph(x), 5, f'\n\n Spanning_tree Nodes: {x}')
    p.evaluate()
    p.analyze()
    x *=2