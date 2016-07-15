# Autonomous Car (无人驾驶车)

## 动力学模型

## 无人驾驶车的传动方式

## 人开车的智能体现

* The estimation of the threat level of planned actions
Such as overtaking, lane changing, or intersection crossing, are mainly evaluated according to a ratio
of risk and time efficiency.

## PID控制

PID控制器（比例-积分-微分控制器），由比例单元P、积分单元I和微分单元D组成。
PID控制器主要适用于基本上线性，且动态特性不随时间变化的系统。
PID控制器是一个在工业控制应用中常见的反馈回路部件。

![PID控制](https://zh.wikipedia.org/wiki/File:Pid-feedback-nct-int-correct.png)

## RTK实时动态定位技术
RTK测量技术，是以载波相位观测量为根据的实时差分GPS测量技术。由于GPS测量数据需要在测后处理，
所以无法实时地给出观测站的定位结果，而且也不能对基准站和用户观测数据的质量进行实时检验。

实时动态测量的基本思想是，在基准站上安置一台GPS接收机，对所有可见GPS卫星进行连续观测，并
将其测量数据通过无线电传输设备，实时地发送给用户观测站。在用户站上，GPS接收机在接收GPS
卫星信号的同时，通过无线电接收设备，接收基准站传输的测量数据，然后根据相对定位的原理，
实时地计算并显示用户站的三维坐标及其精度。通过实时计算的定位结果，便可监测基准站与用户站
测量数据的质量和解算结果的收敛情况，从而可实时地判定解算结果是否成功，以减少冗余测量，
缩短测量时间。

RTK的重点在于高精度定位。


## 无人驾驶车的决策系统

1. rule-based
2. MDP
3. POMDP
4. Reinforcement Learning
5. Fuzzy rule
Mamdani's inference
Ref: Fuzzy control to drive car-like vehicles

## 无人驾驶车的预测系统

Monte-Carlo methods

1. Crash-probability calculation
Ref: Model-based probabilistic collision detection in autonomous driving
Idea: stochastic reachable sets
