import mysql.connector
import yfinance as yf
import time
from decimal import *
import threading
import datetime
import matplotlib.pyplot as plt
    

def plotgraph(ticker):
    
    # = input('Enter Ticker Symbol of Company')
    end = datetime.datetime.today() - datetime.timedelta(days=2)
    start = datetime.datetime(2023,12,1)

    data = yf.download(ticker,start,end)

    plt.figure(figsize=(12,6)) #plot
    plt.plot(data.Close)
    plt.show()
    


# Connect to MySQL database
def connect_to_database():
   return mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Zaqws@2025',
    database='pythonstore'
)


# Function to get real-time stock price from Alpha Vantage
def get_stock_price(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.info
        if 'currentPrice' in stock_info:
            stock_price = Decimal(stock_info['currentPrice']) #DICTIONARY 
            return stock_price
        else:
            print(f"Failed to get current price for {stock_symbol}.") #IF STOCK DOESNT EXIST
            print(f"Stock Info: {stock_info}")
            return None

    except Exception as e:
        print(f"Error fetching data from yfinance: {e}")
        return None

# Function to display the current price of a specific stock symbol directly from the API
def display_stock_price(stock_symbol):
    current_price = get_stock_price(stock_symbol)

    if current_price is not None:
        print(f"\nCurrent Price of {stock_symbol}: ${current_price:.2f}") #2 decimal places
    else:
        print(f"Unable to fetch current price for {stock_symbol}.")

# Function to continuously update stock prices in the background
def update_stock_prices_background():
    while True:
        cursor.execute('SELECT DISTINCT stock_symbol FROM transactions')
        symbols = [row[0] for row in cursor.fetchall()] #LIST OF ALL THE DISCTINCT SYMBOLS

        for symbol in symbols:
            current_price = get_stock_price(symbol)

            if current_price is not None:
                cursor.execute('INSERT INTO stocks (stock_symbol, current_price) VALUES (%s, %s) ON DUPLICATE KEY UPDATE current_price = %s', (symbol, current_price, current_price))
                conn.commit()

        time.sleep(3600)

# Function to buy stocks
def buy_stock(user_id, stock_symbol, quantity):
    stock_price = get_stock_price(stock_symbol)
    if stock_price is None:
        print("Failed to get stock price. Try again later.")
        return

    total_cost = quantity * Decimal(stock_price)

    # Check if the user exists
    cursor.execute('SELECT balance FROM users WHERE user_id = %s', (user_id,))
    result = cursor.fetchone() #TUPLE containing all balances of said user

    if result is None:
        cursor.execute('INSERT INTO users (user_id, balance) VALUES (%s, %s)', (user_id, 100000.0))
        conn.commit() #IF USER DOESNT EXIST ADDS USERID AND ADDS A BALANCE OF 100K
        user_balance = Decimal(100000.0)
    else:
        user_balance = Decimal(result[0]) #If user exists, it takes the existing balance

    if total_cost > user_balance:
        print("Insufficient funds.")
        return
    new_balance = user_balance - total_cost
    cursor.execute('UPDATE users SET balance = %s WHERE user_id = %s', (new_balance, user_id))

    cursor.execute('''
        INSERT INTO transactions (user_id, stock_symbol, quantity, price, transaction_type)
        VALUES (%s, %s, %s, %s, 'buy')
    ''', (user_id, stock_symbol, quantity, stock_price))

    conn.commit()

    print(f"\nRemaining Money: ${new_balance:.2f}")

    print(f"You successfully bought {quantity} shares of {stock_symbol} at ${stock_price:.2f} each.")

# Function to sell stocks
def sell_stock(user_id, stock_symbol, quantity):
    stock_price = get_stock_price(stock_symbol)
    if stock_price is None:
        print("Failed to get stock price. Try again later.")
        return
    cursor.execute('SELECT balance FROM users WHERE user_id = %s', (user_id,))
    result = cursor.fetchone()

    if result is None:
        print(f"User with ID {user_id} not found.")
        return

    user_balance = Decimal(result[0])

    total_earnings = quantity * Decimal(stock_price)
    new_balance = user_balance + total_earnings

    cursor.execute('UPDATE users SET balance = %s WHERE user_id = %s', (new_balance, user_id))

    cursor.execute('''
        INSERT INTO transactions (user_id, stock_symbol, quantity, price, transaction_type)
        VALUES (%s, %s, %s, %s, 'sell')
    ''', (user_id, stock_symbol, quantity, stock_price))

    conn.commit()

    print(f"\nRemaining Money: ${new_balance:.2f}")

    print(f"You successfully sold {quantity} shares of {stock_symbol}.")

# Function to display user portfolio
def display_portfolio(user_id):
    cursor.execute('SELECT balance FROM users WHERE user_id = %s', (user_id,))
    result_balance = cursor.fetchone()

    if result_balance is None:
        print(f"User with ID {user_id} not found.")
        return

    user_balance = result_balance[0]

    cursor.execute('''
        SELECT t.stock_symbol, 
               SUM(CASE WHEN t.transaction_type = 'buy' THEN t.quantity ELSE -t.quantity END) as total_quantity,
               AVG(t.price) as avg_price
        FROM transactions t
        WHERE t.user_id = %s
        GROUP BY t.stock_symbol
    ''', (user_id,))

    portfolio = cursor.fetchall()

    if not portfolio:
        print("Your portfolio is empty.")
    else:
        print("\nYour Portfolio:")
        print("Stock Symbol | Total Quantity | Current Price | Total Value")
        print("-" * 60)

        total_portfolio_value = Decimal(0)

        for stock in portfolio:
            stock_symbol = stock[0]
            total_quantity = int(stock[1])  
            current_price = get_stock_price(stock_symbol)

            if current_price is not None:
                total_value = total_quantity * current_price
                total_portfolio_value += Decimal(total_value)

                print(f"{stock_symbol:<12} | {total_quantity:<14} | ${current_price:.2f}          | ${total_value:.2f}")
            else:
                print(f"Unable to fetch current price for {stock_symbol}.")
            total_portfolio_value = total_portfolio_value.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
        print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")

    user_balance = Decimal(user_balance).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    print(f"\nRemaining Money: ${user_balance:.2f}")
    print("Account Value: ",user_balance+total_portfolio_value)


def get_user_balance(user_id):
    cursor.execute('SELECT balance FROM users WHERE user_id = %s', (user_id,))
    result_balance = cursor.fetchone()

    if result_balance is not None:
        return result_balance[0]
    else:
        print(f"User with ID {user_id} not found.")
        return None

conn = connect_to_database()
cursor = conn.cursor()

#Schedule the update_stock_prices_background function to run in the background
update_thread = threading.Thread(target=update_stock_prices_background)
update_thread.daemon = True
update_thread.start()