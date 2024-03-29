import time
import os
import pythonsql
import stockpredictor
import simulation
global userid
#homepage
def homepage():
    print("+==================================+")
    print("|             "+"\033[1;10mVULCAN X\033[10m"+"             |")
    
    print("+==================================+")
    print("|             "+"\033[3mSIMULATION\033[0m","          |")
    print("|             "+"\033[3mPREDICTION\033[0m","          |")
    print("|             "+"\033[3mQuit\033[0m","                |")
    print("+==================================+")

    print("\033[2mEnter Simulation or Prediction or Quit:\033[0m ")

#Method to display the login/register page
def login_register():
 # print("| \t\033[1;10m      VULCAN X       \033[10m      |")
    print("+==================================+")
    print("|             "+"\033[1;10mVULCAN X\033[10m"+"             |")
    print("+==================================+")
    print("|             "+"\033[3mLOGIN\033[0m","               |")
    print("|             "+"\033[3mRegister\033[0m","            |")
    print("|             "+"\033[3mQuit\033[0m","                |")
    print("+==================================+")

    print("\033[2mEnter Login or Register or Quit:\033[0m ")
    

#Method for the loading page...
def show_loading_page(message, dots=4, delay=0.5):
    print(message, end='', flush=True)
    for _ in range(dots):
        time.sleep(delay)
        print('.', end='', flush=True)
    print()

#Method to print the login page
def login_page():
   
    print("+==================================+")
    print("|             "+"\033[1;10mVULCAN X\033[10m"+"             |")
    print("+==================================+")
    print("\t  UserId:",end="")
    userid = input()
    print("\t\033[3m  Password:\033[0m",end="")
    password = input()
    time.sleep(1.24)    
    os.system('cls')
    data =pythonsql.helper.fetch_all() #Fetches all information (userid, email, first name,second name and password)
    for i in range(0,len(data)):
        if data[i][0] == userid:
                if data[i][4]== password:                 
                    print("\033[3m=====================================\033[0m")
                    print("\033[3m**********LOGIN SUCCESS**************\033[0m")
                    print("\033[3m=====================================\033[0m")
                    time.sleep(2)                    
                    os.system('cls')                   
                    return userid 
                
    print("\033[3m=================================================\033[0m")
    print("\033[3m    USERID or PASSWORD ENTERED DOES NOT EXIST    \033[0m")
    print("\033[3m=================================================\033[0m")
    time.sleep(5)
    os.system('cls') 
    return None
                
                
                    
def get_userid(userID):
    return userID
    

#REGISTER PAGE        
def register_page():
    print("+==================================+")
    print("|             "+"\033[1;10mVULCAN X\033[10m"+"             |")
    print("+==================================+")
    print("\t  UserId:",end="")
    uid = int(input())
    print("\t  EmailI:",end="")
    eid = input()
    print("\t  First Name:",end="")
    firstname1 = input()
    print("\t  Second Name:",end="")
    lastname1 = input()
    print("\t  Create Password:",end="")
    pwd = input()
    print("\t  Confirm Password:",end="")
    confirmpwd = input()
    print("====================================")
    time.sleep(2)
    os.system('cls')
    if confirmpwd == pwd:
        pythonsql.helper.insert_user(uid,eid,firstname1,lastname1,pwd)
        os.system('cls')
        return 1
        
    else:
        print("\033[3m=================================================\033[0m")
        print("\033[3m        PASSWORD ENTERED DOES NOT MATCH          \033[0m")
        print("\033[3m=================================================\033[0m")
        time.sleep(2)
        os.system('cls')
        register_page()
        
