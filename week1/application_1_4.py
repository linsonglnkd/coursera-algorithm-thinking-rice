# DPA
import random
from application_1_lib import *

def make_dpa_graph(num_nodes, num_nodes_start):

    # create a complete graph with m nodes
    result = make_complete_graph(num_nodes_start)

    for node in range(num_nodes_start, num_nodes):
        # compute in degrees for each node
        in_degrees = compute_in_degrees(result)
        total_in_degree = 0
        for each in in_degrees.values():
            total_in_degree += each
        picked_nodes = set([])
        for candidate in result:
            print candidate, in_degrees[candidate] + 1, total_in_degree + len(result)
            if random.random() < float(in_degrees[candidate] + 1) / (total_in_degree + len(result)):
                picked_nodes.add(candidate)
        result[node] = picked_nodes
    return result

print make_dpa_graph(5,3)
