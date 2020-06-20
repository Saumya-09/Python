Python machine learning libraries have grown to become the most preferred language for machine learning algorithm implementations. Let’s have a look at the main Python libraries used for machine learning.

Top Python Machine Learning Libraries
1) NumPy
2) SciPy
3) Scikit-learn
4) Theano
5) TensorFlow
6) Keras
7) PyTorch
8) Pandas
9) Matplotlib


#### 1. NumPy
NumPy is a well known general-purpose array-processing package. An extensive collection of high complexity mathematical functions make NumPy powerful to process large multi-dimensional arrays and matrices. NumPy is very useful for handling linear algebra, Fourier transforms, and random numbers. Other libraries like TensorFlow uses NumPy at the backend for manipulating tensors.

With NumPy, you can define arbitrary data types and easily integrate with most databases. NumPy can also serve as an efficient multi-dimensional container for any generic data that is in any datatype. The key features of NumPy include powerful N-dimensional array object, broadcasting functions, and out-of-box tools to integrate C/C++ and Fortran code.

#### 2. SciPy
With machine learning growing at supersonic speed, many Python developers were creating python libraries for machine learning, especially for scientific and analytical computing. Travis Oliphant, Eric Jones, and Pearu Peterson in 2001 decided to merge most of these bits and pieces codes and standardize it. The resulting library was then named as SciPy library.

The current development of the SciPy library is supported and sponsored by an open community of developers and distributed under the free BSD license.

The SciPy library offers modules for linear algebra, image optimization, integration interpolation, special functions, Fast Fourier transform, signal and image processing, Ordinary Differential Equation (ODE) solving, and other computational tasks in science and analytics.

The underlying data structure used by SciPy is a multi-dimensional array provided by the NumPy module. SciPy depends on NumPy for the array manipulation subroutines. The SciPy library was built to work with NumPy arrays along with providing user-friendly and efficient numerical functions.

#### 3. Scikit-learn
In 2007, David Cournapeau developed the Scikit-learn library as part of the Google Summer of Code project. In 2010 INRIA involved and did the public release in January 2010. Skikit-learn was built on top of two Python libraries – NumPy and SciPy and has become the most popular Python machine learning library for developing machine learning algorithms.

Scikit-learn has a wide range of supervised and unsupervised learning algorithms that works on a consistent interface in Python. The library can also be used for data-mining and data analysis. The main machine learning functions that the Scikit-learn library can handle are classification, regression, clustering, dimensionality reduction, model selection, and preprocessing.

#### 4. Theano
Theano is a python machine learning library that can act as an optimizing compiler for evaluating and manipulating mathematical expressions and matrix calculations. Built on NumPy, Theano exhibits a tight integration with NumPy and has a very similar interface. Theano can work on Graphics Processing Unit (GPU) and CPU.

Working on GPU architecture yields faster results. Theano can perform data-intensive computations up to 140x faster on GPU than on a CPU. Theano can automatically avoid errors and bugs when dealing with logarithmic and exponential functions. Theano has built-in tools for unit-testing and validation, thereby avoiding bugs and problems.

#### 5. TensorFlow
TensorFlow was developed for Google’s internal use by the Google Brain team. Its first release came in November 2015 under Apache License 2.0. TensorFlow is a popular computational framework for creating machine learning models. TensorFlow supports a variety of different toolkits for constructing models at varying levels of abstraction.

TensorFlow exposes a very stable Python and C++ APIs. It can expose, backward compatible APIs for other languages too, but they might be unstable. TensorFlow has a flexible architecture with which it can run on a variety of computational platforms CPUs, GPUs, and TPUs. TPU stands for Tensor processing unit, a hardware chip built around TensorFlow for machine learning and artificial intelligence.

#### 6. Keras
Keras has over 200,000 users as of November 2017. Keras is an open-source library used for neural networks and machine learning. Keras can run on top of TensorFlow, Theano, Microsoft Cognitive Toolkit, R, or PlaidML. Keras also can run efficiently on CPU and GPU.

Keras works with neural-network building blocks like layers, objectives, activation functions, and optimizers. Keras also have a bunch of features to work on images and text images that comes handy when writing Deep Neural Network code.

