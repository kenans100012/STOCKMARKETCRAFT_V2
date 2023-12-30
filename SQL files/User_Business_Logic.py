#User Business Logic
import os
dir=r"D:\Shaun\Documents\Comp_Project"
os.chdir(dir)
from Money_Base import *
def ubl_money(user_id,tot_money,stock_purch,add_money):
    user_id,tot_money, stock_purch,add_money=user_exists_money(user_id,tot_money, stock_purch,add_money)
    return(user_id,tot_money, stock_purch,add_money)
def ubl_money2(Error_code,add_money,user_id,tot_money, stock_purch):
    if tot_money==100000.00:
        Error_code="1"
        return(Error_code,add_money,user_id,tot_money, stock_purch)
    else:
        if tot_money+add_money>100000:
            Error_code="2"
            return(Error_code,add_money,user_id,tot_money, stock_purch)
        else:
            user_id,tot_money, stock_purch,add_money=user_exists_money(user_id,tot_money, stock_purch,add_money)
            return(Error_code,add_money,user_id,tot_money, stock_purch)