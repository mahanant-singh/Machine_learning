import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample Dataset
data = {
    "area": [500, 800, 1000, 1200, 1500, 1800, 2000],
    "price": [10, 15, 20, 24, 30, 35, 40]
}

df = pd.DataFrame(data)

X = df[["area"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "house_price_model.pkl")

print("Model Saved!")