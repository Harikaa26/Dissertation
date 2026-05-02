import pandas as pd

# Load file
df = pd.read_csv("isolation_forest_results.csv")

# Counts
total_packets = len(df)
anomalous_packets = (df['anomaly'] == 1).sum()
normal_packets = (df['anomaly'] == 0).sum()
anomaly_rate = (anomalous_packets / total_packets) * 100

# Print results
print("Total packets:", total_packets)
print("Normal traffic:", normal_packets)
print("Anomalous traffic:", anomalous_packets)
print("Anomaly rate: {:.2f}%".format(anomaly_rate))