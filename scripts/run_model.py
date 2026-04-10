import pickle
import pandas as pd

# Load model
with open("models/parkinsgone_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load dataset
df = pd.read_csv("data/processed/off_features.csv")

# Use the model's expected feature names
feature_cols = model.feature_name_

df["dopamine_score"] = model.predict(df[feature_cols])

df.to_csv("data/processed/off_scored.csv", index=False)
print("Saved data/processed/off_scored.csv")

