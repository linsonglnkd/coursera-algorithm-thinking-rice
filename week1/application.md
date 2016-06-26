## Application 1 - Analysis of citation graphs

### Overview

In the Module 1 Application, we will combine the mathematical analysis that we began in the Homework with the code that you have written in the Project to analyze a real-world problem: How do scientific papers get cited? This part of the module will probably be much more unstructured than you are accustomed to in an on-line class. Our goal is to provide a more realistic simulation of how the concepts that you are learning are actually used in practice. Your key task in this part of the module is to **think** about the problem at hand as you answer each question.

As part of this portion of the module, you'll need to write code that processes medium-sized datasets. You are welcome to use either desktop Python or CodeSkulptor when writing this code. To process the data in CodeSkulptor, you will need to be careful in how you implement your code and will probably need to increase the default timeout from 5 secs to around 20-30 secs. You can reset the timeout using: 

````python
import codeskulptor
codeskulptor.set_timeout(20)
````

###Citation graphs

Our task for this application is to analyze the structure of graphs generated by citation patterns from scientific papers. Each scientific paper cites many other papers, say 20-40, and sometimes (e.g., review papers) hundreds of other papers. But, let's face it: It is often the case that the authors of a paper are superficially familiar with some (many?) of the papers they cite. So, the question is: Are the cited papers chosen randomly (from within the domain of the paper) or is there some "hidden pattern"?

Given that we will be looking at "paper i cites paper j" relationships, it makes sense to represent the citation data as a **directed graph** (a citation graph) in which the nodes correspond to papers, and there is an edge from node i to node j if the paper corresponding to node i cites the paper corresponding to node j. Since we're interested in understanding how papers get cited, we will analyze the in-degree distribution of a specific graph, and contrast it to those of graphs generated by two different random processes.

**Important:** Please use Coursera's "Attach a file" button to attach your plots/images for this Application as required. For each question you can attach more than one image as well as including text and math (LaTeX) in the same answer box. In particular, please do not host your solution plots/images on 3rd party sites. This practice exposes your peers to extra security risks and has the potential for abuse since the contents of a link to an external site may be modified after the hard deadline. Failure to follow this policy may lead to your plots/images being counted as "not submitted".

---

### Question 1 (4 pts)

For this question, your task is to load a provided citation graph for 27,770 high energy physics theory papers. This graph has 352,768 edges. You should use the [following code](http://www.codeskulptor.org/#alg_load_graph.py)  to load the citation graph as a dictionary. In CodeSkulptor, loading the graph should take 5-10 seconds. (For an extra challenge, you are welcome to write your own function to create the citation graph by parsing this [text representation](http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt) of the citation graph.) 

 Your task for this question is to compute the in-degree distribution for this citation graph. Once you have computed this distribution, you should normalize the distribution (make the values in the dictionary sum to one) and then compute a log/log plot of the points in this normalized distribution. How you create this point plot is up to you. You are welcome to use a package such as `matplotlib` for desktop Python, use the `simpleplot` module in CodeSkulptor, or use any other method that you wish. This [class page](https://class.coursera.org/algorithmicthink1-002/wiki/ides?page=plotting) on "Creating, formatting, and comparing plots" gives an overview of some of the options that we recommend for creating plots.

Since `simpleplot` does not support direct log/log plotting, you may simulate log/log plotting as shown in [this example](http://www.codeskulptor.org/#poc_mystery_plot.py) from the PoC video on "[Plotting data](https://class.coursera.org/algorithmicthink1-002/lecture/185)". However, be sure to include an indication on the labels for the horizontal and vertical axes that you are plotting the log of the values and note the base that you are using. (Nodes with in-degree zero can be ignored when computing the log/log plot since *log(0)=−∞*.)

Once you have created your plot, upload your plot in the box below using "Attach a file" button (the button is disabled under the 'html' edit mode; you must be under the 'Rich' edit mode for the button to be enabled). Please review the class guidelines for formatting and comparing plots on the "Creating, formatting, and comparing plots" class page. These guidelines cover the basics of good formatting practices for plots. Your plot will be assessed based on the answers to the following three questions:

* Does the plot follow the formatting guidelines for plots?
* Is the plot that of a normalized distribution on a log/log scale?
* Is the content of the plot correct? 