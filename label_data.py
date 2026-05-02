import pandas as pd

# Load your dataset
df = pd.read_csv("isolation_forest_results.csv")

# AUTO LABEL (based on model output)
# -1 = anomaly → attack (1)
# 1 = normal → normal (0)
df['true_label'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)

# Save new file
df.to_csv("labeled_results.csv", index=False)

print("Done - labeled_results.csv created")