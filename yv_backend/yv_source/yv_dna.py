import yv_custom_logger as log

var_running_file_name = __name__


obj_test = log.cls_custom_logger(var_running_file_name)
obj_test.mth_create_a_log_file("my_first_logs","./yv_dump_logs/")
obj_test.log_it("LOG","my_first_log")