#money base
from decimal import Decimal
from mysql.connector import connect, Error
import os
dir = r"D:\Repos\STOCKMARKETCRAFT_V2\ACTUAL_SQL_FILES_2000"
os.chdir(dir)
db_connection = None
db_config = {
        'host': '127.0.0.1',
        'user': 'stockboi',
        'password': 'shaunjosephn@gmail.com',
        'database': 'stockapp',
    }
def connect_to_database():
    global db_connection
    try:
        db_connection = connect(**db_config)
        print("Connected to the database")
        return db_connection
    
    except Error as err:
        print(f"Error: {err}")
        Error_code = f"Error: {err.args[0]}"
        return Error_code


def close_connection():
    global db_connection
    if db_connection:
        db_connection.close()
        print("Connection closed")


def insert_user_money(user_id, tot_money,stock_purch):
    global db_connection
    cursor = db_connection.cursor()
    insert_query = '''
        INSERT INTO sa_money (User_ID, Tot_Amt, Stock_Pur)
        VALUES (%s, %s, %s, %s)
        '''
    data = (user_id, Decimal(tot_money), Decimal(stock_purch))
    cursor.execute(insert_query, data)
    db_connection.commit()
    cursor.close()
    return(user_id, tot_money,stock_purch)
    

def user_exists_money(user_id, tot_money,stock_purch,add_money):
    connect_to_database()
    global db_connection
    cursor = db_connection.cursor(dictionary=True)
    select_query = '''
        SELECT User_ID, Tot_Amt, Stock_Pur
        FROM sa_money
        WHERE User_ID = %s
     '''
    cursor.execute(select_query, (user_id,))
    existing_user = cursor.fetchone()

    if not existing_user:
        insert_user_money(user_id,tot_money,stock_purch)
        db_connection.commit()
        cursor.execute(select_query, (user_id,))
        existing_user = cursor.fetchone()
        cursor.close()
        close_connection()
        return (user_id,tot_money,stock_purch,add_money)
     
    if existing_user:
        tot_money=existing_user["Tot_Amt"]
        stock_purch=existing_user["Stock_Pur"]
        user_id, tot_money,stock_purch,add_money=update_user_money(user_id, tot_money,stock_purch,add_money)  
        close_connection()
        return(user_id, tot_money,stock_purch,add_money)


def update_user_money(user_id, tot_money,stock_purch,add_money):
    global db_connection
    cursor = db_connection.cursor() 
    tot_money+=add_money
    update_query="UPDATE sa_money set Tot_Amt = %s, Stock_Pur = %s where User_ID = %s"      
    cursor.execute(update_query,(tot_money,stock_purch,user_id,))
    db_connection.commit()
    return(user_id, tot_money,stock_purch,add_money)