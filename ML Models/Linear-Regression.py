from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.linear_model import LinearRegression

X, y = load_diabetes(return_X_y=True)
print(load_diabetes().feature_names)

X_bmi = X[:, np.newaxis, 2]
X_train, X_test, y_train, y_test = train_test_split(X_bmi, y, test_size=0.3)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

score = r2_score(y_test, y_pred)
print(round(score, 4))

plt.bar(['LR'], [score])
plt.show()

plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', linewidth=3, label='Regression line')
plt.xlabel('BMI (normalized)')
plt.ylabel('Disease Progression')
plt.title('Linear Regression: BMI vs Diabetes Progression')
plt.legend(); plt.grid(); plt.show()