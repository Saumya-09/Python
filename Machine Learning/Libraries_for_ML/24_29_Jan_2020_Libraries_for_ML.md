# Pandas
### DataFrame
Pandas DataFrame is a data structure that holds data in two dimensions- as rows and columns. We have the following syntax-

> pandas.DataFrame(data, index, columns, dtype, copy)

Example-

```python
import pandas as pd
data={'Element':['Silver','Gold','Platinum','Copper'],'Atomic Number':[47,79,78,29]}
frame=pd.DataFrame(data,index=['element 1','element 2','element 3','element 4'])
frame
```
##### Output:
[![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2018/07/dataframe.png)](http://https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2018/07/dataframe.png)

### b. Panel
Pandas panel holds data in three dimensions. Etymologically, the term panel data from one source for the name pandas. A panel has the following syntax:

> pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)

```python
data={'Red':pd.DataFrame(np.random.randn(4,2)), 'Blue':pd.DataFrame(np.random.randn(4,3))}
pd.Panel(data)
```

class ‘pandas.core.panel.Panel’
Dimensions: 2 (items) x 4 (major_axis) x 3 (minor_axis)
Items axis: Blue to Red
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 2

#### Series
Pandas Series holds data in one dimension, in a labeled format. The index is the set of axis labels we use.
It has the following syntax-

> pandas.Series(data, index, dtype, copy)

Example-

```python
data=np.array([1,2,3,3,4])
pd.Series(data)
```
##### Output:
0 1
1 2
2 3
3 3
4 4
dtype: int32

# Numpy

#### numpy.amin() and numpy.amax()
These functions return the minimum and the maximum from the elements in the given array along the specified axis.

Example
```python
import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 

print 'Our array is:' 
print a  
print '\n'  

print 'Applying amin() function:' 
print np.amin(a,1) 
print '\n'  

print 'Applying amin() function again:' 
print np.amin(a,0) 
print '\n'  

print 'Applying amax() function:' 
print np.amax(a) 
print '\n'  

print 'Applying amax() function again:' 
print np.amax(a, axis = 0)
It will produce the following output −

Output:

Our array is:
[[3 7 5]
[8 4 3]
[2 4 9]]

Applying amin() function:
[3 3 2]

Applying amin() function again:
[2 4 3]

Applying amax() function:
9

Applying amax() function again:
[8 7 9]
```
#### numpy.ptp()
The numpy.ptp() function returns the range (maximum-minimum) of values along an axis.


```python
import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 

print 'Our array is:' 
print a 
print '\n'  

print 'Applying ptp() function:' 
print np.ptp(a) 
print '\n'  

print 'Applying ptp() function along axis 1:' 
print np.ptp(a, axis = 1) 
print '\n'   

print 'Applying ptp() function along axis 0:'
print np.ptp(a, axis = 0) 
It will produce the following output −

Output:

Our array is:
[[3 7 5]
[8 4 3]
[2 4 9]]

Applying ptp() function:
7

Applying ptp() function along axis 1:
[4 5 7]

Applying ptp() function along axis 0:
[6 3 6]
```
#### numpy.percentile()
Percentile (or a centile) is a measure used in statistics indicating the value below which a given percentage of observations in a group of observations fall. The function numpy.percentile() takes the following arguments.

> numpy.percentile(a, q, axis)

Where,
The axis along which the percentile is to be calculated

Example

```python
import numpy as np 
a = np.array([[30,40,70],[80,20,10],[50,90,60]]) 

print 'Our array is:' 
print a 
print '\n'  

print 'Applying percentile() function:' 
print np.percentile(a,50) 
print '\n'  

print 'Applying percentile() function along axis 1:' 
print np.percentile(a,50, axis = 1) 
print '\n'  

print 'Applying percentile() function along axis 0:' 
print np.percentile(a,50, axis = 0)
It will produce the following output −

Output:

Our array is:
[[30 40 70]
 [80 20 10]
 [50 90 60]]

Applying percentile() function:
50.0

Applying percentile() function along axis 1:
[ 40. 20. 60.]

Applying percentile() function along axis 0:
[ 50. 40. 60.]
```
#### numpy.median()
Median is defined as the value separating the higher half of a data sample from the lower half. The numpy.median() function is used as shown in the following program.

Example

```python
import numpy as np 
a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 

print 'Our array is:' 
print a 
print '\n'  

print 'Applying median() function:' 
print np.median(a) 
print '\n'  

print 'Applying median() function along axis 0:' 
print np.median(a, axis = 0) 
print '\n'  
 
print 'Applying median() function along axis 1:' 
print np.median(a, axis = 1)
It will produce the following output −

Output:

Our array is:
[[30 65 70]
 [80 95 10]
 [50 90 60]]

Applying median() function:
65.0

Applying median() function along axis 0:
[ 50. 90. 60.]

Applying median() function along axis 1:
[ 65. 80. 60.]
```
#### numpy.mean()
Arithmetic mean is the sum of elements along an axis divided by the number of elements. The numpy.mean() function returns the arithmetic mean of elements in the array. If the axis is mentioned, it is calculated along it.

Example

