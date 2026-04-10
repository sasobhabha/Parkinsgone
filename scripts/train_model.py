import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_absolute_error
import joblib

df = pd.read_csv("data/processed/parkinsgone_dataset.csv")

X = df.drop(columns=["dopamine_support_score", "food", "brand", "categories"])
y = df["dopamine_support_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LGBMRegressor(n_estimators=600, learning_rate=0.03)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, preds))

joblib.dump(model, "models/parkinsgone_model.pkl")
print("Saved models/parkinsgone_model.pkl")

