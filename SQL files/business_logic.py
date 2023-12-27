#business logic
import os
dir=r"D:\Shaun\Documents\Comp_Project"
os.chdir(dir)
from DL_register import *
from DL_login import *
def bl_main(bl_function,email_id,user_id,first_name,last_name,passw,Error_code):
    if bl_function=='register':
        access_mode="INSERT"
        access_mode,email_id,user_id,first_name,last_name,Error_code=bl_register(access_mode,email_id,user_id,first_name,last_name,Error_code)
        #access_mode,user_id,passw,Error_code=bl_login(access_mode,user_id,passw,Error_code)
        return(bl_function,email_id,user_id,first_name,last_name,Error_code)
    
def bl_register(access_mode,email_id,user_id,first_name,last_name,Error_code):
    access_mode,email_id,user_id,first_name,last_name,Error_code=DL_register_main(access_mode,email_id,user_id,first_name,last_name,Error_code)
    return(access_mode,email_id,user_id,first_name,last_name,Error_code)

#def bl_login(access_mode,user_id,passw,Error_code):
    access_mode,user_id,passw,Error_code=DL_login_main(access_mode,user_id,passw,Error_code)
    return(access_mode,user_id,passw,Error_code)