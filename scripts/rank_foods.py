import pandas as pd
import joblib

df = pd.read_csv("data/processed/parkinsgone_dataset.csv")
model = joblib.load("models/parkinsgone_model.pkl")

X = df.drop(columns=["dopamine_support_score", "food", "brand", "categories"])
df["predicted_score"] = model.predict(X)

df.sort_values("predicted_score", ascending=False).head(100).to_csv(
    "data/processed/top_parkinsgone_foods.csv", index=False
)

print("Saved data/processed/top_parkinsgone_foods.csv")

