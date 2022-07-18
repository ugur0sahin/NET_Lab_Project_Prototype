import os
import itertools
import networkx as nx
from create_graph_from_db_implemented import generate_graph, plot_generated_graph
from building_graphlet_library import graphlet_library



def not_Egoist_search_Graphlets(Graph, graphlet_library, structured_known_ls=None, log=True):
    global contempary_list

    if structured_known_ls is not None:
        known_ls = []
        for cluster in structured_known_ls:
            for element in cluster:
                known_ls.append(element)
    else:
        known_ls = []
    """
    for iter in itertools.combinations(Graph.nodes, len((graphlet_library[0].pattern))):
        defined_subgraph = Graph.subgraph(iter)
        #print(defined_subgraph.nodes)
    """

    span_list=[]
    for target_graphlet in graphlet_library:
        contempary_list=[]
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

def search_Graphlets_in_egoistic_database(ego_dictionary, Graph):
    span_list = []
    for target_graphlet in graphlet_library:
        print('\n-------------------' + str(target_graphlet.name) + '-------------------\n');
        contempary_list = [target_graphlet.name]
        for node_key in ego_dictionary.keys():
            for primary_dist_node in ego_dictionary[node_key].keys():
                for secondary_dist_node in ego_dictionary[node_key][primary_dist_node]:
                    if (node_key not in [primary_dist_node, secondary_dist_node] and primary_dist_node not in [node_key,                                                                                   secondary_dist_node] and secondary_dist_node not in [
                            node_key, primary_dist_node]) and (
                            None not in [node_key, primary_dist_node, secondary_dist_node]):
                        defined_subgraph = Graph.subgraph(
                            [node_key, primary_dist_node, secondary_dist_node])
                        if nx.is_connected(defined_subgraph) and nx.is_isomorphic(defined_subgraph,
                                                                                  target_graphlet.pattern):
                            contempary_list.append(defined_subgraph.edges)
                            print(defined_subgraph.edges)

        span_list.append(contempary_list)
    return span_list

