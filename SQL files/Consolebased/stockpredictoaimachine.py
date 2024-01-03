
import yfinance as yf
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from joblib import load  # Use this import statement for scikit-learn 0.23 and later
import pytz

# ... (rest of the code remains unchanged)

# Load the trained model and scaler
model_path = 'path_to_your_trained_model.pkl'
scaler_path = 'path_to_your_trained_scaler.pkl'

model = load(model_path)
scaler = load(scaler_path)


# Function to get the latest stock data
def get_latest_stock_data(ticker):
    live_data = yf.Ticker(ticker)
    return live_data.history(period="1d")

# Function to create features
def create_features(data):
    data['Price_Up'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)
    X = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    return X

# Function to standardize features
def standardize_features(X, scaler):
    return scaler.transform(X)

# Function to predict the next day's movement and rate
def predict_next_day_movement(model, X_scaled):
    prediction = model.predict(X_scaled)
    probability = model.predict_proba(X_scaled)[0][1]
    return prediction, probability

if __name__ == "__main__":
    # Specify the stock symbol
    stock_symbol = "AAPL"

    # Get the latest stock data
    live_data = get_latest_stock_data(stock_symbol)

    # Convert timestamps to a specific time zone (e.g., New York)
    live_data.index = live_data.index.tz_convert('Asia/Kolkata')

    # Create features
    X_live = create_features(live_data)

    # Load the trained model and scaler
    model = RandomForestClassifier(random_state=42)
    scaler = StandardScaler()

    # Load the model and scaler from the training phase
    # Replace this with the actual paths to your saved model and scaler
    model_path = 'path_to_your_trained_model.pkl'
    scaler_path = 'path_to_your_trained_scaler.pkl'

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    # Standardize features
    X_live_scaled = standardize_features(X_live, scaler)

    # Predict the next day's movement and rate
    prediction, probability = predict_next_day_movement(model, X_live_scaled)
    
    if prediction == 1:
        movement = "Up"
    else:
        movement = "Down"

    print(f"Predicted movement for the next day: {movement}")
    print(f"Probability: {probability:.2%}")
