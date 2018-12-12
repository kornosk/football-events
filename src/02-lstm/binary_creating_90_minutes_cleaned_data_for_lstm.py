"""
This Python script operates on the 90_minutes_cleaned_data_for_lstm.csv. 
The 90_minutes_cleaned_data_for_lstm.csv file contains a breakdown of each of the 90 minutes (t = 0 to t = 89) for a given game.
Each minute of a given game is modeled as a sequence of 16 events. The sequence is an aggregate of the occurrences of a given event for that minute of the game.
For example, if 2 fouls occur during a given minute of a game, then the row will have the value 2 under 'Foul'.

This Python script simply converts the aggregated values in the event sequence to binary values. So, if there were 2 fouls at time t for a game,
this file replaces it with a 1, indicating that at least one foul occurred in that minute. 

The changes are made and written to the file binary_90_minutes_cleaned_data_for_lstm.csv. The new file will later be used in an LSTM.
"""

import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Input, Dense
from keras.models import Model
import os
import sys
import numpy as np
from google.colab import drive
drive.mount('/content/drive')


filename = "drive/Team Drives/Deep Learning Project/armaan/90_minutes_cleaned_data_for_lstm.csv"
df = pd.read_csv(filename)

#Select only the columns of interest, which pertain to the game, time, and all the events.
df = df[['id_odsp', 'time', 'Attempted_Shot', 'Corner_Kick', 'Foul', 'First_Yellow_Card', 'Second_Yellow_Card', 'Straight_Red_Card', 'Substitution', 'Free_Kick_Awarded', 'Off_Sides', 'Hand_Ball', 'Penalty_Awarded', 'Key_Pass', 'Failed_Through_Ball', 'Sending_Off', 'Own_Goal', 'is_goal']]
df = df.dropna()

cols = df.columns.tolist()
cols = cols[2:]	   #Gather all of the columns that pertain to the events.
print(cols)	

#Iterate through each of the event columns and replace any value > 1, with a 1.
for col in cols:
  df.loc[df[col] > 1, col] = 1

#Write the binary output to the binary_90_minutes_cleaned_data_for_lstm.csv file.
df.to_csv("drive/Team Drives/Deep Learning Project/armaan/binary_90_minutes_cleaned_data_for_lstm.csv", index = False)

