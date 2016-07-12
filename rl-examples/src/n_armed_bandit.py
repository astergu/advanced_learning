#coding=utf8

import numpy as np
from scipy import stats
import random
import matplotlib.pyplot as plt

n = 10
arms = np.random.rand(n)
eps = 0.1

av = np.ones(n) # initialize action-value array
counts = np.zeros(n)  # stores counts of how many times we've taken a particular action
# stores our softmax-generated probability ranks for each action
av_softmax = np.zeros(n)
av_softmax[:] = 0.1  # initialize each action to have equal probability
tau = 1.12  # tau was selected by trial and error

def softmax(av):
    probs = np.zeros(n)
    for i in range(n):
        softm = (np.exp(av[i]/tau) / np.sum(np.exp(av[:]/tau)))
        probs[i] = softm
    return probs


def reward(prob):
    """
        mimic the reward ranging from 0 to 10.
    """
    reward = 0
    for i in range(10):
        if random.random() < prob:
            reward += 1
    return reward


if __name__ == '__main__':
    plt.xlabel("Plays")
    plt.ylabel("Mean Reward")
    for i in range(500):
        choice = np.where(arms == np.random.choice(arms, p=av_softmax))[0][0]
        counts[choice] += 1
        k = counts[choice]
        rwd = reward(arms[choice])
        old_avg = av[choice]
        new_avg = old_avg + (1/k) * (rwd - old_avg)
        av[choice] = new_avg
        av_softmax = softmax(av)  # update softmax probabilities for next play

        runningMean = np.average(av, weights=np.array([counts[j]/np.sum(counts) for j in range(len(counts))]))
        plt.scatter(i, runningMean)
    plt.show()
