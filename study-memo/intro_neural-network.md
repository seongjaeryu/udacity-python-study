> 2021-05-26
> From Udacity, AI Programming with Python Nanodegree Program
> Written with [StackEdit](https://stackedit.io/).


# Gradient Calculation

In the last few videos, we learned that in order to minimize the error function, we need to take some derivatives. So let's get our hands dirty and actually compute the derivative of the error function. The first thing to notice is that the sigmoid function has a really nice derivative. Namely,

> $\sigma'(x) = \sigma(x) (1-\sigma(x))$

σ′(x)=σ(x)(1−σ(x))

The reason for this is the following, we can calculate it using the quotient formula:

![](https://video.udacity-data.com/topher/2017/May/5910e6c6_codecogseqn-49/codecogseqn-49.gif)

And now, let's recall that if we have  mm  points labelled  $x^{(1)}, x^{(2)}, \ldots, x^{(m)}$ the error formula is:

$E = -\frac{1}{m} \sum_{i=1}^m \left( y_i \ln(\hat{y_i}) + (1-y_i) \ln (1-\hat{y_i}) \right)$

where the prediction is given by  $\hat{y_i} = \sigma(Wx^{(i)} + b)$.

Our goal is to calculate the gradient of  $E$,  at a point  $x = (x_1, \ldots, x_n)$,  given by the partial derivatives

$\nabla E =\left(\frac{\partial}{\partial w_1}E, \cdots, \frac{\partial}{\partial w_n}E, \frac{\partial}{\partial b}E \right)$

To simplify our calculations, we'll actually think of the error that each point produces, and calculate the derivative of this error. The total error, then, is the average of the errors at all the points. The error produced by each point is, simply,

$E = - y \ln(\hat{y}) - (1-y) \ln (1-\hat{y})$

In order to calculate the derivative of this error with respect to the weights, we'll first calculate  $\frac{\partial}{\partial w_j} \hat{y}$.
Recall that  $\hat{y} = \sigma(Wx+b)$, so:

![](https://video.udacity-data.com/topher/2017/May/590eac24_codecogseqn-43/codecogseqn-43.gif)

The last equality is because the only term in the sum which is not a constant with respect to  w_jwj​  is precisely  w_j x_j,wj​xj​,  which clearly has derivative  x_j.xj​.

Now, we can go ahead and calculate the derivative of the error  EE  at a point $x$, with respect to the weight $w_j$.

![](https://video.udacity-data.com/topher/2018/January/5a716f3e_codecogseqn-60-2/codecogseqn-60-2.png)

A similar calculation will show us that

![](https://video.udacity-data.com/topher/2017/September/59b75d1d_codecogseqn-58/codecogseqn-58.gif)

This actually tells us something very important. For a point with coordinates $(x_1, \ldots, x_n)$, label  $y$, and prediction $\hat{y}$,  the gradient of the error function at that point is $\left(-(y - \hat{y})x_1, \cdots, -(y - \hat{y})x_n, -(y - \hat{y}) \right)$.

In summary, the gradient is below.

$\nabla E = -(y - \hat{y}) (x_1, \ldots, x_n, 1)$

So, a small gradient means we'll change our coordinates by a little bit, and a large gradient means we'll change our coordinates by a lot.

If this sounds anything like the perceptron algorithm, this is no coincidence! We'll see it in a bit.

# Gradient Descent Step

Therefore, since the gradient descent step simply consists in subtracting a multiple of the gradient of the error function at every point, then this updates the weights in the following way:

$w_i' \leftarrow w_i -\frac{\alpha}{m} [-(y - \hat{y}) x_i]$ ,

which is equivalent to

$w_i' \leftarrow w_i + \frac{\alpha}{m}  (y - \hat{y}) x_i$ .

Similarly, it updates the bias in the following way:

$b' \leftarrow b + \frac{\alpha}{m} (y - \hat{y})$


# Gradient Descent Algorithm
1. Start with random weights and bias:
	> $(w_1, \ldots, w_n, b)$
2. For every point $(x_1, \ldots, x_n)$ :
	2.1. For i = 1, ... , n
		2.1.1. Update $w_i' \leftarrow w_i + \frac{\alpha}{m}  (y - \hat{y}) x_i$ 
		2.1.2. Upadte $b' \leftarrow b + \frac{\alpha}{m} (y - \hat{y})$


# Perceptron vs. Gradient Descent

**Gradient Descent Algorithm** : y = from 0 to 1
- if correctly classified: Make it go farther away
> Change:
> $w_i' \leftarrow w_i + \frac{\alpha}{m}  (y - \hat{y}) x_i$ 
> $b' \leftarrow b + \frac{\alpha}{m} (y - \hat{y})$

**Perceptron Algorithm** : y = 1 or 0
- if correctly classified:  Do nothing
> If x is misclassified, change:
> 1. if positive:
>  $w_i' \leftarrow w_i + \alpha x_i$
> 2. if negative:
> $w_i' \leftarrow w_i - \alpha x_i$

> If correctly classified: $y-\hat{y} = 0$
>
> If misclasified:
> 1. If positive:
> $y-\hat{y} = 1$
> 2. If negative:
> $y-\hat{y} = -1$

Perceptron Algorithm code below.
```
import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i]-y_hat == 1: # 1 & 0
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat == -1: # 0 & 1
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b
    
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines
```
#### Perceptron: AND node
```
import pandas as pd

# TODO: Set weight1, weight2, and bias
weight1 = 1.0
weight2 = 1.0
bias = -1.5


# DON'T CHANGE ANYTHING BELOW
# Inputs and outputs
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [False, False, False, True]
outputs = []

# Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
    output = int(linear_combination >= 0)
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

# Print output
num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(output_frame.to_string(index=False))
```

#### Perceptron:  NOT node
```
import pandas as pd

# TODO: Set weight1, weight2, and bias
weight1 = 0.0
weight2 = -1.0
bias = 0.5


# DON'T CHANGE ANYTHING BELOW
# Inputs and outputs
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [True, False, True, False]
outputs = []

# Generate and check output
for test_input, correct_output in zip(test_inputs, correct_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
    output = int(linear_combination >= 0)
    is_correct_string = 'Yes' if output == correct_output else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

# Print output
num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(output_frame.to_string(index=False))
```
#### Perceptron: XOR node set
> - **NAND**  operator as the combination of  **AND** $\rightarrow$ **NOT**
> - Two-layer perceptron model  **XOR**
> -  ![alt text](https://d17h27t6h515a5.cloudfront.net/topher/2017/May/59112cdf_xor-quiz2/xor-quiz2.png)




# Softmax

**TO-DO**
> Things from hand-written notes.

Softmax code below.
```
def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result
    
    # Note: The function np.divide can also be used here, as follows:
    # def softmax(L):
    #     expL = np.exp(L)
    #     return np.divide (expL, expL.sum())
```


# Cross-Entropy

**TO-DO**
> Things from hand-written notes.

Cross-Entropy code below.
```
def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
```




# Links

## Activation Function vs. Squashing Function
Source: [Activation function vs Squashing function - Data Science Stack](https://datascience.stackexchange.com/questions/36533/activation-function-vs-squashing-function)

### An activation function

This the name given to a function, which is applied to a neuron that just had a weight update as a result of new information. It can refer to any of the well known activation funtions, such as the Rectified Linear Unit (ReLU), the hyperbolic tangent function (tanh) or even the identity function! Have a look at somewhere like the  [Keras documentation](https://keras.io/activations/)  for a nice little list of examples.

We usually define the activation function as being a non-linear function, as it is that property, which gives a neural network its ability to approximate  [**any**  equation (given a few constraints)](https://en.wikipedia.org/wiki/Universal_approximation_theorem). However, an activation function can also be linear e.g. the identity function.

### A squashing function

This can mean one of two things, as far as I know, in the context of a neural network - the tag you added to the question - and they are close, just differently applied.

The first and most commonplace example, is when people refer to the  **softmax function**, which  _squashes_  the final layer's activations/logits into the range [0, 1]. This has the effect of allowing final outputs to be directly interpreted as probabilities (i.e. they must sum to 1).

The second and newest usage of these words in the context of neural networks is from the relatively recent papers ([one](https://arxiv.org/pdf/1710.09829.pdf)  and  [two](https://openreview.net/pdf?id=HJWLfGWRb)) from Sara Sabour, Geoffrey Hinton, and Nicholas Frosst, which presented the idea of  **Capsule Networks**. What these are and how they work is beyond the scope of this question; however, the term "squashing function" deserves special mention. Paper number one introduces it followingly:

> We want the length of the output vector of a capsule to represent the probability that the entity represented by the capsule is present in the current input. We therefore use a non-linear "squashing" function to ensure that short vectors get shrunk to almost zero length and long vectors get shrunk to a length slightly below 1.

That description makes it sound very similar indeed to  [the softmax!](https://en.wikipedia.org/wiki/Softmax_function)

This  _squashing function_  is defined as follows:

𝑣𝑗=||𝑠𝑗||21+||𝑠𝑗||2⋅𝑠𝑗||𝑠𝑗||vj=||sj||21+||sj||2⋅sj||sj||

> where  𝑣𝑗  is the vector output of capsule  𝑗 and  𝑠𝑗 is its total input.

If this is all new to you and you'd like to learn more, I'd recommend having a read of those two papers, as well as perhaps a nice overview blog,  [like this one](https://medium.com/ai%C2%B3-theory-practice-business/understanding-hintons-capsule-networks-part-i-intuition-b4b559d1159b).

## Python: Sigmoid Function
$$f(x)=\sigma(x)=\frac{1}{1+e^{-x}}$$
Source: [Implement sigmoid function using Numpy - GeeksforGeeks](https://www.geeksforgeeks.org/implement-sigmoid-function-using-numpy/)

```
# Import matplotlib, numpy and math
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10, 10, 100)
z = 1/(1 + np.exp(-x))

plt.plot(x, z)
plt.xlabel("x")
plt.ylabel("Sigmoid(X)")

plt.show()
```
