def get_team_game_data():
    '''
    data for teams and games csv was sources from:
    http://www.masseyratings.com/
    
    function loads 2 csv and names cols
    '''
    # load games csv
    games_df = pd.read_csv('ncaa_2016_games.csv', header=None)
    # load teams csv
    teams_df = pd.read_csv('ncaa_2016_teams.csv', header=None)

    # drop unneed cols (dates of games and home field advantage)
    games_df.drop([0, 1, 3, 6], axis=1, inplace=True)
    
    # rename cols
    games_df.columns = ['team_a', 'a_score', 'team_b', 'b_score']
    teams_df.columns = ['team_num', 'team_name']
    
    return games_df, teams_df