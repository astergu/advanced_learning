#coding=utf8

import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt

n = 10
arms = np.random.rand(n)
eps = 0.1

def reward(prob):
    """
        mimic the reward ranging from 0 to 10.
    """
    reward = 0
    for i in range(10):
        if random.random() < prob:
            reward += 1
    return reward

# memory array; has 1 row defaulted to random action index
av = np.array([np.random.randint(0, (n+1)), 0]).reshape(1, 2)  # action-value

def bestArm(a):
    bestArm = 0
    bestMean = 0
    for u in a:
        avg = np.mean(a[np.where[(a[:,0] == u[0])[:,1]) # calculate mean reward for each action
        if bestMean < avg:
        bestMean = avg
        beatArm = u[0]
    
    return bestArm


