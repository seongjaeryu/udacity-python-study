> 2021-05-17
> From Udacity, AI Programming with Python Nanodegree Program
> Written with [StackEdit](https://stackedit.io/).


# Bivariate Visualization
Visualizations of two variables.

## Scatterplots for Quantitative variable vs. Quantitative variable


- Scatterplot observation -> data results in a cloud of points
- Pearson Correlation Coefficient
	- Statistic quantifying the strength of linear correlation between two numeric variables
	- r : -1 ~ 1. Closer to the Zero means a weaker relationship. Opposite means a stronger relataionship.
- Scale Tranforamtion
	- It can be useful to change a non-linear trend in the natural units into a linear trend in the transformed units.
	- e.g. shape of log(y) and x relationship in a regression approach
		- log(y) = b0 + b1x

- Overplotting
	- Where a plot is created with too many overlapping points
	- e.g. undetailed blob or discrete in nature
	- resolve with:
		- Sampling
			- e.g. random selection
		- Transparency
		- Jitter
			- Jittering adds a small amount of random noise to the position of each point

- Heat Maps
	- 2-D histogram.
	- Good for discrete variable vs. discrete variable
	- Good alternative to transparancy for a lot of data
	- Bin sizes are important !!
```
plt.hist2d(data = fuel_econ, x = 'displ', y = 'comb', cmin=0.5, cmap='viridis_r')
# cmin=0.5 means that a cell will only get colored if it contains at least one point
```

- 


## Violin Plots for Quantitative variable vs.  Qualitative variable

- Violini plots are on the lower level of abstraction.
- For each level of the categorical variable, a distribution of the values on the numeric variable is plotted.
- The distribution is plotted as a kernel density estimate, something like a smoothed histogram.


- Box Plot
	- Compared to the violin plot, the box plot leans more on the summarization of the data, primarily just reporting a set of descriptive statistics for the numeric values on each categorical level.
	- A set of Descriptive Statistics :
		- Min ( Q0 )
		- Q1
		- Median ( Q2 )
		- Q3
		- Max ( Q4 )
		- Whikser Bound
			- IQR: interquartile range
			- IQR = Q3 - Q1
			- Upper Whikser Bound example
				- Q3 + 1.5 * IQR

> Typically, a maximum range is set on whisker length; by default, this is 1.5 times the IQR. For the Gamma level, there are points below the lower whisker that indicate **individual outlier points** that are more than 1.5 times the IQR below the first quartile.

> On the other hand, the box plot lacks as nuanced a depiction of distributions as the violin plot: you can't see the slight bimodality present in the Alpha level values. The violin plot may be a better option for exploration, especially since seaborn's implementation also includes the box plot by default.


## Clustered Bar Charts for Qualitative variable vs. Quantitative variable

> In a clustered bar chart, bars are organized into clusters based on levels of the first variable, and then bars are ordered consistently across the second variable within each cluster.

```
# Sample Code
fuel_econ_ft_mask = fuel_econ['fuelType'].isin(['Premium Gasoline', 'Regular Gasoline'])
sedan_classes = ['Minicompact Cars', 'Subcompact Cars', 'Compact Cars', 'Midsize Cars', 'Large Cars']
vclasses = pd.api.types.CategoricalDtype(ordered=True, categories=sedan_classes)
fuel_econ['VClass'] = fuel_econ['VClass'].astype(vclasses)
sns.countplot(data = fuel_econ[fuel_econ_ft_mask], x = 'VClass', hue = 'fuelType');
```

## Faceting

> One general visualization technique that will be useful for you to know about to handle plots of two or more variables is **faceting**. In faceting, the data is divided into disjoint subsets, most often by different levels of a categorical variable. For each of these subsets of the data, the same plot type is rendered on other variables. Faceting is a way of comparing distributions or relationships across levels of additional variables, especially when there are three or more variables of interest overall. While faceting is most useful in multivariate visualization, it is still valuable to introduce the technique here in our discussion of bivariate plots.

> For example, rather than depicting the relationship between one numeric variable and one categorical variable using a violin plot or box plot, we could use faceting to look at a histogram of the numeric variable for subsets of the data divided by categorical variable levels. Seaborn's [FacetGrid](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html) class facilitates the creation of faceted plots. There are two steps involved in creating a faceted plot. First, we need to create an instance of the FacetGrid object and specify the feature we want to facet by (_vehicle class, "VClass" in our example_). Then we use the `map` method on the FacetGrid object to specify the plot type and variable(s) that will be plotted in each subset (_in this case, the histogram on combined fuel efficiency "comb"_).

## Adapted Bar Charts

> Histograms and bar charts were introduced in the previous lesson as depicting the distribution of numeric and categorical variables, respectively, with the height (or length) of bars indicating the number of data points that fell within each bar's range of values. These plots can be adapted for use as bivariate plots by, instead of indicating count by height, indicating a mean or other statistic on a second variable.

> For example, we could plot a numeric variable against a categorical variable by adapting a bar chart so that its bar heights indicate the mean of the numeric variable. This is the purpose of seaborn's  [`barplot`](https://seaborn.pydata.org/generated/seaborn.barplot.html)  function:

## Line Plots

> The  **line plot**  is a fairly common plot type that is used to plot the trend of one numeric variable against values of a second variable. In contrast to a scatterplot, where all data points are plotted, in a line plot, only one point is plotted for every unique x-value or bin of x-values (like a histogram). If there are multiple observations in an x-bin, then the y-value of the point plotted in the line plot will be a summary statistic (like mean or median) of the data in the bin. The plotted points are connected with a line that emphasizes the sequential or connected nature of the x-values.
>
> If the x-variable represents time, then a line plot of the data is frequently known as a  **time series**  plot. For example, we have only one observation per time period, like in stock or currency charts.
>
> We will make use of Matplotlib's  [errorbar()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.errorbar.html)  function, performing some processing on the data in order to get it into its necessary form.

```
fuel_econ['displ'].describe()
```
```
# Set a number of bins into which the data will be grouped.
# Set bin edges, and compute center of each bin 
bin_edges = np.arange(0.6, 7+0.2, 0.2)
bin_centers = bin_edges[:-1] + 0.2 / 2

# Cut the bin values into discrete intervals. Returns a Series object.
displ_binned = pd.cut(fuel_econ['displ'], bin_edges, include_lowest = True)
displ_binned
```
```
# For the points in each bin, we compute the mean and standard error of the mean.
comb_mean = fuel_econ['comb'].groupby(displ_binned).mean()
comb_std = fuel_econ['comb'].groupby(displ_binned).std()

# Plot the summarized data
plt.errorbar(x=bin_centers, y=comb_mean, yerr=comb_std)
plt.xticks(rotation=15);
plt.ylabel('Avg. Combined Fuel Efficiency (mpg)');
```

 - Documentation: Refer to the [cut()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html) function syntax.

- Instead of computing summary statistics on fixed bins, you can also make computations on a rolling window through use of pandas' [`rolling`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rolling.html) method. Since the rolling window will make computations on sequential rows of the dataframe, we should use [`sort_values`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html) to put the x-values in ascending order first.
	- **Note about the DataFrame object used in the examples below**

		> The visualizations below are based on a synthetic dataframe object `df`, and show the plots based on its numeric (quantitative) variables, `num_var1`, `num_var2`, and a categorical (qualitative) variable, `cat_var`. **The new dataframe has been chosen to reflect the additional relationship between the selected variables.**

		```
		# compute statistics in a rolling window
		df_window = df.sort_values('num_var1').rolling(15)
		x_winmean = df_window.mean()['num_var1']
		y_median = df_window.median()['num_var2']
		y_q1 = df_window.quantile(.25)['num_var2']
		y_q3 = df_window.quantile(.75)['num_var2']

		# plot the summarized data
		base_color = sb.color_palette()[0]
		line_color = sb.color_palette('dark')[0]
		plt.scatter(data = df, x = 'num_var1', y = 'num_var2')
		plt.errorbar(x = x_winmean, y = y_median, c = line_color)
		plt.errorbar(x = x_winmean, y = y_q1, c = line_color, linestyle = '--')
		plt.errorbar(x = x_winmean, y = y_q3, c = line_color, linestyle = '--')

		plt.xlabel('num_var1')
		plt.ylabel('num_var2')
		```


> Another bivariate application of line plots is to plot the distribution of a numeric variable for different levels of a categorical variable. This is another alternative to using violin plots, box plots, and faceted histograms. With the line plot, one line is plotted for each category level, like overlapping the histograms on top of one another. This can be accomplished through multiple `errorbar` calls using the methods above, or by performing multiple [`hist`](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html) calls, setting the `histtype = step` parameter so that the bars are depicted as unfilled lines.

```
bin_edges = np.arange(-3, df['num_var'].max()+1/3, 1/3)
g = sb.FacetGrid(data = df, hue = 'cat_var', size = 5)
g.map(plt.hist, "num_var", bins = bin_edges, histtype = 'step')
g.add_legend()
```
> Mike Yi:
> unctions you provide to the `map` method of FacetGrid objects do not need to be built-ins. Below, I've written a function to perform the summarization operations seen above to plot an `errorbar` line for each level of the categorical variable, then fed that function (`freq_poly`) to `map`.
```
def freq_poly(x, bins = 10, **kwargs):
    """ Custom frequency polygon / line plot code. """
    # set bin edges if none or int specified
    if type(bins) == int:
        bins = np.linspace(x.min(), x.max(), bins+1)
    bin_centers = (bin_edges[1:] + bin_edges[:-1]) / 2

    # compute counts
    data_bins = pd.cut(x, bins, right = False,
                       include_lowest = True)
    counts = x.groupby(data_bins).count()

    # create plot
    plt.errorbar(x = bin_centers, y = counts, **kwargs)

bin_edges = np.arange(-3, df['num_var'].max()+1/3, 1/3)
g = sb.FacetGrid(data = df, hue = 'cat_var', size = 5)
g.map(freq_poly, "num_var", bins = bin_edges)
g.add_legend()
```

- Example of FacetGrid
	```
	group_mask = fuel_econ.groupby(['make']).count()['id'] > 80
	group_mean = fuel_econ[['make', 'comb']].groupby(['make']).mean()[group_mask]
	group_order = group_mean.sort_values(['comb'], ascending = False).index
	g = sns.FacetGrid(data = fuel_econ, col = 'make', col_wrap = 6, col_order = group_order)
	g.map(plt.hist, 'comb');
	```

- Example of Barplot ( horizontal )
	```
	group_mask = fuel_econ.groupby(['make']).count()['id'] > 80
	group_mean = fuel_econ[['make', 'comb']].groupby(['make']).mean()[group_mask]
	group_order = group_mean.sort_values(['comb'], ascending = False).index

	sns.barplot(data = fuel_econ, y = 'make', x = 'comb',
	            order = group_order, color = sns.color_palette()[0], ci = 'sd')

	plt.xlabel('Avg. Combined Fuel Efficiency (mpg)');
	```

- Sample
	- https://matplotlib.org/stable/tutorials/introductory/sample_plots.html
	- https://seaborn.pydata.org/examples/index.html

# Glossary from Uadacity Class

Below is a list of functions from both Matplotlib and Seaborn, that you have learned in this lesson. Observe the tables below carefully, and recall the examples that you have practiced so far. This will help you understand the difference between the utility of Matplotlib and Seaborn packages.

## Univariate Visualization Functions

Plot type

matplotlib.pyplot function

seaborn function

**Bar Chart**

---

[countplot()](https://seaborn.pydata.org/generated/seaborn.countplot.html)  
[barplot()](https://seaborn.pydata.org/generated/seaborn.barplot.html)

**Pie Chart**

[pie()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html)

---

**Histogram**

[hist()](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.hist.html)

[distplot()](https://seaborn.pydata.org/generated/seaborn.distplot.html)  
[displot()](https://seaborn.pydata.org/generated/seaborn.displot.html#seaborn.displot)  
[histplot()](https://seaborn.pydata.org/generated/seaborn.histplot.html#seaborn.histplot)

## Bivariate Visualization Functions

Plot type

matplotlib.pyplot function

seaborn function

**Scatterplot**

[scatter()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html)

[regplot()](https://seaborn.pydata.org/generated/seaborn.regplot.html)

**Heat Map**

[hist2d()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist2d.html)

[heatmap()](https://seaborn.pydata.org/generated/seaborn.heatmap.html)

**Violin Plot**

---

[violinplot()](https://seaborn.pydata.org/generated/seaborn.violinplot.html)

**Box Plot**

---

[boxplot()](https://seaborn.pydata.org/generated/seaborn.boxplot.html)

**Clustered Bar Chart**

---

[countplot()](https://seaborn.pydata.org/generated/seaborn.countplot.html)  
[heatmap()](https://seaborn.pydata.org/generated/seaborn.heatmap.html)

**Faceting**

---

[FacetGrid()](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)

**Bar Plot**

---

[barplot()](https://seaborn.pydata.org/generated/seaborn.barplot.html)

**Point Plot**

---

[pointplot()](https://seaborn.pydata.org/generated/seaborn.pointplot.html)

**Line Plot**

[errorbar()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.errorbar.html)

---

## Other useful functions

Utility

matplotlib.pyplot function

**Subplots**

[subplot()](https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.subplot.html)

**Figure**

[figure()](https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.figure.html)

**Axes**

[Axes()](https://matplotlib.org/api/axes_api.html#the-axes-class)

**Get current axes**

[gca()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gca.html)

**Set current axes**

[sca()](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.sca.html?highlight=sca)

## Comprehensive List of Plots

See the comprehensive list of visualization functions.

1.  [matplotlob.pyplot functions](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html)
2.  [seaborn functions](https://seaborn.pydata.org/api.html)





# Extra

## Multivariate Visualization

- Using Color for Third Variables
	> The `violinplot`, `boxplot`, and `barplot` functions can all be made with third-variable clusters by adding a "hue" parameter. Code for heat maps can be adapted to depict third variables rather than counts, just by changing the "weights" parameter for `hist2d`, or the aggregation functions for your data to be fed into `heatmap`.

```
plt.scatter(data = df, x = 'num_var1', y = 'num_var2', c = 'num_var3')
plt.colorbar()
```
![](https://video.udacity-data.com/topher/2018/March/5abbe123_l5-c03-color2/l5-c03-color2.png)

```
g = sb.FacetGrid(data = df, hue = 'cat_var1', size = 5)
g.map(plt.scatter, 'num_var1', 'num_var2')
g.add_legend()
```
![](https://video.udacity-data.com/topher/2018/March/5abbc9e1_l5-c03-color1/l5-c03-color1.png)

- Types of Color Palettes
	> **Qualitative palettes** are built for nominal-type data. This is the palette class taken by the default palette. In a qualitative palette, consecutive color values are distinct so that there is no inherent ordering of levels implied. Colors in a good qualitative palette should also try and avoid drastic changes in brightness and saturation that would cause a reader to interpret one category as being more important than the others - unless that emphasis is deliberate and purposeful.
	![](https://video.udacity-data.com/topher/2018/March/5abbe740_l5-c03-color3/l5-c03-color3.png)
	
	> For other types of data (ordinal and numeric), a choice may need to be made between a sequential scale and a diverging scale. In a **sequential palette**, consecutive color values should follow each other systematically. Typically, this follows a light-to-dark trend across a single or small range of hues, where light colors indicate low values and dark colors indicate high values. The default sequential color map, "viridis", takes the opposite approach, with dark colors indicating low values, and light values indicating high. 
	![](https://video.udacity-data.com/topher/2018/March/5abbf5e5_l5-c03-color4/l5-c03-color4.png)

	> Most of the time, a sequential palette will depict ordinal or numeric data just fine. However, if there is a meaningful zero or center value for the variable, you may want to consider using a **diverging palette**. In a diverging palette, two sequential palettes with different hues are put back to back, with a common color (usually white or gray) connecting them. One hue indicates values greater than the center point, while the other indicates values smaller than the center.
	![](https://video.udacity-data.com/topher/2018/March/5abbf873_l5-c03-color5/l5-c03-color5.png)


- https://stackoverflow.com/questions/20144529/shifted-colorbar-matplotlib

- Faceting Across Two Variables
	> Earlier in the lesson, you saw how  **FacetGrid**  could be used to subset your dataset across levels of a categorical variable, and then create one plot for each subset. Where the faceted plots demonstrated were univariate before, you can actually use any plot type, allowing you to facet bivariate plots to create a multivariate visualization.

	> **FacetGrid**  also allows for faceting a variable not just by columns, but also by rows. We can set one categorical variable on each of the two facet axes for one additional method of depicting multivariate trends.
	```
	g = sb.FacetGrid(data = df, col = 'cat_var2', row = 'cat_var1', size = 2.5,
	                 margin_titles = True)
	g.map(plt.scatter, 'num_var1', 'num_var2')
	```
	![](https://video.udacity-data.com/topher/2018/March/5abc3ac4_l5-c05-faceting2/l5-c05-faceting2.png)

	> Setting `margin_titles = True` means that instead of each facet being labeled with the combination of row and column variable, labels are placed separately on the top and right margins of the facet grid. This is a boon, since the default plot titles are usually too long.


## Swarm Plots

```
plt.figure(figsize = [12, 5])
base_color = sb.color_palette()[0]

# left plot: violin plot
plt.subplot(1, 3, 1)
ax1 = sb.violinplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)

# center plot: box plot
plt.subplot(1, 3, 2)
sb.boxplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)
plt.ylim(ax1.get_ylim()) # set y-axis limits to be same as left plot

# right plot: swarm plot
plt.subplot(1, 3, 3)
sb.swarmplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)
plt.ylim(ax1.get_ylim()) # set y-axis limits to be same as left plot
```

![](https://video.udacity-data.com/topher/2018/March/5ab55333_l4-c18-swarmplot1/l4-c18-swarmplot1.png)

- It is only reasonable to use a swarm plot if we have a **small** or moderate **amount of data**. If we have too many points, then the restrictions against overlap will cause too much distortion or require a lot of space to plot the data comfortably.



## Rug and Strip Plots

- Rug Plot
	> You might encounter, or be interested in, marginal distributions that are plotted alongside bivariate plots such as scatterplots. A marginal distribution is simply the univariate distribution of a variable, ignoring the values of any other variable. For quantitative data, histograms or density curves are fine choices for marginal plot, but you might also see the **rug plot** employed. In a rug plot, all of the data points are plotted on a single axis, one tick mark or line for each one. Compared to a marginal histogram, the rug plot suffers somewhat in terms of readability of the distribution, but it is more compact in its representation of the data.

	```
	g = sb.JointGrid(data = df, x = 'num_var1', y = 'num_var2')
	g.plot_joint(plt.scatter)
	g.plot_marginals(sb.rugplot, height = 0.25)
	```

	![](https://video.udacity-data.com/topher/2018/March/5ab58c38_l4-c17-rugplot1/l4-c17-rugplot1.png)

- Strip Plot

	> Another supporting plot type similar to the rug plot is the **strip plot**. It's like a swarm plot (see the previous page) but without any dodging or jittering to keep points separate or off the categorical line. You can also think of it as a rug plot faceted by categorical levels. You can use seaborn's [`swarmplot`](https://seaborn.pydata.org/generated/seaborn.swarmplot.html) function to add a swarm plot to any other plot. The `inner = "stick"` and `inner = "point"` options can also be used with the `violinplot` function to include a swarm plot inside of the violin areas, instead of a box plot.

	```
	plt.figure(figsize = [10, 5])
	base_color = sb.color_palette()[0]

	# left plot: strip plot
	plt.subplot(1, 2, 1)
	ax1 = sb.stripplot(data = df, x = 'num_var', y = 'cat_var',
	                   color = base_color)

	# right plot: violin plot with inner strip plot as lines
	plt.subplot(1, 2, 2)
	sb.violinplot(data = df, x = 'num_var', y = 'cat_var', color = base_color,
	             inner = 'stick')
	```

	![](https://video.udacity-data.com/topher/2018/March/5ab9416a_l4-c17-rugplot2/l4-c17-rugplot2.png)

## Stacked Plot

> The most basic stacked chart takes a single bar representing the full count, and divides it into colored segments based on frequencies on a categorical variable.

> Given this similarity, cautions regarding use of the stacked bar are fairly similar to that of the pie chart:
>
> -   Make sure that relative frequencies are a meaningful comparison.
> -   Try to limit yourself to a small number of categories, up to about five.
> -   Make sure that categories are arranged in a sensible order, e.g. by frequency for nominal data or by levels for ordinal data.

- e.g. plotting by absolute frequency and plotting by relative frequency
	
	```
	cat1_order = ['East', 'South', 'West', 'North']
	cat2_order = ['Type X', 'Type Y', 'Type Z', 'Type O']

	plt.figure(figsize = [12, 5])

	# left plot: clustered bar chart, absolute counts
	plt.subplot(1, 2, 1)
	sb.countplot(data = df, x = 'cat_var1', hue = 'cat_var2',
	             order = cat1_order, hue_order = cat2_order)
	plt.legend()

	# right plot: stacked bar chart, absolute counts
	plt.subplot(1, 2, 2)

	baselines = np.zeros(len(cat1_order))
	# for each second-variable category:
	for i in range(len(cat2_order)):
	    # isolate the counts of the first category,
	    cat2 = cat2_order[i]
	    inner_counts = df[df['cat_var2'] == cat2]['cat_var1'].value_counts()
	    # then plot those counts on top of the accumulated baseline
	    plt.bar(x = np.arange(len(cat1_order)), height = inner_counts[cat1_order],
	            bottom = baselines)
	    baselines += inner_counts[cat1_order]

	plt.xticks(np.arange(len(cat1_order)), cat1_order)
	plt.legend(cat2_order)
	```

	![](https://video.udacity-data.com/topher/2018/November/5be095c0_l4-c19-stackedbars2/l4-c19-stackedbars2.png)

- -   Eager Eyes:  [Stacked Bars are the Worst](https://eagereyes.org/techniques/stacked-bars-are-the-worst)
