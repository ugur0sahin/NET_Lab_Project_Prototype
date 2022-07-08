import os
import numpy as np
from network_matrix_conversion import get_paths

def get_headline(array):
    return array[0], array[:-1]

# score function should be evaluate raw score to generate an output.

def _score_obtained_vectors(vectorA, vectorB):
    #distance = np.linalg.norm(vectorA - vectorB)
    #print(distance)
    #unit_score = 1 / (distance + 1)
    score=0
    for i in range(len(vectorA)):
        if vectorA[i]==vectorB[i]:
            score +=1
    unit_score = score **2
    maximum_possible_score= len(vectorA) **2
    return unit_score/ maximum_possible_score


def align_binary_matrices(G1,G2):
    #Fuse the lists as unique
    fuse_Gene_Symb_ls = list(set(G1[0]) | set(G2[0]))
    fuse_Gene_Symb_ls.remove('Gene_Symb')
    graph_list=[G1,G2]
    return_aligned_matrix_ls=[]
    for graph in graph_list:
        # Generate Null Matrix
        # Get their shape and manipulate them to arrange null matrix
        null_mat=np.zeros([len(fuse_Gene_Symb_ls),len(fuse_Gene_Symb_ls)]); null_mat=np.asarray(null_mat,object)
        gene_sym_ls_total=np.array(fuse_Gene_Symb_ls); null_mat=np.insert(null_mat,0,gene_sym_ls_total,axis=0)
        gene_sym_ls_total=np.insert(gene_sym_ls_total,0,'Gene_Symb'); null_mat = np.insert(null_mat, 0, gene_sym_ls_total, axis=1)
        shape_of_null, shape_objected,  = np.shape(null_mat), np.shape(graph)

        #Arange
        for i in range(shape_objected[0]):
            for j in range(shape_objected[1]):
                for i_null in range(shape_of_null[0]):
                    for j_null in range(shape_of_null[1]):
                        if null_mat[0][i_null] == graph[0][i] and null_mat[:,0][j_null] == graph[:,0][j]:
                            null_mat[i_null,j_null]=graph[i,j]
        return_aligned_matrix_ls.append(null_mat)
    return return_aligned_matrix_ls[0], return_aligned_matrix_ls[1]


# Compare vectors and output value should be send to score function
# A window should be created to scan both affinity matrices to compare (However in this version windows should be Nx1 vector)

def compare_matrices_from_euclidian(G1,G2):
    keep_score = []
    for array_G1 in G1:
        for array_G2 in G2:
            headline_of_interested_G1, array_of_interested_G1 = get_headline(array_G1); headline_of_interested_G2, array_of_interested_G2 = get_headline(array_G2)
            if headline_of_interested_G1 == headline_of_interested_G2:
                unit_score = _score_obtained_vectors(array_of_interested_G1, array_of_interested_G2)
                keep_score.append(unit_score)
    return keep_score

if __name__ == '__main__':
    G1_binariy_matrice = get_paths(str(os.getcwd())+'/example_dbs/312_confidence_db',
                                   str(os.getcwd())+'/example_dbs/312_prototype_db')
    G2_binariy_matrice = get_paths(str(os.getcwd()) + '/example_dbs/313_confidence_db',
                                   str(os.getcwd()) + '/example_dbs/313_prototype_db')
    G1_Aligned_binariy_matrice, G2_Aligned_binariy_matrice=align_binary_matrices(G1_binariy_matrice,G2_binariy_matrice)
    score=compare_matrices_from_euclidian(G1_Aligned_binariy_matrice,G2_Aligned_binariy_matrice)
    #print('')
    #print('---------Euclidian Similarity---------')
    #print(sum(score)/len(score))