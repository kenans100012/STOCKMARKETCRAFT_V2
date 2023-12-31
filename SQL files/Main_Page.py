#Main_Page
import random
import smtplib
import os
from business_logic import *
from User_Business_Logic import *
dir=r"D:\Repos\STOCKMARKETCRAFT_V2\ACTUAL_SQL_FILES_2000"
os.chdir(dir)
email_id,user_id,first_name,last_name,passw,Error_code='0','0','0','0','0','0'
print("Enter the option")
print("1 for Register")
print("2 for Login")
print("3 for reset password")
print("9 for logging out/exit")
option_id=int(input("Enter your Option : "))
if option_id!=1 and option_id!=2 and option_id!=3 and option_id!=9:
   print("Wrong output")
   exit()
if option_id==9:
   print("Have a good day")
   exit()

if option_id==1:
    email_id=input("Enter your email ID : ")
    user_id=input("Enter the user ID you want to use : ")
    first_name=input("Enter your first name : ")
    last_name=input("Enter your last name : ")
    passw=input("Enter your password : ")
    confirm_password=input("Reconfirm your password : ")
    if not passw==confirm_password:
        print("Both Passwords are not matching")
        exit()
    bl_function='register'
    Error_code=None
    print("Error code ",Error_code )
    bl_function,email_id,user_id,first_name,last_name,passw,Error_code=bl_main(bl_function,email_id,user_id,first_name,last_name,passw,Error_code)
    if Error_code==None:
        print("Successfully Registered")
        print("2 for Login")
        print("9 for logging out/exit")
        option_id=int(input("Enter your Option : "))
    elif Error_code[7:8]=='1':
        print("Error, Email ID already exists, please register")
    else:
        print("Error, User ID already exists, please register")
if option_id==9:
   exit() 

if option_id==2:
    bl_function='login'
    user_id=input("Enter the user ID : ")
    passwd1=input("Enter your password : ")
    passw=passwd1
    Error_code=None
    user_id,passw,Error_code=bl_main(bl_function,'',user_id,'','',passw,Error_code)
    if passw!=passwd1 or Error_code==1:
       print("Error, Wrong User id or password")
    else:
        print("Successfully logged in")
        print("4 for Add Money")
        print("5 for All Stocks")
        print("6 for My Stocks")
        print("9 for logging out/exit")
        option_id=int(input("Enter your option: "))
        if option_id!=4 and option_id!=5 and option_id!=6 and option_id!=9:
           print("Wrong output")
           exit()
        if option_id==9:
           exit()
        if option_id==4:
           bank_money,tot_money,stock_purch,add_money=100000,0,0,0
           user_id,tot_money,stock_purch,add_money=ubl_money(user_id,tot_money,stock_purch,add_money)
           print("Money In Wallet:",tot_money)
           print("Remaining Amount: ",tot_money-stock_purch)
           print("Purchased Amount",stock_purch)
           print("2 for Adding Money")
           print("9 for loggin out/exit")
           option_id=int(input("Enter your option: "))
           if option_id!=2 and option_id!=9:
              print("Wrong output")
              exit()
           if option_id==9:
              exit()
           if option_id==2:
              add_money=int(input("Enter how much to add : ")) 
              Error_code,add_money,user_id,tot_money,stock_purch=ubl_money2(Error_code,add_money,user_id,tot_money,stock_purch)  
              if Error_code=="1":
                 print("Cannot add anymore, Max Amount reached")   
              if Error_code=="2":
                 print("Amount added is overlimit, Reduce Amount")  
                 print("Max amount that can be added: ",bank_money-tot_money)
              else:
                 print("Amount Added")
                 print("Total Amount: ",tot_money)

if option_id==3:
    otp=''.join([str(random.randint(0,9)) for i in range(4)])
    print ("otp -",otp)
    bl_function='reset'
    email_id=input("Enter your registered email ID: ")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('stockappbeta@gmail.com','ikhlpqbnwazvltap')
    server.sendmail('stockappbeta@gmail.com',email_id,otp)
    otp_enter=input("Check your email and enter the OTP : ")
    if otp==otp_enter:
       print("OTP matches")
       passw=input("Enter your password : ")
       confirm_password=input("Reconfirm your password : ")
       if not passw==confirm_password:
        print("Both Passwords are not matching")
        exit() 

    Error_code=None
    bl_function,email_id,user_id,first_name,last_name,passw,Error_code=bl_main(bl_function,email_id,user_id,first_name,last_name,passw,Error_code)  
    exit() 
