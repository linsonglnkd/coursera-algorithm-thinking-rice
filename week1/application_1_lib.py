def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a
    complete directed graph with the specified number of nodes. A complete graph
    contains all possible edges subject to the restriction that self-loops are not
    allowed. The nodes of the graph should be numbered 0 to num_nodes - 1 when
    num_nodes is positive. Otherwise, the function returns a dictionary corresponding
    to the empty graph.
    '''
    graph = {}
    for node in range(num_nodes):
        graph[node] = set(range(num_nodes))
        graph[node].remove(node)
    return graph

def compute_in_degrees(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes
     the in-degrees for the nodes in the graph. The function should return a dictionary
     with the same set of keys (nodes) as digraph whose corresponding values are the number
     of edges whose head matches a particular node.
    '''
    in_degrees = {}
    for node in digraph:
        in_degrees[node] = 0
    for node_1 in digraph:
        for node_2 in digraph[node_1]:
            in_degrees[node_2] += 1
    return in_degrees

def in_degree_distribution(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized
     distribution of the in-degrees of the graph. The function should return a dictionary whose
     keys correspond to in-degrees of nodes in the graph. The value associated with each particular
     in-degree is the number of nodes with that in-degree. In-degrees with no corresponding nodes
     in the graph are not included in the dictionary.
    '''
    result = {}
    in_degrees = compute_in_degrees(digraph)
    for each in in_degrees.values():
        result[each] = result.get(each,0) + 1
    return result

def in_degree_distribution_norm(digraph):
    '''
    Takes a directed graph digraph (represented as a dictionary) and computes the normalized
     distribution of the in-degrees of the graph. The function should return a dictionary whose
     keys correspond to in-degrees of nodes in the graph. The value associated with each particular
     in-degree is the frequency of that in-degree. In-degrees with no corresponding nodes
     in the graph are not included in the dictionary.
    '''
    un_norm_dist = in_degree_distribution(digraph)
    sum = 0.0
    for value in un_norm_dist.values():
        sum += value
    result = {}
    for key in un_norm_dist:
        result[key] = un_norm_dist[key] / sum
    return result
