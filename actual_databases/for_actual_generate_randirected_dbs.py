import random
from create_graph_from_db_implemented import generate_graph, plot_generated_graph, pd
import os
# Main purpose is manipulating main prototype_db to direct it (Affect similarity)
# To do that randomly impact the nodes

"There should be 3 feature to change system"#
"1)Randomly delete the node(s)"
"2)Generate new interactions that is not "
"Main part is differantiate step by step but choose the type differentiation," \
" total edge change is same but one of them belongs one node, another one independent"

def find_and_delete(pair1,pair2,df):
    for index,row in df.iterrows():
        if (row['Gene Name Interactor A'] == pair1 or row['Gene Name Interactor B'] == pair1) and (row['Gene Name Interactor A'] == pair2 or row['Gene Name Interactor B'] == pair2):
            return index
def diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def change_refer(ref,ref_nod,unit_step,node_weight,edge_weight,trial_no):
    #Edge weight + Node weight should be equal to 1
    database = pd.read_csv(ref)
    ref_node=pd.read_csv(ref_nod)
    unit_step_for_rand_edge, unit_step_for_node = round(edge_weight*unit_step), round(node_weight*unit_step)
    init_db, init_edge=database['Gene_Symb'].values.tolist(), [ref_node['Gene Name Interactor A'].values.tolist(), ref_node['Gene Name Interactor B'].values.tolist()]
    print('Initial node_count' + str(database.shape))
    print('-------------------------1--------------------------------')
    for iterator in range(unit_step_for_rand_edge):
        try:
            random_number = random.randint(0, ref_node.shape[0] - 1)
            print(ref_node.iloc[random_number])
            ref_node=ref_node.drop(random_number, axis='index')
        except:
            random_number = random.randint(0, ref_node.shape[0]- 1)
            print(ref_node.iloc[random_number])
            ref_node = ref_node.drop(random_number, axis='index') #Dogru sayiyi buluna kadar while da dene
        print(ref_node.shape)
        print('-------------------------2--------------------------------')
    while unit_step_for_node != 0:
        random_numb=random.randint(0,len(database['Gene_Symb'].values.tolist())-unit_step)
        chosen_node=database['Gene_Symb'].values.tolist()[random_numb]
        #Find pairs
        pair_ls_for_chosen_node=[]
        #print(chosen_node)
        for index, row in ref_node.iterrows():
            if row['Gene Name Interactor A'] == chosen_node:
                pair_ls_for_chosen_node.append(row['Gene Name Interactor B'])
            if row['Gene Name Interactor B'] == chosen_node:
                pair_ls_for_chosen_node.append(row['Gene Name Interactor A'])
        #print(pair_ls_for_chosen_node)
        if len(pair_ls_for_chosen_node) < unit_step_for_node:
            '''
            try:
                ref_node=ref_node[ref_node['Gene Name Interactor A'].str.contains(chosen_node) == False]
            except:
                ref_node = ref_node[ref_node['Gene Name Interactor B'].str.contains(chosen_node) == False]
            '''
            for item in pair_ls_for_chosen_node:
                #print(item), print(chosen_node), print(ref_node)
                indice = find_and_delete(item,chosen_node,ref_node)
                print(ref_node.iloc[indice])
                ref_node=ref_node.drop(indice, axis='index')
                print(ref_node.shape)
                print('-------------------------3--------------------------------')
            unit_step_for_node = unit_step_for_node - len(pair_ls_for_chosen_node)

        else:
            pair_ls_for_chosen_node = pair_ls_for_chosen_node[:unit_step_for_node]
            for pair in pair_ls_for_chosen_node:
                indice=find_and_delete(pair,chosen_node,ref_node)
                print(ref_node.iloc[indice])
                ref_node=ref_node.drop(indice, axis='index')
                print(ref_node.shape)
                print('-------------------------4--------------------------------')
            break
    All_Term_Nodes, All_In_Nodes = ref_node['Gene Name Interactor B'].values.tolist(), ref_node['Gene Name Interactor A'].values.tolist()
    for index,row in database.iterrows():
        if (row['Gene_Symb'] in All_Term_Nodes ) or (row['Gene_Symb'] in All_In_Nodes):
            pass
        else:
            #database = database[database['Gene_Symb'].str.contains(row['Gene_Symb']) == False]
            drop_ls=database.index[database['Gene_Symb'] == row['Gene_Symb']].tolist()
            for drop_index in drop_ls:
                database = database.drop(drop_index,axis='index')

    ref_node.to_csv("randirected_confidence_"+str(trial_no), index=None)
    database.to_csv("randirected_node_db_"+str(trial_no), index=None)
    end_db, end_edge = database['Gene_Symb'].values.tolist(), [ref_node['Gene Name Interactor A'].values.tolist(), ref_node['Gene Name Interactor B'].values.tolist()]
    print('Finished node_count' + str(database.shape))
    print('Name(s) of removed nodes' + str(diff(init_db,end_db)))
    dif_of_edge_in=diff(init_db[0],end_edge[0])
    dif_of_edge_term=diff(init_db[1],end_edge[1])
    #for i in range(len(dif_of_edge_in)):
    #    print(str(dif_of_edge_in[i])+'--'+str(dif_of_edge_term[i]))
    return "randirected_node_db_"+str(trial_no), "randirected_confidence_"+str(trial_no)

