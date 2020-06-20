# Introduction to Data Science
[![](https://www.360logica.com/blog/wp-content/uploads/2019/02/data-science-1.jpg)](http://https://www.360logica.com/blog/wp-content/uploads/2019/02/data-science-1.jpg)

Data is the new Oil. This statement shows how every modern IT system is driven by capturing, storing and analysing data for various needs. Be it about making decision for business, forecasting weather, studying protein structures in biology or designing a marketing campaign. All of these scenarios involve a multidisciplinary approach of using mathematical models, statistics, graphs, databases and of course the business or scientific logic behind the data analysis.

Data science is the process of deriving knowledge and insights from a huge and diverse set of data through organizing, processing and analysing the data. It involves many different disciplines like mathematical and statistical modelling, extracting data from it source and applying data visualization techniques. Often it also involves handling big data technologies to gather both structured and unstructured data

####  Python in Data Science
1. The programming requirements of data science demands a very versatile yet flexible language which is simple to write the code but can handle highly complex mathematical processing. Python is most suited for such requirements .

1. A simple and easy to learn language which achieves result in fewer lines of code than other similar languages like R. Its simplicity also makes it robust to handle complex scenarios with minimal code and much less confusion on the general flow of the program.

1. It is cross platform, so the same code works in multiple environments without needing any change. That makes it perfect to be used in a multi-environment setup easily.

1. It executes faster than other similar languages used for data analysis like R and MATLAB.

1. Its excellent memory management capability, especially garbage collection makes it versatile in gracefully managing very large volume of data transformation, slicing, dicing and visualization.


# Difference between AI, ML and DL

[![](https://miro.medium.com/max/1146/0*vHQxsXbMZlGE29KS)](http://https://miro.medium.com/max/1146/0*vHQxsXbMZlGE29KS)


### What is AI ?

**AI (Artificial Intelligence) involves machines that can perform tasks that are characteristic of human intelligence.** While this is rather general, it includes things like planning, understanding language, recognizing objects and sounds, learning, and problem-solving.

John McCarthy first coined the term artificial intelligence in 1956 when he invited a group of researchers from a variety of disciplines including language simulation, neuron nets, complexity theory and more to a summer workshop called the Dartmouth Summer Research Project on Artificial Intelligence to discuss what would ultimately become the field of AI. At that time, the researchers came together to clarify and develop the concepts around “thinking machines” which up to this point had been quite divergent. McCarthy is said to have picked the name artificial intelligence for its neutrality; to avoid highlighting one of the tracks being pursued at the time for the field of “thinking machines” that included cybernetics, automata theory and complex information processing. The proposal for the conference said, “The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it.”

Today, modern dictionary definitions focus on AI being a sub-field of computer science and how machines can imitate human intelligence (being human-like rather than becoming human). The English Oxford Living Dictionary gives this definition: “The theory and development of computer systems able to perform tasks normally requiring human intelligence, such as visual perception, speech recognition, decision-making, and translation between languages.”

**AI has three different levels:**

1. **Narrow AI:** A artificial intelligence is said to be narrow when the machine can perform a specific task better than a human. `The current research of AI is here now.`
2. **General AI:** An artificial intelligence reaches the general state when it can perform any intellectual task with the same accuracy level as a human would
3. **Active AI:** An AI is active when it can beat humans in many tasks

### What is ML ?

**Machine learning** is the best tool so far to analyze, understand and identify a pattern in the data. One of the main ideas behind machine learning is that the computer can be trained to automate tasks that would be exhaustive or impossible for a human being.

The clear breach from the traditional analysis is that machine learning can take decisions with minimal human intervention.

Machine learning uses data to feed an algorithm that can understand the relationship between the input and the output. When the machine finished learning, it can predict the value or the class of new data point.

Machine Learning is the subset of AI where Machine Learning algorithms are designed in such a way that the machine tries to learn by itself without being explicitly programmed on each and every instruction. So, as it will be exposed to more and more data, it tries to internally modify itself and adjust according to the data to which it is exposed so that it will not rely on human experts to program them.

There are basically three types of Machine Learning as shown below:
[![](https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-07-1.jpg)](http://https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-07-1.jpg)

1. Supervised Learning
In supervised learning, the machine is provided with the labeled dataset. It already has input and output parameters. So, when the machine is given a new dataset, the supervised learning algorithm examines the data and produces the correct output according to the labeled data.
> Use case: Detecting cancer patientsUse case: Detecting cancer patients

1. Unsupervised Learning
In unsupervised learning, the machine would not have any labelled dataset. The algorithm is designed in a way that it tries to learn by itself without any supervision of data. This involves clustering of data.
> Example: Consider few objects such as pencil, eraser, and matchbox
[![](https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-02.jpg)](http://https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-02.jpg)

Here, the machine does not even know what these objects are; rather, it makes clusters of similar objects, and when any input dataset is given, it gives the output by examining the data it has clustered.
[![](https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-13.jpg)](http://https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-13.jpg)

Netflix recommendation system works on the same technique as it saves the users’ watched history and recommends a similar content to the user.

![](ML_model.PNG)

Reinforcement Learning
In reinforcement learning, the algorithms are designed in such a way that the machine tries to find an optimal solution. It adopts the principle of reward and punishment, and by this approach it moves to the correct result.

Consider a scenario where a young cricketer tries to learn the technique of hitting a 6 for a particular shot. Whenever he tries to play the shot and misses it, he gets a score of −1.
[![](https://intellipaat.com/blog/wp-content/uploads/2018/07/Cricketer_bowledA.jpg)](http://https://intellipaat.com/blog/wp-content/uploads/2018/07/Cricketer_bowledA.jpg)
The bowler bowls again, and the batsman tries to hit that shot by adjusting his position. After trying for five to six times, he finally hits a 6 with a suitable position and gets a score of +6.
[![](https://intellipaat.com/blog/wp-content/uploads/2018/07/cricket1A.jpg)](http://https://intellipaat.com/blog/wp-content/uploads/2018/07/cricket1A.jpg)

This way he learns the technique for hitting a 6. Reinforcement algorithm works in a similar way.

##### What is the machine learning Model?
The machine learning model is nothing but a piece of code; an engineer or data scientist makes it smart through training with data. So, if you give garbage to the model, you will get garbage in return, i.e. the trained model will provide false or wrong predictions.

### What is DL ?

**Deep learning** is a computer software that mimics the `network of neurons` in a brain. It is a subset of machine learning and is called deep learning because it makes use of deep `neural networks`. A neural network is an architecture where the layers are stacked on top of each other.

Deep Learning has evolved from Machine Learning. It works in a layered architecture and uses the artificial neural network, a concept inspired by the biological neural network. The human brain usually analyzes and converts the information it receives and tries to identify it from the past information the brain has stored. The brain does this through labeling and assigning information into various groups in a fraction of a millisecond.

In a similar way, Deep Learning algorithms are trained to identify patterns and classify various types of information to give the desired output when it receives an input.

So, to understand Deep Learning vs Machine Learning, you must know the difference between Machine Learning and Deep Learning and the major difference is that we need to provide the features manually in Machine Learning. But in Deep Learning, it automatically extracts features for classification which in turn demands a huge amount of data for training DL algorithms. So, in Deep Learning, the accuracy of the output depends on the amount of data.
Now, let us look at artificial neural networks in Deep Learning.


#### Artificial Neural Network (ANN)
It is a concept inspired by the biological neural network. It consists of three layers:
[![](https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-09.jpg)](http://https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-09.jpg)

Input Layer: The input layer is used for taking the input data from external sources and then passing it on to the hidden layers of the neural network. It does not perform any computation.
Hidden Layer: This layer consists of many hidden layers. All the computation is performed in this layer. After all the computation is done, it passes the output to the output layer.
Output Layer: This layer is used for computing and giving the output to the outside world.



These layers consist of nodes that are interconnected with each other. The nodes interact with each other with the help of links by which they are connected. This connection of nodes is designed in such a way that it produces output for a given input.

The links are associated with a real number that is called the weight of those links. These weights are initialized randomly, and hence there could be a large difference between the actual values and the predicted values. Due to this, it will not give the desired output in one iteration.
[![](https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-11.jpg)](http://https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-11.jpg)

Even after the weight is assigned and the computation is done if it does not give the desired output, we go back and update the weight of the link with the current value to get closer to the desired output. We do this progressively until we get the best possible output.

Also, the weights assigned to the links decides how fast the triggering of the activation function will occur.
There is another term ‘bias,’ which is used to decide when to trigger the activation function.
Now, we will see the details of the activation function.

In the real world, the data is always 3-dimensional. For example, let’s say, an image of a car is given as an input to the neural network; we can plot the length and height of the car in a 2-D plane. However, there are a lot more attributes to be considered while computing to recognize it as a car. The computation of this data is a complex task. So, to reduce this difficulty, we use the activation function. It pumps the wide range of values assigned to the data into a specific domain so that computation becomes easy.
[![](https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-12.jpg)](http://https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-12.jpg)

This is how the artificial neural network works and helps in achieving perfection in Artificial Intelligence.
[![](https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-10.jpg)](http://https://intellipaat.com/blog/wp-content/uploads/2018/07/ALMLDL-10.jpg)
To summarize, Artificial Intelligence is an umbrella term, and Machine Learning and Deep Learning are the subdomains of this field that help in achieving Artificial Intelligence.

### Difference between ML and DL

![](https://miro.medium.com/max/720/1*zLJnMjuGdamCpN4yJMTR5g.png)

![](ML_vs_DL.PNG)

###When to use ML or DL?

In the table below, we summarize the difference between machine learning and deep learning.

![](ML_DL_use.PNG)
![](https://social.technet.microsoft.com/wiki/cfs-file.ashx/__key/communityserver-wikis-components-files/00-00-00-00-05/7002.5_5F00_1.PNG)

# Introduction to Anaconda

Packages or additional libraries help in scientific computing and computational modelling. In Python, the packages are not the part of the Python standard library. Few major packages are –

1. numpy : matrices and linear algebra
2. scipy : many numerical routines
3. matplotlib:  creating plots of data
4. sympy : symbolic computation
5. pytest : a code testing framework

####What is Anaconda Python?
Together with a list of Python packages, tools like editors, Python distributions include the Python interpreter. Anaconda is one of several Python distributions. Anaconda is a new distribution of the Python and R data science package. It was formerly known as Continuum Analytics. Anaconda has more than 100 new packages.

This work environment, Anaconda is used for scientific computing, data science, statistical analysis, and machine learning. The latest version of Anaconda 5.0.1 is released in October 2017.

The released version 5.0.1 addresses some minor bugs and adds useful features, such as updated R language support. All of these features weren’t available in the original 5.0.0 release.

This package manager is also an environment manager, a Python distribution, and a collection of open source packages and contains more than 1000 R and Python Data Science Packages.

Why Anaconda for Python?
There’s no big reason to switch to Anaconda if you are completely happy with you regular python. But some people like data scientists who are not full-time developers, find anaconda much useful as it simplifies a lot of common problems a beginner runs into.

Anaconda can help with –

1. Installing Python on multiple platforms
2. Separating out different environments
3. Dealing with not having correct privileges and
4. Getting up and running with specific packages and libraries

#### How to Download Anaconda 5.0.1?
The free version of Anaconda distribution community edition can be downloaded directly from Anaconda’s website. For the enterprise edition, one need professional support from Anaconda’s sales team.

Conda treats Python the same as any other package, so it is easy to manage and update multiple installations.

Anaconda supports Python 2.7, 3.4, 3.5 and 3.6. The default is Python 2.7 or 3.6, depending on which installer you used:

1. For the installers “Anaconda” and “Miniconda,” the default is 2.7.
2. For the installers “Anaconda 3” or “Miniconda 3,” the default is 3.6.
#### How to Install Anaconda?
Once downloaded the .exe file, run through the installer. Do accept the terms, and finish the installation. To check, close the browser and pull up the terminal.

Once the installation is complete, it should have automatically added that to the path. To test this, go ahead and type ‘python’.

The version of python i.e. 3 will show and also the anaconda distribution will be seen. If you install the 4 versions of Anaconda, then all the packages, which are there in the packages, can also be imported easily.