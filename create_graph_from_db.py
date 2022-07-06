from prototype_body import *

def generate_graph(db_name):
    database = pd.read_csv(db_name, sep=';')
    print(database)
    G=nx.Graph() #Define Null Graph
    for index, row in database.iterrows():
        assign_node(G, Gene(row['Gene_Symb'], row['Transcription_Level'], row['CRISPR_KO_Effect'],
                            row['Hotpoint_Mutation'], row['Differentiation_Rate']))

    wire_database = pd.read_csv('confidence_db.csv', sep=';')

    for index, row in wire_database.iterrows():
        assign_wire(G, Wire(row['InNode'], row['TermNode'], row['confidence'], True))
    return G
def plot_generated_graph(G,trial_no):
    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    nx.draw_networkx_labels(G, pos)

    labels = nx.get_edge_attributes(G, 'weight_based_conf')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    figure = plt.gcf()
    figure.set_size_inches(15, 10)
    plt.savefig("Map_Prototoype"+str(trial_no)+".png", dpi=400)
    plt.show()
'''
if __name__ == '__main__':
    defined_db_name= str(os.getcwd())+'/example_dbs/53453_confidence_db' # defined name of the graph genrated db in example 
    Graph=generate_graph(defined_db_name)
    plot_generated_graph(Graph,defined_db_name)
'''