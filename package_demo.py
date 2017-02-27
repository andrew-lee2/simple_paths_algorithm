from simple_paths_algorithm import paths_functions, examples

'''
this is a very simple example of the simple paths package
'''


# load in demo data
nodes, edges = examples.example_graph_2()
# compute scores
results_df = paths_functions.get_simple_paths_result(nodes, edges, 5)

print results_df