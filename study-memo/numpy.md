# UDACITY, Introduction to Python
##### Markdown Editor: https://stackedit.io/
##### Mini Project: [Mean Normalization and Data Separation.ipynb](https://github.com/udacity/AIPND/blob/master/NumPy%20Mini-Project/Mean%20Normalization%20and%20Data%20Separation.ipynb)


### Category: General Purpose

**Function/Method**

**Description**

[`numpy.ndarray.dtype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dtype.html)

Return the data-type of the elements of the array. Remember, arrays are homogeneous.

[`numpy.ndarray.ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.ndim.html)

Return the  _number_  of array-dimensions (rank), e.g., it will return 2 for a 4x3 array.

[`numpy.ndarray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html)

Return a tuple representing the array dimensions, e.g., it will return  `(rows,columns)`  for a rank 2 array.

[`numpy.ndarray.size`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.size.html)

Return the number of elements present in the array.

[`numpy.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html)

Save an array to  `.npy`  (numpy) format.

[`numpy.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html)

Load array from the  `.npy`  files.

[`numpy.random.random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html)

Return random floats values from the interval [0.0, 1.0), in a specified shape.

[`numpy.random.randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html)

Return random integers from the half-open interval [a, b), in a specified shape.

[`numpy.random.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)

Return random samples from a Gaussian (normal) distribution.

[`numpy.random.permutation`](https://numpy.org/devdocs/reference/random/generated/numpy.random.permutation.html)

Return a randomly permuted sequence from the given list

[`numpy.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)  
[`numpy.ndarray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape)

Returns an array containing the same elements with a new shape, without affecting the the original array.




### Category: Array Creation

**Function/Method**

**Description**

[`numpy.ones`](https://numpy.org/devdocs/reference/generated/numpy.ones.html)

Return a new array of given shape and type, filled with 1s.

[`numpy.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros)

Return a new array of given shape and type, filled with 0s.

[`numpy.full`](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full)

Return a new array of given shape and type, filled with a specific value.

[`numpy.eye`](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy-eye)

Return a 2-D array with 1s on the diagonal and 0s elsewhere.

[`numpy.diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html)

Extract the diagonal elements.

[`numpy.unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html)

Return the sorted unique elements of an array.

[`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

Create an n-dimensional array.

[`numpy.arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)

Return evenly spaced values within a given half-open interval [a, b).

[`numpy.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace)

Return evenly spaced numbers over a specified interval [a,b].

[`numpy.ndarray.copy`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.copy.html)

Returns a copy of the array.




### Category: Operating with Elements and Indices

**Function/Method**

**Description**

[`numpy.insert`](https://numpy.org/doc/stable/reference/generated/numpy.insert.html)

Insert values along the given axis before the specified indices.

[`numpy.delete`](https://numpy.org/doc/stable/reference/generated/numpy.delete.html)

Return a new array, after deleting sub-arrays along a specified axis.

[`numpy.append`](https://numpy.org/doc/stable/reference/generated/numpy.append.html)

Append values at the end of the specified array.

[`numpy.hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html)

Return a stacked array formed by stacking the given arrays in sequence horizontally (column-wise).

[`numpy.vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html)

Return a stacked array formed by stacking the given arrays, will be at least 2-D, in sequence vertically (row-wise).

[`numpy.sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)

Return a sorted copy of an array.

[`numpy.ndarray.sort`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.sort.html#numpy-ndarray-sort)

Sort an array in-place.




### Category: Set Operations

**Function/Method**

**Description**

[`numpy.intersect1d`](https://numpy.org/doc/stable/reference/generated/numpy.intersect1d.html#numpy-intersect1d)

Find the intersection of two arrays.

[`numpy.setdiff1d`](https://numpy.org/doc/stable/reference/generated/numpy.setdiff1d.html#numpy-setdiff1d)

Find the set difference of two arrays.

[`numpy.union1d`](https://numpy.org/doc/stable/reference/generated/numpy.union1d.html)

Return the unique, sorted array of values that are in either of the two input arrays.




### Category: Arithmetic and Statistical Operations

**Function/Method**

**Description**

[`numpy.add`](https://numpy.org/doc/stable/reference/generated/numpy.add.html)

Element-wise add given arrays

[`numpy.subtract`](https://numpy.org/doc/stable/reference/generated/numpy.subtract.html)

Subtract arguments of given arrays, element-wise.

[`numpy.multiply`](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html)

Multiply arguments of given arrays, element-wise.

[`numpy.divide`](https://numpy.org/doc/stable/reference/generated/numpy.divide.html)

Returns a true division of the inputs, element-wise.

[`numpy.exp`](https://numpy.org/doc/stable/reference/generated/numpy.exp.html)

Calculate the exponential of all elements in the input array.

[`numpy.power`](https://numpy.org/doc/stable/reference/generated/numpy.power.html)

First array elements raised to powers from second array, element-wise.

[`numpy.sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html)

Return the non-negative square-root of an array, element-wise.

[`numpy.ndarray.min`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html)

Return the minimum along the specified axis.

[`numpy.ndarray.max`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html)

Return the maximum along a given axis.

[`numpy.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)  
[`numpy.ndarray.mean`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mean.html#:~:text=method%20ndarray.,mean%20for%20full%20documentation.)

Compute the arithmetic mean along the specified axis.

[`numpy.median`](https://numpy.org/doc/stable/reference/generated/numpy.median.html)

Compute the median along the specified axis.