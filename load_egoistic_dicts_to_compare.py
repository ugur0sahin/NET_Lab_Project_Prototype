import os
import pickle

path_of_diminished = os.getcwd()+"/actual_databases/Graph_HIPPIE_confidence_075_diminished_dictionary_db.pkl"
path_of_diminished_pruned = os.getcwd()+"/actual_databases/Graph_HIPPIE_confidence_075_diminished_pruned_dictionary_db.pkl"

file_dim_pruned = open(path_of_diminished_pruned, "rb")
#dict_egoistic_db_diminished=pickle.Unpickler(file_dim_pruned).load()
dict_egoistic_db_diminished = pickle.load(file_dim_pruned)
file_dim_pruned.close()

file_dim = open(path_of_diminished, "rb")
#dict_egoistic_db_diminished_pruned=pickle.Unpickler(file_dim).load()
dict_egoistic_db_diminished_pruned = pickle.load(file_dim)
file_dim.close()

ls= dict_egoistic_db_diminished_pruned["UBE2N"].keys()
for i in ls:
    print(i)
