import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import ModelCheckpoint

# Assuming your OHLCV data is stored in a DataFrame called 'data'
data = pd.read_csv('STOCK_INDEX.csv')  # Your OHLCV data of size 2000


# Extract the adjusted close values from the OHLCV data
adj_close = np.array(data['Close'])

# Split data into input sequences and corresponding output values
input_sequences = []
output_values = []

seq_length = 100  # Length of input sequences
num_samples = len(adj_close) - seq_length

for i in range(num_samples):
    input_sequences.append(adj_close[i:i+seq_length])
    output_values.append([adj_close[i+seq_length], adj_close[i+seq_length+1]])

# Convert the data to numpy arrays
input_sequences = np.array(input_sequences)
output_values = np.array(output_values)

# Normalize the input data (optional)
normalized_input = input_sequences / np.max(input_sequences)
normalized_output = output_values / np.max(output_values)

# Reshape the input sequences to match the expected input shape of LSTM
normalized_input = np.reshape(normalized_input, (normalized_input.shape[0], normalized_input.shape[1], 1))

# Build the LSTM model
model = Sequential()
model.add(LSTM(64, input_shape=(seq_length, 1)))
model.add(Dense(2))
model.compile(loss='mean_squared_error', optimizer='adam')

# Define the checkpoint to save the best model during training
checkpoint = ModelCheckpoint('lstm_model.h5', save_best_only=True)

# Train the model
model.fit(normalized_input, normalized_output, epochs=10, batch_size=32, callbacks=[checkpoint])
