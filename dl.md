<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# Deep Learning Notes

* 2016-07-04 Yoshua Bengio参加Idiap举办的深度学习研讨会，发表题为《Representations中的深度监督学习》的演讲。
在机器学习模型中加入组合性是通往人工智能未来、打破“维度魔咒”的一个关键。最近，深度学习有3大进展：Attention、Reasoning、Planning和Reinforcement Learning.
另外，技术应用上走在最前沿的是融合技术，比如视觉与自然语言理解的结合，下一个前沿应用将是推理和回答问题。


## Neural Networks (神经网络)

神经网络可以提供非线性的复杂模型。

### 感知器（perceptron）
感知器由科学家Frank Rosenblatt发明于1950至1960年代，现今实用的神经网络中主要采用
sigmoid神经元模型。感知器的输入是几个二进制，x1, x2, ..., 输出是一位单独的二进制。
通过引入权重和阈值，由输入的加权和与阈值相比较，来决定输出。

![感知器]{http://neuralnetworksanddeeplearning.com/images/tikz0.png}

可以理解为这是一个通过给evidence赋予不同权重而作出决策的机器。只有一个简单的感知器显然
是不足以作出复杂的决策的。那么由感知器构成的复杂网络是否可以做出更加精细的决策呢？

在这个网络中，第一层感知器通过赋予输入的evidence权重，做出三个非常简单的决策。每一个
第二层感知器通过赋予权重给第一层感知器的决策结果，来做出决策。通过这种方式，第二层感知器
可以比第一层感知器做出更加复杂以及更高层次抽象的决策。第三层感知器能够做出更加复杂的决策。

用偏移(bias)来替代阈值threshold，b=-threshold，可以将偏移理解为感知器为了得到输出为1的
容易度的度量。如果从生物的角度来理解，偏移是使神经元被激活的容易度的度量。

实际上，感知器网络还可以用来计算任何逻辑函数。因为NAND门在计算上是通用的，这意味着我们可以
使用NAND门构建任意逻辑运算。

感知器网络尽管看上去不过是一种新的NAND门，但是可以设计学习算法（learning algorithm）使得
自动地调整人工神经网络的权重和偏移。这种调整能够对外部刺激作出响应，而不需要程序员的直接
干预。

### 后向传播算法／反向传播算法（Backpropagation）

反向传播：计算对网络中所有权重计算损失函数的梯度。这个梯度会反馈给最优化方法，用来更新权值以最小化损失函数。

反向传播（缩写为BP）是“误差反向传播”的简称，是一种与最优化方法（如）梯度下降法
结合使用的，用来训练人工神经网络的常见方法。该方法计算对网络中所有权重计算损失函数
的梯度。



### 前向传播算法（Forward propagation）

如果后向传播对应训练的话，那么前向传播就对应预测（分类）。

### 常用激活函数
* 线性函数（Linear Function）
f(x)=k*x+c

* 斜面函数（Ramp Function）

* 阈值函数（Threshold Function）

以上3个激活函数都属于线性函数。

* Sigmoid函数

神经元的其非线性作用函数，-x是优点幂数。连续可导。



$$f(x)=\frac{1}{1+e^{-x}}$$

![单极性Sigmoid函数图象](https://takinginitiative.files.wordpress.com/2008/04/sigmoidfunction.png?w=680g)

Sigmoid函数的值域范围为(0, 1).

* 双极S形函数

双极S形函数与S形函数的主要区别在于函数的值域，双形S形函数值域是(-1, 1)，而S形函数值域是(0, 1)。

* Softmax函数


### 神经网络的学习算法——BP算法

神经网络的学习是基于一组样本进行的，输入和输出由有多少个分量就有多少个输入和输出神经元与之对应。最初神经网络的权值（Weight）和阈值（Threshold）
是任意给定的，学习就是逐渐调整权值和阈值使得网络的实际输出和期望输出一致。

## Q-Learning


## Existing Framework/Toolkits

* Caffe
Caffe是由Berkeley Vision and Learning Center（BVLC）建立的深度学习框架。它是模块化的，速度极快。
而且被应用于学术界和产业界的start-of-the-art应用程序中。
你可以在一个空白文档里定义你的模型架构和解决方案，建立一个JSON文件类型的.prototxt配置文件。
Caffe二进制文件提取这些.prototxt文件并培训你的网络。Caffe完成培训之后，你可以把你的网络和经过分类的新图像通过Caffe二进制文件，
更好的就直接通过Python或MATLAB的API。

但是，在.prototxt文件内部构建架构可能会变得相当乏味和无聊。更重要的是，Caffe不能用程序调整超参数。

* Theano
Theano是一个Python库，用来定义、优化和评估涉及多维数组的数学表达式。 Theano通过与numpy的紧密集成，透明地使用GPU来完成这些工作。

* TensorFlow
与Theano类似，TensorFlow是使用数据流图进行数值计算的开源库（这是所有神经网络固有的特征）。
最初由谷歌的机器智能研究机构内的Google Brain Team研究人员开发，此后库一直开源，并提供给公众。
相比于Theano ，TensorFlow的主要优点是分布式计算，特别是在多GPU的环境中（虽然这是Theano正在攻克的项目）。

* Lasagne
Lasagne是Theano中用于构建和训练网络的轻量级库。这里的关键词是轻量级的，也就意味着它不是一个像Keras一样围绕着Theano的重包装的库。
虽然这会导致你的代码更加繁琐，但它会把你从各种限制中解脱出来，同时还可以让您根据Theano进行模块化的构建。

* Keras
Keras是一个最低限度的、模块化的神经网络库，可以使用Theano或TensorFlow作为后端。
Keras最主要的用户体验是，从构思到产生结果将会是一个非常迅速的过程。
在Keras中架构网络设计是十分轻松自然的。它包括一些state-of-the-art中针对优化（Adam，RMSProp）、
标准化（BatchNorm）和激活层（PReLU，ELU，LeakyReLU）最新的算法。

Keras唯一的问题是它不支持多GPU环境中并行地训练网络。这可能会也可能不会成为你的大忌。
如果我想尽快地训练网络，那么我可能会使用mxnet。但是如果我需要调整超参数，
我就会用Keras设置四个独立的实验（分别在我的Titan X GPUs上运行）并评估结果。

* mxnet
Mxnet库真正出色的是分布式计算，它支持在多个CPU / GPU机训练你的网络，甚至可以在AWS、Azure以及YARN集群。
它确实需要更多的代码来设立一个实验并在mxnet上运行（与Keras相比），但如果你需要跨多个GPU或系统分配训练，我推荐mxnet。


### Keras
keras.io


