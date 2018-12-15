This folder pertains to the first experiment in which we generate team-based and game-based features 
for creating the ANN model. 

1.) aggregating_game_features.ipynb - creates the aggregate game-based features from the "events.csv" file.

2.) team_based.py - creates the team-based features from the "events.csv" file.

3.) ANN_single.pynb - The model combines the 10 team-based and the 38 game-based features, for a total of 48 features. We will use this combined information for predicting the outcomes of more than 9000 games. More precisely, we will see whether the home team wins, the away team wins, or the game ends in a tie.
