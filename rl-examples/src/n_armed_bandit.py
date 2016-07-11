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


def bestArm(a):
    bestArm = 0
    bestMean = 0
    for u in a:
        avg = np.mean(a[np.where(a[:,0] == u[0])][:,1]) # calculate mean reward for each action
        if bestMean < avg:
            bestMean = avg
            beatArm = u[0]
    
    return bestArm


if __name__ == '__main__':
    # memory array; has 1 row defaulted to random action index
    av = np.array([np.random.randint(0, (n+1)), 0]).reshape(1, 2)  # action-value
    
    plt.xlabel("Plays")
    plt.ylabel("Avg Reward")
    for i in range(500):
        print av
        if random.random() > eps:  # greedy arm selection
            choice = bestArm(av)
            thisAv = np.array([[choice, reward(arms[choice])]])
            av = np.concatenate((av, thisAv), axis=0)
        else:  # random arm selection
            choice = np.where(arms == np.random.choice(arms))[0][0]
            thisAV = np.array([[choice, reward(arms[choice])]])  # choice, reward
            av = np.concatenate((av, thisAV), axis=0)
        # calculate the percentage the correct arm is chosen (you can plot this instead of reward)
        percCorrect = 100 * (len(av[np.where(av[:,0] == np.argmax(arms))])/len(av))
        runningMean = np.mean(av[:,1])
        plt.scatter(i, runningMean)
    plt.show()

