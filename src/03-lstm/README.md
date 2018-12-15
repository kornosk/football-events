## Long short-term memory

The /notebooks directory contains the following Jupyter Notebooks:

1.) binary_90_minutes_LSTM.ipynb - Reads in the binary_90_minutes_cleaned_data_for_lstm.csv file and runs it through an LSTM model.  It constructs the LSTM such that if we are given the first half sequence of events for every minute, we can predict the sequence of events for every minute of the second half of a given game. 

2.) binary_90_minutes_LSTM_isGoal.ipynb - Creates an LSTM model that will take in the first 45 minutes (t = 0 to 44) of every game as X, and whether or not a goal is scored during each minute of the second half as Y. Thus, if we are given the first half sequence of events for every minute, we can predict whether a goal is made during each mintue of the second half. However, we do not use the results in our ensemble ANN. 

3.) binary_90_minutes_LSTM_with_team_info.ipynb - Similar to binary_90_minutes_LSTM.ipynb except that we each team has its own event attribute. Whereas the previous model only cared about predicting whether a sequence of events would occur at each minute of a game's second half, we now care about whether the details for a team.  


The other files in the directory are as follows:


1.) binary_90_minutes_LSTM.py - Python script version of /notebooks/binary_90_minutes_LSTM.ipynb.

2.) binary_90_minutes_LSTM_isGoal.py - Python script version of /notebooks/binary_90_minutes_LSTM_isGoal.ipynb.

3.) creating_aggregate_game_with_16_features.py - This Python script goes through the events.csv file and does data cleaning. This script will create new columns that are dedicated to each of these 15 additional events we are interested in. Keeping "is_goal", we have a total of 16 features. Creates output: aggregate_game_with_16_features.csv.

4.) creating_90_minutes_cleaned_data_for_lstm.py - This Python script operates on the file aggregate_game_with_16_features.csv. The code will perform data cleaning in which it will only retain columns pertaining to the 16 events (15 events plus goal) we are interested in. Each row will correspond to a game, time, and the sequence of events. For each game, we will aggregate all events of the same time or minute (ie: aggregate the rows for each gave with the same time). Creates 90_minutes_cleaned_data_for_lstm.csv

5.) binary_creating_90_minutes_cleaned_data_for_lstm.py - This Python script operates on the 90_minutes_cleaned_data_for_lstm.csv. It converts the aggregated values int he event sequence to binary values. 

6.) 90_minutes_cleaned_data_for_lstm.csv - Output from creating_90_minutes_cleaned_data_for_lstm.py.

