# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Generate synthetic data
np.random.seed(42)  # for reproducibility
X = np.linspace(0, 10, 100).reshape(-1, 1)   # feature (single predictor)
true_slope = 2.5
true_intercept = 1.0
y = true_intercept + true_slope * X.ravel() + np.random.normal(0, 1.5, X.shape[0])  # add noise

# 2. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# 5. Evaluate the model
print("Model coefficients:")
print(f"  Intercept: {model.intercept_:.3f}")
print(f"  Slope: {model.coef_[0]:.3f}")
print("\nPerformance on test set:")
print(f"  Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred_test):.3f}")
print(f"  R² score: {r2_score(y_test, y_pred_test):.3f}")

# 6. Visualize the results
plt.scatter(X_test, y_test, color='blue', label='Actual values (test)')
plt.scatter(X_test, y_pred_test, color='red', marker='x', label='Predicted values (test)')
plt.plot(X_test, model.predict(X_test), color='green', linewidth=2, label='Regression line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression: Test Set')
plt.legend()
plt.show()