def generate_db_name_csv_for_edge_files(Graph,trial_ID_or_Name="?",headlines="Gene_Symb,Transcription_Level,Hotpoint_Mutation,CRISPR_KO_Effect,Differentiation_Rate\n", target_path=os.getcwd()+"/"):
    db_headline_ls = headlines.rsplit(","); headline_count= len(db_headline_ls)
    db_file = open(str(target_path)+str(trial_ID_or_Name), "w")
    db_file.write(headlines)
    for node in Graph.nodes:
        line=str(node)
        for number_of_headlines in range(headline_count-1):
            line+=",NA/N"
        line+="\n"
        db_file.write(line)
    db_file.close()


if __name__ == '__main__':

    #Trial for a database that have already a node_set database as csv
    """
    n_weight,e_weight,s_size=0.3,0.7,15 #Define the random rate
    print('node_diff_rate: '+str(n_weight) +' edge_diff_rate:' +str(e_weight) + ' total_step_size'+ str(s_size))
    #trial_code=input('trial_number: ')
    trial_code=313
    print(os.getcwd())
    database,wire_database=str(os.getcwd())+'/prototype_db.csv',str(os.getcwd())+'/confidence_db.csv'
    directed_db, directed_wired = change_refer(database,wire_database,s_size,n_weight,e_weight,trial_code)
    #print(directed_db, directed_wired)
    G = generate_graph(directed_db, directed_wired)
    #print(G)
    #plot_generated_graph(G,trial_code)
    """

    #Trial for generate an edge system from only nodes
    """
    wire_database=str(os.getcwd()+'/confidence_db.csv')
    G,trial_ID = generate_graph(wire_database, trial_ID="001")
    generate_db_name_csv_for_edge_files(G,trial_ID_or_Name="002",)
    """

    #Trial 3
    n_weight, e_weight, s_size = 0.3, 0.7, 45  # Define the random rate
    print('node_diff_rate: ' + str(n_weight) + ' edge_diff_rate: ' + str(e_weight) + ' total_step_size: ' + str(s_size))
    trial_code = "HIPPIE-node-075.csv"
    wire_database = str(os.getcwd() + '/HIPPIE-confidence-075.csv')
    G, trial_ID = generate_graph(wire_database, trial_ID=trial_code)
    generate_db_name_csv_for_edge_files(G, trial_ID_or_Name=trial_ID)

    database, wire_database = str(os.getcwd()) + '/HIPPIE-node-075.csv', str(os.getcwd()) + '/HIPPIE-confidence-075.csv'
    directed_db, directed_wired = change_refer(database, wire_database, s_size, n_weight, e_weight, trial_code)
    G = generate_graph(directed_wired)
    print(G)
    # plot_generated_graph(G,trial_code)



