import pandas as pd
import pkg_resources

def load_csv(csv_name):
    '''
    placeholder
    '''
    csv_path = pkg_resources.resource_filename(__name__, 'data/' + csv_name)
    csv_df = pd.read_csv(csv_path, header=None)

    return csv_df

def example_graph_2():
    '''
    placeholder
    '''
    return load_csv('ex_2_nodes.csv'), load_csv('ex_2_edges.csv')

def ncaa_2016_data():
    '''
    placeholder
    '''
    return load_csv('ncaa_2016_teams.csv'), load_csv('ncaa_2016_games.csv')
