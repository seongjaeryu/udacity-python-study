> 2021-05-19
> From Udacity, AI Programming with Python Nanodegree Program
> Written with [StackEdit](https://stackedit.io/).

# Brief of Neural Network

> The design of the  **Artificial Neural Network**  was inspired by the biological one. The neurons used in the artificial network below are essentially mathematical functions.
> 
> Each network has:
> 
> -   Input neurons- which we refer to as the  _input layer_  of neurons
> -   Output neurons- which we refer to as the  _output layer_  of neurons
> 
> and
> 
> -   Internal neurons- which we refer to as the  _hidden layer_  of neurons. Each neural network can have many hidden layers
> 
> The following picture is of a simple neural network with a single hidden layer.
> 
> ![](https://video.udacity-data.com/topher/2018/January/5a7241d0_screen-shot-2018-01-31-at-2.22.49-pm/screen-shot-2018-01-31-at-2.22.49-pm.png)
> 
> _Simplified Artificial Neural Network_

> This version of a simplified artificial neural network is comprised out of:
> 
> -   An input vector  $\vec{x}=\begin{bmatrix} x_1 & x_2 & x_3 & ... &x_n \end{bmatrix}$
> 
> -   A hidden layer vector  $\vec{h}=\begin{bmatrix} h_1 & h_2 & h_3 & ... &h_m \end{bmatrix}$
> 
> and
> 
> -   An output vector  $\vec{y}=\begin{bmatrix} y_1 & y_2 & y_3 & ... &y_k \end{bmatrix}$
> 
> Each element in the vectors is a mathematical argument which we will elaborate on very soon.
> 
> Notice that there is no connection between the number of inputs, number of hidden neurons in the hidden layer or number of outputs.
> 
> > (The notation we used here is of a row vector, these vectors can be expressed as column vectors as well)
>
> Notice the "lines" connecting the different neurons?
> 
> -   In practice, these lines symbolize a coefficient (a scalar) that is mathematically connecting one neuron to the next. These coefficients are called  **weights**.
>     
> -   The "lines" connect each neuron in a specific layer to  **all**  of the neurons on the following. For example, in our example, you can see how each neuron in the hidden layer is connected to a neuron in the output one.
>     
> 
> Since there are so many  **weights**  connecting one layer to the next, we mathematically organize those coefficients in a matrix, denoted as the  **weight matrix**.
> 
> ![](https://video.udacity-data.com/topher/2018/January/5a7248c3_screen-shot-2018-01-31-at-2.52.19-pm/screen-shot-2018-01-31-at-2.52.19-pm.png)
> 
> _Simplified Artificial Neural Network With A Weight Matrix_
>
>
> We use subscripts as well as superscript as a numeric notation for the weight matrix.
>
> For example:
> 
> -   $W_k$​  is weight matrix  $k$.
> -   $W_{ij}^k$  is the $ij$ element of weight matrix  $k$.

> When working with neural networks we have 2 primary phases:
> 
> -   Training
> 
> and
> 
> -   Evaluation.
> 
> During the training phase, we take the data set (also called the training set), which includes many pairs of inputs and their corresponding targets (outputs). Our goal is to find a set of weights that would best map the inputs to the desired outputs.
> 
> In the evaluation phase, we use the network that was created in the training phase, apply our new inputs and expect to obtain the desired outputs.
> 
> The training phase will include two steps:
> 
> -   Feedforward
> 
> and
> 
> -   Backpropagation
> 
> We will repeat these steps as many times as we need until we decide that our system has reached the best set of weights, giving us the best possible outputs.

## The Feedforward Process - Finding  $\vec{h}$

vector  \vec{h'}h′⃗  of the hidden layer will be calculated by multiplying the input vector with the weight matrix  $W^{1}$  the following way:

$\vec{h'} = (\bar{x} W^1 )$

Using vector by matrix multiplication, we can look at this computation the following way:

![](https://video.udacity-data.com/topher/2018/February/5a725e7c_screen-shot-2018-01-31-at-4.25.16-pm/screen-shot-2018-01-31-at-4.25.16-pm.png)

_Equation 17_

After finding  $\vec{h'}$ we need an activation function.

The symbol we use for the activation function is the Greek letter phi:  $\Phi$ Φ.

This activation function finalizes the computation of the hidden layer's values.

We can use the following two equations to express the final hidden vector  $\vec{h'}$

$\vec{h} = \Phi(\vec{x} W^1 )$

or

$\vec{h} = \Phi(\vec{h'})$

Since  $W_{ij}$ represents the weight component in the weight matrix, connecting neuron  **i**  from the input to neuron  **j**  in the hidden layer, we can also write these calculations using a  **linear combination**: (notice that in this example we have  _n_  inputs and only 3 hidden neurons)

![](https://video.udacity-data.com/topher/2018/February/5a725f86_screen-shot-2018-01-31-at-4.29.38-pm/screen-shot-2018-01-31-at-4.29.38-pm.png)

_Equation 18_

As you've seen in the video above, the process of calculating the output vector is mathematically similar to that of calculating the vector of the hidden layer. We use, again, a vector by matrix multiplication. The vector is the newly calculated hidden layer and the matrix is the one connecting the hidden layer to the output.

![](https://video.udacity-data.com/topher/2018/February/5a8743de_screen-shot-2018-02-16-at-12.49.05-pm/screen-shot-2018-02-16-at-12.49.05-pm.png)

Essentially, each new layer in an neural network is calculated by a vector by matrix multiplication, where the vector represents the inputs to the new layer and the matrix is the one connecting these new inputs to the next layer.

In our example, the input vector is  \vec{h}h⃗  and the matrix is  $W^2$, therefore  $\vec{y}=\vec{h}W^2$.

![](https://video.udacity-data.com/topher/2018/February/5a874420_screen-shot-2018-02-16-at-12.50.25-pm/screen-shot-2018-02-16-at-12.50.25-pm.png)

_Equation 19_