Apart from the standard neural network, Keras supports convolutional and recurrent neural networks.

#### 7. PyTorch
PyTorch has a range of tools and libraries that support computer vision, machine learning, and natural language processing. The PyTorch library is open-source and is based on the Torch library. The most significant advantage of PyTorch library is it’s ease of learning and using.

PyTorch can smoothly integrate with the python data science stack, including NumPy. You will hardly make out a difference between NumPy and PyTorch. PyTorch also allows developers to perform computations on Tensors. PyTorch has a robust framework to build computational graphs on the go and even change them in runtime. Other advantages of PyTorch include multi GPU support, simplified preprocessors, and custom data loaders.

#### 8. Pandas
Pandas are turning up to be the most popular Python library that is used for data analysis with support for fast, flexible, and expressive data structures designed to work on both “relational” or “labeled” data. Pandas today is an inevitable library for solving practical, real-world data analysis in Python. Pandas is highly stable, providing highly optimized performance. The backend code is purely written in C or Python.

The two main types of data structures used by pandas are :

- Series (1-dimensional)
- DataFrame (2-dimensional)
These two put together can handle a vast majority of data requirements and use cases from most sectors like science, statistics, social, finance, and of course, analytics and other areas of engineering.

#### 9. Matplotlib
Matplotlib is a data visualization library that is used for 2D plotting to produce publication-quality image plots and figures in a variety of formats. The library helps to generate histograms, plots, error charts, scatter plots, bar charts with just a few lines of code.

It provides a MATLAB-like interface and is exceptionally user-friendly. It works by using standard GUI toolkits like GTK+, wxPython, Tkinter, or Qt to provide an object-oriented API that helps programmers to embed graphs and plots into their applications.

# Dataset

Datasets and Machine Learning
One of the hardest problems to solve in deep learning has nothing to do with neural nets: it’s the problem of getting the right data in the right format.

Getting the right data means gathering or identifying the data that correlates with the outcomes you want to predict; i.e. data that contains a signal about events you care about. The data needs to be aligned with the problem you’re trying to solve. Kitten pictures are not very useful when you’re building a facial identification system. Verifying that the data is aligned with the problem you seek to solve must be done by a data scientist. If you do not have the right data, then your efforts to build an AI solution must return to the data collection stage.

Deep learning, and machine learning more generally, needs a good training set to work properly. Collecting and constructing the training set – a sizable body of known data – takes time and domain-specific knowledge of where and how to gather relevant information. The training set acts as the benchmark against which deep-learning nets are trained. That is what they learn to reconstruct before they’re unleashed on data they haven’t seen before.

Training sets that require much time or expertise can serve as a proprietary edge in the world of data science and problem solving. The nature of the expertise is largely in telling your algorithm what matters to you by selecting what goes into the training set.

#### The Different Data Sets of Machine Learning
Machine learning typically works with two data sets: **training and test**.

The first set you use is the training set, the largest of the three. Running a training set through a neural network teaches the net how to weigh different features, adjusting them coefficients according to their likelihood of minimizing errors in your results.

Those coefficients, also known as parameters, will be contained in tensors and together they are called the model, because they encode a model of the data they train on. They are the most important takeaways you will obtain from training a neural network.

The second set is your test set. It functions as a seal of approval, and you do not use it until the end. After you have trained and optimized your data, you test your neural net against this final random sampling. The results it produces should validate that your net accurately recognizes images, or recognizes them at least [x] percentage of them.

If you do not get accurate predictions, go back to the training set, look at the hyperparameters you used to tune the network, as well as the quality of your data and look at your pre-processing techniques.

# 6 V's of Data
###### 1. Volume

Big data implies enormous volumes of data. It used to be employees created data. Now that data is generated by machines, networks and human interaction on systems like social media the volume of data to be analyzed is massive. Yet, Inderpal states that the volume of data is not as much the problem as other V’s like veracity.


###### 2. Variety

