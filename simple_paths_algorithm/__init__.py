import pandas as pd
import networkx as nx
import numpy as np

def get_node_edge_data(nodes_csv, edges_csv):
    '''
    data for teams and games csv was sources from:
    http://www.masseyratings.com/

    function loads 2 csvs (no headers in either):

    format of nodes:
    |Node|Node text name|

    format of edges:
    |Node A|value of A|Node B|value of B|
    '''
    # load games csv
    edges_df = pd.read_csv(edges_csv, header=None)
    # load teams csv
    nodes_df = pd.read_csv(nodes_csv, header=None)

    # rename cols
    edges_df.columns = ['node_a', 'a_value', 'node_b', 'b_value']
    nodes_df.columns = ['node', 'node_text']

    return nodes_df, edges_df

def get_node_edge_lists(node_df, edge_df):
    '''
    placeholder
    '''

    node_list = [int(node) for node in node_df.node.tolist()]

    # construct tuple list
    edge_tuple_list = []
    for _, edge in edge_df.iterrows():
        # explain how we handle ties? though i think its impossible to tie in college football?
        if edge.a_value == edge.b_value:
            continue
        elif edge.a_value > edge.b_value:
            edge_tuple_list.append((edge.node_a, edge.node_b))
        else:
            edge_tuple_list.append((edge.node_b, edge.node_a))

    return node_list, edge_tuple_list

# make function that creates the graph from the csv
def get_graph(nodes_csv, edges_csv):
    '''
    placeholder
    '''

    # load in csvs
    node_df, edge_df = get_node_edge_data(nodes_csv, edges_csv)
    # get node and edge lists
    node_list, edge_list = get_node_edge_lists(node_df, edge_df)

    # create graph and add attributes
    di_graph = nx.DiGraph()
    di_graph.add_nodes_from(node_list)
    di_graph.add_edges_from(edge_list)

    return di_graph, node_df

def get_node_simple_paths(graph, nodes, starting_node, depth):
    '''
    placeholder
    '''

    node_paths_list = []

    for node in nodes:
        # we dont want the simple paths from origin node to itself so continue
        if node == starting_node:
            continue
        else:
            paths_temp = nx.all_simple_paths(graph, starting_node, node, cutoff=depth)
            node_paths_list += list(paths_temp)

    return node_paths_list

# change this function to return dictionary
def get_node_weights(graph, list_of_nodes):
    '''
    placeholder
    '''

    node_all_dict = graph.degree(list_of_nodes)

    weight_dict = {}

    for i in node_all_dict:
        node_weight = 1 / float(node_all_dict[i])
        weight_dict[i] = node_weight

    return weight_dict

def get_node_score(node_paths_list, weight_dict):
    '''
    placeholder
    '''

    node_value = 0
    for path in node_paths_list:
        temp_path_value_list = []
        for i in range(len(path) - 1):
            temp_path_value_list.append(weight_dict[path[i]])

        node_value += np.prod(temp_path_value_list)

    return node_value

# make function to return dataframe
def get_graph_score(graph, depth):
    '''
    placeholder
    '''

    node_list = graph.nodes()
    # get weight for each node
    node_weights = get_node_weights(graph, node_list)

    node_info_list = []

    for node in node_list:
        # get paths for node
        node_paths_list = get_node_simple_paths(graph, node_list, node, depth)
        #get score for node
        node_score = get_node_score(node_paths_list, node_weights)

        node_info_list.append([node, node_score])

    node_score_df = pd.DataFrame(node_info_list, columns=['node', 'node_score'])

    return node_score_df

def get_simple_paths_result(nodes_csv, edges_csv, depth):
    '''
    placeholder
    '''

    graph, nodes_df = get_graph(nodes_csv, edges_csv)
    scores_df = get_graph_score(graph, depth)
    results_df = pd.merge(nodes_df, scores_df, on='node', how='left')
    # save results to csv
    results_df.to_csv('simple_paths_algo_results.csv', index=False)

    return results_df
    