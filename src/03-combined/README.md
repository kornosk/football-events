## Combined models

This folder contains our ensemble ANN models. The files are as follows:

1.) aggregating_game_features.ipynb: Input event.csv, generate game_based features for the ANN models

2.) team_based.py: Input event.csv, generate team_based features for the ANN models

3.) ANN_Combined_45mins.ipynb: Input aggregated_game_based_36_features.csv, Established ANN models combining all the features from the original ANN, CNN and RNN using the events happpened in the first half of the team to predict the final outcomes

4.) ANN_Combined_60mins.ipynb: Input aggregated_game_based_36_features_60min.csv, Established ANN models combining all the features from the original ANN, CNN and RNN using the events happpened in the first 60 mins to predict the final outcomes

5.) ANN_Combined_70mins.ipynb: Input aggregated_game_based_36_features_70min.csv, Established ANN models combining all the features from the original ANN, CNN and RNN using the events happpened in the first 70 mins to predict the final outcomes

6.) ANN_Combined_80mins.ipynb: Input aggregated_game_based_36_features_80min.csv, Established ANN models combining all the features from the original ANN, CNN and RNN using the events happpened in the first 80 mins to predict the final outcomes

7.) ANN_single.ipynb: Input aggregated_game_based_36_features.csv, Established ANN models using the game-based and team based features of the events happened in the first half of the game to predict the final outcomes.
