import os
import itertools
import networkx as nx
from create_graph_from_db import generate_graph, plot_generated_graph
from building_graphlet_library import graphlet_library



def search_Graphlets(Graph, graphlet_library, log=True):
    span_list=[]
    for target_graphlet in graphlet_library:
        if log:
            print('\n-------------------'+str(target_graphlet.name)+'-------------------\n'); contempary_list=[target_graphlet.name]
        for nodes_of_subgraph in itertools.combinations(Graph.nodes, len((target_graphlet.pattern))):
            defined_subgraph = Graph.subgraph(nodes_of_subgraph)
            if nx.is_connected(defined_subgraph) and nx.is_isomorphic(defined_subgraph, target_graphlet.pattern):
                contempary_list.append(defined_subgraph.edges)
                if log:
                    print(defined_subgraph.edges)

        span_list.append(contempary_list)
    return span_list

def generate_image_of_all_found_motifs(found_motif_list,ID, log=True):

    counter =0; starting_path = os.getcwd()+'/sub_graph_dir/'
    ID_path = os.path.join(starting_path, str(ID) )
    try:
        os.mkdir(ID_path)
    except:
        pass
    for found_motif_category in found_motif_list:
        if log:
            print(found_motif_category)
        path = os.path.join( ID_path, str(found_motif_category[0]))
        try:
            os.mkdir(path)
        except:
            pass

        for found_actual_motif in found_motif_category[1:]:
            plot_generated_graph(nx.Graph(found_actual_motif),str(ID)+'_'+str(counter),path=path,plot_show=False, dpi_chosen=80); counter+=1
            if log:
                print(found_actual_motif)
    if log:
        print("The actual subgraph's images are extracted to " + str(starting_path) +" file to it's relevant categoris.")

"""
if __name__ == '__main__':
    Graph, ID = generate_graph(str(os.getcwd() + '/example_dbs/312_prototype_db'),
                           str(os.getcwd() + '/example_dbs/312_confidence_db'))

    found_motifs = search_Graphlets(Graph,graphlet_library,log=True)
    generate_image_of_all_found_motifs(found_motifs, ID, log=True)
"""

