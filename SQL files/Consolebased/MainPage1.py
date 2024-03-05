import time
import os
import pythonsql
import stockpredictor
import simulation


#homepage
def homepage():
    print("+==================================+")
    print("|\t\033[1;10mSTOCK MARKETCRAFT PRO\033[10m      |")
    print("+==================================+")
    print("|             "+"\033[3mSIMULATION\033[0m","           |")
    print("|             "+"\033[3mPREDICTION\033[0m","           |")
    print("|             "+"\033[3mRANKS\033[0m","                |")
    print("|             "+"\033[3mQuit\033[0m","                 |")
    print("+==================================+")

    print("\033[2mEnter Simulation or Prediction or Ranks or Quit:\033[0m ")

#Method to display the login/register page
def login_register():
  
    print("+==================================+")
    print("|\t\033[1;10mSTOCK MARKETCRAFT PRO\033[10m      |")
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

login_register()
choice = input()
choice =choice.lower()

#Method to print the login page
def login_page():
    print("+==================================+")
    print("|\t\033[1;10mSTOCK MARKETCRAFT PRO\033[10m      |")
    print("+==================================+")
    print("\t  UserId:",end="")
    userid = input()
    print("\t\033[3m  Password:\033[0m",end="")
    password = input()
    time.sleep(2)
    os.system('cls')
    data =pythonsql.helper.fetch_all()
    c=False
    for i in range(len(data)):
        if data[i][0] == userid:
                if data[i][4]== password:                    
                    print("\033[3m=====================================\033[0m")
                    print("\033[3m**********LOGIN SUCCESS**************\033[0m")
                    print("\033[3m=====================================\033[0m")
                    time.sleep(2)
                    os.system('cls')
                    return True,userid
                       
    print("\033[3m=================================================\033[0m")
    print("\033[3m    USERID or PASSWORD ENTERED DOES NOT EXIST    \033[0m")
    print("\033[3m=================================================\033[0m")
    time.sleep(2)
    os.system('cls') 
    login_page()
    
def get_userid(userID):
    return userID
    

#REGISTER PAGE        
def register_page():
    print("+==================================+")
    print("|\t\033[1;10mSTOCK MARKETCRAFT PRO\033[10m      |")
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
        login_page()
        
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

    # Fetch historical stock data
    stock_data = stockpredictor.get_stock_data(stock_symbol)

    if stock_data.empty:
        print(f"Could not fetch data for {stock_symbol}. Please check the stock symbol and try again.")
    else:
        # Prepare data for training
        processed_data = stockpredictor.prepare_data(stock_data)

        # Train the model
        model = stockpredictor.train_model(processed_data)

        # Predict stock movement for the next day
        last_record = processed_data.tail(1)
        input_data = last_record[['1. open', '2. high', '3. low', '5. volume']].values[0]
        predicted_close = stockpredictor.predict_movement(model, input_data)

        # Display the prediction
        print(f"Predicted Close Price for {stock_symbol} next day: {predicted_close:.2f}")
        if predicted_close > last_record['4. close'].values[0]:
            print(f"The stock is predicted to rise by {((predicted_close - last_record['4. close'].values[0]) / last_record['4. close'].values[0]) * 100:.2f}%.")
        else:
            print(f"The stock is predicted to fall by {((last_record['4. close'].values[0] - predicted_close) / last_record['4. close'].values[0]) * 100:.2f}%.")
    
def simulationSTOCKS():
    while(True):
                    print("\033[3m+===============================================+\033[0m")
                    print("\033[4m|     STOCK MARKETCRAFT PRO SIMULATION PAGE     |\033[0m")
                    print("\033[3m+===============================================+\033[0m")
                    print("\033[3m|                 1.BUY STOCK                   |\033[0m")
                    print("\033[3m|                 2.SELL STOCK                  |\033[0m")
                    print("\033[3m|                 3.DISPLAY PROFILE             |\033[0m")
                    print("\033[3m|                 4.DISCOVER STOCKS             |\033[0m")
                    print("\033[3m|                 5.BACK                        |\033[0m")
                    print("\033[3m|                 6.QUIT PROGRAM                |\033[0m")
                    print("\033[3m+===============================================+\033[0m")
                     
                    choiceSIM = input("Enter your choice (1-6): ")
                    if choice ==1:
                         user_id = int(input("Enter your user ID: "))
                         stock_symbol = input("Enter the stock symbol: ")
                         quantity = int(input("Enter the quantity to buy: "))
                         simulation.buy_stock(user_id, stock_symbol, quantity)
                    elif choice == '2':
                         
                         stock_symbol = input("Enter the stock symbol: ")
                         quantity = int(input("Enter the quantity to sell: "))
                         simulation.sell_stock(user_id, stock_symbol, quantity)

                    elif choice == '3':
                        user_id = int(input("Enter your user ID: "))
                        simulation.display_portfolio(user_id)

                    elif choice == '4':
                        stock_symbol = input("Enter the stock symbol : ")
                        simulation.plotgraph(stock_symbol)
                        simulation.display_stock_price(stock_symbol)

                    elif choice == '5':
                        break

                    else:
                        print("Invalid choice. Please enter a number between 1 and 5.")


while(True):
    if (choice == "login"):
        show_loading_page(f"Loading Login page", dots=5, delay=0.5)
        time.sleep(0.5)
        os.system('cls')
        bool1= False
        bool1 , uid =login_page()
        if(bool1 ==True):
            homepage()
            homechoice = input().upper()
            if homechoice =="SIMULATION":
                    simulationSTOCKS()
            elif homechoice =='PREDICTION':
              
                    stockpredictor1()
                    break
                    
            else:
                 login_page()
                
    elif(choice == "register"):
        show_loading_page(f"Loading Register page", dots=5, delay=0.5)
        time.sleep(0.5)
        os.system('cls')
        register_page()
    elif(choice =="quit"):
        show_loading_page(f"Quiting program", dots=5, delay=0.5)
        exit()