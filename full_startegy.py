import numpy as np
import pandas as pd
from arch import arch_model
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def evaluate():
    df = pd.read_csv('sample_input.csv')
     
    actual_close = np.loadtxt('sample_close.txt')
    
    pred_close = predict_func(df)
    
    # Calculation of squared_error
    actual_close = np.array(actual_close)
    pred_close = np.array(pred_close)
    mean_square_error = np.mean(np.square(actual_close-pred_close))


    pred_prev = [df['Close'].iloc[-1]]
    pred_prev.append(pred_close[0])
    pred_curr = pred_close
    
    actual_prev = [df['Close'].iloc[-1]]
    actual_prev.append(actual_close[0])
    actual_curr = actual_close

    # Calculation of directional_accuracy
    pred_dir = np.array(pred_curr)[:, 0] - np.array(pred_prev[1])
    actual_dir = np.array(actual_curr) - np.array(actual_prev)
    dir_accuracy = np.mean((pred_dir*actual_dir)>0)*100

    print(f'Mean Square Error: {mean_square_error:.6f}\nDirectional Accuracy: {dir_accuracy:.1f}')
    
def predict_func(df):
    df.ffill(inplace=True)
    # Prepare the DataFrame with log returns
    df['log_returns'] = np.log(df['Close']).diff().dropna()
    # Create a scaler to normalize the data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df['Close'].values.reshape(-1, 1))
    # Split the data into training and test sets
    train_size = int(len(scaled_data) * 0.8)
    train_data = scaled_data[:train_size]
    test_data = scaled_data[train_size:]

    # Prepare the training data for LSTM
    X_train_lstm, y_train_lstm = [], []
    lookback_lstm = 10  # Adjust the lookback window for LSTM

    for i in range(lookback_lstm, len(train_data)):
        X_train_lstm.append(train_data[i-lookback_lstm:i, 0])
        y_train_lstm.append(train_data[i, 0])

    X_train_lstm, y_train_lstm = np.array(X_train_lstm), np.array(y_train_lstm)

    # Reshape the input data for LSTM
    X_train_lstm = np.reshape(X_train_lstm, (X_train_lstm.shape[0], X_train_lstm.shape[1], 1))

    # Create and fit the LSTM model
    lstm_model = Sequential()
    lstm_model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train_lstm.shape[1], 1)))
    lstm_model.add(LSTM(units=50))
    lstm_model.add(Dense(units=1))
    lstm_model.compile(optimizer='adam', loss='mean_squared_error')
    lstm_model.fit(X_train_lstm, y_train_lstm, epochs=10, batch_size=32)

    # Prepare the test data for LSTM
    inputs_lstm = df['Close'].values[len(df) - len(test_data) - lookback_lstm:]
    inputs_lstm = inputs_lstm.reshape(-1, 1)
    inputs_lstm = scaler.transform(inputs_lstm)

    X_test_lstm = []

    for i in range(lookback_lstm, len(inputs_lstm)):
        X_test_lstm.append(inputs_lstm[i-lookback_lstm:i, 0])

    X_test_lstm = np.array(X_test_lstm)
    X_test_lstm = np.reshape(X_test_lstm, (X_test_lstm.shape[0], X_test_lstm.shape[1], 1))

    # Make predictions using LSTM model
    predicted_prices_lstm = lstm_model.predict(X_test_lstm)
    predicted_prices_lstm = scaler.inverse_transform(predicted_prices_lstm)

    # Prepare the test data for EMA
    inputs_ema = df['Close'].values[len(df) - len(test_data) - lookback_lstm:]
    inputs_ema = inputs_ema.reshape(-1, 1)
    inputs_ema = scaler.transform(inputs_ema)

    # Calculate EMA using alpha 0.75
    ema = [inputs_ema[0]]  # Initialize the first EMA value as the first data point
    alpha = 0.85
    for i in range(1, len(inputs_ema)):
        ema_value = alpha * inputs_ema[i] + (1 - alpha) * ema[i - 1]
        ema.append(ema_value)

    ema = np.array(ema)
    ema = scaler.inverse_transform(ema)

    # Adjust the shapes of predicted_prices_lstm and ema arrays
    predicted_prices_lstm = predicted_prices_lstm[-len(ema):]

    # Combine the predictions
    combined_predictions = 0.05 * predicted_prices_lstm[-10:] + 0.95 * ema[-10:]
    # Return the combined predictions for the next two days
    next_two_days = combined_predictions[-2:]
    return next_two_days

if(__name__ == '__main__'):
    evaluate()