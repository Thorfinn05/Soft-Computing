from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier, plot_tree

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(round(acc, 4))

plt.bar(["Decision Tree"], [acc])
plt.show()

sns.heatmap(confusion_matrix(y_test, y_pred), annot=True)
plt.show()

# Plotting the Decision Tree
plt.figure(figsize=(15, 10))
plot_tree(model,
          feature_names=load_iris().feature_names,
          class_names=load_iris().target_names,
          rounded=True)
plt.title("Decision Tree")
plt.show()