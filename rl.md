# Reinforcement Learning Notes

## 主要概念
大多数强化学习算法都假设待解决问题是马尔可夫决策过程（或者近似于马尔可夫决策过程）。

### 马尔可夫决策过程（Markov Decision Process）
强化学习(Reinforcement Learning）的基本算法是马尔可夫决策过程。马尔可夫决策过程是

* 值函数(value function)
* 回馈函数(Reward function)

## 现有RL实现框架或工具

* OpenAIGym
Documentation: https://gym.openai.com/docs




## 什么情况下适用强化学习？

## 自动驾驶&强化学习

### 自动驾驶问题定义

假设本文讨论的是全自动驾驶，即可以在没有驾驶员允许和操作的情况下，完全由程序驾驶车辆行驶。
目前我们主要讨论在道路上的驾驶，而不包括所有非道路状况驾驶（比如土路，泥路等没有车道线和标志的行驶环境）。

具体来说，又可以把道路驾驶分为高速路驾驶和路口驾驶。
*高速路驾驶*
可以认为顺着道路驾驶，与其他车的交互主要是并线和超车。

*路口驾驶*
路口驾驶情况比较复杂，比如包含红绿灯的十字路口，涉及到更复杂的和其他车的交互，比如根据交通灯指示和
路权优先规则让车或直接行驶，以及由于路口没有车道线的行驶轨迹如何确定等问题。



#### 自动驾驶的状态

* 环境状态
* 自身状态

## Perception
occupancy grid

## References
Tutorial: Deep Reinforcement Learning
http://icml.cc/2016/tutorials/deep_rl_tutorial.pdf

http://www0.cs.ucl.ac.uk/staff/d.silver/web/Resources_files/deep_rl.pdf
