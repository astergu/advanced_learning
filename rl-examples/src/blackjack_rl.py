#coding=utf8

import numpy as np

# Create a list of all the possible states
def initStateSpace():
    states = []
    for card in range(1, 11):
        for val in range(11, 22):
            states.append((val, False, card))
            states.append((val, True, card))

# Create a dictionary of all possible state_actions and their values
# This creates our Q-value look up table
def initStateActions(states):
    av = {}
    for state in states:
        av[(state, 0)] = 0.0
        av[(state, 1)] = 0.0
    return av

# Setup a dictionary of state-actions to record how many times we've experienced
# a given state-action pair. We need this to re-calculate reward averages
def initSAcount(stateActions):
    counts = {}
    for sa in stateActions:
        counts[sa] = 0
    return counts

# This calculates the reward of the game, either +1 for winning,
# 0 for draw, or -1 for losing
# We can determine this by simply substracting the game status value from 3
def calcReward(outcome):
    return 3-outcome

# This calculates the average rewards of our Q-value lookup table
def updateQtable(av_table, av_count, returns):
    for key in returns:
        av_table[key] = av_table[key] + (1/av_count[key]) * (returns[key] - av_table[key])
    return av_table

# returns Q-value/avg rewards for each action given a state
def qsv(state, av_table):
    stay = 
