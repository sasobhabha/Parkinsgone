import pandas as pd

df = pd.read_csv("data/processed/off_features.csv")

df["dopamine_support_score"] = (
    df["tyrosine_mg"].fillna(0) * 0.4 +
    df["phenylalanine_mg"].fillna(0) * 0.4 +
    df["fiber_g"].fillna(0) * 0.1 +
    df["polyphenol_flag"] * 10 +
    df["fermented_flag"] * 15
)

df.to_csv("data/processed/parkinsgone_dataset.csv", index=False)
print("Saved data/processed/parkinsgone_dataset.csv")

