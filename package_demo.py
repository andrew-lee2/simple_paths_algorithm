from simple_paths_algorithm import examples
from simple_paths_algorithm.paths_functions import SimplePaths


'''
this is a very simple example of the simple paths package
'''

nodes, edges = examples.example_graph_2()
simple_path = SimplePaths(nodes, edges)
results_df = simple_path.get_simple_paths_result(5)
