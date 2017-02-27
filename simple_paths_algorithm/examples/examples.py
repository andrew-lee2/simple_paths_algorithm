import pandas as pd

def load_csv(file_path):
    '''
    placeholder
    '''
    return pd.read_csv(file_path, header=None)

# need to return 2 dataframes here
def example_2():
    '''
    placeholder
    '''
    return load_csv('ex_2_nodes.csv'), load_csv('ex_2_edges.csv')