```python
import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

print 'Our array is:' 
print a 
print '\n'  

print 'Applying mean() function:' 
print np.mean(a) 
print '\n'  

print 'Applying mean() function along axis 0:' 
print np.mean(a, axis = 0) 
print '\n'  

print 'Applying mean() function along axis 1:' 
print np.mean(a, axis = 1)
It will produce the following output −

Output:

Our array is:
[[1 2 3]
 [3 4 5]
 [4 5 6]]

Applying mean() function:
3.66666666667

Applying mean() function along axis 0:
[ 2.66666667 3.66666667 4.66666667]

Applying mean() function along axis 1:
[ 2. 4. 5.]
```
#### numpy.average()
Weighted average is an average resulting from the multiplication of each component by a factor reflecting its importance. The numpy.average() function computes the weighted average of elements in an array according to their respective weight given in another array. The function can have an axis parameter. If the axis is not specified, the array is flattened.

Considering an array [1,2,3,4] and corresponding weights [4,3,2,1], the weighted average is calculated by adding the product of the corresponding elements and dividing the sum by the sum of weights.

Weighted average = (1*4+2*3+3*2+4*1)/(4+3+2+1)

Example

```python
import numpy as np 
a = np.array([1,2,3,4]) 

print 'Our array is:' 
print a 
print '\n'  

print 'Applying average() function:' 
print np.average(a) 
print '\n'  

# this is same as mean when weight is not specified 
wts = np.array([4,3,2,1]) 

print 'Applying average() function again:' 
print np.average(a,weights = wts) 
print '\n'  

# Returns the sum of weights, if the returned parameter is set to True. 
print 'Sum of weights' 
print np.average([1,2,3, 4],weights = [4,3,2,1], returned = True)
It will produce the following output −

Output:

Our array is:
[1 2 3 4]

Applying average() function:
2.5

Applying average() function again:
2.0

Sum of weights
(2.0, 10.0)
```


#### Standard Deviation
Standard deviation is the square root of the average of squared deviations from mean. The formula for standard deviation is as follows −

> std = sqrt(mean(abs(x - x.mean())**2))

Example

```python
import numpy as np 
print np.std([1,2,3,4])

Output:

1.1180339887498949 
```

#### Variance
Variance is the average of squared deviations, i.e., mean(abs(x - x.mean())**2). In other words, the standard deviation is the square root of variance.
Example

```python
import numpy as np 
print np.var([1,2,3,4])

Output:

1.25
```
# Data Visualization

Data visualization is the technique to present the data in a pictorial or graphical format. It enables stakeholders and decision makers to analyze data visually. The data in a graphical format allows them to identify new trends and patterns easily.

Example
Let's look at an example below.

We are a sales manager in a leading global organization. The organization plans to study the sales details of each product across all regions and countries. This is to identify the product which has the highest sales in a particular region end up the production.This research will enable the organization to increase the manufacturing of that product in the particular region. The data involved in this research might be huge and complex. The research on this large numeric data is difficult and time-consuming when it is performed manually.

When this numerical data is plotted on a graph for converted to charts it's easy to identify the patterns and predicted the result accurately.

The main benefits of data visualization are as follows:

- It simplifies the complex quantitative information
- It helps analyze and explore big data easily
- It identifies the areas that need attention or improvement
- It identifies the relationship between data points and variables
- It explores new patterns and reveals hidden patterns in the data

**Three major considerations for Data Visualization:**
1. Clarity
1. Accuracy
1. Efficiency

Clarity ensures that the data set is complete and relevant. This enables the data scientist to use the new patterns yield from the data in the relevant places.

Accuracy ensures using appropriate graphical representation to convey the right message.

Efficiency uses efficient visualization technique which highlights all the data points.

There are some basic factors that one would need to be aware of before visualizing the data.
- Visual effect
- Coordination System
- Data Types and Scale
- Informative Interpretation
- Visual Effect includes the usage of appropriate shapes, colors, and size to represent the analyzed data.

The Coordinate System helps to organize the data points within the provided coordinates.

The Data Types and Scale choose the type of data such as numeric or categorical.

The Informative Interpretation helps create visuals in an effective and easily interpreted ill manner using labels, title legends, and pointers.

##### Python Libraries
Many new python data visualization libraries are introduced recently, such as matplotlib, Vispy, bokeh, Seaborn, pygal, folium, and networkx. The matplotlib has emerged as the main data visualization library.

##### matplotlib
matplotlib is a python two-dimensional plotting library for data visualization and creating interactive graphics or plots. Using pythons matplotlib, the data visualization of large and complex data becomes easy.

Advantages
There are several advantages of using matplotlib to visualize data.

- A multi-platform data visualization tool built on the numpy and sidepy framework. Therefore, it's fast and efficient.
- It possesses the ability to work well with many operating systems and graphic backends.
- It possesses high-quality graphics and plots to print and view for a range of graphs such as histograms, bar charts, pie charts, scatter plots and heat maps.
- With Jupyter notebook integration, the developers have been free to spend their time implementing features rather than struggling with  compatibility.
- It has large community support and cross-platform support as it is an open source tool.
- It has full control over graph or plot styles such as line properties, thoughts, and access properties.

Understanding the Plot
Let's now try to understand a plot. A plot is a graphical representation of data, which shows the relationship between two variables or the distribution of data.
Example

This is a line plot of the random numbers on the y-axis and the range on the x-axis. The background of the plot is called a grid. The text first plot denotes the title of the plot and text line one denotes the legend.

[![](https://www.simplilearn.com/ice9/free_resources_article_thumb/matplotlib-plot-data.JPG)](http://https://www.simplilearn.com/ice9/free_resources_article_thumb/matplotlib-plot-data.JPG)

We can create a plot using four simple steps.

1. Import the required libraries
1. Define or import the required data set
1. Set the plant parameters
1. Display the created plant



