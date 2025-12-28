import pandas as pd
import pickle
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_pickle("laptops.pkl")

# Select feature columns
features = ["ram_num", "core_num", "threads_num", "price"]
X = df[features]

# Scaling for better accuracy
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train KNN recommendation model
model = NearestNeighbors(n_neighbors=3, metric="euclidean")
model.fit(X_scaled)

# Save trained model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("Model training complete! 🚀")
print("New model.pkl and scaler.pkl generated ✔️")
