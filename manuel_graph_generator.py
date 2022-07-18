import os
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
# This is the part that collected data


# Locating
# This part prepare a gene class for every element that
# is obtained from the raw data file
class Gene():
    def __init__(self,name,transcription_level,crispr_KO,hotpoint_mut,differentiation_rate):
        self.name=name
        self.transcription_level=transcription_level
        self.KO=crispr_KO
        self.hotpoint_mut=hotpoint_mut
        self.differentiation_rate=differentiation_rate

    def __str__(self):
        return str(self.name)
# Prepare function that assign gene to node

def assign_node(Graph,gene):
    Graph.add_node(str(gene.name),TL=gene.transcription_level,KO=gene.KO,HP=gene.hotpoint_mut)

# Wiring

#wire_database=pd.read_csv('confidence_db.csv',sep=';')
#print(wire_database.iterrows('InNode'))

class Wire():
    def __init__(self,nodeI,nodeT,confidence,state):
        self.InNode=nodeI
        self.TermNode=nodeT
        self.confidence=confidence
        self.state=state

    def __str__(self):
        return '/' + str(self.InNode)+' - '+ str(self.TermNode) + '/'

def assign_wire(Graph,Wire):
    Graph.add_edge(Wire.InNode, Wire.TermNode, weight_based_conf=Wire.confidence, S=Wire.state)


#print(G.edges['PI3KA','APC']) #Denotes all_features
#print(G.edges['PI3KA','APC']['weight_based_conf']) #Denotes only weight_based_cond

# Ploting
'''
plt.figure()
pos_nodes = nx.spring_layout(G)
nx.draw(G, pos_nodes, with_labels=True)

pos_attrs = {}
for node, coords in pos_nodes.items():
    pos_attrs[node] = (coords[0], coords[1] + 0.08)

node_attrs = nx.get_node_attributes(G, 'weight_based_conf')
custom_node_attrs = {}
for node, attr in node_attrs.items():
   custom_node_attrs[node] = "{'weight_based_conf': '" + attr + "'}"

nx.draw_networkx_labels(G, pos_attrs, labels=custom_node_attrs)

def plot_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G,pos)
    nx.draw_networkx_labels(G, pos)

    labels = nx.get_edge_attributes(G, 'weight_based_conf')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    figure=plt.gcf()
    figure.set_size_inches(15, 10)
    plt.savefig('Map_Prototype.png',dpi=400)
    plt.show()
'''

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
    #plt.savefig(path+name_of_map+str(trial_no)+".png", dpi=dpi_chosen)
    if plot_show:
        plt.show()
    plt.clf(); plt.cla(); plt.close()

if __name__ != '__main__':
    """
    sample_Actual = True
    if not sample_Actual:
        database = pd.read_csv(str(os.getcwd())+'/example_dbs/prototype_db.csv', sep=';')
        #print(database['Gene_Symb'].values.tolist())
        G = nx.Graph()  # Define Null Graph
        for index, row in database.iterrows():
            assign_node(G, Gene(row['Gene_Symb'], row['Transcription_Level'], row['CRISPR_KO_Effect'],
                                row['Hotpoint_Mutation'], row['Differentiation_Rate']))
        # print(G.adj) # From this point adding nodes with their features is completed
        # print(G.nodes['NCOR']['TL']) # This is the print func check whether features are assigned or not

        wire_database = pd.read_csv(str(os.getcwd())+'/example_dbs/confidence_db.csv', sep=';')
        for index, row in wire_database.iterrows():
            assign_wire(G, Wire(row['InNode'], row['TermNode'], row['confidence'], True))
        # print(G.adj) #This is the updated (wired version of map)
        plot_generated_graph(G,211,path=str(os.getcwd())+'/example_dbs/')

    if sample_Actual:
        wire_database = pd.read_csv(str(os.getcwd())+'/actual_databases/HIPPIE-confidence-075.csv')
        print(wire_database)
        Graph_HIPPIE_confidence_075=nx.Graph()
        for index, row in wire_database.iterrows():
            assign_wire(Graph_HIPPIE_confidence_075, Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'],True))
        print(Graph_HIPPIE_confidence_075)
        #plot_generated_graph(G, "Actual_Graph", path=str(os.getcwd()) + '/actual_databases/')
        
    """
    wire_database = pd.read_csv(str(os.getcwd()) + '/actual_databases/HIPPIE-confidence-075.csv')
    print(wire_database)
    Graph_HIPPIE_confidence_075 = nx.Graph()
    for index, row in wire_database.iterrows():
        assign_wire(Graph_HIPPIE_confidence_075,
                    Wire(row['Gene Name Interactor A'], row['Gene Name Interactor B'], row['Confidence Value'], True))
    print(Graph_HIPPIE_confidence_075)
    # plot_generated_graph(G, "Actual_Graph", path=str(os.getcwd()) + '/actual_databases/')