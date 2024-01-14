from datetime import datetime


class cls_custom_logger:
    def __init__(self,para_running_file_name):
        self.var_running_file_name = para_running_file_name
    def mth_create_a_log_file(self , para_log_file_name , para_log_file_path):
        self.var_log_file_name = str(para_log_file_path)+str(para_log_file_name)+str(datetime.now().strftime("%Y%m%d%H%M%S"))
        print("Your Log file name is : "+str(self.var_log_file_name))

        try:
            with open(self.var_log_file_name, "w") as f: 
                f.write("Starting log file \n")
        except :
            print("Your Log file name creation had some issue")
    def log_it(self , para_log_type , para_log_msg):
        try:
            var_log_msg = str(para_log_type)+" | "+str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))+" | "+str(self.var_running_file_name)+" | "+str(para_log_msg)+"\n"
            with open(self.var_log_file_name, "a") as f: 
                f.write(var_log_msg)
        except : 
            print("Your Log file name write had some issue")
