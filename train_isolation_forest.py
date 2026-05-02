import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

# load dataset
df = pd.read_csv("traffic_dataset.csv")

# keep useful columns
df = df[["protocol", "length", "src_port", "dst_port"]].copy()

# fill blanks
df["src_port"] = pd.to_numeric(df["src_port"], errors="coerce").fillna(0)
df["dst_port"] = pd.to_numeric(df["dst_port"], errors="coerce").fillna(0)
df["length"] = pd.to_numeric(df["length"], errors="coerce").fillna(0)

# encode protocol
le = LabelEncoder()
df["protocol"] = le.fit_transform(df["protocol"].astype(str))

# train model
model = IsolationForest(contamination=0.2, random_state=42)
df["anomaly"] = model.fit_predict(df)

# convert output: -1 = anomaly, 1 = normal
df["anomaly"] = df["anomaly"].map({1: 0, -1: 1})

# save results
df.to_csv("isolation_forest_results.csv", index=False)

# print summary
print(df["anomaly"].value_counts())
print("Results saved to isolation_forest_results.csv")