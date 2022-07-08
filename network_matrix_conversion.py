import numpy as np
import pandas as pd
import os

#Node by Node Interaction to Bool
def get_bool_array_from_index(interact_ls,gene_sym_ls):
    arr=np.zeros(len(gene_sym_ls))
    for item in interact_ls:
        arr[gene_sym_ls.index(item)]=1
    return arr

#Get the directed files w/ their paths
def get_paths(wired_database_path, node_database_path):
    node_df, wired_df = pd.read_csv(node_database_path, sep=';'), pd.read_csv(wired_database_path, sep=';')
    #Creating a list to obtain labeled colons
    no_nodes, gene_sym_ls,notated_arrays=node_df.shape[0], node_df['Gene_Symb'].values.tolist(), []
    #print("Gene Symbol List is: " + str(gene_sym_ls))
    #print('--------------------------------------------------------------------------ALL NODE INTERACTIONS----------------------------------------------------------------------------------------------------------------------------------------------------------')

    for objected_node in gene_sym_ls:
        pair_ls=[]
        pair_df_In=wired_df[wired_df['InNode'].str.contains(objected_node)]
        pair_df_Out= wired_df[wired_df['TermNode'].str.contains(objected_node)]
        for index, row in pair_df_In.iterrows():
            if row['InNode'] == objected_node or row['TermNode'] == objected_node:
                pair_ls.append(row['TermNode'])
        for index, row in pair_df_Out.iterrows():
            if row['InNode'] == objected_node or row['TermNode'] == objected_node:
                pair_ls.append(row['InNode'])
        #print(str(objected_node),pair_ls)
        notated_arrays.append(get_bool_array_from_index(pair_ls,gene_sym_ls))

    main_array = np.array(gene_sym_ls, dtype=object)
    main_array = np.insert(main_array,0,'Gene_Symb')
    for array_index in range(len(notated_arrays)):
        wo_in_object_array=np.asarray(notated_arrays[array_index],object)
        name_inc_bool_array=np.insert(wo_in_object_array,0,gene_sym_ls[array_index])
        main_array=np.vstack((main_array,name_inc_bool_array))
    return main_array


'''
if __name__ == '__main__':
    get_paths(str(os.getcwd())+'/example_dbs/53453_confidence_db',str(os.getcwd())+'/example_dbs/53454_prototype_db')
'''