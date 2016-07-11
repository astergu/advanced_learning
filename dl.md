<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# Deep Learning Notes

## Neural Networks (神经网络)

神经网络可以提供非线性的复杂模型。

### 感知器（perceptron）



### 后向传播算法／反向传播算法（Backpropagation）

反向传播（缩写为BP）是“误差反向传播”的简称，是一种与最优化方法（如）梯度下降法
结合使用的，用来训练人工神经网络的常见方法。该方法计算对网络中所有权重计算损失函数
的梯度。

### 前向传播算法（Forward propagation）

如果后向传播对应训练的话，那么前向传播就对应预测（分类）。


### Sigmoid函数

神经元的其非线性作用函数，-x是优点幂数。连续可导。


$$f(x)=\frac{1}{1+e^{-x}}$$

![单极性Sigmoid函数图象](https://takinginitiative.files.wordpress.com/2008/04/sigmoidfunction.png?w=680g)

Sigmoid函数的值域范围为(0, 1).

### 神经网络的学习算法——BP算法

神经网络的学习是基于一组样本进行的，输入和输出由有多少个分量就有多少个输入和输出神经元与之对应。最初神经网络的权值（Weight）和阈值（Threshold）
是任意给定的，学习就是逐渐调整权值和阈值使得网络的实际输出和期望输出一致。

## Existing Framework/Toolkits

### Keras
keras.io