Variety refers to the many sources and types of data both structured and unstructured. We used to store data from sources like spreadsheets and databases. Now data comes in the form of emails, photos, videos, monitoring devices, PDFs, audio, etc. This variety of unstructured data creates problems for storage, mining and analyzing data. Jeff Veis, VP Solutions at HP Autonomy presented how HP is helping organizations deal with big challenges including data variety.

###### 3. Velocity

Big Data Velocity deals with the pace at which data flows in from sources like business processes, machines, networks and human interaction with things like social media sites, mobile devices, etc. The flow of data is massive and continuous. This real-time data can help researchers and businesses make valuable decisions that provide strategic competitive advantages and ROI if you are able to handle the velocity. Inderpal suggest that sampling data can help deal with issues like volume and velocity.

###### 4. Veracity

Big Data Veracity refers to the biases, noise and abnormality in data. Is the data that is being stored, and mined meaningful to the problem being analyzed. Inderpal feel veracity in data analysis is the biggest challenge when compares to things like volume and velocity. In scoping out your big data strategy you need to have your team and partners work to help keep your data clean and processes to keep ‘dirty data’ from accumulating in your systems.

###### 5. Validity

Like big data veracity is the issue of validity meaning is the data correct and accurate for the intended use. Clearly valid data is key to making the right decisions. Phil Francisco, VP of Product Management from IBM spoke about IBM’s big data strategy and tools they offer to help with data veracity and validity.

###### 6. Volatility

Big data volatility refers to how long is data valid and how long should it be stored. In this world of real time data you need to determine at what point is data no longer relevant to the current analysis.
Big data clearly deals with issues beyond volume, variety and velocity to other concerns like veracity, validity and volatility.

#### Features and Labels
###### - Feature:
Features are individual independent variables that act as the input in your system. Prediction models use features to make predictions. New features can also be obtained from old features using a method known as ‘feature engineering’. More simply, you can consider one column of your data set to be one feature. Sometimes these are also called attributes. And the number of features are called dimensions.

###### - Label:
Labels are the final output. You can also consider the output classes to be the labels. When data scientists speak of labeled data, they mean groups of samples that have been tagged to one or more labels.

# Encoding in ML

Machine learning and deep learning models, like those in Keras, require all input and output variables to be numeric.

This means that if your data contains categorical data, you must encode it to numbers before you can fit and evaluate a model.

The two most popular techniques are an **integer encoding** and a **one hot encoding**, although a newer technique called learned embedding may provide a useful middle ground between these two methods.

#### The Challenge With Categorical Data
A categorical variable is a variable whose values take on the value of labels.

For example, the variable may be “color” and may take on the values “red,” “green,” and “blue.”

Sometimes, the categorical data may have an ordered relationship between the categories, such as “first,” “second,” and “third.” This type of categorical data is referred to as ordinal and the additional ordering information can be useful.

Machine learning algorithms and deep learning neural networks require that input and output variables are numbers.

This means that categorical data must be encoded to numbers before we can use it to fit and evaluate a model.

There are many ways to encode categorical variables for modeling, although the three most common are as follows:

1. Integer Encoding: Where each unique label is mapped to an integer.
1. One Hot Encoding: Where each label is mapped to a binary vector.
1. Learned Embedding: Where a distributed representation of the categories is learned.

#####  Integer Encoding
As a first step, each unique category value is assigned an integer value.
For example, “red” is 1, “green” is 2, and “blue” is 3.
This is called a label encoding or an integer encoding and is easily reversible.
For some variables, this may be enough.
The integer values have a natural ordered relationship between each other and machine learning algorithms may be able to understand and harness this relationship.


##### One-Hot Encoding
For categorical variables where no such ordinal relationship exists, the integer encoding is not enough.
In fact, using this encoding and allowing the model to assume a natural ordering between categories may result in poor performance or unexpected results (predictions halfway between categories).
In this case, a one-hot encoding can be applied to the integer representation. This is where the integer encoded variable is removed and a new binary variable is added for each unique integer value.
In the “color” variable example, there are 3 categories and therefore 3 binary variables are needed. A “1” value is placed in the binary variable for the color and “0” values for the other colors.

The previous module introduced the idea of dividing your data set into two subsets:

