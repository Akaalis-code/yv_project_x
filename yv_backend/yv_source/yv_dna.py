import yv_custom_logger as log

var_running_file_name = __name__

obj_log = log.cls_custom_logger(var_running_file_name)
obj_log.mth_create_a_log_file("my_first_logs","./yv_dump_logs/")
obj_log.log_it("LOG","my_first_log")

class cls_parent:
    def __init__(self,para_generation,para_unique_id_in_that_gen,para_dna_structure):
        self.var_generation = str("G")+str(para_generation)
        self.var_unique_id_as_a_whole = str(self.var_generation)+str(para_unique_id_in_that_gen)
        self.var_dna_structure = para_dna_structure




class cls_child:
    def __init__(self , para_parent_1 , para_parent_2 , para_num_of_children):
        self.var_parent_1 = para_parent_1
        self.var_parent_2 = para_parent_2
        self.var_num_of_children = para_num_of_children

    def mth_next_gen(self):
        next_gen_genes_list=[]
        for i in range(0,self.var_num_of_child_genes):
            for j in range(0,len(self.var_parent_gene_1.var_dna_structure):



