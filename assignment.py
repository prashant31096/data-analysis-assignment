# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load the data
data = pd.read_csv(r'C:\Users\prashant kumar\Desktop\Sample_Data.csv')

# Convert the Timestamp column to datetime for easier processing
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Plot the initial chart
plt.figure(figsize=(12, 6))
plt.plot(data['Timestamp'], data['Values'], label="Voltage Readings")
plt.title("Voltage vs. Timestamp")
plt.xlabel("Timestamp")
plt.ylabel("Voltage")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Compute 5-period moving average
data['Moving_Average'] = data['Values'].rolling(window=5).mean()

# Find local peaks and troughs
peaks, _ = find_peaks(data['Values'])
troughs, _ = find_peaks(-data['Values'])

# Plot with moving average, peaks, and troughs
plt.figure(figsize=(14, 7))
plt.plot(data['Timestamp'], data['Values'], label="Voltage Readings")
plt.plot(data['Timestamp'], data['Moving_Average'], linestyle='--', color='orange', label="5-Period Moving Average")
plt.scatter(data['Timestamp'].iloc[peaks], data['Values'].iloc[peaks], marker='^', color='green', label='Peaks')
plt.scatter(data['Timestamp'].iloc[troughs], data['Values'].iloc[troughs], marker='v', color='red', label='Troughs')
plt.title("Voltage vs. Timestamp with Moving Average, Peaks, and Troughs")
plt.xlabel("Timestamp")
plt.ylabel("Voltage")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Tabulate instances where voltage went below 20
below_20_instances = data[data['Values'] < 20][['Timestamp', 'Values']]
print("Instances where Voltage went below 20:")
print(below_20_instances)

# Detect downward slope accelerations (difference between consecutive slopes)
data['Slope'] = data['Values'].diff()
data['Slope_Change'] = data['Slope'].diff()
downward_accelerations = data[(data['Slope'] < 0) & (data['Slope_Change'] < 0)][['Timestamp', 'Slope', 'Slope_Change']]

print("Downward slope acceleration instances:")
print(downward_accelerations)

# Save results to CSV files
below_20_instances.to_csv("Voltage_Below_20_Instances.csv", index=False)
downward_accelerations.to_csv("Downward_Accelerations.csv", index=False)
