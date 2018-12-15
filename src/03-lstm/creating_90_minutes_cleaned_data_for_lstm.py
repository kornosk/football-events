# -*- coding: utf-8 -*-
"""
This Python script operates on the file aggregate_game_with_16_features.csv. The code
will perform data cleaning in which it will only retain columns pertaining to the
16 events (15 events plus goal) we are interested in. Each row will correspond to 
a game, time, and the sequence of events. For each game, we will aggregate all 
events of the same time or minute (ie: aggregate the rows for each gave with the same time). 

The original file does not contain entries for a given minute of a game if no event happened.
To account for this discrepancy between games, we adjust each game so that it contains rows between time 0 and 89. 
If a game never contained an entry for a certain minute, we simply add a row with that minute and make all its events 0. 
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

#Read in the file.
filename = "drive/Team Drives/Deep Learning Project/armaan/aggregate_game_with_16_features.csv"
df = pd.read_csv(filename)

df = df[['id_odsp', 'time', 'Attempted_Shot', 'Corner_Kick', 'Foul', 'First_Yellow_Card', 'Second_Yellow_Card', 'Straight_Red_Card', 'Substitution', 'Free_Kick_Awarded', 'Off_Sides', 'Hand_Ball', 'Penalty_Awarded', 'Key_Pass', 'Failed_Through_Ball', 'Sending_Off', 'Own_Goal', 'is_goal']]
df = df.dropna()

#For each game, aggregate all events for the same time or minute (ie: aggregate the rows for each gave with the same time)
df = df.groupby(['id_odsp','time']).sum()
df = df.reset_index()

#Make sure that each game has an event sequence for time 0 to 90.
iterables = [df['id_odsp'].unique(), list(range(0, 90))]
df = df.set_index(['id_odsp','time'])
df = df.reindex(index=pd.MultiIndex.from_product(iterables, names=['id_odsp', 'time']), fill_value= 0).reset_index()
df.drop(df[df.time > 89].index, inplace=True)  #Remove rows from a game that are over 90 minutes. We are not accounting for overtime.

df.to_csv("drive/Team Drives/Deep Learning Project/armaan/90_minutes_cleaned_data_for_lstm.csv", index = False)
os.system('say "Hey, Armaan, your program has finished."')

