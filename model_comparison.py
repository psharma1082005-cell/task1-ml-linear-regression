# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score


# Load Dataset

data = fetch_california_housing(as_frame=True)

df = pd.concat(
    [data.data, data.target.rename("HousePrice")],
    axis=1
)

print("Dataset Shape:", df.shape)
print(df.head())


# Features and Target

X = df.drop("HousePrice", axis=1)
y = df["HousePrice"]


# Feature Scaling

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)


# Models

models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Decision Tree": DecisionTreeRegressor(max_depth=5)
}


# Training and Evaluation

results = {}

for name, model in models.items():

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results[name] = [mse, r2]

    print("\n", "="*40)
    print(name)
    print("MSE:", mse)
    print("R2 Score:", r2)


# Results Table

results_df = pd.DataFrame(
    results,
    index=["MSE", "R2 Score"]
).T

print("\nModel Comparison Table")
print(results_df)


# Graph

results_df.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Model Comparison")
plt.ylabel("Score")
plt.xlabel("Models")
plt.xticks(rotation=0)

plt.show()
