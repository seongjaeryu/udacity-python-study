> Udacity
> Written with [StackEdit](https://stackedit.io/).
> [LaTeX Mathematical Equations](https://www.authorea.com/users/77723/articles/110898-how-to-write-mathematical-equations-expressions-and-symbols-with-latex-a-cheatsheet)
> [LaTex Cookbook](http://www.personal.ceu.hu/tex/cookbook.html#inline)


# Vector
> The case that the vector is rooted at the origin. e.g. Coorinate System
- an ordered list of numbers.
- n Dimentional Vector
	- $\vec{x}=\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ : \\x_n \end{bmatrix}$
- Graphically: Arrow ( tail & tip )
- mathematical notation to define a vector :
	- $\vec{x}$

- Each **element** in the vector, also called **component** or **coordinate**, is a number, denoted here by $x_i$.

- This specific vector (in the picture above ) has $n$ elements and can be in the field of Real Numbers $\mathbb{R}$.
	- $\vec{x}\in\mathbb{R}^n$

- Scaling Vector by Scalars

## Vector Transpose

- Column Vector $\vec{x}=\begin{bmatrix} a_1 \\ a_2 \\ a_3 \\ : \\a_n \end{bmatrix}$
- Row Vector $\vec{y}= \begin{bmatrix} a_1&a_2 &a_3& ...& a_n \end{bmatrix}$

$$\begin{bmatrix} a_1 \\ a_2 \\ a_3 \\ : \\a_n \end{bmatrix}^T= \begin{bmatrix} a_1&a_2 &a_3& ...& a_n \end{bmatrix}$$

- tilted by $90^{\circ}$.

- Equation
	- $\vec{x}^T=\vec{y}$
	- $\vec{y}^T=\vec{x}$

### maginitude
- To calculate the magnitude of a 2D vector
	- https://en.wikipedia.org/wiki/Pythagorean_theorem
	- $\vec{x}=\begin{bmatrix}x_1\\x_2\end{bmatrix}$
	- $\left \| \vec{x}\right \|=\sqrt{x_1^2+x_2^2}$

### direction of the movement
- Degrees or Radians
	- https://www.mathwarehouse.com/trigonometry/radians/convert-degee-to-radians.php
- Degree: an angle
	- $\vec{u}$ has an angle $\theta$ with respect to the horizontal axis.
	- $\displaystyle\theta=tan^{-1}\frac{y}{x}$

	> $\displaystyle\sin{\theta}=\frac{y}{\left \|\vec{v}\right\|}$
	>
	> $\displaystyle\cos{\theta}=\frac{x}{\left \|\vec{v}\right\|}$
	>
	> $\displaystyle\tan{\theta}=\frac{y}{x}$

#### Operations in the Field  $\mathbb{R^n}$
- [What is the definition of  $\mathbb{R^n}$?](https://math.stackexchange.com/questions/2376563/what-is-the-definition-of-mathbb-rn)
> - Addition
> - Multiplication
> 
> The above operations satisfy the [**field axioms**](http://mathworld.wolfram.com/FieldAxioms.html):
> -   Associativity
> -   Commutativity
> -   Distributivity
> -   Identity (defining  _zero addition_  and  _multiplication by one_)
> -   Inverse (defining  _Subtraction-Additive Inverse_  and  _Division-Multiplicative Inverse_)

## Vector Addition

> The mathematical definition of a  **vector addition**  in  \mathbb{R^n}Rn  is to add the elements entry by entry.
>
> Lets look at the following example of two vectors:
> 
> -   $\vec{x}=\begin{bmatrix} a_1 \\ a_2 \\ a_3 \\ : \\a_n \end{bmatrix}\in\mathbb{R^n}$
> 
> -   $\vec{y}=\begin{bmatrix} b_1 \\ b_2 \\ b_3 \\ : \\b_n \end{bmatrix}\in\mathbb{R^n}$
> 
> The result,  $\vec{x}+\vec{y}$will be in  $\mathbb{R^n}$ as well.
>
> Mathematically:
> 
> $\vec{x}+\vec{y}=\begin{bmatrix} a_1+b_1 \\ a_2+b_2 \\ a_3+b_3 \\ : \\a_n+b_n \end{bmatrix}\in\mathbb{R^n}$

## Scalar by Vector Multiplication
> A scalar by vector multiplication is also defined by multiplying the vector entry by entry.
>
> If
> 
> $\alpha\in\mathbb{R}$
> 
> and
> 
> $\vec{x}=\begin{bmatrix} a_1 \\ a_2 \\ a_3 \\ : \\a_n \end{bmatrix}\in\mathbb{R^n}$
> 
> then
> 
> $\vec{}y=\alpha\vec{x}=\begin{bmatrix}\alpha a_1 \\\alpha a_2 \\ \alpha a_3 \\ : \\\alpha a_n \end{bmatrix}\in\mathbb{R^n}$


#### Unit Vector
$\hat{\bm{i}}$ and $\hat{\bm{j}}$ are the **basis** vectors of the $xy$ coordinate system.

> $$\vec{r}=x\hat{i}+y\hat{j}+z\hat{k}$$
> - x direction: $\hat{\bm{i}}$
> - y direction: $\hat{\bm{j}}$
> - z direction: $\hat{\bm{k}}$
> - $x$ is the x-coordinate.
> - ...

## Linear Combination of two vectors, Span, and Linear Dependency
$$\large a\vec{v}+b\vec{w}$$
- $a$ and $b$ are **scalar**s.
- $\vec{v}$ and $\vec{w}$ are vectors.

#### Span
> _( Let $a$ and $b$ vary over all real number. )_
> _( If $\vec{v_1}, \vec{v_2},....., \vec{v_n}\in \mathbb{R}$ )_
> 
> The **span** of $\vec{v}$ and $\vec{w}$ is the set of all their linear combinations.
>
>
> **Linearly dependent**
> _if the two vectors are lined up, the span of the two vectors is just a line._
> 
>
>_When one vector **can** be defined as a linear combination of the other vectors, they are a set of **linearly dependent** vectors._
>
> _if not_
> **Linearly independent**

- Technical definition of **basis** :
> The basis of a vector space is a set of linearly independent vectors that span the full space

- Mathematically, the span of the set of vectors is written as:
	- $Sp(\vec{v_1}, \vec{v_2},....., \vec{v_n})$

- Example
> The three following vectors: $\vec{v_1}=\begin{bmatrix} 1 \\0 \\0 \end{bmatrix}$, $\vec{v_2}=\begin{bmatrix} 0 \\1 \\0 \end{bmatrix}$ and $\vec{v_3}=\begin{bmatrix} 0 \\0 \\1 \end{bmatrix}$ span any vector in $\mathbb{R}^3$


The easiest way to know if a set of vectors is linear dependent or not, is with the use of [**determinants**](https://en.wikipedia.org/wiki/Determinant#:~:text=In%20mathematics%2C%20the%20determinant%20is,map%20represented%20by%20the%20matrix.).


### A system of $n$ Linear Equations

A set of equations can be solved using three theoretical methods:

-   Graphical method
-   Substitution method
-   Elimination method

#### Terms
- **Perpendicular lines** are lines that create 90 degree angles when they intersect.
- **Parallel lines** are lines that never intersect. In other words, they run parallel to one another.
- The **slope** of a line through the point $(x_ 1, y_ 1)$ and $(x_ 2, y_ 2)$
