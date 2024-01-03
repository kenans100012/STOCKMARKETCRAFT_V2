import yfinance as yf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pytz
import time

# Function to get historical stock data
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Function to create features and labels
def create_features_labels(data):
    data['Price_Up'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)
    X = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    y = data['Price_Up']
    return X, y

# Function to train and evaluate the model
def train_evaluate_model(X_train, y_train, X_test, y_test):
    # Standardize the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train the RandomForestClassifier
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train_scaled, y_train)

    # Make predictions
    predictions = model.predict(X_test_scaled)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)
    return model, scaler

# Function to predict the next day's movement
def predict_next_day_movement(model, scaler, data):
    last_data_point = data.iloc[-1][['Open', 'High', 'Low', 'Close', 'Volume']].values.reshape(1, -1)
    last_data_point_scaled = scaler.transform(last_data_point)
    prediction = model.predict(last_data_point_scaled)
    return "Up" if prediction == 1 else "Down"

if __name__ == "__main__":
    # Specify the stock symbol, start date, and end date
    stock_symbol = "AAPL"
    start_date = "2022-01-01"
    end_date = "2023-12-31"

    # Get historical stock data
    stock_data = get_stock_data(stock_symbol, start_date, end_date)

    # Convert timestamps to a specific time zone (e.g., New York)
    stock_data.index = stock_data.index.tz_localize('UTC').tz_convert('Asia/Kolkata')

    # Create features and labels
    X, y = create_features_labels(stock_data)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model, scaler = train_evaluate_model(X_train, y_train, X_test, y_test)

    # Predict the next day's movement
    prediction = predict_next_day_movement(model, scaler, stock_data)
    
    print(f"Predicted movement for the next day: {prediction}")
def simulate_stock_increase(initial_value, increase_rate, duration):
    current_value = initial_value
    print(f"Initial Stock Value: ${current_value}")

    for _ in range(duration):
        time.sleep(1)  # Simulating a one-second interval
        current_value *= (1 + increase_rate)
        print(f"Current Stock Value: ${current_value:.2f}")

    return current_value

# Example usage
initial_stock_value = 100.0
rate_of_increase = 0.02  # 2% increase per second
simulation_duration = 5  # Run for 5 seconds

final_stock_value = simulate_stock_increase(initial_stock_value, rate_of_increase, simulation_duration)

print(f"Final Stock Value: ${final_stock_value:.2f}")