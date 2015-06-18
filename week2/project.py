'''
Code for project 2
'''

def bfs_visited(ugraph, start_node):
    '''
    Takes the undirected graph ugraph and the node start_node and returns the set consisting
     of all nodes that are visited by a breadth-first search that starts at start_node
    '''
    from collections import deque
    queue = deque()
    visited = set([start_node])
    queue.append(start_node)
    while len(queue) > 0:
        node_j = queue.popleft()
        for neighbor_node in ugraph[node_j]:
            if neighbor_node not in visited:
                visited.add(neighbor_node)
                queue.append(neighbor_node)
    return visited

def cc_visited(ugraph):
    '''
    Takes the undirected graph ugraph and returns a list of sets, where each set consists of all the
     nodes (and nothing else) in a connected component, and there is exactly one set in the list for
      each connected component in ugraph and nothing else.
    '''
    remaining_nodes = set(g.keys())
    connected_component = list()
    while len(remaining_nodes) > 0:
        node_i = remaining_nodes.pop()
        set_w = bfs_visited(ugraph, node_i)
        print set_w
        connected_component.append(set_w)
        remaining_nodes = remaining_nodes - set_w
    return connected_component

def largest_cc_size(ugraph):
    '''
    Takes the undirected graph ugraph and returns the size (an integer) of the largest connected component
     in ugraph.
    '''
    connected_component = cc_visited(ugraph)
    cc_size = 0
    for each in connected_component:
        if len(each) > cc_size:
            cc_size = len(each)
    return cc_size

def compute_resilience(ugraph, attack_order):
    '''
    Takes the undirected graph ugraph, a list of nodes attack_order and iterates through the nodes in attack_order.
     For each node in the list, the function removes the given node and its edges from the graph and then computes
      the size of the largest connected component for the resulting graph.
    The function should return a list whose k+1th entry is the size of the largest connected component in the graph
     after the removal of the first k nodes in attack_order. The first entry (indexed by zero) is the size of
      the largest connected component in the original graph.
    '''
    result = [largest_cc_size(ugraph)]
    for node in attack_order:
        print node
        # delete the nodes that got attacked
        del ugraph[node]
        # delete the edge
        for each in ugraph:
            ugraph[each] = ugraph[each] - set([node])
        print ugraph
        result.append(largest_cc_size(ugraph))
    return result

# test cases
g = {1:set([2,3]), 2:set([1,4]), 3:set([1]), 4:set([2,5]), 5:set([2,6]), 6:set([5])}
print cc_visited(g)
print largest_cc_size(g)
print compute_resilience(g, [3])
