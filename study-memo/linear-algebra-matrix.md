> Udacity
> Written with [StackEdit](https://stackedit.io/).
> [LaTeX Mathematical Equations](https://www.authorea.com/users/77723/articles/110898-how-to-write-mathematical-equations-expressions-and-symbols-with-latex-a-cheatsheet)
> [LaTex Cookbook](http://www.personal.ceu.hu/tex/cookbook.html#inline)


# Matrix

> A  **Matrix**  is a two dimensional array that contains the same elements as the vector.
>
> A Matrix can have  mm  rows and  nn  columns.
>
> If a Matrix has  $m$  rows and  $n$  columns is it called an  mm  x  nn  matrix.
>
>Each Element: $a_{ij}$ is a numerical value displayed in row $i$ and column $j$.
> - the  ${ij}$th element of the matrix

## Matrix Addition
To add one matrix to the other we need to:
-   Verify that the matrices are of the same dimensions
-   Make sure we add elements in the correct corresponding index.

## Multiplication of Square Matrices
Each element  ijij  in  PPxQQ  is a result of multiplying all elements in row  ii  of matrix  PP  with the corresponding  jj  elements in column j of matrix  QQ.

See the picture below for an illustration :

![](https://video.udacity-data.com/topher/2018/February/5a84cd95_screen-shot-2018-02-14-at-3.59.39-pm/screen-shot-2018-02-14-at-3.59.39-pm.png)

if A is an n × m matrix and B is an m × p matrix, their matrix product AB is an n × p matrix, in which the **m entries across a row of A** are multiplied with the **m entries down a column of B** and summed to produce an entry of AB.

When two linear transformations are represented by matrices, then the matrix product represents the composition of the two transformations. _Linear Transformation_

Since $A B\neq BA$ , we say they there are not [**commutative**](https://en.wikipedia.org/wiki/Commutative_property).



### Linear Transformation with Basis vectors
$$\begin{bmatrix} i_1 & j_1 \\ i_2 & j_2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}=\begin{bmatrix} i_1x+ j_1y \\ i_2x + j_2y \end{bmatrix}$$
$\hat{i}$, $\hat{j}$ : basis vector


> $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ : $90^{\circ}$ Rotation Counterclockwise
>
> $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ : Shear 

if the basis vectors ( $\hat{i}$ and $\hat{j}$ ) is **linearly dependent**,
> resulting one dimentional **span** of those two linearly dependent vectors ( _the linear transformation **squishes**_ all of the 2D space onto the line where those two vectors sit )
