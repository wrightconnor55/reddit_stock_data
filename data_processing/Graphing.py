
import pandas as pd
import numpy as np
from datetime import datetime, timedelta



# Initialize parameters
initial_value = 100  # Starting value
value = initial_value
start_time = datetime.now()

# Simulation parameters
total_minutes = 1440  # Number of minutes to simulate (1 day)
#Put other percent change here
daily_percentage_change = np.random.uniform(-0.01, 0.01)  # Daily change between -1% and 1%
minute_rate_of_change = daily_percentage_change / total_minutes
fluctuation_probability = 0.05  # Probability of a random fluctuation occurring in a given minute
fluctuation_magnitude = 0.001  # Magnitude of random fluctuations (±2%)

# List to store data points
data_points = []

# Generate data points
for minute in range(total_minutes):
    # Calculate the current time
    current_time = start_time + timedelta(minutes=minute)
    
    # Apply the continuous rate of change
    value *= (1 + minute_rate_of_change)
    
    # Occasionally apply random fluctuations
    if np.random.rand() < fluctuation_probability:
        fluctuation = np.random.uniform(-fluctuation_magnitude, fluctuation_magnitude)
        value *= (1 + fluctuation)
    
    # Append the current time and value to the data points
    data_points.append({'Time': current_time, 'Value': value})

# Create a DataFrame from the data points
df = pd.DataFrame(data_points)

# Print the DataFrame
print(df)


df.to_csv('graph_test.csv', index = False)


