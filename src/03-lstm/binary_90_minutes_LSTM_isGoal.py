"""
This Python script will read in the binary_90_minutes_cleaned_data_for_lstm.csv file and run it through an LSTM model. 
The binary_90_minutes_cleaned_data_for_lstm.csv file contains a breakdown for each of the 90 minutes (t = 0 to t = 89) of a given game.
Each minute of a given game is modeled as a binary sequence of 16 types of events. If a given event takes place at the given minute of a game, then
a 1 is put in place; a 0 otherwise. 

Here, we will create an LSTM model that will take in the first 45 minutes (t = 0 to 44) of every game as X, and 
whether or not a goal is scored during each minute of the second half as Y. The file will construct the LSTM such that if we are 
given the first half sequence of events for every minute, we can predict whether a goal is made during each mintue of the second half. 
We, in effect, are creating a many-to-one LSTM model. The file is, therefore, appropriately named "binary_90_minutes_LSTM_isGoal.py".
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import Libraries and packages from Keras
from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint, TensorBoard
from keras.layers import Dense, Activation, Flatten
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

from google.colab import drive
drive.mount('/content/drive')

# Importing the dataset.
filename = "drive/Team Drives/Deep Learning Project/armaan/binary_90_minutes_cleaned_data_for_lstm.csv"
dataset = pd.read_csv(filename)

cols = dataset.columns

for col in cols:
    if col == 'id_odsp':
        dataset.id_odsp = dataset.id_odsp.astype(str)
    else:
        dataset[col] = dataset[col].astype(int)


dataset = dataset.as_matrix() # Using multiple predictors.

X = []
Y = []
    
current_game = "" 

new_row_X = []  #To store the sequence of events for the first half, between t = 0 to 44, for a given game only.
new_row_Y = []  #To store the sequence of goals for the second half, between t = 45 to 89, for a given game only.


#Iterate through the dataset and partition the sequence of
# events for a minute as X (first half) or Y (second half).
for index, row in enumerate(dataset):
    if current_game == row[0]:
        if row[1] <= 44:
            row = np.delete(row, 0)     #drop the game id from the row
            row = np.delete(row, 0)     #drop the time from the row
            new_row_X.append(row)       #Add the sequence of events to the game's first half.
        else:
            new_row_Y.append(row[17])   #Store only whether a goal takes place or not.
    else:
        if index != 0:
            #If operating on a new game, write out the previous game's data to X and Y.
            X.append(new_row_X)         
            Y.append(new_row_Y)
        new_row_X = []
        new_row_Y = []
        current_game = row[0]
        if row[1] <= 45:
            row = np.delete(row, 0)
            row = np.delete(row, 0)
            new_row_X.append(row)
        else:
            new_row_Y.append(row[17]) #Store only whether a goal takes place or not.

#Write out the data for the last game.
if len(new_row_X) > 0 and len(new_row_Y) > 0:
    X.append(new_row_X)
    Y.append(new_row_Y)



X = np.array(X)
Y = np.array(Y)

# Initializing the LSTM model.
lstm_model = Sequential()

#Adding the first LSTM layer and some Dropout regularization.
lstm_model.add(LSTM(units=50, return_sequences=True, input_shape=(45, 16)))
lstm_model.add(Dropout(0.2))

#Adding a second LSTM layer and some Dropout regularization.
lstm_model.add(LSTM(units=50, return_sequences=True))
lstm_model.add(Dropout(0.2))

#Adding a third LSTM layer and some Dropout regularization.
lstm_model.add(LSTM(units=50, return_sequences=True))
lstm_model.add(Dropout(0.2))

#Adding a fourth LSTM layer and some Dropout regularization.
lstm_model.add(LSTM(units=50, return_sequences = True))
lstm_model.add(Dropout(0.2))

#Adding the output layer.
lstm_model.add(Dense(units = 1, activation = 'sigmoid'))

#Use the trained model to predict the second half sequence of goal results.
second_half_prediction = lstm_model.predict(X)

#Print out the results.
print(second_half_prediction)

np.save('binary_lstm_predicted_second_half_isGoal', second_half_prediction)


