# build an ER chart

import random
from application_1_lib import *

def er_graph(prob,num_nodes):
    result = {}
    for i in range(num_nodes):
        result[i] = set([])
        for j in range(num_nodes):
            if i != j and random.random() < prob:
                result[i].add(j)
    return result

prob = 0.1
num_nodes = 1000

mygraph = er_graph(prob,num_nodes)

result = in_degree_distribution_norm(mygraph)

x = []
y = []

for key in result:
    x.append(key)
    y.append(result[key])

print x
print y

import matplotlib.pyplot as plt
plt.loglog(x,y)
plt.xlabel("# of in-degrees")
plt.ylabel("frequency")
plt.title("Question 1: Loglog plot of ER Chart (prob=0.1, num_nodes=1000)")
plt.show()
