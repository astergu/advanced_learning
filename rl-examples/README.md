# README

参考网站http://outlace.com/Reinforcement-Learning-Part-1 进行，顺着进行Part2, Part3。

## Simple Problem
假设在赌场，一台10个槽的老虎机上写着“Play for free! Max payout is $10!”，也就是，每一个槽给的回报介于0到$10之间。
问题是，每一个槽位的平均回报是不一样的，找出平均回报最大的槽位是哪个。这可以被称为n-armed bandit problem。

我们可以有n个可能的操作（这里n=10），每一次操作k我们都可以从n个槽位中的任意一个选择一个拉，
随即得到一个相应的回报R_k。随着操作次数的增多，我们可以逐步得到每个action的期望回报。

但是问题是，我们需要平衡exploration和exploitation，exploration就是根据历史知识选取最佳的操作，
但是我们需要exploitation来探索更多操作，以使得可以学习更多知识。我们可以通过增加一个epsilon，
即选择概率，来平衡随机性和根据先验选择。

## Blackjack (21点问题）
1. 从状态集中选择一个随机的状态S_0，这是初始化initGame()做的；
2. 从操作集中选择一个操作，通常是根据给定状态S_0.
3. 根据一个策略pi，和初始状态、初始动作，生成一个完整的episode;
4. 对每一个(s, a)对，计算从(s,a)对起始的回报G
5. 对每一个状态s，采用epsilon贪心选择算法来找出最佳的策略pi。
