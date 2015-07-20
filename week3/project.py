"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster
import urllib2


######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    if len(cluster_list) < 2:
        return None
    result = pair_distance(cluster_list, 0, 1)
    for dummy_i in range(len(cluster_list)):
        for dummy_j in range(dummy_i+1, len(cluster_list)):
            dist =  pair_distance(cluster_list, dummy_i, dummy_j)
            if dist[0] < result[0]:
                result = dist
    return result



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    if len(cluster_list) <= 3:
        return slow_closest_pair(cluster_list)
    else:
        mid = len(cluster_list) / 2
        cluster_left = [cluster_list[index].copy() for index in range(mid)]
        cluster_right = [cluster_list[index].copy() for index in range(mid, len(cluster_list))]
        result_left = fast_closest_pair(cluster_left)
        result_right = fast_closest_pair(cluster_right)
        # the right one need to add mid to get the original index
        result_right = (result_right[0], result_right[1]+mid, result_right[2]+mid)
        # get the smaller
        if result_left[0] <= result_right[0]:
            result = result_left
        else:
            result = result_right
        
        horiz_center = 0.5 * (cluster_list[mid-1].horiz_center() + cluster_list[mid].horiz_center())
        half_width = result[0]
        result_strip = closest_pair_strip(cluster_list, horiz_center, half_width)
        if result_strip[0] < result[0]:
            return result_strip
    return result


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    # copy the original input, and keep the index
    v_sorted = [(cluster_list[index].copy(),index) for index in range(len(cluster_list))]
    v_sorted.sort(key = lambda cluster: cluster[0].vert_center())
    # select points in the strip
    cluster_in_strip = [item for item in v_sorted \
                        if abs(item[0].horiz_center()-horiz_center) < half_width]
    result = (float("inf"), -1, -1)
    for dummy_i in range(len(cluster_in_strip)):
        for dummy_j in range(dummy_i+1, min(dummy_i+4, len(cluster_in_strip))):
            dist = pair_distance(cluster_list, cluster_in_strip[dummy_i][1], cluster_in_strip[dummy_j][1])
            if dist[0] <= result[0]:
                result = dist
    return result
            
 
    
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    # copy the input cluster list
    cluster_list_copy = [item.copy() for item in cluster_list]
    cluster_list_copy.sort(key = lambda cluster: cluster.horiz_center())
    while len(cluster_list_copy) > num_clusters:
        closest_pair = fast_closest_pair(cluster_list_copy)
        print 'close pair', closest_pair
        idx_1 = closest_pair[1]
        idx_2 = closest_pair[2]
        cluster_list_copy[idx_1] = cluster_list_copy[idx_1].merge_clusters(cluster_list_copy[idx_2])
        del cluster_list_copy[idx_2]
        cluster_list_copy.sort(key = lambda cluster: cluster.horiz_center())
    return cluster_list_copy


######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
    # make a copy
    cluster_list_copy = [item.copy() for item in cluster_list]
    cluster_list_copy.sort(key = lambda cluster: -cluster.total_population())
    cluster_center = [(item.horiz_center(), item.vert_center()) for item in cluster_list_copy[:num_clusters]]

    for dummy_i in range(num_iterations):
        # initial k empty clusters
        clusters = [alg_cluster.Cluster(set([]), item[0], item[1], 0, 0) for item in cluster_center]
        assign_cluster = list()
        for dummy_j in range(len(cluster_list_copy)):
            dist = float("inf")
            tmp_assign = -1
            for dummy_l in range(len(clusters)):
                tmp_dist = cluster_list_copy[dummy_j].distance(clusters[dummy_l])
                if tmp_dist < dist:
                    tmp_assign = dummy_l
                    dist = tmp_dist
            assign_cluster.append(tmp_assign)
        print cluster_center
        print assign_cluster
        for dummy_j in range(len(cluster_list_copy)):
            clusters[assign_cluster[dummy_j]].merge_clusters(cluster_list_copy[dummy_j])
        # update the centers
        clusters.sort(key = lambda cluster: -cluster.total_population())
        cluster_center = [(item.horiz_center(), item.vert_center()) for item in clusters[:num_clusters]]
                           
    return clusters
