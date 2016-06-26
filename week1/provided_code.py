"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2

# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

#citation_graph = load_graph(CITATION_URL)

"""
Counting the number of iterations in various mystery functions
"""

import simpleplot
import math

# Plot options
STANDARD = True
LOGLOG = False

# global counter that records the number of iterations for inner loops
counter = 0

###############################################
# three mystery functions
def mystery1(input_val):
    """ 
    Function whose loops update global counter    
    """
    global counter
    for index in range(input_val):
        for dummy_index in range(5):
            counter += 1

def mystery2(input_val):
    """ 
    Function whose loops update global counter   
    """
    global counter
    for index in range(input_val):
        for dummy_index in range(index / 2, index):
            counter += 1

def mystery3(input_val):
    """ 
    Function whose loops update global counter    
    """
    global counter
    for index in range(input_val):
        for dummy_index in range(int(1.1 ** index)):
            counter += 1
    
def build_plot(plot_size, plot_function, plot_type = STANDARD):
    """
    Build plot of the number of increments in mystery function
    """
    global counter
    plot = []
    for input_val in range(2, plot_size):
        counter = 0
        plot_function(input_val)
        if plot_type == STANDARD:
            plot.append([input_val, counter])
        else:
            plot.append([math.log(input_val), math.log(counter)])
    return plot



###############################################
# plottting code
plot_type = STANDARD
plot_size = 40

# Pass name of mystery function in as a parameter
plot1 = build_plot(plot_size, mystery1, plot_type)
plot2 = build_plot(plot_size, mystery2, plot_type)
plot3 = build_plot(plot_size, mystery3, plot_type)
simpleplot.plot_lines("Iteration counts", 600, 600, 
                      "input", "counter", [plot1, plot2, plot3])


"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
    