def stockpredictor1():
    
    # Get user input for stock symbol
    stock_symbol = input("Enter the stock symbol: ").upper()
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    # Fetch historical stock data   
    stock_data = stockpredictor.get_stock_data(stock_symbol,start_date,end_date)
   

    if stock_data.empty:
        print(f"Could not fetch data for {stock_symbol}. Please check the stock symbol and try again.")
    else:
        processed_data = stockpredictor.prepare_data(stock_data)

        # Train the model
        model = stockpredictor.train_model(processed_data)

        # Predict stock movement for the next day
        last_record = processed_data.tail(1) #retreives the last record , the latest day historical data
        input_data = last_record[['Open', 'High', 'Low', 'Volume']].values[0] #RETURNS NUMPY array [single row]
        predicted_close = stockpredictor.predict_movement(model, input_data)
        
        # Display the prediction
        print(f"Predicted Close Price for {stock_symbol} next day: {predicted_close:.2f}")
        if predicted_close > last_record['Close'].values[0]:
            print(f"The stock is predicted to rise by {((predicted_close - last_record['Close'].values[0]) / last_record['Close'].values[0]) * 100:.2f}%.")
        else:
            print(f"The stock is predicted to fall by {((last_record['Close'].values[0] - predicted_close) / last_record['Close'].values[0]) * 100:.2f}%.")
        print("   ")
        print("   ")
        print("   ")



def simulationSTOCKS(user_id):
    while(True):
                  
                    
                    print("\033[3m+===============================================+\033[0m")
                    print("|             "+"\033[1;10mVULCAN X\033[10m"+"                          |")
                    print("\033[3m+===============================================+\033[0m")
                    print("\033[3m|                 1.BUY STOCK                   |\033[0m")
                    print("\033[3m|                 2.SELL STOCK                  |\033[0m")
                    print("\033[3m|                 3.DISPLAY PROFILE             |\033[0m")
                    print("\033[3m|                 4.DISCOVER STOCKS             |\033[0m")
                    print("\033[3m|                 5.BACK                        |\033[0m")
                    print("\033[3m|                 6.QUIT PROGRAM                |\033[0m")
                    print("\033[3m+===============================================+\033[0m")
                    
                    
                    choice = int(input("Enter your choice (1-6): "))
                    if choice ==1:
                        
                         stock_symbol = input("Enter the stock symbol: ")
                         quantity = int(input("Enter the quantity to buy: "))
                         simulation.buy_stock(user_id, stock_symbol, quantity)
                         print()                 
                         print("=================================================")
                         print()
                         
                    elif choice == 2:
                         
                         stock_symbol = input("Enter the stock symbol: ")
                         quantity = int(input("Enter the quantity to sell: "))
                         simulation.sell_stock(user_id, stock_symbol, quantity)
                         print()                 
                         print("=================================================")
                         print()

                    elif choice == 3:
                      #  user_id = int(input("Enter your user ID: "))
                        simulation.display_portfolio(user_id)

                    elif choice == 4:
                        stock_symbol = input("Enter the stock symbol : ")
                        simulation.plotgraph(stock_symbol)
                        simulation.display_stock_price(stock_symbol)

                    elif choice == 5:
                     
                        break
                    elif choice ==6:
                        exit()

                    else:
                        print("Invalid choice. Please enter a number between 1 and 5.")
                        


#MAIN CODING                       
while True:
    login_register()
    choice = input().lower()

    if choice == "login":
        show_loading_page(f"Loading Login page", dots=5, delay=0.5)
        time.sleep(0.5)
        os.system('cls')
        user_id = login_page()
        if user_id is not None:
            while True:
                homepage()
                homechoice = input().upper()
                if homechoice == "SIMULATION":
                           
                    print("=================================================")
                    print()
                    simulationSTOCKS(user_id)
                elif homechoice == 'PREDICTION':
                    stockpredictor1()
                elif homechoice == 'QUIT':
                    exit()
                else:
                    login_page()


    elif choice == "register":
        show_loading_page(f"Loading Register page", dots=5, delay=0.5)
        time.sleep(0.5)
        os.system('cls')
        if register_page()==1:
            continue

    elif choice == "quit":
        show_loading_page(f"Quitting program", dots=5, delay=0.5)
        exit()

    else:
        print("Invalid choice. Please enter 'login', 'register', or 'quit'.") 
                        