**training set**—a subset to train a model.
**test set**—a subset to test the trained model.
You could imagine slicing the single data set as follows:

A horizontal bar divided into two pieces: 80% of which is the training set and 20% the test set.
[![](https://developers.google.com/machine-learning/crash-course/images/PartitionTwoSets.svg)](http://https://developers.google.com/machine-learning/crash-course/images/PartitionTwoSets.svg)

Make sure that your test set meets the following two conditions:

1. Is large enough to yield statistically meaningful results.
1. Is representative of the data set as a whole. In other words, don't pick a test set with different characteristics than the training set.

Assuming that your test set meets the preceding two conditions, your goal is to create a model that generalizes well to new data. Our test set serves as a proxy for new data. For example, consider the following figure. Notice that the model learned for the training data is very simple. This model doesn't do a perfect job—a few predictions are wrong. However, this model does about as well on the test data as it does on the training data. In other words, this simple model does not overfit the training data.
[![](https://developers.google.com/machine-learning/crash-course/images/TrainingDataVsTestData.svg)](http://https://developers.google.com/machine-learning/crash-course/images/TrainingDataVsTestData.svg)
Two models: one run on training data and the other on test data.  The model is very simple, just a line dividing the orange dots from the blue dots.  The loss on the training data is similar to the loss on the test data.


**Never train on test data**. If you are seeing surprisingly good results on your evaluation metrics, it might be a sign that you are accidentally training on the test set. For example, high accuracy might indicate that test data has leaked into the training set.

For example, consider a model that predicts whether an email is spam, using the subject line, email body, and sender's email address as features. We apportion the data into training and test sets, with an 80-20 split. After training, the model achieves 99% precision on both the training set and the test set. We'd expect a lower precision on the test set, so we take another look at the data and discover that many of the examples in the test set are duplicates of examples in the training set (we neglected to scrub duplicate entries for the same spam email from our input database before splitting the data). We've inadvertently trained on some of our test data, and as a result, we're no longer accurately measuring how well our model generalizes to new data.

# Loading Dataset
The following code block shows how to load dataset:
```python
data=pd.read_csv('forestfires.csv')
data.head()
```
##### Output:
[![](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2018/08/forestfires.png)](http://https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2018/08/forestfires.png)

# Data Cleaning

Data forms the backbone of any data analytics you do. Regarding data, there are many things to go wrong – be it the construction, arrangement, formatting, spellings, duplication, extra spaces, and so on. To perform the data analytics properly we need various data cleaning techniques so that our data is ready for analysis. It is commonly said that,

> “Data scientists spend 80% of their time cleaning and manipulating data and only 20% of their time actually analyzing it.”

Thus, it is important to grow accustomed to the process of data cleaning techniques and all of the data cleansing tools that are related to data cleansing methods.

1. Get Rid of Extra Spaces
2. Select and Treat All Blank Cells
3. Convert Numbers Stored as Text into Numbers
4. Remove Duplicates
5. Highlight Errors
6. Change Text to Lower/Upper/Proper Case
7. Spell Check
8. Delete all Formatting

#### What is Data Cleaning?
Data cleansing or data cleaning is the process of identifying and removing (or correcting) inaccurate records from a dataset, table, or database and refers to recognising unfinished, unreliable, inaccurate or non-relevant parts of the data and then restoring, remodelling, or removing the dirty or crude data.

Data cleaning techniques may be performed as batch processing through scripting or interactively with data cleansing tools.

After cleaning, a dataset should be uniform with other related datasets in the operation. The discrepancies identified or eliminated may have been basically caused by user entry mistakes, by corruption in storage or transmission, or by various data dictionary descriptions of similar items in various stores.

Are Data Cleaning Techniques Essential?
Data cleaning techniques are not only an essential part of the data science process – it’s also the most time-consuming part.
Unfortunately, Data Cleaning techniques are generally not spoken about in the media nor is it taught in most intro Data Scientist Course because it is not as important as training a neural network or identifying images but to perform those things data cleaning plays a very important role.
Without the data cleaning techniques, the neural networks and image identification modules will not be as efficient as we want them to be.


