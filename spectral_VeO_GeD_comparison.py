from network_matrix_conversion import get_paths
from compare_binary_interacted_networks import align_binary_matrices, get_headline
import math
import numpy as np
import os


def common_elements(ls1, ls2):
    """
    Return a list containing the elements which are in both list1 and list2
    """
    same_ls=[]
    for element in ls1:
        if element in ls2:
            same_ls.append(element)
    return same_ls

def get_common_and_union_node(g_ls):
    """
        This function obtain nodes similarity unit score
        From the Graph_list that contain like G_ls = [G1, G2]
        """
    # get union, all nodes
    all_nodes = list(set(g_ls[1][::, 0]) | set(g_ls[1][::, 0]));all_nodes.remove('Gene_S')
    # belonged nodes in the graph
    graph_genes_ls = []
    for G in g_ls:
        g_unique_element_ls = []
        for row in G:
            hdline, array = get_headline(row)
            if 1 in array:
                g_unique_element_ls.append(hdline)
        graph_genes_ls.append(g_unique_element_ls)
    common_element_ls_of_graphs = common_elements(graph_genes_ls[0], graph_genes_ls[1])
    return common_element_ls_of_graphs, all_nodes

def get_common_and_union_edges(g_ls):
    """
    This function obtain edges similarity unit score
    From the Graph_list that contain like G_ls = [G1, G2]
    """
    #After this line common and union nodes have been found.
    #Common edges and total edges should be found.
    graph_edges_ls=[]
    for G in g_ls:
        g_unique_edges_ls=[]
        for row_index in range(np.shape(G)[0]):
            for colon_index in range(np.shape(G)[1]):
                try:
                    if G[row_index][colon_index] == 1:
                        edge = str(G[row_index][0]) + '-' + str(G[0][colon_index])
                        g_unique_edges_ls.append(edge)
                except:
                    pass
            graph_edges_ls.append(g_unique_edges_ls)
    common_edges_ls_of_graphs=common_elements(graph_edges_ls[0],graph_edges_ls[1])

    all_edges=list(set(graph_edges_ls[0]) | set(graph_edges_ls[1]))
    return common_edges_ls_of_graphs,all_edges


def vertex_overlap_similarity(G_ls):
    '''
    Vertex/Edge Overlap (VEO) [5]: For two graphs G1(V1, E1) and G2(V2, E2):
    simVEO(G1,G2)=2 |E1 ∩E2|+|V1 ∩V2| / |E1| + |E2| + |V1| + |V2|
    '''
    common_edges_ls_of_graphs, all_edges = get_common_and_union_edges(G_ls)
    common_element_ls_of_graphs, all_nodes = get_common_and_union_node(G_ls)
    simvVeOv= 2*(len(common_edges_ls_of_graphs)+len(common_element_ls_of_graphs))/(len(all_edges)+len(all_nodes))
    return simvVeOv

def graph_edit_distance_similarity(g_ls):
    '''
    Graph Edit Distance (GED) [4]: GED has quadratic complexity in general, so they [4] consider the case where only insertions and deletions are allowed.
    simGED(G1,G2) = |V1|+|V2|−2|V1 ∩V2| + |E1| + |E2| − 2|E1 ∩ E2|.
    For V1 = V2 and unweighted graphs, simGED is equivalent to hamming distance(A1 , A2 ) = sum(A1 XOR A2).
    '''
    common_edges_ls_of_graphs, all_edges = get_common_and_union_edges(g_ls)
    common_element_ls_of_graphs, all_nodes = get_common_and_union_node(g_ls)
    node_score= (len(all_nodes)) - (2*len(common_element_ls_of_graphs))
    edge_score = (len(all_edges)) - (2*len(common_edges_ls_of_graphs))
    simGeD = edge_score + node_score
    return simGeD


def spectral_comparison(g_ls):
    """
    The last 3 methods are variations of the well-studied
    spectral method “λ-distance” ([4], [10], [11]).
    Let {λ1i}|V1| and {λ2i}|V2| be the eigenvalues of the ma- i=1 i=1
    trices that represent G1 and G2. Then, λ-distance is givenby 􏰇􏰆 k
    Edges
    dλ(G1, G2) = 􏰆􏰅􏰁 (λ1i − λ2i)2, i=1
    where k is max(|V1 |, |V2 |) (padding is required for the smallest vector of eigenvalues).
    The variations of the method are based on three different matrix representa- tions of the graphs:
    adjacency (λ-d Adj.), laplacian (λ-d Lap.) and normalized laplacian matrix (λ-d N.L.).
    0 corresponds to identical
    to find increasing sim = 1/(1+score)
    """
    """"
    shape_tuple_of_graphs = np.shape(g_ls[0])
    for row_index in range(1,shape_tuple_of_graphs[0]):
        objected_vector_ls=[]
        for G in g_ls:
            headline, array = get_headline(G[row_index])
            objected_vector_ls.append(array)
        ## Obtaining Eigenvalues of Vectors
        for vector_belonged_graph in objected_vector_ls:
            print(np.linalg.eigvals(vector_belonged_graph[1:]))
    #graph_edges_ls.append(g_unique_edges_ls)
    #common_edges_ls_of_graphs = common_elements(graph_edges_ls[0], graph_edges_ls[1])
    """
    eigen_val_ls=[]
    for G in g_ls:
        G = np.delete(G,[0],axis=1); G=np.delete(G,[0],axis=0);G=np.asarray(G,float)
        eigen_vals=np.linalg.eigvals(G)
        eigen_val_ls.append(eigen_vals)

    shape_of_eigenls=np.shape(eigen_val_ls[0])
    score_total_ls=[]
    for index_eigenval in range(shape_of_eigenls[0]):
        diff_eigenval = (eigen_val_ls[0][index_eigenval] - eigen_val_ls[1][index_eigenval])**2
        score_total_ls.append(diff_eigenval)
    spectral_score = math.sqrt(sum(score_total_ls))
    return spectral_score



"""
if __name__ == '__main__':
    G1_binariy_matrice = get_paths(str(os.getcwd())+'/example_dbs/312_confidence_db',
                                   str(os.getcwd())+'/example_dbs/312_prototype_db')
    G2_binariy_matrice = get_paths(str(os.getcwd()) + '/example_dbs/313_confidence_db',
                                   str(os.getcwd()) + '/example_dbs/313_prototype_db')
    G1_Aligned_binariy_matrice, G2_Aligned_binariy_matrice=align_binary_matrices(G1_binariy_matrice,G2_binariy_matrice)

    vertex_overlap_score = vertex_overlap_similarity([G1_Aligned_binariy_matrice, G2_Aligned_binariy_matrice])

    graph_edit_distance_score = graph_edit_distance_similarity([G1_Aligned_binariy_matrice, G2_Aligned_binariy_matrice])

    #spectral_sim_score = spectral_comparison([G1_Aligned_binariy_matrice, G2_Aligned_binariy_matrice])
"""