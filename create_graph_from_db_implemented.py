import os
from manuel_graph_generator import assign_wire, assign_node, Wire, Gene, pd, nx, plt


def get_trial_code_from_filename(file):
    file_direc=file.split('/')
    trial_name=file_direc[-1].split('_')[0]
    return trial_name

def generate_graph(db_wire, db_name=None, trial_ID="?"):
    G = nx.Graph()  # Define Null Graph

    if not db_name == None:
        if trial_ID is "?":
            trial_ID=get_trial_code_from_filename(db_name)
        database = pd.read_csv(db_name)
        #print(database)

        for index, row in database.iterrows():
            assign_node(G, Gene(row['Gene_Symb'], row['Transcription_Level'], row['CRISPR_KO_Effect'],
                                row['Hotpoint_Mutation'], row['Differentiation_Rate']))

    wire_database = pd.read_csv(db_wire)

    for index, row in wire_database.iterrows():
        assign_wire(G, Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))
    return G, trial_ID

def plot_generated_graph(G,trial_no,path='', plot_show=True, dpi_chosen=400, name_of_map="/Map_Prototoype"):
    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    nx.draw_networkx_labels(G, pos)

    labels = nx.get_edge_attributes(G, 'weight_based_conf')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    figure = plt.gcf()
    figure.set_size_inches(15, 10)
    plt.savefig(path+name_of_map+str(trial_no)+".png", dpi=dpi_chosen)
    if plot_show:
        plt.show()
    plt.clf(); plt.cla(); plt.close()

"""
if __name__ != '__main__':
    defined_db_name= str(os.getcwd())+'/example_dbs/312_prototype_db' # defined name of the graph genrated db in example
    defined_wire_db_name=str(os.getcwd())+'/example_dbs/312_confidence_db'
    Graph, trial_ID = generate_graph(defined_wire_db_name, db_name=defined_db_name)
    plot_generated_graph(Graph,312,plot_show=True, path=str(os.getcwd()))
"""

