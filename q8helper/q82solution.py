import cProfile
from graph_goody import random_graph, spanning_tree
import pstats

# Put script below to generate data for Problem #2
# In case you fail, the data appears in sample8.pdf in the helper folder

n = 15000
graph = random_graph(n, lambda x: x*10)

cProfile.run('spanning_tree(graph)', 'profileName')

r =pstats.Stats('profileName')
r.strip_dirs().sort_stats('ncalls').print_stats(10)
r.strip_dirs().sort_stats('tottime').print_stats(10)
