import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import pickle

# Load dataset
df_full = pd.read_csv("laptop_cleaned_dataset.csv")

# Select numeric features for ML training
features = ['price', 'ram_num', 'core_num', 'threads_num']
df_full = df_full.dropna(subset=features)
df_numeric = df_full[features]


# Scale training data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_numeric)

# Train Recommendation Model
model = NearestNeighbors(n_neighbors=3, metric='euclidean')
model.fit(X_scaled)

# Save model + scaler + FULL dataset (not numeric only)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

df_full.to_pickle("laptops.pkl")

print("Model and data saved successfully!")
