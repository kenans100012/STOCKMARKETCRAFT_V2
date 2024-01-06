import os
import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Function to fetch historical stock data using Alpha Vantage API
def get_stock_data(symbol):
    api_key = "BBKKPSDUF19ZKSJW"
    ts = TimeSeries(key=api_key, output_format='pandas') #OUTPUT IS PANDAS DATASTRUCTURE FORMAT
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
    #print(meta_data)
    return data

# Function to preprocess and prepare data for training
def prepare_data(data):
    data['Date'] = pd.to_datetime(data.index)
    data['Next_Close'] = data['4. close'].shift(-1)  # Shift close prices to get the next day's closing price
    data['Movement'] = np.where(data['Next_Close'] > data['4. close'], 1, 0)  # 1 for rise, 0 for fall
    data = data.dropna()
    return data

# Function to train a linear regression model
def train_model(data):
    X = data[['1. open', '2. high', '3. low', '5. volume']]
    y = data['Next_Close']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define numeric features for scaling
    numeric_features = X.columns

    # Create a column transformer for numeric features
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features)
        ])

    # Create a pipeline with the column transformer and the linear regression model
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

    return model

# Function to predict stock movement for the next day
def predict_movement(model, input_data):
    # Convert input data to DataFrame with correct column names
    input_df = pd.DataFrame([input_data], columns=['1. open', '2. high', '3. low', '5. volume'])
    prediction = model.predict(input_df)[0] #inputed model uses the predict function to predict a list of prediction which later returns index 0 (first index of list)
    return prediction

'''if __name__ == "__main__":
    # Get user input for stock symbol
    stock_symbol = input("Enter the stock symbol: ").upper()

    # Fetch historical stock data
    stock_data = get_stock_data(stock_symbol)

    if stock_data.empty:
        print(f"Could not fetch data for {stock_symbol}. Please check the stock symbol and try again.")
    else:
        # Prepare data for training
        processed_data = prepare_data(stock_data)

        # Train the model
        model = train_model(processed_data)

        # Predict stock movement for the next day
        last_record = processed_data.tail(1)
        input_data = last_record[['1. open', '2. high', '3. low', '5. volume']].values[0]
        predicted_close = predict_movement(model, input_data)

        # Display the prediction
        print(f"Predicted Close Price for {stock_symbol} next day: {predicted_close:.2f}")
        if predicted_close > last_record['4. close'].values[0]:
            print(f"The stock is predicted to rise by {((predicted_close - last_record['4. close'].values[0]) / last_record['4. close'].values[0]) * 100:.2f}%.")
        else:
            print(f"The stock is predicted to fall by {((last_record['4. close'].values[0] - predicted_close) / last_record['4. close'].values[0]) * 100:.2f}%.")
'''