if __name__ == '__main__':
    ##Trial-1
    #Last Trial
    """
    ## Generating Graph from the DB
    ## Import Graph to the Indexing Function
    ## This block do not search graphlets it only reindex the database
    """
    from reindex_as_egoistic_structure_databases import reindex_dataset_as_ego_structure
    from create_graph_from_db_implemented import generate_graph, plot_generated_graph
    #Although plot_generated function is implemented, it is not going to run
    path = os.getcwd() + "/actual_databases/"
    Graph_HIPPIE_confidence_075, trial_ID=generate_graph("HIPPIE-confidence-075.csv", trial_ID="Actual_")
    ego_dictionary = reindex_dataset_as_ego_structure(Graph_HIPPIE_confidence_075, save_dict=True, name="Actual_HIPPIE-confidence-075", path="/actual_databases/")

    ##Trial-2
    ##Import Genearated Graph_Not_egoistic_Search
    """
    import pandas as pd
    from manuel_graph_generator import assign_wire, Wire
    wire_database = pd.read_csv(str(os.getcwd()) + '/actual_databases/HIPPIE-confidence-075.csv')
    wire_database = wire_database.drop(range(5000,96343),axis='index')
    print(wire_database)

    Graph_HIPPIE_confidence_075 = nx.Graph()
    for index, row in wire_database.iterrows():
        assign_wire(Graph_HIPPIE_confidence_075,
                    Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))
    found_motifs_from_actual = not_Egoist_search_Graphlets(Graph_HIPPIE_confidence_075, graphlet_library)
    print(found_motifs_from_actual)
    
    """
    #Trial-3
    ##Defined_egoistic_structure
    # Database is diminished also manuel graph generation processes are takes placed
    """
    from reindex_as_egoistic_structure_databases import reindex_dataset_as_ego_structure, assign_wire, Wire, pd

    wire_database = pd.read_csv(str(os.getcwd()) + '/actual_databases/HIPPIE-confidence-075.csv')
    wire_database = wire_database.drop(range(100, 95000), axis='index')
    wire_database.to_csv("wire_database_diminished_Actual", index=True)

    Graph_HIPPIE_confidence_075 = nx.Graph()
    for index, row in wire_database.iterrows():
        assign_wire(Graph_HIPPIE_confidence_075,
                    Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))

    ego_dictionary = reindex_dataset_as_ego_structure(Graph_HIPPIE_confidence_075, save_dict=False,
                                                      name="HIPPIE-confidence-075", path="/actual_databases/")

    found_graphlets = search_Graphlets_in_egoistic_database(ego_dictionary, Graph_HIPPIE_confidence_075) #AMAZING


    """
    # Trial-3
    ##Defined_egoistic_structure
    """
    from reindex_as_egoistic_structure_databases import  load_dict_with_pickle, pd, assign_wire, Wire, reindex_dataset_as_ego_structure

    wire_database = pd.read_csv(str(os.getcwd()) + '/actual_databases/HIPPIE-confidence-075.csv')
    wire_database = wire_database.drop(range(100, 95000), axis='index')
    wire_database.to_csv("wire_database_diminished_Actual", index=True)

    Graph_HIPPIE_confidence_075 = nx.Graph()
    for index, row in wire_database.iterrows():
        assign_wire(Graph_HIPPIE_confidence_075,
                    Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))

    #ego_dictionary = reindex_dataset_as_ego_structure(Graph_HIPPIE_confidence_075, save_dict=False,
    #                                                  name="HIPPIE-confidence-075", path="/actual_databases/")

    path = os.path.join(os.getcwd(),"actual_databases/HIPPIE-confidence_dictionary_db.pkl")
    egoistic_dict_db=load_dict_with_pickle(path)
    search_Graphlets_in_egoistic_database(egoistic_dict_db,Graph_HIPPIE_confidence_075)
    """
    #Trial -4
    """
    from reindex_as_egoistic_structure_databases import reindex_dataset_as_ego_structure, assign_wire, Wire, pd, plot_generated_graph

    wire_database312 = pd.read_csv(str(os.getcwd()) + '/example_dbs/312_confidence_db', sep=';')
    #wire_database312 = wire_database312.drop(range(100, 95000), axis='index')
    #wire_database312.to_csv("wire_database_diminished_Actual", index=True)

    wire_Graph_312 = nx.Graph()
    for index, row in wire_database312.iterrows():
        assign_wire(wire_Graph_312,
                    Wire(row['InNode'], row['TermNode'], row['confidence'], True))

    ego_dictionary = reindex_dataset_as_ego_structure(wire_Graph_312, save_dict=False,
                                                      name="HIPPIE-confidence-075", path="/actual_databases/")

    found_graphlets_312 = search_Graphlets_in_egoistic_database(ego_dictionary, wire_Graph_312)  # AMAZING
    plot_generated_graph(wire_Graph_312,312, name_of_map="/Map_Prototoype_312")
    #found_graphlets_312 = set(found_graphlets_312[1])

    ############ Second

    print("#############################################################################################################")

    from reindex_as_egoistic_structure_databases import reindex_dataset_as_ego_structure, assign_wire, Wire, pd, plot_generated_graph

    wire_database313 = pd.read_csv(str(os.getcwd()) + '/example_dbs/313_confidence_db', sep=';')
    #wire_database313 = wire_database313.drop(range(100, 95000), axis='index')
    #wire_database313.to_csv("wire_database_diminished_Actual", index=True)

    wire_Graph_313 = nx.Graph()
    for index, row in wire_database313.iterrows():
        assign_wire(wire_Graph_313,
                    Wire(row['InNode'], row['TermNode'], row['confidence'], True))

    ego_dictionary = reindex_dataset_as_ego_structure(wire_Graph_313, save_dict=False,
                                                      name="HIPPIE-confidence-075", path="/actual_databases/")

    found_graphlets_313 = search_Graphlets_in_egoistic_database(ego_dictionary, wire_Graph_313)  # AMAZING
    plot_generated_graph(wire_Graph_313,313, name_of_map="/Map_Prototoype_313")

    #found_graphlets_313 = set(found_graphlets_313[1])

    #print(found_graphlets_312.difference(found_graphlets_313))
    """
    #Trial-5


