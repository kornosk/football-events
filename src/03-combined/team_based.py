# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:40:44 2018

@author: hanji
"""

import pandas as pd
from collections import Counter
from copy import copy
df = pd.read_csv("events.csv")
df = df.ix[:,[0,8,9,16]]
game = df['id_odsp'].unique()
game_base = df.groupby('id_odsp')

game_dic = {}
for i in game:
    game_dic[i]=0
    
for each in game:
    this_game = game_base.get_group(each)
    this_game_goal = this_game.groupby('is_goal')


    if len(this_game['is_goal'].unique()) ==2:
        goal = this_game_goal.get_group(1)
        if len(goal['event_team'].unique())==2:
            a = dict(Counter(goal['event_team']))
            temp = copy(a)
            if list(temp.values())[0] > list(temp.values())[1]:
                a['win']=list(temp.keys())[0]
                a['loss']=list(temp.keys())[1]
                a['draw']=None
            else:
                if list(temp.values())[0] == list(temp.values())[1]:
                        a['win']=None
                        a['loss']=None
                        a['draw']=list(temp.keys())
                else:
                    a['win']=list(temp.keys())[1]
                    a['loss']=list(temp.keys())[0]
                    a['draw']=None
            game_dic[each]=a
        else:
            b = dict(Counter(goal['event_team']))
            temp = copy(b)
            other_team = list(this_game['event_team'].unique())
            for i in other_team:
                if list(temp.keys())[0] != i:
                    b[i]=0
                    opponent = i
            b['win'] = list(temp.keys())[0]
            b['loss'] = opponent
            b['draw'] = None
            game_dic[each]=b
    else:
        team = this_game['event_team'].unique()
        c = {}
        for i in team:

            c[i]=0
        temp = copy(c)
        c['win']=None
        c['loss']=None
        c['draw']=list(temp.keys())
        game_dic[each]=c
            
team = df['event_team'].unique()
goals=[]
loss = []
wins = []
losing_score = []
number_games = []
draws = []

for item in team:
    total_goal = 0
    total_score = 0
    count_games = 0
    total_wins = 0
    total_loss = 0
    total_draws =0
    for value in list(game_dic.values()):
        if item in list(value.keys()):
            total_goal = total_goal + value[item]
            opponent = [i for i in list(value.keys()) if i not in [item,'win','draw','loss']]
            total_score = total_score + int(value[opponent[0]])
            count_games = count_games +1
            if item == value['win']:
                total_wins = total_wins +1
            else:
                if item == value['loss']:
                    total_loss = total_loss +1
                else:
                    total_draws = total_draws +1
                    
            
            
    goals.append(total_goal)
    losing_score.append(total_score)
    number_games.append(count_games)
    loss.append(total_loss)
    draws.append(total_draws)
    wins.append(total_wins)

            
# team based data
dic = {'team': team, 'goals':goals, 'losing scores': losing_score,'wins':wins,'loss':loss,'#games':number_games,'tie':draws}        
df = pd.DataFrame(dic)
df['winning rate'] = df['wins']/df['#games']
df['loss rate'] = df['loss']/df['#games']
df['average goals'] = df['goals']/df['#games']
df['average losing score'] = df['losing scores']/df['#games']
df['tie rate'] = df['tie']/df['#games']
        
df.to_csv('team based data.csv',index = False)        