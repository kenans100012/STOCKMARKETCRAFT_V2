#Main_Page
import os
from business_logic import *
dir=r"D:\Shaun\Documents\Comp_Project"
os.chdir(dir)
print("Enter the option")
print("1 for Register")
print("2 for Login")
print("3 for Add Money")
print("4 for My Stocks")
print("5 for All Stocks")
option_id=int(input("Enter your Option : "))
if option_id==1:
    email_id=input("Enter your email ID : ")
    user_id=input("Enter the user ID you want to use : ")
    first_name=input("Enter your first name : ")
    last_name=input("Enter your last name : ")
    passw=input("Enter your password : ")
    confirm_password=input("Reconfirm your password : ")
    bl_function='register'
    Error_code=""
    bl_function,email_id,user_id,first_name,last_name,passw,Error_code=bl_main(bl_function,email_id,user_id,first_name,last_name,passw,Error_code)
    #print("Error Code: ",Error_code)
  