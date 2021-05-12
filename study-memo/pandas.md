# UDACITY, Introduction to Python
##### Markdown Editor: https://stackedit.io/
##### Mini Project: [Statistics from Stock Data.ipynb](https://github.com/udacity/AIPND/blob/master/Pandas%20Mini-Project/Statistics%20from%20Stock%20Data.ipynb)


### Category: Initialization and Utility

[`Function/Method`]

[`Description`]

[`pandas.read_csv(relative_path_to_file)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html?highlight=read_csv)

Reads a comma-separated values (csv) file present at relative_path_to_file and loads it as a DataFrame

[`pandas.DataFrame(data)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame)

Returns a 2-D heterogeneous tabular data. Note: There are other optional arguments as well that you can use to create a dataframe.

[`pandas.Series(data, index)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series)

Returns 1-D ndarray with axis labels

[`pandas.Series.shape`]

[`pandas.DataFrame.shape`]

Returns a tuple representing the dimensions

[`pandas.Series.ndim`]

[`pandas.DataFrame.ndim`]

Returns the number of the dimensions (rank). It will return 1 in case of a Series

[`pandas.Series.size`]

[`pandas.DataFrame.size`]

Returns the number of elements

[`pandas.Series.values`]

Returns the data available in the Series

[`pandas.Series.index`]

Returns the indexes available in the Series

[`pandas.DataFrame.isnull()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isnull.html#pandas.DataFrame.isnull)

Returns a same sized object having True for NaN elements and False otherwise.

[`pandas.DataFrame.count(axis)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.count.html#pandas.DataFrame.count)

Returns the count of non-NaN values along the given axis. If axis=0, it will count down the dataframe, meaning column-wise count of non-NaN values.

[`pandas.DataFrame.head([n])`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head)

Return the first _n_ rows from the dataframe. By default, n=5.

[`pandas.DataFrame.tail([n])`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail)

Return the last _n_ rows from the dataframe. By default, n=5. Supports negative indexing as well.

[`pandas.DataFrame.describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe)

Generate the descriptive statistics, such as, count, mean, std deviation, min, and max.

[`pandas.DataFrame.min()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.min.html#pandas.DataFrame.min)

Returns the minimum of the values along the given axis.

[`pandas.DataFrame.max()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.max.html#pandas.DataFrame.max)

Returns the maximum of the values along the given axis.

[`pandas.DataFrame. mean()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html#pandas.DataFrame.mean)

Returns the mean of the values along the given axis.

[`pandas.DataFrame.corr()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr)

Compute pairwise correlation of columns, excluding NA/null values.

[`pandas.DataFrame.rolling(windows)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html?highlight=dataframe%20rolling#pandas.DataFrame.rolling)

Provide rolling window calculation, such as pandas.DataFrame.rolling(15).mean() for rolling mean over window size of 15.

[`pandas.DataFrame.loc[label]`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc)

Access a group of rows and columns by label(s)

[`pandas.DataFrame.groupby(mapping_function)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby)

Groups the dataframe using a given mapper function or or by a Series of columns.




### Category: Manipulation

[`Function/Method`]

[`Description`]

[`pandas.Series.drop(index)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.drop.html#pandas.Series.drop)

Drops the element positioned at the given index(es)

[`pandas.DataFrame.drop(labels)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop)

Drop specified labels (entire columns or rows) from the dataframe.

[`pandas.DataFrame.pop(item)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pop.html#pandas.DataFrame.pop)

Return the item and drop it from the frame. If not found, then raise a KeyError.

[`pandas.DataFrame.insert(location, column, values)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.insert.html#pandas.DataFrame.insert)

Insert column having given values into DataFrame at specified location.

[`pandas.DataFrame.rename(dictionary-like)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename)

Rename label(s) (columns or row-indexes) as mentioned in the dictionary-like

[`pandas.DataFrame.set_index(keys)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index)

Set the DataFrame's row-indexes using existing column-values.

[`pandas.DataFrame.dropna(axis)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna)

Remove rows (if axis=0) or columns (if axis=1) that contain missing values.

[`pandas.DataFrame.fillna(value, method, axis)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna)

Replace NaN values with the specified value along the given axis, and using the given method (‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None)

[`pandas.DataFrame.interpolate(method, axis)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate)

Replace the NaN values with the estimated value calculated using the given method along the given axis.