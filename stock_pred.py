import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20, 10

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense

# Load the dataset
df = pd.read_csv("NSE-TATA.csv")
df.head()

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df.Date, format="%Y-%m-%d")
df.index = df['Date']

# Plot the closing price history
plt.figure(figsize=(16, 8))
plt.plot(df["Close"], label='Close Price history')
plt.legend()
plt.show()

# Prepare data for LSTM model
data
