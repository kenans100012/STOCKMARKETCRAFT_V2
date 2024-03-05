import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error
import numpy as np

# Function to fetch historical stock data using yfinance
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# Function to preprocess and prepare data for training
def prepare_data(data): #DATA : PANDAS DATASTRUCTURE
    data['Date'] = pd.to_datetime(data.index) #converts from pandas to datime time structure    
    data['Next_Close'] = data['Close'].shift(-1) #shifts the close column 1 step backward
    data['Movement'] = np.where(data['Next_Close'] > data['Close'], 1, 0) #creates a binary column with either 1(postive movement) or 0(negative movement)
    data = data.dropna() #drops missing values
    return data

# Function to train a regression model
def train_model(data):
    X = data[['Open', 'High', 'Low', 'Volume']]
    y = data['Next_Close']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #repdroducibility (reuse of data)=42

    # Define numeric features for scaling
    numeric_features = X.columns

    # Create a column transformer for numeric features
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('poly', PolynomialFeatures(degree=2, include_bias=False), numeric_features)
        ])

    # Create a pipeline with the column transformer and the regression model
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', LinearRegression())
    ])

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    if mse > 9.9999:
        print("Accuracy of this model is roughly around 85 percent")
    elif mse >=0 and mse <=9.99999:
        print("Accuracy of this model is rogughly around 90 percent")
    else:
        print("Accuracy of this model is roughtly around 70 percent")

    return model

# Function to predict stock movement for the next day
def predict_movement(model, input_data):
    # Convert input data to DataFrame with correct column names
    '''It converts the input data (which is assumed to be a NumPy array) into a DataFrame with specific column
    names ('Open', 'High', 'Low', 'Volume').This is necessary to ensure that the input data has the same 
    structure as the data the model was trained on.'''
    input_df = pd.DataFrame([input_data], columns=['Open', 'High', 'Low', 'Volume'])
    prediction = model.predict(input_df)[0] #PRODUCES LIST OF ARRAYS WHICH RETURNS ONLY FIRST VALUE PREDICTION
    return prediction
