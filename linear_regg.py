import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
tips = sns.load_dataset("tips")

# Use just 'total_bill' to visualize simple linear regression
X = tips[['total_bill']]
y = tips['tip']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("R² Score:", round(r2_score(y_test, y_pred), 4))
print("RMSE:", round(mean_squared_error(y_test, y_pred), 4))

# 👉 Plot regression line
plt.figure(figsize=(8, 5))
sns.regplot(x='total_bill', y='tip', data=tips, line_kws={"color": "red"})
# line_kws  Line Keyword Arguments — used to customize the appearance of the regression line.
plt.title("Linear Regression: Tip vs Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.grid(True)
plt.show()
