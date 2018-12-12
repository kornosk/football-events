"""
This Python script goes through the events.csv file and does the first stages of data cleaning.
The events.csv file was the dataset provided by Kaggle. Each row pertains to a game and minute.
The file contains a column called "event_type", which contains a number that maps to a certain
type of event (15 total). 

This script will create new columns that are dedicated to each of these 15 additional events we are interested in.
Please note that the 15 events are not all the events we are interested in. We are also interested in 'is_goal',
which has already been explicitly provided for us so we don't need to do any extraction.
"""

import numpy as pd
import pandas as pd

import tensorflow as tf
from keras import Sequential
from keras.layers import Input, Dense
from keras.models import Model

from google.colab import drive
drive.mount('/content/drive')

filename = "drive/Team Drives/Deep Learning Project/events.csv"
df = pd.read_csv(filename)
columns = list(df.columns.values)

df.head()

attempted_shot = []
corner_kick = []
isFoul = []
isYellowCard1 = []
isYellowCard2 = []
straight_red_card = []
substitution = []
free_kick_awarded = []
off_sides = []
is_hand_ball = []
penalty_awarded = []
key_pass = []
failed_through_ball = []
sending_off = []
own_goal = []

for index, row in df.iterrows():
    #Shot attempted event.
    if int(row['event_type']) == 1 or row['event_type'] == "1":
        attempted_shot.append(1)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)
    
    #Corner kick.
    elif int(row['event_type']) == 2 or row['event_type'] == "2":
        corner_kick.append(1)
        attempted_shot.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)

    #Foul event.
    elif int(row['event_type']) == 3 or row['event_type'] == "3":
        isFoul.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)

    #First yellow card event.        
    elif int(row['event_type']) == 4 or row['event_type'] == "4":
        isYellowCard1.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)
    
    #Second yellow card event.
    elif int(row['event_type']) == 5 or row['event_type'] == "5":
        isYellowCard2.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)
        
    #Straight red card event.
    elif int(row['event_type']) == 6 or row['event_type'] == "6":
        straight_red_card.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)
        
    #Player substitution event.
    elif int(row['event_type']) == 7 or row['event_type'] == "7":
        substitution.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)

    #Free kick awarded event.
    elif int(row['event_type']) == 8 or row['event_type'] == "8":
        free_kick_awarded.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)
    
    #Is off-sides event.
    elif int(row['event_type']) == 9 or row['event_type'] == "9":
        off_sides.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)

    #Is hand ball event.
    elif int(row['event_type']) == 10 or row['event_type'] == "10":
        is_hand_ball.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)

    #Penalty awarded event.
    elif int(row['event_type']) == 11 or row['event_type'] == "11":
        penalty_awarded.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)
        
    #Key pass event.
    elif int(row['event_type']) == 12 or row['event_type'] == "12":
        key_pass.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)
        own_goal.append(0)
    
    #Failed-through-ball event.
    elif int(row['event_type']) == 13 or row['event_type'] == "13":
        failed_through_ball.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        sending_off.append(0)
        own_goal.append(0)
    
    #Sending off event.
    elif int(row['event_type']) == 14 or row['event_type'] == "14":
        sending_off.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        own_goal.append(0)
    
    #Own goal event.
    elif int(row['event_type']) == 15 or row['event_type'] == "15":
        own_goal.append(1)
        attempted_shot.append(0)
        corner_kick.append(0)
        isFoul.append(0)
        isYellowCard1.append(0)
        isYellowCard2.append(0)
        straight_red_card.append(0)
        substitution.append(0)
        free_kick_awarded.append(0)
        off_sides.append(0)
        is_hand_ball.append(0)
        penalty_awarded.append(0)
        key_pass.append(0)
        failed_through_ball.append(0)
        sending_off.append(0)

#Create new columns for the 15 additional events.
df["Attempted_Shot"] = pd.Series(attempted_shot)
df["Corner_Kick"] = pd.Series(corner_kick)
df["Foul"] = pd.Series(isFoul)
df["First_Yellow_Card"] = pd.Series(isYellowCard1)
df["Second_Yellow_Card"] = pd.Series(isYellowCard2)
df["Straight_Red_Card"] = pd.Series(straight_red_card)
df["Substitution"] = pd.Series(substitution)
df["Free_Kick_Awarded"] = pd.Series(free_kick_awarded)
df["Off_Sides"] = pd.Series(off_sides)
df["Hand_Ball"] = pd.Series(is_hand_ball)
df["Penalty_Awarded"] = pd.Series(penalty_awarded)
df["Key_Pass"] = pd.Series(key_pass)
df["Failed_Through_Ball"] = pd.Series(failed_through_ball)
df["Sending_Off"] = pd.Series(sending_off)
df["Own_Goal"] = pd.Series(own_goal)

filename = "drive/Team Drives/Deep Learning Project/armaan/aggregate_game_with_16_features.csv"
df.to_csv(filename, sep=',')

