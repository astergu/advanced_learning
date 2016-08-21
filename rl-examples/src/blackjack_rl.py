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
    stay = av_table[(state, 0)]
    hit = av_table[(state, 1)]
    return np.array([stay, hit])
   
# converts a game state of the form ((player total, ace), (dealer total, ace), status)
# to a condensed state we'll use for our RL algorithm (player total, usable ace, dealer card)
def getRLstate(state):
    player_hand, dealer_hand, status = state
    player_val, player_ace = player_hand
    return (player_val, player_ace, dealer_hand[0])


if __name__ == '__main__':
    epoches = 5000000
    epsilon = 0.1
    
    state_space = initStateSpace()
    av_table = initStateActions(state_space)
    av_count = initSAccount(av_table)

    for i in range(epoches):
        # initialize new game; observe current state
        state = initGame()
        player_hand, dealer_hand, status = state
        # if player's total is less than 11, increase total by adding another card
        # we do this because whenever the players