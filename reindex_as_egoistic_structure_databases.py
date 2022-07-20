from manuel_graph_generator import *

def find_another_node_in_edge(edge,node):
    for node_in_edge in edge:
        if node != node_in_edge:
            return node_in_edge

def load_dict_with_pickle(path):
    import pickle
    with open(path, 'rb') as f:
        loaded_dict = pickle.load(f)  # This code is required to load saved dictionary
    return loaded_dict

def reindex_dataset_as_ego_structure(Graph_HIPPIE_confidence, save_dict=False, name="egoisticly_reindexed_database_as_dict", path=""):
    node_dict = dict()
    for node in Graph_HIPPIE_confidence.nodes:
        #print(node)
        belonged_dict= dict()
        for edge in Graph_HIPPIE_confidence.edges:
            if node in edge:
                interacted_node = find_another_node_in_edge(edge,node)
                #This is important in this part 1st dimension is found and it hasn't added to key yet.
                dim_2nd_ls = list()
                for edge_2nd in Graph_HIPPIE_confidence.edges:
                    if interacted_node in edge_2nd:
                        interacted_edge_2nd_dim = find_another_node_in_edge(edge_2nd,interacted_node)
                        dim_2nd_ls.append(interacted_edge_2nd_dim)

                belonged_dict[interacted_node]=(dim_2nd_ls)
        node_dict[node] =belonged_dict

    print('Dictionart Structure is {A:{B:[...], C:[...], D:[...]},  T:{B:[...], Y:[...], P:[...]}________'
          '___Node_Init:{Node_in_1st_dist:[..2nd_sit_nodes..], Another_node_in_1st_dist:[..2nd_sit_nodes..]}}')

    if save_dict:
        import pickle
        path_n=str(os.getcwd())+path
        f = open(str(path_n)+str(name)+"_dictionary_db"+'.pkl', 'wb')
        pickle.dump(node_dict, f)
        print("This dictionary saved as .pkl format")

    return node_dict
"""
if __name__ == "__main__":
    wire_database = pd.read_csv(str(os.getcwd()) + '/actual_databases/HIPPIE-confidence-075.csv')
    wire_database = wire_database.drop(range(100, 95000), axis='index')
    wire_database.to_csv("wire_database_diminished_Actual", index=True)

    Graph_HIPPIE_confidence_075 = nx.Graph()
    for index, row in wire_database.iterrows():
        assign_wire(Graph_HIPPIE_confidence_075,
                    Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))
    print(Graph_HIPPIE_confidence_075)

    ego_dictionary = reindex_dataset_as_ego_structure(Graph_HIPPIE_confidence_075, save_dict=True, name="HIPPIE-confidence", path="/actual_databases/")
"""