> 2021-05-13
> From Udacity, AI Programming with Python Nanodegree Program
> For the perpose of personal study memo
> Written with [StackEdit](https://stackedit.io/).

# Data Visualization: Univariate Plot

## Overview
1. Create **bar charts** for **qual**itativevariables, for example, the amount (number) of eggs consumed in a meal (categories: {breakfast, lunch, or dinner}). In general, bar chart maps categories to numbers.
2. Create Pie charts. A **pie chart** is a common univariate plot type that is used to depict  _relative_  **frequencies** for levels of a categorical variable. A pie chart is preferably used when the number of categories is less, and you'd like to see the  _proportion_  of each category.
3.  Create **histogram**s for **quant**itative variables. A histogram splits the (tabular) data into evenly sized intervals and displays the count of rows in each interval with bars. A histogram is similar to a bar chart, except that the "category" here is a range of values.
4.  Analyze the bar charts and histograms.


## Terms
- **tidy** format
	- In short, a tidy dataset is a **tabular** dataset where:
		- each variable is a column
		- each observation is a row
		- each type of observational unit is a table
		![An image of two tables (patients and treatments) with each table highlighted](https://video.udacity-data.com/topher/2018/January/5a6278ec_tidy-data-three/tidy-data-three.png)
		e.g. for non-tidy format ![A non-tidy representation of the patients and treatments table. Each variable does not form a column and one table exists for two observational units.](https://video.udacity-data.com/topher/2018/January/5a6278e7_tidy-data-four/tidy-data-four.png)

- **Data Wrangling**
	- Reshaping data or performing transformations to split or combine features in your data, resulting in new data columns. These operations collectively are called _data-wrangling_.
	- [Data Wrangling with pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

- Univariate Visualization
	- Visualizations of single variables
- Bivariate
- Discrete Variable ( ↔ Continous variable )
	- How to plot a discrete quantitative variable ?
		- https://statisticsbyjim.com/basics/data-types/

## Qualitative Variables


- e.g. categorical variables


- **Bar Chart**
	- depicting the distribution of a categorical variable
	- for **Sorted Nominal** Data
		- e.g. sorting data in terms of frequency
	- for **Ordinal** Data
		- keep the **inderent order of the levels**, more important to convey
	- Usual: Vertical Orientation
		- X indicates Category and Y indicates Frequency
	- Horizontal Orientation is good to use when:
		- e.g. category names are long.
	 * [`CategoricalDtype`](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.api.types.CategoricalDtype.html)


- Relative Frequency
	- The proportion of the data that falls each category 
	- Relative Frequency (e.g. portion) ↔ Absolute Frequency (e.g. count)


- Pie Chart
	- a common univariate plot type for when to depict **relative frequencies** for level of a  categorical variable.
	- lesser ( 2~3 slices ) is better
		- 4~5 slices : OK when wedge sizes can be distinguished 
	- Plot the data systematically
		- Typical Method:
			- **Clockwise** from most to least
			- Start at **12 o'clock**: divide line, pointing 12 o'clock
				-  e.g. 3 categories: 2 on top of each side, and the last at the bootom )
	- Donut Chart
		- Aesthetic difference and purpose.
		- [Wedge patches](https://matplotlib.org/api/_as_gen/matplotlib.patches.Wedge.html)
	- Square Pie ( **Waffle** ) Charts
		- [_square pie_  or  _waffle charts_](https://eagereyes.org/techniques/square-pie-charts)
	- [**_What to Consider when Creating a Pie Chart_**](https://academy.datawrapper.de/article/127-what-to-consider-when-creating-a-pie-chart)


## Quantitative Variables


- e.g. numeric values
- bin size & boundary point


- **Histogram**
	- to plot the distribution of a numeric variable
		- grouped into continuous bins
		- one bar for each bin is plotted to depict the number
	- kernel density estimate (KDE)


## Figures, Axes, and Subplots

> 
> Since we don't have a Figure area to plot inside, Python first creates a Figure object. And since the Figure doesn't start with any Axes to draw the histogram onto, an Axes object is created inside the Figure. Finally, the histogram is drawn within that Axes.
> ![](https://video.udacity-data.com/topher/2018/August/5b804b9b_l3-c09b-subplotsa/l3-c09b-subplotsa.png)
>
> This hierarchy of objects is useful to know about so that we can take more control over the layout and aesthetics of our plots.
>
>> `fig = plt.figure()`
>> axes_object : `ax = fig.add_axes([.2, .2, .8, .8])`
>>> **matplotlib**, _axes_object_.hist(...) : 
>>> `ax.hist(data=data, x='num_val')`
>>> **seaborn**: sns.counterplot(... ax = _axes_object_) : 
>>>`sb.counterplot(data=data, x ='cat_var', ax=ax)`

- How to create a gird of sub-plots
	```
	fig, axes = plt.subplots(3, 4) # grid of 3x4 subplots
	axes = axes.flatten() # reshape from 3x4 array into 12-element vector
	for i in range(12):
	    plt.sca(axes[i]) # set the current Axes
	    plt.text(0.5, 0.5, i+1) # print conventional subplot index number to middle of Axes
    ```
## Extra


### Descriptive Statistics, Outliers, and Axis Limits


- Set a limit of an axis to take a close look at the **_underlying patterns_** of data


### Scales and Transformations

#### Log-normal Distribution example
> Certain data distributions will find themselves amenable to scale transformations. The most common example of this is data that follows an approximately [log-normal](https://en.wikipedia.org/wiki/Log-normal_distribution) distribution. This is data that, in their natural units, can look highly skewed: lots of points with low values, with a very long tail of data points with large values. However, after applying a logarithmic transform to the data, the data will follow a normal distribution. (If you need a refresher on the logarithm function, check out [this lesson on Khan Academy](https://www.khanacademy.org/math/algebra2/exponential-and-logarithmic-functions).)
>
> _Source from Udacity_

- Example of a variable requiring a different scale: Finance
	- tendency to have a **range** that **crosses many orders of magnitude**
	- usaually **right skewed**

1. Linear Scale
	- arithmetic differences
2. from Linear Scale to Logarithmic Scale
	- multiplicative differences
	> All the values in a variable must be positive in order to use log-transform.
3. Axis Transformations
	- e.g. from price to LOG10(price)
	- useful because allowing interpreting data with naturally recording units
	- same picture as the orgininal data

> [examples of places where log-normal distributions have been observed](https://en.wikipedia.org/wiki/Log-normal_distribution#Occurrence_and_applications)

### Plotting univariate visualizations with Pandas
- https://www.kaggle.com/residentmario/univariate-plotting-with-pandas

### Kernel Density Estimation ( KDE )
- Kernel density estimation is one way of estimating the probability density function of a variable. In a KDE plot, you can think of each observation as replaced by a small ‘lump’ of area. Stacking these lumps all together produces the final density curve. The default settings use a normal-distribution kernel, but most software that can produce KDE plots also include other kernel function options.
- `seaborn`
	1.  sns.[`displot()`](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot)  - A figure-level function with similar flexibility.
	2. sns.[`histplot()`](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot)  - An axes-level function for histograms.
	3. sns.[`kdeplot()`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) 
	4. sns.[`rugplot()`](https://seaborn.pydata.org/generated/seaborn.rugplot.html)


> **REVISIT**
> -   **Univariate visualizations**: Visualize single-variables, such as bar charts, histograms, and line charts.
> -   **Bivariate visualizations**: Plots representing the relationship between two variables measured on the given sample data. These plots help to identify the relationship pattern between the two variables.
> -   **Ordinal data**: It is a categorical data type where the variables have natural and ordered categories. The distances between the categories are unknown, such as the survey options presented on a five-point scale.

