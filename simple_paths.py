import pandas as pd

def get_team_game_data(nodes, edges):
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
    edges_df = pd.read_csv(edges, header=None)
    # load teams csv
    nodes_df = pd.read_csv(nodes, header=None)

    # drop unneed cols (dates of games and home field advantage)
#     games_df.drop([0, 1, 3, 6], axis=1, inplace=True)
    
    # rename cols
    edges_df.columns = ['node_a', 'a_value', 'node_b', 'b_value']
    nodes_df.columns = ['node', 'node_text']
    
    return edges_df, nodes_df